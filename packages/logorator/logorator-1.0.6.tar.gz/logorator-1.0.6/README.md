# Logorator Documentation

Logorator is a decorator-based logging library for Python that provides hierarchical logging, function call tracking, execution time measurement, and ANSI color support. It's designed to be simple to use while offering powerful logging capabilities.

## Table of Contents

1. [Installation](#installation)
2. [Basic Usage](#basic-usage)
3. [Core Concepts](#core-concepts)
4. [API Reference](#api-reference)
5. [Configuration Options](#configuration-options)
6. [Advanced Usage](#advanced-usage)
7. [Examples](#examples)
8. [Best Practices](#best-practices)

## Installation

```bash
pip install logorator
```

## Basic Usage

```python
from logorator import Logger

@Logger()
def example_function(x, y):
    return x + y

result = example_function(3, 5)

# Output:
# Running example_function
#   3
#   5
# Finished example_function Time elapsed: 0.10 ms
```

## Core Concepts

Logorator works primarily through the `Logger` class, which serves as a decorator for functions. When a decorated function is called, logorator logs:

1. The function name when it starts
2. All arguments passed to the function
3. The function name when it finishes, along with execution time

For nested function calls, logorator maintains a hierarchical structure with proper indentation, making it easy to trace execution flow.

### Key Features

- **Hierarchical Logging**: Nested function calls are properly indented
- **Execution Time Tracking**: Measures and reports execution time for functions
- **ANSI Color Support**: Uses colors in console output for better readability
- **File Output**: Option to write logs to a file instead of stdout
- **Custom Notes**: Add custom notes to your logs at any point
- **Multiple Output Modes**: Choose between normal (newline-separated) and short (tab-separated) formats

## API Reference

### Logger Class

#### Constructor

```python
Logger(silent=None, mode="normal", override_function_name=None)
```

- **silent** (bool, optional): If True, suppresses logging output. Defaults to None, which uses the global `Logger.SILENT` value.
- **mode** (str, optional): Determines the logging format. Options are 'normal' (default) or 'short' (tab-separated).
- **override_function_name** (str, optional): If provided, uses this name in logs instead of the actual function name.

#### Class Methods

##### `set_silent(silent=True)`

Sets the global silent mode for all Logger instances.

- **silent** (bool): If True, suppresses all logging output globally. Defaults to True.

##### `set_output(filename=None)`

Sets the global output file for all Logger instances.

- **filename** (str | None): The path to the file where logs should be written. If None, logs are written to the console.

##### `note(note="", mode="normal")`

Logs a custom note with the current logging level's indentation.

- **note** (str): The custom message to log. Defaults to an empty string.
- **mode** (str): The logging mode ('normal' or 'short'). Defaults to 'normal'.

##### `log(message="", end="")`

Static method to write a log message.

- **message** (str): The message to log.
- **end** (str): The string appended after the message (default is empty string).

#### Instance Methods

##### `eol()`

Returns the end-of-line character(s) based on the current mode.

##### `ensure_newline()`

Ensures a newline is printed if the nesting level increases.

##### `__call__(func)`

Makes Logger instances callable as decorators.

- **func** (callable): The function to decorate.

### Global Variables

- **LOG_LEVEL**: Current nesting level of function calls
- **LAST_LOG_LEVEL**: Previous nesting level
- **LAST_LOG_MODE**: Previous logging mode
- **SILENT**: Global flag to suppress all logging
- **OUTPUT_FILE**: Global setting for log file path

## Configuration Options

### Logging Modes

- **normal**: Each log entry appears on a new line (default)
- **short**: Log entries are separated by tabs, useful for compact logging

### Output Destinations

- **Console Output**: Default behavior
- **File Output**: Set with `Logger.set_output("path/to/file.log")`

### Silence Control

- **Per-Instance**: `Logger(silent=True)`
- **Global**: `Logger.set_silent(True)`

## Advanced Usage

### Nested Function Calls

Logorator automatically handles nested function calls with proper indentation:

```python
from logorator import Logger

@Logger()
def outer_function(x):
    return inner_function(x * 2)

@Logger()
def inner_function(y):
    return y + 5

result = outer_function(10)

# Output:
# Running outer_function
#   10
# Running inner_function
#   20
# Finished inner_function Time elapsed: 0.05 ms
# Finished outer_function Time elapsed: 0.15 ms
```

### Custom Notes

Add custom notes at any point in your code:

```python
from logorator import Logger

@Logger()
def process_data(data):
    # Some processing
    Logger.note("Data validation complete")
    # More processing
    Logger.note("Processing step 2 complete")
    return processed_data

process_data([1, 2, 3])
```

### Custom Function Names

Override the displayed function name:

```python
@Logger(override_function_name="DataProcessor")
def process_data(data):
    # Function logic here
    return processed_data
```

### Logging to File

```python
# Set up file logging
Logger.set_output("logs/application.log")

@Logger()
def main():
    # Your application logic
    pass

main()
```

## Examples

### Basic Logging

```python
from logorator import Logger

@Logger()
def calculate(a, b, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "multiply":
        return a * b
    else:
        raise ValueError(f"Unknown operation: {operation}")

result = calculate(5, 3)
result = calculate(5, 3, operation="multiply")
```

### Conditional Logging

```python
from logorator import Logger
import os

# Enable logging only in development
is_dev = os.environ.get("ENVIRONMENT") == "development"
Logger.set_silent(not is_dev)

@Logger()
def my_function():
    # Function logic
    pass
```

### Temporary File Logging

```python
from logorator import Logger
import contextlib

@contextlib.contextmanager
def log_to_file(filename):
    previous_output = Logger.OUTPUT_FILE
    Logger.set_output(filename)
    try:
        yield
    finally:
        Logger.set_output(previous_output)

with log_to_file("debug_session.log"):
    # All logging in this block goes to the file
    @Logger()
    def debug_function():
        # Function logic
        pass
    
    debug_function()
```

## Best Practices

1. **Use Meaningful Function Names**: Since function names appear in logs, use descriptive names.

2. **Control Verbosity**: Use the `silent` parameter to control logging at different levels of your application.

3. **Switch to File Logging in Production**: Console logging can impact performance in production environments.

4. **Add Strategic Notes**: Use `Logger.note()` at key points in your code to mark significant events or state changes.

5. **Handle Large Arguments**: Be aware that arguments are converted to strings and truncated at 1000 characters in the logs.

6. **Consider Thread Safety**: While logorator uses class variables for state, be cautious in highly concurrent environments.

7. **Clear Log Files Regularly**: If using file output, implement a rotation strategy to prevent files from growing too large.

8. **Use Short Mode for Compact Logs**: When logging many small functions, consider using `mode="short"` for more compact output.
