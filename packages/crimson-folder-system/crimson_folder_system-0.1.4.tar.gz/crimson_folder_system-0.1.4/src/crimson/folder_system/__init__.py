"""
---
```
Filter:
    - summary: Filter path to search
    - description: Use `FnFilter` or `ReFilter` as predefined `Filter`,
    or define your own `Filter`.
search:
    - summary: search folder or path
```
---
"""
from crimson.folder_system.filter import Filter, FnFilter, ReFilter
from crimson.folder_system.search import search
from crimson.folder_system.delete import delete_files
