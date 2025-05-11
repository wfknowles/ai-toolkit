# Function to add two numbers
```python
def add_two_numbers(num1: float, num2: float) -> float:
    """
    Adds two numbers and returns the result.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The sum of num1 and num2.
    """
    try:
        result = num1 + num2
        return result
    except TypeError:
        # Or raise a more specific error, or handle as per requirements
        print("Error: Invalid input types. Both inputs must be numbers.")
        return None # Or raise an error
```