import os
from typing import List

def normalize_filename(filename: str, keep_last: int) -> str:
    """
    Normalize a file path by keeping only the last `keep_last` segments.

    For example, if filename is '/home/user/project/module/script.py' and 
    keep_last=2, the function returns 'module/script.py'.
    """
    parts = filename.split(os.sep)
    return os.path.join(*parts[-keep_last:]) if len(parts) >= keep_last else filename
