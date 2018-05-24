# -*- coding: utf-8 -*-
import sys
import os

def read_controller():
    path = os.path.abspath(os.path.dirname(__file__))
    parentpath = os.path.dirname(path)
    controllerFilePath = os.path.join(parentpath,'BusinessAction', 'all_controller.txt')
    controller = []
    for line in open(controllerFilePath):
        print line
        if '#' not in line:
            controller.append(line.replace('\n',''))
    return controller
