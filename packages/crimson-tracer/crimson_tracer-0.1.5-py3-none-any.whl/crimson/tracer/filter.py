from types import FrameType
from typing import List, Optional

class FrameFilter:
    """
    A class for filtering stack frames during tracing.

    - If `include` is `None`, **all files are included**, and only `exclude` is applied.
    - If `include` is set, only matching patterns are included, and then `exclude` is applied.

    Args:
        include (Optional[List[str]]): A list of filename patterns to include (e.g., `["src/", "lib/"]`).
            If `None`, all files are included.
        exclude (Optional[List[str]]): A list of filename patterns to exclude (e.g., `["test/", "logs/"]`).
            If `None`, nothing is excluded.

    Examples:
        # 1. Include all files except specific patterns
        filter_all = FrameFilter(exclude=["test/", "logs/"])

        # 2. Include only specific directories and exclude certain files
        filter_specific = FrameFilter(include=["src/", "lib/"], exclude=["logs/"])

        # 3. Exclude specific file patterns
        filter_exclude_only = FrameFilter(exclude=["venv/", "test_"])
    """

    def __init__(self, include: Optional[List[str]] = None, exclude: Optional[List[str]] = None):
        self.include = include  # If None, all files are included
        self.exclude = exclude  # If None, nothing is excluded

    def __call__(self, frame: FrameType) -> bool:
        """
        Determines whether a given stack frame should be included based on filter conditions.

        - If `include` is `None`, all files are allowed, and `exclude` is applied.
        - If `include` is set, only files matching the patterns are allowed, and then `exclude` is applied.

        Args:
            frame (FrameType): The stack frame to check.

        Returns:
            bool: `True` if the frame should be included, `False` otherwise.
        """
        filename = frame.f_code.co_filename

        # 1. If include is set, allow only matching files
        if self.include is not None and not any(path in filename for path in self.include):
            return False

        # 2. If exclude is set, filter out matching files
        if self.exclude is not None and any(term in filename for term in self.exclude):
            return False

        return True
