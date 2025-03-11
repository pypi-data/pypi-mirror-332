# Example Package Documentation

Welcome to the documentation for the Example Package.

## Installation

```bash
pip install example_package
```

## Usage

Basic usage of the package:

```python
from example_package import example_module

# Using a function
greeting = example_module.example_function()
print(greeting)  # Output: Hello from example_package!

# Using a class
example = example_module.ExampleClass("User")
personalized_greeting = example.greet()
print(personalized_greeting)  # Output: Hello, User!
```

## API Reference

### example_function()

Returns a standard greeting string.

### ExampleClass

A class that generates personalized greetings.

- `__init__(name="World")`: Initialize with an optional name
- `greet()`: Return a personalized greeting 