import argparse

DESCRIPTION = "Basic CLI interface for @soyaya_bot"

class Cli():
    def __init__(self, argv):
        self.parser = argparse.ArgumentParser(description=DESCRIPTION)
        self.add_args()
        self.args = self.parse_args(argv)
        self.check_valid_command()

    def add_args(self):
        self.parser.add_argument('command', type=str,
            help="Type of functionality to execute: look/listen")

    def parse_args(self, argv):
        return self.parser.parse_args(argv)

    def check_valid_command(self):
        if self.args.command not in ['look', 'listen']:
            raise NotImplementedError
