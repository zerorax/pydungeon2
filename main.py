#!/usr/bin/python3

import time
import interface
import resize


STATE_MENU = 0
STATE_NAME = 1
STATE_CLASS = 2
STATE_STATS = 3
STATE_INTRO = 4
STATE_INGAME = 5

TICK_SECONDS = 1.0


class Command:
    def __init__(self, name, min_argc, function,help):
        self.name = name
        self.min_argc = min_argc
        self.function = function
        self.help = help

    def execute(self,character, argc, argv):
        self.function(character, argc, argv)
        character.lastcommand = argv


class GameState:
    def __init__(self):
        self.state = STATE_MENU
        self.roomdict = {}
        self.npc_protos = {}
        self.npclist = []
        self.commandlist = []
        self.closing = False

    def loop(self):
        pass

    def addcommand(self,name,min_argc,function):
        self.commandlist.append(Command(name,min_argc,function))

    def timerloop(self):
        starttime = time.time()
        while self.closing != True and self.character.dead != True:
            time.sleep(TICK_SECONDS - ((time.time()) - starttime) % TICK_SECONDS)