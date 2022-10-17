#! /usr/bin/env python3

from enum import Enum

class GameSideSettings():
    input_not_interpretable = "ご主人さまあ〜！　ごめんなさい、よくわかりません。もう一度言ってください♡"
    exit_command = [
        "exit",
        "ex",
        "escape",
        "esc",
        "quit",
        "終了"
    ]

class Protagonist():
    def __init__(self, _name):
        self.name = _name

class Auxiliary():
    """ A class that contains all auxiliary functions.
    """
    @staticmethod
    def event_type(_string):
        """ Converts one letter strings to EventType.
        """
        if _string == "S":
            return EventType.Story
        else:
            raise Exception("Parsing error.")

    @staticmethod
    def check_exit_command(_string) -> bool:
        """ Checks string for an exit command in accordance to the valid commands defined in
        GameSideSettings.exit_command. Used to interpret user input.
        """
        for command in GameSideSettings.exit_command:
            if _string == command:
                return True
        return False

    # TODO
    @staticmethod
    def read_script():
        pass

class EventType(Enum):
    Story = 0

class Option():
    """ Class that represents an options given to the player. This class is NOT a collection of
    options (next events) associated to an event.

    Attributes:
        type (EventType): The event type of the option.
        id (int): The integer ID of the option.
        text (str): The text that represents the option. This is NOT
    """
    def __init__(self, _line):
        self.type, self.id, self.text = self.parser(_line)
    
    def parser(self, _line):
        full_id, text = _line.split("[")
        full_id = full_id.strip()
        text = text.replace("]", "")
        text = text.strip()
        return Auxiliary.event_type(full_id[0]), int(full_id[1:]), text

    def __str__(self) -> str:
        """ Used for debugging purposes.
        """
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


class Engine():

    def __init__(self, _change_this_later):
        self.event_cache = []
        self.current_event = Event(_change_this_later)

    def player_chooses_option(self):
        while True:
            user_input = input()
            if Auxiliary.check_exit_command(user_input):
                quit()
            for option in self.current_event.options:
                if user_input == option.text:
                    return option
            print(GameSideSettings.input_not_interpretable)

    def core_game_loop(self):
        while True:
            print(self.current_event.text)
            for option in self.current_event.options:
                print(option.text)
            decision = self.player_chooses_option()




class Graphic():
    pass




def main(example):


    engine = Engine(example[0])
    engine.core_game_loop()

if __name__ == "__main__":
    example = [
        "S0 // S1[中に入る], S2[やっぱり家に帰る]// メイドカフェにようこそ♡",
        "S2 // // ご主人さま♡　おかえりなさい♡",
        "S3 // // 恥ずかしすぎる。私は家に帰った。"
    ]
    main(example)

