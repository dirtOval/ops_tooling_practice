#!/usr/bin/env python3
import argparse
import json

def parse_logs(file):
  with open(file) as f:
    for x in f:
      print(x)


parse_logs('test_logs.txt')

#we're going to make a shell script that will read a log file containing JSON
#and parse it, providing data about the messages.

#first up is counting logs by severity
#could also be cool to detect duplicates
#really cool would be to make it listen. point it at a stream and report on
#that
#not sure if that last one is happening tho. one thing at a time!