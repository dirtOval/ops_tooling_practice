#!/usr/bin/env python3
import argparse
import json

def parse_logs(file):
  log_count: dict = {
    'DEBUG': 0,
    'INFO': 0,
    'WARN': 0,
    'ERROR': 0,
    'CRITICAL': 0,
  }
  with open(file) as f:
    for x in f:
      log = json.loads(x)
      print(log['level'])
      if log['level'] in log_count:
        log_level: string = log['level']
        log_count[log_level] += 1
      else:
        raise KeyError(f'Error level not found: {log_level}')
  print(log_count)
parse_logs('test_logs.txt')

#we're going to make a shell script that will read a log file containing JSON
#and parse it, providing data about the messages.

#first up is counting logs by severity
#could also be cool to detect duplicates
#really cool would be to make it listen. point it at a stream and report on
#that
#not sure if that last one is happening tho. one thing at a time!