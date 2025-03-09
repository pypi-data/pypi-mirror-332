# DNAWave Python Client

The official Python client for the DNAWave API. This package provides a simple and intuitive way to interact with DNAWave's services.

## Installation

```bash
pip install dnawave
```

## Quick Start

```python
from dnawave import DNAWaveClient, Dataset, Workflow

# Initialize the client
client = DNAWaveClient(api_key="your-api-key")
Dataset.set_client(client)
Workflow.set_client(client)

# Create a dataset
dataset = Dataset.create(
    name="My Dataset",
    bucket_key="s3-bucket-key",
    description="My dataset description",
    keywords=["gene", "sequence"],
    tags=[{"id": "tag-id", "name": "tag-name"}]
)

# List datasets
datasets = Dataset.list()
for dataset in datasets:
    print(dataset.name)

# Get a specific dataset
dataset = Dataset.get("dataset-id")

# Update a dataset
dataset.description = "Updated description"
dataset.save()

# Delete a dataset
dataset.delete()

# Work with workflows
workflow = Workflow.create(
    name="My Workflow",
    engine="nextflow",
    parameter_template={"param1": "value1"}
)

workflows = Workflow.list()
```

## Features

- Full support for DNAWave API endpoints
- Easy-to-use object-oriented interface
- Automatic request retries and error handling
- Type hints for better IDE support

## Error Handling

```python
from dnawave import DNAWaveError, AuthenticationError

try:
    dataset = Dataset.get("non-existent-id")
except AuthenticationError:
    print("Invalid API key")
except DNAWaveError as e:
    print(f"API error: {str(e)}")
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
