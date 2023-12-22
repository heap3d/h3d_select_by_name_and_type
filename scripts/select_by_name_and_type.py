#!/usr/bin/python
# ================================
# (C)2019-2022 Dmytro Holub
# heap3d@gmail.com
# --------------------------------
# modo python
# select items by type and search string in the name
# ================================

import modo
import lx

import h3d_utilites.scripts.h3d_utils as h3du
from h3d_select_by_name_and_type.scripts.select_items import select_items


USERVAL_NAME_SEARCH_TYPE = 'h3d_sbnt_search_type'
USERVAL_NAME_SEARCH_STR = 'h3d_sbnt_search_str'


def main():
    print('')
    print('start select_by_name_and_type.py...')

    USERVAL_VAL_SEARCH_TYPE = h3du.get_user_value(USERVAL_NAME_SEARCH_TYPE)
    SEARCH_TYPE = None if USERVAL_VAL_SEARCH_TYPE == '' else USERVAL_VAL_SEARCH_TYPE
    SEARCH_STR = h3du.get_user_value(USERVAL_NAME_SEARCH_STR)

    if not lx.args():
        items = modo.Scene().items(itype=SEARCH_TYPE)
    elif lx.args()[0] == 'selected':
        items = modo.Scene().selected
    else:
        items = modo.Scene().items(itype=SEARCH_TYPE)

    modo.Scene().deselect()
    select_items(from_items=items, search_str=SEARCH_STR, itype=SEARCH_TYPE)

    print('done.')


if __name__ == '__main__':
    main()
