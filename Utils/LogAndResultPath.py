# Author: jiangchunxiao
import os


def GetLogAndResultDirectory():
    path = os.path.abspath(os.path.dirname(__file__))
    parentpath = os.path.dirname(path)
    logpath = os.path.join(parentpath, 'Log')
    resultpath = os.path.join(parentpath, 'Result')
    return logpath, resultpath

