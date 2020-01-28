#!/usr/bin/python3

import time
import interface
import resize


class Command:
    def __init__(self, name, min_argc, function):
        self.name = name
        self.min_argc = min_argc
        self.function = function


STATE_NAME = 0
STATE_CLASS = 1
STATE_STATS = 2
STATE_INTRO = 3
STATE_INGAME = 4


class GameState:
    def __init__(self):
        self.state = STATE_NAME
        self.roomdict = {}
        self.npc_protos = {}
        self.npclist = []

    def loop(self):
        pass
