#!/usr/bin/python3
"""return path name."""
import sys
"""syst ."""
import os
"""os save ."""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""Load and save file"""

args = sys.argv
del args[0]
filename = "add_item.json"
my_list = []

if os.path.exists(filename):
    load = load_from_json_file(filename)
    if len(args) > 0:
        my_list.extend(load)
        my_list.extend(args)
        save_to_json_file(my_list, filename)

else:
    save_to_json_file(my_list, filename)
