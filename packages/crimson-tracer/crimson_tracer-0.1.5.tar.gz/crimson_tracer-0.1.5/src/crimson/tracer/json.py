import json
from typing import Any, Dict, List, Tuple, Union

def stringify_keys(data: Any) -> Any:
    """
    Recursively converts all dictionary keys to strings.

    Args:
        data (Any): The input data.

    Returns:
        Any: The modified data with all dictionary keys as strings.
    """
    if isinstance(data, dict):
        return {str(k): stringify_keys(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [stringify_keys(item) for item in data]
    elif isinstance(data, tuple):
        return tuple(stringify_keys(item) for item in data)
    else:
        return data


class AllStringEncoder(json.JSONEncoder):
    """
    Custom JSON encoder that converts non-serializable objects to strings.
    """
    def default(self, obj: Any) -> Any:
        try:
            return super().default(obj)
        except TypeError:
            return str(obj)


def dumps(data: Any, indent: int = 2) -> str:
    """
    Converts data into a JSON-formatted string.

    - Converts dictionary keys to strings.
    - Handles non-serializable objects by converting them to strings.

    Args:
        data (Any): The input data to serialize.
        indent (int): Number of spaces for indentation in JSON formatting.

    Returns:
        str: A JSON-formatted string.
    """
    # Convert all dictionary keys to strings
    stringified_data = stringify_keys(data)

    # Serialize to JSON
    return json.dumps(stringified_data, cls=AllStringEncoder, indent=indent)
