# Reversible Anonymizer

A Python package for reversible text anonymization using Google Cloud services.

## Installation

```bash```
pip install reversible-anonymizer
## Prerequisites
### Google Cloud project with the following services enabled:
#### Cloud DLP API (dlp.googleapis.com)
##### Cloud Firestore API (firestore.googleapis.com)
##### AI Platform API (aiplatform.googleapis.com)
##### Google Cloud credentials configured
## Usage
from reversible_anonymizer import ReversibleAnonymizer

# Initialize with default settings
anonymizer = ReversibleAnonymizer(project="your-project-id")

# Or customize the settings
anonymizer = ReversibleAnonymizer(
    project="your-project-id",
    info_types=[
        {"name": "PERSON_NAME"},
        {"name": "EMAIL_ADDRESS"}
    ],
    collection_name="custom_mappings",
    location="us-central1"
)

# Anonymize text
original_text = "Hello, my name is John Doe"
anonymized_text = anonymizer.anonymize(original_text)
print(f"Anonymized: {anonymized_text}")

# De-anonymize text
original_text = anonymizer.deanonymize(anonymized_text)
print(f"De-anonymized: {original_text}")

## Error Handling
The package provides custom exceptions:

ServiceNotEnabledError: Raised when required Google Cloud services are not enabled
AnonymizationError: Raised when anonymization fails
DeAnonymizationError: Raised when de-anonymization fails
## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.


4. Create a test file:

`tests/test_anonymizer.py`:
```python
import pytest
from reversible_anonymizer import ReversibleAnonymizer
from reversible_anonymizer.exceptions import ServiceNotEnabledError

def test_anonymizer_initialization():
    with pytest.raises(ServiceNotEnabledError):
        ReversibleAnonymizer("invalid-project")

def test_custom_info_types():
    anonymizer = ReversibleAnonymizer(
        "your-project-id",
        info_types=[{"name": "EMAIL_ADDRESS"}],
        check_services=False
    )
    assert anonymizer.info_types == [{"name": "EMAIL_ADDRESS"}]

# Add more tests as needed
To use the package:

Install the package:
pip install reversible-anonymizer
Use in your code:
from reversible_anonymizer import ReversibleAnonymizer

try:
    # Initialize with custom settings
    anonymizer = ReversibleAnonymizer(
        project="your-project-id",
        info_types=[
            {"name": "PERSON_NAME"},
            {"name": "EMAIL_ADDRESS"},
            {"name": "PHONE_NUMBER"}
        ],
        collection_name="custom_mappings"
    )

    # Anonymize text
    original_text = "Hello, my name is John Doe. Call me at 123-456-7890"
    anonymized_text = anonymizer.anonymize(original_text)
    print(f"Anonymized: {anonymized_text}")

    # De-anonymize text
    original_text = anonymizer.deanonymize(anonymized_text)
    print(f"De-anonymized: {original_text}")

except Exception as e:
    print(f"Error: {str(e)}")