#!/usr/bin/env python3
import argparse
import json

def count_by_level(file, service=None):
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
      if service and log['service'] not in service:
        continue
      if log['level'] in log_count:
        log_level: string = log['level']
        log_count[log_level] += 1
      else:
        raise KeyError(f'Error level not found: {log_level}')
  return log_count

def main():
  parser = argparse.ArgumentParser(description="Count error logs by severity level")
  parser.add_argument('-f', '--file', type=str, default=None, help='The log file to be parsed' )
  parser.add_argument('-s', '--service', type=str, nargs='*', default=None, help='The service(s) to be monitored.')
  args = parser.parse_args()

  result = count_by_level(args.file, args.service)
  output_text: str = ''
  if args.service:
    output_text += 'services monitored: '
    for service in args.service: output_text += f'{service} '
    output_text += '\n'
  for x in result.keys():
    output_text += f'{x}: {result[x]}\n'
    # print(f'{x}: {result[x]}')
  print(output_text)
if __name__ == "__main__":
  main()
#we're going to make a shell script that will read a log file containing JSON
#and parse it, providing data about the messages.

#first up is counting logs by severity
#could also be cool to detect duplicates
#really cool would be to make it listen. point it at a stream and report on
#that
#not sure if that last one is happening tho. one thing at a time!