from typing import Optional, List, Dict, Any, Union, TypedDict, Tuple
import uuid
import concurrent.futures
import time
import logging
from datetime import datetime
import hashlib
import re
from google.cloud import dlp_v2, service_usage_v1

from .models import AnonymizationResult, LRUCache
from .storage.base import MemoryAdapter
from .storage.firestore_adapter import FirestoreAdapter
from .storage.secure_firestore_adapter import SecureFirestoreAdapter
from .infotypes.catalog import InfoTypeCatalog
from .config import AnonymizerConfig
from .common import (
    AnonymizerMode,
    InfoTypeCategory,
    ServiceNotEnabledError,
    AnonymizationError,
    DeAnonymizationError,
    StorageError,
    ConfigurationError,
    AnonymizerLogger
)


class ReversibleAnonymizer:
    """Enterprise-grade reversible text anonymization using Google Cloud DLP."""

    def __init__(
            self,
            project: str,
            info_types: Optional[List[Union[str, Dict[str, str]]]] = None,
            collection_name: str = "anonymization_mappings",
            location: str = "global",
            check_services: bool = True,
            mode: str = "strict",
            cache_size: int = 1000,
            cache_ttl: int = 3600,
            storage_type: str = "firestore",
            encryption_key: Optional[str] = None,
            batch_size: int = 500
    ):
        """
        Initialize the ReversibleAnonymizer.

        Args:
            project: Google Cloud project ID
            info_types: List of info types to detect (simple strings or dicts)
            collection_name: Firestore collection name for storing mappings
            location: Google Cloud location
            check_services: Whether to check if required services are enabled
            mode: Operation mode ("strict", "tolerant", or "audit")
            cache_size: Size of the in-memory cache
            cache_ttl: Cache time-to-live in seconds
            storage_type: Storage adapter type ("firestore" or "memory")
            encryption_key: Optional key for encrypting stored mappings
            batch_size: Size of batches for batch operations
        """
        # Initialize configuration
        self.project = project
        self.info_types = self._normalize_info_types(info_types or [
            "PERSON_NAME", "PHONE_NUMBER", "EMAIL_ADDRESS", "CREDIT_CARD_NUMBER"
        ])
        self.collection_name = collection_name
        self.location = location
        self.mode = AnonymizerMode(mode)
        self.batch_size = batch_size

        # Set up logger
        self.logger = AnonymizerLogger(
            name="reversible_anonymizer_gcp",
            level=logging.INFO
        )

        # Check required services
        if check_services:
            self._check_required_services()

        # Initialize DLP client
        try:
            self.dlp_client = dlp_v2.DlpServiceClient()
        except Exception as e:
            self.logger.error(f"Failed to initialize DLP client: {str(e)}")
            if self.mode == AnonymizerMode.STRICT:
                raise AnonymizationError(f"DLP client initialization failed: {str(e)}")

        # Initialize faker for generating fake data
        from faker import Faker
        self.faker = Faker()

        # Initialize cache
        self.cache = LRUCache(capacity=cache_size, ttl=cache_ttl)

        # Initialize storage adapter
        if storage_type == "memory":
            self.storage = MemoryAdapter()
        elif storage_type == "firestore":
            if encryption_key:
                self.storage = SecureFirestoreAdapter(
                    project=project,
                    collection_name=collection_name,
                    encryption_key=encryption_key
                )
            else:
                self.storage = FirestoreAdapter(
                    project=project,
                    collection_name=collection_name
                )
        else:
            raise ConfigurationError(f"Unsupported storage type: {storage_type}")

        self.logger.info(f"Initialized ReversibleAnonymizer with {len(self.info_types)} info types")

    @classmethod
    def from_config(cls, config_path: Optional[str] = None) -> 'ReversibleAnonymizer':
        """Create an anonymizer instance from a configuration file or environment variables."""
        if config_path:
            config = AnonymizerConfig.from_file(config_path)
        else:
            config = AnonymizerConfig.from_env()

        # Validate configuration
        errors = AnonymizerConfig.validate_config(config)
        if errors:
            raise ConfigurationError(f"Configuration errors: {', '.join(errors)}")

        return cls(**config)

    def _normalize_info_types(self, info_types: List[Union[str, Dict[str, str]]]) -> List[Dict[str, str]]:
        """Convert info types to the format required by DLP API."""
        normalized = []
        for info_type in info_types:
            if isinstance(info_type, str):
                normalized.append({"name": info_type})
            elif isinstance(info_type, dict) and "name" in info_type:
                normalized.append(info_type)
            else:
                raise ConfigurationError(f"Invalid info type format: {info_type}")
        return normalized

    def _check_required_services(self) -> None:
        """Check if required Google Cloud services are enabled."""
        required_services = [
            "dlp.googleapis.com",
            "firestore.googleapis.com"
        ]

        client = service_usage_v1.ServiceUsageClient()
        parent = f"projects/{self.project}"

        for service in required_services:
            request = service_usage_v1.GetServiceRequest(
                name=f"{parent}/services/{service}"
            )
            try:
                response = client.get_service(request=request)
                if response.state != service_usage_v1.State.ENABLED:
                    raise ServiceNotEnabledError(
                        f"Service {service} is not enabled for project {self.project}"
                    )
            except Exception as e:
                raise ServiceNotEnabledError(
                    f"Error checking service {service}: {str(e)}"
                )

        self.logger.debug("All required services are enabled")

    def _generate_fake_data(self, info_type: str, original_data: str) -> str:
        """Generate appropriate fake data based on info type."""
        # Generate a consistent unique ID based on the original data
        unique_id = hashlib.md5(original_data.encode()).hexdigest()[:8]

        # Generate appropriate fake data based on info type
        if info_type == "PERSON_NAME":
            return f"PERSON-{unique_id}"
        elif info_type == "EMAIL_ADDRESS":
            return f"EMAIL-{unique_id}@example.com"
        elif info_type == "PHONE_NUMBER":
            return f"PHONE-{unique_id}"
        elif info_type == "CREDIT_CARD_NUMBER":
            return f"CC-{unique_id}"
        elif info_type == "US_SOCIAL_SECURITY_NUMBER":
            return f"SSN-{unique_id}"
        elif info_type == "STREET_ADDRESS":
            return f"ADDR-{unique_id}"
        elif info_type == "FIRST_NAME":
            return f"FNAME-{unique_id}"
        elif info_type == "LAST_NAME":
            return f"LNAME-{unique_id}"

        # Get category for more generic handling
        category = InfoTypeCatalog.get_category_for_infotype(info_type)
        if category == InfoTypeCategory.PERSON:
            return f"PII-{unique_id}"
        elif category == InfoTypeCategory.FINANCIAL:
            return f"FIN-{unique_id}"
        elif category == InfoTypeCategory.HEALTH:
            return f"MED-{unique_id}"
        elif category == InfoTypeCategory.CREDENTIALS:
            return f"CRED-{unique_id}"
        elif category == InfoTypeCategory.LOCATION:
            return f"LOC-{unique_id}"
        elif category == InfoTypeCategory.DOCUMENT:
            return f"DOC-{unique_id}"

        # Default for unknown info types
        return f"DATA-{info_type}-{unique_id}"

    def anonymize(
            self,
            text_to_deidentify: str,
            detailed_result: bool = False,
            run_id: Optional[str] = None
    ) -> Union[str, AnonymizationResult]:
        """
        Anonymize text by replacing sensitive information with fake data.

        Args:
            text_to_deidentify: Text to anonymize
            detailed_result: Whether to return detailed result information
            run_id: Optional identifier for this anonymization run

        Returns:
            By default: Anonymized text string
            If detailed_result=True: AnonymizationResult with text and metadata
        """
        # Generate a run ID if not provided
        if run_id is None:
            run_id = uuid.uuid4().hex

        # Statistics for detailed result
        stats = {
            "start_time": time.time(),
            "total_findings": 0,
            "findings_by_type": {}
        }

        try:
            # Set up the DLP request
            parent = f"projects/{self.project}/locations/{self.location}"
            inspect_config = dlp_v2.InspectConfig(
                info_types=[dlp_v2.InfoType(name=it["name"]) for it in self.info_types],
                include_quote=True,
                min_likelihood=dlp_v2.Likelihood.POSSIBLE
            )
            item = dlp_v2.ContentItem(value=text_to_deidentify)

            # Execute the DLP inspect request
            self.logger.debug(f"Inspecting text with run_id: {run_id}")
            response = self.dlp_client.inspect_content(
                request={"parent": parent,
                         "inspect_config": inspect_config,
                         "item": item}
            )

            # Process the findings and replace sensitive data
            anonymized_text = text_to_deidentify
            findings_data = []

            # Group findings by offset to handle overlapping matches correctly
            findings_by_offset = {}
            for finding in response.result.findings:
                offset = finding.location.byte_range.start
                findings_by_offset[offset] = finding

            # Process findings in reverse order of offsets (to avoid changing positions)
            for offset in sorted(findings_by_offset.keys(), reverse=True):
                finding = findings_by_offset[offset]
                stats["total_findings"] += 1

                # Update statistics by info type
                info_type = finding.info_type.name
                stats["findings_by_type"][info_type] = stats["findings_by_type"].get(info_type, 0) + 1

                # Check cache first
                original_data = finding.quote
                cached_fake_data = self.cache.get(original_data)

                if cached_fake_data:
                    fake_data = cached_fake_data
                else:
                    # Generate new fake data
                    fake_data = self._generate_fake_data(info_type, original_data)

                    # Store the mapping
                    try:
                        metadata = {
                            "info_type": info_type,
                            "run_id": run_id,
                            "timestamp": datetime.utcnow().isoformat()
                        }
                        self.storage.store_mapping(fake_data, original_data, metadata)
                    except StorageError as e:
                        self.logger.error(f"Storage error: {str(e)}")
                        if self.mode == AnonymizerMode.STRICT:
                            raise

                    # Update the cache
                    self.cache.put(original_data, fake_data)

                # Collect finding data for detailed result
                if detailed_result:
                    findings_data.append({
                        "info_type": info_type,
                        "quote": original_data,
                        "fake_data": fake_data,
                        "likelihood": str(finding.likelihood),
                        "location": {
                            "start": finding.location.byte_range.start,
                            "end": finding.location.byte_range.end
                        }
                    })

                # Replace in the original text
                start = finding.location.byte_range.start
                end = finding.location.byte_range.end
                prefix = anonymized_text[:start]
                suffix = anonymized_text[end:]
                anonymized_text = prefix + fake_data + suffix

            # Complete statistics
            stats["end_time"] = time.time()
            stats["duration_ms"] = int((stats["end_time"] - stats["start_time"]) * 1000)

            # Log the result
            self.logger.info(
                f"Anonymization completed for run_id: {run_id}",
                extra={"findings": stats["total_findings"], "duration_ms": stats["duration_ms"]}
            )

            # Return appropriate result
            if detailed_result:
                return {
                    "anonymized_text": anonymized_text,
                    "findings": findings_data,
                    "stats": stats,
                    "run_id": run_id
                }
            return anonymized_text

        except Exception as e:
            error_msg = f"Anonymization failed: {str(e)}"
            self.logger.error(error_msg, exc_info=True)

            if self.mode == AnonymizerMode.TOLERANT:
                # In tolerant mode, return original text
                return text_to_deidentify if not detailed_result else {
                    "anonymized_text": text_to_deidentify,
                    "findings": [],
                    "stats": {"error": str(e)},
                    "run_id": run_id
                }
            else:
                # In strict mode, raise exception
                raise AnonymizationError(error_msg, details={"run_id": run_id})

    def deanonymize(self, text: str) -> str:
        """
        De-anonymize text by replacing fake data with original data.

        Args:
            text: Text to de-anonymize

        Returns:
            De-anonymized text
        """
        try:
            deanonymized_text = text

            # Extract all potential fake data patterns

            # Match patterns for our standard fake data formats
            patterns = [
                r'PERSON-[0-9a-f]{8}',
                r'EMAIL-[0-9a-f]{8}@example\.com',
                r'PHONE-[0-9a-f]{8}',
                r'CC-[0-9a-f]{8}',
                r'SSN-[0-9a-f]{8}',
                r'ADDR-[0-9a-f]{8}',
                r'FNAME-[0-9a-f]{8}',
                r'LNAME-[0-9a-f]{8}',
                r'PII-[0-9a-f]{8}',
                r'FIN-[0-9a-f]{8}',
                r'MED-[0-9a-f]{8}',
                r'CRED-[0-9a-f]{8}',
                r'LOC-[0-9a-f]{8}',
                r'DOC-[0-9a-f]{8}',
                r'DATA-[A-Z_]+-[0-9a-f]{8}',
            ]

            # Find all matches for all patterns
            fake_data_items = []
            for pattern in patterns:
                fake_data_items.extend(re.findall(pattern, deanonymized_text))

            # If no matches found, try a more general approach
            if not fake_data_items:
                # Get all mappings and try to identify tokens that match
                all_mappings = self.storage.get_all_mappings(limit=1000)
                for fake_data in all_mappings.keys():
                    if fake_data in deanonymized_text:
                        fake_data_items.append(fake_data)

            # Remove duplicates
            fake_data_items = list(set(fake_data_items))

            # Early return if no fake data found
            if not fake_data_items:
                return text

            # Batch retrieve original data for all fake data items
            try:
                mappings = self.storage.batch_get_originals(fake_data_items)
            except StorageError as e:
                self.logger.error(f"Storage error during deanonymization: {str(e)}")
                if self.mode == AnonymizerMode.STRICT:
                    raise DeAnonymizationError(f"Storage error: {str(e)}")
                mappings = {}

            # Replace each fake data with its original, in reverse length order
            # to avoid replacing parts of other fake data
            sorted_fake_data = sorted(mappings.keys(), key=len, reverse=True)

            for fake_data in sorted_fake_data:
                original_data = mappings[fake_data]
                deanonymized_text = deanonymized_text.replace(fake_data, original_data)

            return deanonymized_text

        except Exception as e:
            error_msg = f"De-anonymization failed: {str(e)}"
            self.logger.error(error_msg, exc_info=True)

            if self.mode == AnonymizerMode.TOLERANT:
                # In tolerant mode, return original text
                return text
            else:
                # In strict mode, raise exception
                raise DeAnonymizationError(error_msg)

    def anonymize_batch(self, texts: List[str], max_workers: int = 5) -> List[str]:
        """
        Anonymize multiple texts efficiently in parallel.

        Args:
            texts: List of texts to anonymize
            max_workers: Maximum number of parallel workers

        Returns:
            List of anonymized texts
        """
        result = [""] * len(texts)

        try:
            # Process in parallel for better performance
            with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
                # Start the load operations and mark each future with its index
                future_to_index = {
                    executor.submit(self.anonymize, text): i
                    for i, text in enumerate(texts)
                }

                # Process results as they complete
                for future in concurrent.futures.as_completed(future_to_index):
                    index = future_to_index[future]
                    try:
                        result[index] = future.result()
                    except Exception as e:
                        self.logger.error(f"Error processing batch item {index}: {str(e)}")
                        if self.mode == AnonymizerMode.STRICT:
                            raise
                        result[index] = texts[index]  # Use original in case of error

            return result
        except Exception as e:
            error_msg = f"Batch anonymization failed: {str(e)}"
            self.logger.error(error_msg, exc_info=True)

            if self.mode == AnonymizerMode.TOLERANT:
                # In tolerant mode, return original texts
                return texts
            else:
                # In strict mode, raise exception
                raise AnonymizationError(error_msg)

    def deanonymize_batch(self, texts: List[str], max_workers: int = 5) -> List[str]:
        """
        De-anonymize multiple texts efficiently in parallel.

        Args:
            texts: List of texts to de-anonymize
            max_workers: Maximum number of parallel workers

        Returns:
            List of de-anonymized texts
        """
        result = [""] * len(texts)

        try:
            # Process in parallel for better performance
            with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
                # Start the load operations and mark each future with its index
                future_to_index = {
                    executor.submit(self.deanonymize, text): i
                    for i, text in enumerate(texts)
                }

                # Process results as they complete
                for future in concurrent.futures.as_completed(future_to_index):
                    index = future_to_index[future]
                    try:
                        result[index] = future.result()
                    except Exception as e:
                        self.logger.error(f"Error de-anonymizing batch item {index}: {str(e)}")
                        if self.mode == AnonymizerMode.STRICT:
                            raise
                        result[index] = texts[index]  # Use original in case of error

            return result
        except Exception as e:
            error_msg = f"Batch de-anonymization failed: {str(e)}"
            self.logger.error(error_msg, exc_info=True)

            if self.mode == AnonymizerMode.TOLERANT:
                # In tolerant mode, return original texts
                return texts
            else:
                # In strict mode, raise exception
                raise DeAnonymizationError(error_msg)

    def get_supported_infotypes(self) -> List[str]:
        """Get list of all supported info types."""
        return InfoTypeCatalog.get_all_infotypes()

    def get_infotypes_by_category(self, category_name: str) -> List[str]:
        """Get info types for a specific category."""
        try:
            category = InfoTypeCategory(category_name)
            return InfoTypeCatalog.get_infotypes_by_category(category)
        except ValueError:
            raise InfoTypeNotSupportedError(f"Invalid category: {category_name}")

    def get_categories(self) -> List[str]:
        """Get all available info type categories."""
        return [category.value for category in InfoTypeCatalog.get_categories()]

    def is_valid_infotype(self, info_type: str) -> bool:
        """Check if an info type is valid."""
        return InfoTypeCatalog.is_valid_infotype(info_type)


