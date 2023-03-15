#!/usr/bin/python
# ================================
# (C)2019-2022 Dmytro Holub
# heap3d@gmail.com
# --------------------------------
# modo python
# select items by type and search string in the name
# ================================

def select_items(from_items, search_str='', itype=None):
    for item in from_items:
        if item.type != itype and itype is not None:
            continue
        if search_str.lower() not in item.name.lower():
            continue

        item.select()
