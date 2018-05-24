# -*- coding: utf-8 -*-
from read_controller import read_controller
import os

def excute_controller():
    controllers = read_controller()
    for controller in controllers:
        if controller != 'F:\\AutoTest\\BusinessAction\\create_controller.py':
            os.system('python '+controller)