# """Main anonymization module."""
# from typing import Optional, List, Dict, Any
# from faker import Faker
# from google.cloud import dlp_v2, firestore
# import google.api_core.exceptions as google_exceptions
# from .config import (
#     DEFAULT_INFO_TYPES,
#     REQUIRED_SERVICES,
#     DEFAULT_COLLECTION_NAME,
#     DEFAULT_LOCATION,
# )
# from .exceptions import AnonymizationError, DeAnonymizationError
# from .utils import check_required_services
#
#
# class ReversibleAnonymizer:
#     def __init__(
#             self,
#             project: str,
#             info_types: Optional[List[Dict[str, str]]] = None,
#             collection_name: str = DEFAULT_COLLECTION_NAME,
#             location: str = DEFAULT_LOCATION,
#             check_services: bool = True
#     ):
#         """
#         Initialize the ReversibleAnonymizer.
#
#         Args:
#             project: Google Cloud project ID
#             info_types: List of info types to detect (default: DEFAULT_INFO_TYPES)
#             collection_name: Firestore collection name for storing mappings
#             location: Google Cloud location
#             check_services: Whether to check if required services are enabled
#         """
#         self.project = project
#         self.info_types = info_types or DEFAULT_INFO_TYPES
#         self.collection_name = collection_name
#         self.location = location
#
#         if check_services:
#             check_required_services(project, REQUIRED_SERVICES)
#
#         self.dlp = dlp_v2.DlpServiceClient()
#         self.fake = Faker()
#         self.db = firestore.Client()
#
#     def anonymize(self, text_to_deidentify: str) -> str:
#         """
#         Anonymize text by replacing sensitive information with fake data.
#
#         Args:
#             text_to_deidentify: Text to anonymize
#
#         Returns:
#             Anonymized text
#
#         Raises:
#             AnonymizationError: If anonymization fails
#         """
#         try:
#             parent = f"projects/{self.project}/locations/{self.location}"
#             inspect_config = dlp_v2.InspectConfig(
#                 info_types=self.info_types,
#                 include_quote=True
#             )
#             item = dlp_v2.ContentItem(value=text_to_deidentify)
#
#             response = self.dlp.inspect_content(
#                 request={"parent": parent,
#                          "inspect_config": inspect_config,
#                          "item": item}
#             )
#
#             for finding in response.result.findings:
#                 docs = (
#                     self.db.collection(self.collection_name)
#                     .where("original_data", "==", finding.quote)
#                     .stream()
#                 )
#                 docs = list(docs)
#
#                 if docs:
#                     fake_data = docs[0].id
#                 else:
#                     fake_data = self._generate_fake_data(finding.info_type.name)
#                     doc_ref = self.db.collection(
#                         self.collection_name
#                     ).document(fake_data)
#                     doc_ref.set({"original_data": finding.quote})
#
#                 text_to_deidentify = text_to_deidentify.replace(
#                     finding.quote, fake_data
#                 )
#
#             return text_to_deidentify
#
#         except Exception as e:
#             raise AnonymizationError(f"Anonymization failed: {str(e)}")
#
#     def deanonymize(self, text: str) -> str:
#         """
#         De-anonymize text by replacing fake data with original data.
#
#         Args:
#             text: Text to de-anonymize
#
#         Returns:
#             De-anonymized text
#
#         Raises:
#             DeAnonymizationError: If de-anonymization fails
#         """
#         try:
#             docs = self.db.collection(self.collection_name).stream()
#             for doc in docs:
#                 text = text.replace(doc.id, doc.to_dict()["original_data"])
#             return text
#
#         except Exception as e:
#             raise DeAnonymizationError(f"De-anonymization failed: {str(e)}")
#
#     def _generate_fake_data(self, info_type: str) -> str:
#         """Generate fake data based on info type."""
#         fake_data_mapping = {
#             "PERSON_NAME": self.fake.name,
#             "FIRST_NAME": self.fake.first_name,
#             "LAST_NAME": self.fake.last_name,
#             "PHONE_NUMBER": self.fake.phone_number,
#         }
#
#         generator = fake_data_mapping.get(info_type, self.fake.word)
#         return generator()