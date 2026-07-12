#parse the JSON into dicts, then compare launch_time to current time among those with "running" state

import argparse
import json
from datetime import datetime, timezone

def main():
  parser = argparse.ArgumentParser(description="determine which EC2 instances have been running 24+ hours")
  parser.add_argument('-f', '--file', type=str, required=True, help='The JSON file to be scanned')
  args = parser.parse_args()
  running_instances: list = []

  #get the running instances, ignore the rest
  with open(args.file) as f:
    instances = json.load(f)['Reservations']
    running_instances = [instance for instance in instances if instance['Instances'][0]['State']['Name'] == 'running']

  current_time = datetime.now(timezone.utc).isoformat()
  t1 = datetime.fromisoformat(current_time)
  output: list = []
  for instance in running_instances:
    launch_time = instance['Instances'][0]['LaunchTime']
    t2 = datetime.fromisoformat(launch_time)
    diff = t2 - t1
    diff_hours = abs(diff.total_seconds() / 3600)
    if diff_hours > 24:
      output.append({'id': instance['Instances'][0]['InstanceId'], 'uptime': f'{diff_hours} hours'})
  print(output)

if __name__ == '__main__':
  main()