import cv2
import pyautogui

import sys
import time
import subprocess

def mouse_click():
    if sys.platform == 'linux':
        subprocess.call(['xdotool', 'mousedown', '1'])
        time.sleep(0.02)
        subprocess.call(['xdotool', 'mouseup', '1'])
    elif sys.platform == 'win32':
        pyautogui.mouseDown()
        time.sleep(0.02)
        pyautogui.mouseUp()
    else:
        raise Exception("This system is not supported yet: {0}".format(sys.platform))

class InitializationFisherState():
    def __init__(self):
        self.code = "INIT"
        self.description = "Waiting for user..."

    def update(self, sense):
        if sense > 1:
            return CastingFisherState(cast = False)
        else: return None

class CastingFisherState():
    def __init__(self, cast = True):
        self.code = "CAST"
        self.description = "Casting the line"
        self.created_at = time.time()
        if cast: mouse_click()

    def update(self, sense):
        if (time.time() - self.created_at) > 1 and sense < 1:
            return WaitingFisherState()
        else: return None

class WaitingFisherState():
    def __init__(self):
        self.code = "WAIT"
        self.description = "Waiting for movement"
        self.created_at = time.time()

    def update(self, sense):
        if (time.time() - self.created_at) > 1 and sense > 1:
            return ReelingInFisherState()
        else: return None

class ReelingInFisherState():
    def __init__(self):
        self.code = "REEL"
        self.description = "Hooked - reeling in"
        self.created_at = time.time()
        mouse_click()

    def update(self, sense):
        if (time.time() - self.created_at) > 0.5 and sense < 1:
            return CastingFisherState()
        else: return None


class FisherStateMachine():
    def __init__(self):
        self.state = InitializationFisherState()

    def update(self, sense):
        result = self.state.update(sense)
        if result:
            self.state = result
