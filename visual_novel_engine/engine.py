#! /usr/bin/env python3

from enum import Enum

class GlobalSettings():
    pass

class Protagonist():
    def __init__(self, _name):
        self.name = _name

class Auxiliary():
    @staticmethod
    def event_type(_string):
        if _string == "S":
            return EventType.Story
        else:
            raise Exception("Parsing error.")

class EventType(Enum):
    Story = 0

class Option():
    def __init__(self, _line):
        self.type, self.id, self.text = self.parser(_line)
    
    def parser(self, _line):
        full_id, text = _line.split("[")
        full_id = full_id.strip()
        print(full_id[0])
        text = text.replace("]", "")
        text = text.strip()
        return Auxiliary.event_type(full_id[0]), int(full_id[1:]), text

    def __str__(self) -> str:
        _ = "OPTION OBJECT\nEvent Type: {}\nID: {}\nText: {}"
        return _.format(str(self.type), str(self.id), self.text)




class Event():
    def __init__(self, _line):
        self.type, self.id, self.options, self.text = self.parser(_line)

    def parser(self, _line):

        # for story events, these lines will start with 'S'
        if _line[0] == "S":
            full_id, options, text = _line.split("//")
            event_options = [Option(item) for item in options.split(",")]
            return EventType.Story, int(full_id[1:]), event_options, text.strip()
        
        else:
            raise Exception("Parsing error.")


def main(example):
    event = Event(example)
    print(event.type)
    print(event.id)
    print()
    for item in event.options:
        print(item)
    print()
    print(event.text)

if __name__ == "__main__":
    example = "S123 // S002[次], S003[この次]// メイドカフェにようこそ♡"
    main(example)

