# RealIsEven: AI-Powered Even/Odd Number Detection

RealIsEven is a Python package that determines whether a number is even or odd using OpenAI's GPT-4 model. This package combines traditional mathematical operations with artificial intelligence to provide a unique approach to number classification.

The package leverages the OpenAI API to process numerical inputs and return boolean results, demonstrating an innovative (albeit unconventional) way of performing basic arithmetic operations. While this approach may seem overengineered for such a simple task, it serves as an excellent example of integrating AI capabilities into basic mathematical operations and showcases proper Python package structure, API integration, and error handling.

## Repository Structure
```
realiseven/
├── __init__.py          # Package initialization and version definition
├── core.py             # Main logic implementation with OpenAI API integration
└── models.py           # Pydantic data model definitions
├── requirements.txt    # Project dependencies
└── setup.py           # Package installation and distribution configuration
```

## Usage Instructions

### Prerequisites
- Python 3.8 or higher
- OpenAI API key set in your environment
- Internet connection for API access

### Installation

```bash
# Install from PyPI
pip install realiseven

# Install from source
git clone https://github.com/kreiza/realiseven
cd realiseven
pip install -e .
```

### Quick Start

1. Set up your OpenAI API key:
```bash
export OPENAI_API_KEY='your-api-key-here'
```

2. Use the package in your Python code:
```python
from realiseven import is_even

# Check if a number is even
result = is_even(42)
print(result)  # True

result = is_even(7)
print(result)  # False
```

### More Detailed Examples

```python
from realiseven import is_even

# Basic usage with positive integers
print(is_even(100))  # True
print(is_even(99))   # False

# Error handling example
try:
    result = is_even("not a number")
except TypeError as e:
    print(f"Error: {e}")  # Error: Input must be an integer

# Using with negative numbers
print(is_even(-4))   # True
print(is_even(-7))   # False
```

### Troubleshooting

Common issues and solutions:

1. OpenAI API Key Not Found
```
Error: OpenAI API key not found
Solution: Ensure OPENAI_API_KEY environment variable is set correctly
```

2. API Connection Issues
```python
# Enable debug logging for API calls
import logging
logging.basicConfig(level=logging.DEBUG)
```

3. Type Errors
- Problem: Receiving TypeError when passing non-integer values
- Solution: Ensure you're passing integer values to the is_even function
- Debug: Print the type of your input using `print(type(your_input))`

## Data Flow

The package processes integer inputs through the OpenAI API to determine if a number is even or odd. The flow involves input validation, API communication, and response parsing.

```ascii
[Input Integer] -> [Type Validation] -> [OpenAI API Request] -> [Response Parsing] -> [Boolean Result]
     |                    |                     |                       |                |
     +--------------------+---------------------+-----------------------+----------------+
```

Component interactions:
1. Input validation ensures only integers are processed
2. OpenAI client sends formatted prompts to the API
3. API responses are parsed using Pydantic models
4. Error handling manages API failures and invalid inputs
5. Results are returned as boolean values
6. The IsEven model validates the API response structure
7. The core module handles the main business logic and API interaction