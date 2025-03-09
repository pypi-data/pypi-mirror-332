# Crimson Tracer

Crimson Tracer is a lightweight Python tracing utility that records function call events and provides useful insights into your code execution. It captures details such as function inputs, file names, line numbers, and more, allowing you to analyze the call flow. Additionally, you can convert raw trace events into a nested tree structure and serialize them to JSON for further processing.

## Features

- **Function Call Tracing:** Automatically capture call, line, and return events during execution.
- **Tree Generation:** Convert a linear list of trace events into a nested tree structure for easy visualization.
- **JSON Serialization:** Serialize trace data to JSON, ensuring all dictionary keys are strings.
- **Frame Filtering:** Include or exclude specific frames based on filename patterns using the built-in `FrameFilter`.
- **Customizable Event Editing:** Modify trace events on the fly with an optional custom event editor.

## Install

```sh
pip install crimson-tracer
```

## Example

### Tracer

The `TraceManager` collects all called functions along with valuable details such as function inputs and execution context.  
For a complete example, see [tracer.ipynb](./example/tracer.ipynb).

```python
from crimson.tracer import TraceManager

def sample_function():
    # Your function logic here
    return "result"

# Run the tracer on the sample function
TraceManager.run_trace(sample_function, name="sample_trace")
trace_events = TraceManager.get_trace("sample_trace")
```

### Node

Convert the traced result into a nested tree structure for a clearer view of the call hierarchy using `generate_trace_tree`.  
For more details, refer to [node.ipynb](./example/node.ipynb).

```python
from crimson.tracer import generate_trace_tree, TraceManager

trace_events = TraceManager.get_trace("sample_trace")
trace_tree = generate_trace_tree(trace_events)
```

## API Overview

- **TraceManager:**  
  Manages the tracing process, collects trace events, and provides methods to run and retrieve traces.
  
- **TraceEvent:**  
  A Pydantic model that represents a trace event with details like function name, filename, line number, event type, local variables, and more.
  
- **generate_trace_tree:**  
  Transforms a list of trace events into a nested tree structure to reflect the call hierarchy.
  
- **dumps:**  
  Serializes trace data into a JSON-formatted string with all dictionary keys as strings.
  
- **FrameFilter:**  
  Allows filtering of stack frames based on inclusion and exclusion rules to refine the tracing process.

Crimson Tracer offers a flexible and efficient way to monitor and analyze function calls in your Python applications. Enjoy exploring your code's execution flow with ease!