from markdownify import markdownify as md
from typing import Optional, Union


def cache_find(diff: Union[dict, list]) -> Optional[str]:
    values = diff if isinstance(diff, list) else diff.values()
    for value in values:
        if isinstance(value, (list, dict)):
            if cache := cache_find(value):
                return cache
        if isinstance(value, str) and value.startswith(("<p>", "<h1>")):
            return md(value).strip()

    return None
