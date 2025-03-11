# Reversible Anonymizer

![PyPI version](https://img.shields.io/pypi/v/reversible-anonymizer)
![Python versions](https://img.shields.io/pypi/pyversions/reversible-anonymizer)
![License](https://img.shields.io/pypi/l/reversible-anonymizer)

An enterprise-grade Python package for reversible text anonymization using Google Cloud services.

## Overview

Reversible Anonymizer provides a powerful, scalable solution for detecting and replacing sensitive information in text with realistic-looking fake data, while maintaining the ability to reverse the process and recover the original information.

### Key features:

- **Complete Google DLP InfoType Support**: Over 100 pre-configured detectors for PII, financial data, healthcare information, and more
- **Consistent Anonymization**: Name parts and repeated information anonymized consistently
- **Multiple Cache Strategies**: In-memory LRU cache and Google Cloud Memcache support
- **Asynchronous Storage**: High throughput processing with asynchronous storage updates
- **Realistic or Token-based Replacement**: Choose between human-readable fake data or systematic tokens
- **Batch Operations**: Process multiple texts efficiently in parallel
- **Production-ready Resilience**: Comprehensive error handling, fallbacks, and operational modes

## Installation

```python
pip install reversible-anonymizer

# With Memcache support
pip install reversible-anonymizer[memcache]
```


## Prerequisites
- Python 3.8+
- Google Cloud project with the following services enabled:
- Cloud DLP API (dlp.googleapis.com)
- Cloud Firestore API (firestore.googleapis.com)
- [Optional] Memorystore for Memcached (memcache.googleapis.com)
- Google Cloud credentials configured

## Quick Start
```python
from reversible_anonymizer import ReversibleAnonymizer

# Initialize the anonymizer
anonymizer = ReversibleAnonymizer(project="your-project-id")

# Anonymize text
original_text = "Hello, my name is John Smith. Please contact me at john.smith@example.com."
anonymized_text = anonymizer.anonymize(original_text)
print(f"Anonymized: {anonymized_text}")
# Output: "Hello, my name is Michael Johnson. Please contact me at robert.brown@domain.net."

# De-anonymize back to original
recovered_text = anonymizer.deanonymize(anonymized_text)
print(f"De-anonymized: {recovered_text}")
# Output:
"Hello, my name is John Smith. Please contact me at john.smith@example.com."
```

## Usage Examples

### Basic Configuration

```python
anonymizer = ReversibleAnonymizer(
    project="your-project-id",
    info_types=["PERSON_NAME", "EMAIL_ADDRESS", "PHONE_NUMBER"]
)
```

### Realistic vs Token-Based Anonymization
```python
# Realistic fake data (default)
anonymizer = ReversibleAnonymizer(
    project="your-project-id",
    use_realistic_fake_data=True
)

# Token-based anonymization
anonymizer = ReversibleAnonymizer(
    project="your-project-id",
    use_realistic_fake_data=False
)
```

### Detailed Results with Statistics

```python
result = anonymizer.anonymize(text, detailed_result=True)
print(f"Anonymized: {result['anonymized_text']}")
print(f"Findings: {len(result['findings'])}")
print(f"Duration: {result['stats']['duration_ms']} ms")
print(f"Cache hits: {result['stats']['cache_hits']}")
```

### Batch Processing

```python
texts = [
    "John Smith lives in New York.",
    "Jane Doe is from Seattle.",
    "Contact John Smith at john@example.com."
]

# Process in parallel
anonymized_texts = anonymizer.anonymize_batch(texts)
```

### Modes of Operation
```python
# Strict mode (default) - raises exceptions on errors
anonymizer = ReversibleAnonymizer(
    project="your-project-id",
    mode="strict"
)

# Tolerant mode - continues despite errors
anonymizer = ReversibleAnonymizer(
    project="your-project-id",
    mode="tolerant"
)

# Audit mode - detects but doesn't replace sensitive information
anonymizer = ReversibleAnonymizer(
    project="your-project-id",
    mode="audit"
)
```

### Caching Strategies

#### In-Memory Cache (Default)
```python
anonymizer = ReversibleAnonymizer(
    project="your-project-id",
    cache_type="memory",
    cache_config={
        "capacity": 10000,  # Maximum items in cache
        "ttl": 3600         # Time-to-live in seconds
    }
)
```

#### Google Cloud Memcache
```python
# Connect to existing Memcache instance by host
anonymizer = ReversibleAnonymizer(
    project="your-project-id",
    cache_type="memcache",
    cache_config={
        "host": "10.0.0.1",          # Memcache IP address
        "port": 11211,               # Memcache port
        "ttl": 86400                 # Cache TTL in seconds
    }
)

# Or connect using instance name and let the adapter discover endpoints
anonymizer = ReversibleAnonymizer(
    project="your-project-id",
    cache_type="memcache",
    cache_config={
        "instance_id": "anonymizer-cache",
        "region": "us-central1",
        "create_if_missing": True     # Auto-create if not exists
    }
)
```

### Asynchronous Storage Updates
```python
# Enable async storage updates for better performance
anonymizer = ReversibleAnonymizer(
    project="your-project-id",
    async_storage_updates=True
)
```

## Supported InfoTypes

Reversible Anonymizer supports all Google DLP InfoTypes, organized into categories:
### Person Information
- PERSON_NAME
- FIRST_NAME, LAST_NAME
- EMAIL_ADDRESS
- PHONE_NUMBER
- AGE, DATE_OF_BIRTH, GENDER
### Financial Information
- CREDIT_CARD_NUMBER
- BANK_ACCOUNT, IBAN_CODE
- SWIFT_CODE, CURRENCY
### Government IDs
- US_SOCIAL_SECURITY_NUMBER
- PASSPORT_NUMBER
- DRIVER_LICENSE_NUMBER
### Location Information
- STREET_ADDRESS
- CITY, STATE, ZIPCODE
- GPS_COORDINATES
And many more!
#### List available InfoTypes:

```python
# Get all supported info types
info_types = anonymizer.get_supported_infotypes()

# Get info types by category
health_info_types = anonymizer.get_infotypes_by_category("Health Information")

```
## Configuration Options

### Environment Variables
```bash
# Core configuration
ANONYMIZER_PROJECT=your-project-id
ANONYMIZER_INFO_TYPES=PERSON_NAME,EMAIL_ADDRESS,PHONE_NUMBER
ANONYMIZER_COLLECTION=custom_mappings
ANONYMIZER_MODE=tolerant
ANONYMIZER_USE_REALISTIC_FAKE_DATA=true

# Cache configuration
ANONYMIZER_CACHE_TYPE=memcache
ANONYMIZER_MEMCACHE_HOST=10.0.0.1
ANONYMIZER_MEMCACHE_PORT=11211
ANONYMIZER_CACHE_TTL=3600

```

### Configuration File
```bash
# Load from file
anonymizer = ReversibleAnonymizer.from_config("config.json")

```
#### Example config.json:
```json
{
  "project": "your-project-id",
  "info_types": ["PERSON_NAME", "EMAIL_ADDRESS", "PHONE_NUMBER"],
  "collection_name": "custom_mappings",
  "mode": "strict",
  "use_realistic_fake_data": true,
  "cache_type": "memcache",
  "cache_config": {
    "host": "10.0.0.1",
    "port": 11211,
    "ttl": 3600
  }
}

```

## CLI Usage
```bash
# List supported info types
anonymizer --project your-project-id list-info-types

# Anonymize a file
anonymizer --project your-project-id anonymize --input input.txt --output anonymized.txt

# De-anonymize a file
anonymizer --project your-project-id deanonymize --input anonymized.txt --output original.txt
```
### Memcache Setup
```bash
# Enable the API
python -m tools.memcache_setup --project your-project-id enable-api

# Create a new Memcache instance
python -m tools.memcache_setup --project your-project-id create \
  --name anonymizer-cache \
  --region us-central1 \
  --node-count 1 \
  --node-memory 1
```
## Error Handling

The package provides custom exceptions:
- **ServiceNotEnabledError**: Raised when required Google Cloud services are not enabled
- **AnonymizationError**: Raised when anonymization fails
- **DeAnonymizationError**: Raised when de-anonymization fails
- **InfoTypeNotSupportedError**: Raised when an unsupported info type is requested
- **StorageError**: Raised when there's an error with the storage adapter
- **ConfigurationError**: Raised when there's a configuration error

## Security Best Practices
- Use secure storage: Enable encryption for stored mappings
- Limit access: Use IAM to restrict access to the Firestore collection
- Set appropriate TTLs: Configure cache TTLs to minimize data exposure
- Enable audit logging: Use detailed_result to log anonymization operations

## Performance Considerations
- Use Memcache: For high-throughput applications
- Enable async storage: Reduce latency by updating storage asynchronously
- Batch processing: Use batch methods for multiple texts
- Optimize info types: Select only the info types you need

## Contributing
Contributions are welcome! Please feel free to submit a pull request.
1. Fork the repository
2. Create your feature branch (git checkout -b feature/amazing-feature)
3. Commit your changes (git commit -m 'Add some amazing feature')
4. Push to the branch (git push origin feature/amazing-feature)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
- Google Sensitive Data Protection (formerly Cloud DLP) for the powerful detection capabilities
- Faker library for generating realistic fake data

