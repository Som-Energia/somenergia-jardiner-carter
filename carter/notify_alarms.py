import sys
import pendulum
from sqlalchemy import create_engine


def notify_alarms():

  args = sys.argv[1:]
  data_interval_start=pendulum.parse(args[0])
  data_interval_end=pendulum.parse(args[1])

  engine = create_engine(args[2])
  notifier_smtp_url = args[3]
  notifier_smtp_port = args[4]
  notifier_smtp_user = args[5]
  notifier_smtp_password = args[6]

  print(f"Sending alert to {notifier_smtp_url}:{notifier_smtp_port} as {notifier_smtp_user}")

if __name__ == '__main__':
    notify_alarms()