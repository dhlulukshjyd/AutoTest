# Author: jiangchunxiao

import logging
import LogAndResultPath
import os


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def GetRunDirectory():
    allRunFolders = [fd for fd in os.listdir(".") if os.path.isdir(fd) and fd.startswith("TestRun")]
    latestFolder = max(allRunFolders, key=os.path.getmtime)
    return latestFolder

def CreateLoggerFile(filename):
    try:
        path = LogAndResultPath.GetLogAndResultDirectory()
        logpath = path[0]
        fulllogname = logpath + "\\" + filename + ".log"
        fh = logging.FileHandler(fulllogname)
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s [line:%(lineno)d] %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    except Exception as err:
        logger.debug("Error when creating log file, error message: {}".format(str(err)))


def Log(message):
    logger.debug(message)