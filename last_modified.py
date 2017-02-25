#! /usr/bin/python

import os
import sys
import datetime


def list_files(dir):
    file_mtime_list = []
    for top, sub_dir, file_list in os.walk(dir):
        if file_list:
            for file in file_list:
                file_mtime_list.append((file, os.path.getmtime(os.path.join(top, file))))

    sorted_file_list = sorted(file_mtime_list, key=lambda x: x[1], reverse=True)
    for file in sorted_file_list:
        print(file[0], ": ", datetime.datetime.fromtimestamp(file[1]).strftime('%c'))


if __name__ == '__main__':
    if os.path.isdir(sys.argv[1]):
        list_files(sys.argv[1])
