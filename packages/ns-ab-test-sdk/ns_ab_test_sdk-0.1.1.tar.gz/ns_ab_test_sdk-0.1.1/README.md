# AB Test SDK

A simple A/B testing SDK for recording and saving data.

## Installation

```bash
pip install ns_ab_test_sdk
```

## Usage

```python
from ns_ab_test_sdk import recorder

# your code...

# Record data
recorder.put("test_key", "test_value")

# your code...
```