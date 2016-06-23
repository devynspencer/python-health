#!/usr/bin/env python

import argparse
import os
import time

def stale_at(time, minutes):
    return time - (minutes * 60)

def modified_at(file):
    return os.path.getctime(file)

def is_stale(file):
    return stale_at(time.time(), args.threshold) > modified_at(file)

def stale_files(files):
    stale_files = []
    [stale_files.append(file) for file in files if is_stale(file)]
    return stale_files

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check for unmodified files within a time frame.")
    parser.add_argument("threshold", default=30, type=int, nargs="?", help="minutes a file can be unmodified for without being considering 'stale', ex: 30")
    parser.add_argument("files", default=[], nargs="*", help="list of files to check, ex: /var/log/messages /var/log/mail.log")
    args = parser.parse_args()

    for stale in stale_files(args.files):
        print stale