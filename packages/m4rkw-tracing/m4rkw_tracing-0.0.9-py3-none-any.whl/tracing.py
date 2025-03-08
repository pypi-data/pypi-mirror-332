import os
import sys
import yaml
import traceback
from singleton import Singleton
from pushover import Client

class Tracing(metaclass=Singleton):

    def __init__(self, label):
        config_file = "/etc/tracing.yaml"

        if not os.path.exists(config_file):
            raise Exception(f"config file not found: {config_file}")

        self.config = yaml.safe_load(open(config_file).read())

        self.label = label

        self.state_file = f"/tmp/.tracing_{os.getuid()}_{self.label}"

        if os.path.exists(self.state_file):
            self.state = int(open(self.state_file).read().rstrip())
        else:
            self.state = 0
            self.save_state()

        system = os.popen("uname").read().rstrip().lower()
        self.pushover = pushover = Client(self.config['pushover']['user'], api_token=self.config['pushover'][system])


    def save_state(self):
        with open(self.state_file + '.new', 'w') as f:
            f.write(str(self.state))
        os.rename(self.state_file + '.new', self.state_file)


    def failure(self):
        self.state += 1

        exception = traceback.format_exc()
        with open(f"{self.state_file}.exception.new","w") as f:
            f.write(exception)
        os.rename(f"{self.state_file}.exception.new", f"{self.state_file}.exception")

        if self.state == self.config['threshold']:
            self.pushover.send_message(exception, title=self.label)

        self.save_state()


    def success(self):
        if self.state == 0:
            return

        self.state = 0

        if self.state >= self.config['threshold']:
            self.pushover.send_message('resolved', title=self.label)

        self.save_state()
