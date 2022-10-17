#! /usr/bin/env python3

from enum import Enum

class GlobalSettings():
    pass

class Protagonist():
    def __init__(self, _name):
        self.name = _name


class Option():
    def __init__(self, _line):
        pass

class EventType(Enum):
    Story = 0


class Event():
    def __init__(self, _line):
        self.type, self.id, self.options, self.text = self.parser(_line)

    def parser(self, _line):

        # for story events, these lines will start with 'S'
        if _line[0] == 'S':
            event_id, options, text = _line.split("//")
            event_options = [Option(item) for item in options.split(",")]
            return EventType.Story, int(event_id[1:]), event_options, text.strip()


def main(example):
    event = Event(example)
    print(event.type)
    print(event.id)
    print(event.options)
    print(event.text)

if __name__ == "__main__":
    example = "S123 // S002[], S003[]// メイドカフェにようこそ♡"
    main(example)

