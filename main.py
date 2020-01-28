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
START_RNUM = 1

class Character:
    def __init__(self, name, shortdesc, longdesc, location=START_RNUM, gold=0, inventory=[]):
        self.name = name
        self.shortdest = shortdesc
        self.longdest = longdesc
        self.gold = gold
        self.inventory = inventory
        self.location = gamestate.roomdict[location]


class Command:
    def __init__(self, name, min_argc, function, docs):
        self.name = name
        self.min_argc = min_argc
        self.function = function
        self.docs = docs

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
        self.ticks = 0

    def input_loop(self):
        pass

    def tick(self):
        pass

    def addcommand(self,name,min_argc,function):
        self.commandlist.append(Command(name,min_argc,function))

    def timerloop(self):
        starttime = time.time()
        while self.closing != True and self.character.dead != True:
            time.sleep(TICK_SECONDS - ((time.time()) - starttime) % TICK_SECONDS)
            self.ticks += 1
            self.tick()