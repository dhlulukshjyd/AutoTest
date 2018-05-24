# -*- coding: utf-8 -*-
import sys
import os


# check the python file
def check_if_python(fileName):
    if fileName.endswith('.py'):
        return True


def create_controllerlist():
    path = sys.path[0]  # 该py文件所在的绝对路径F:\AutoTest\BusinessAction
    controllerlist = []
    # os.path.join(path, 'BusinessAction') --F:\AutoTest\BusinessAction
    for i in os.walk(path):
        for fileName in i[2]:
            if check_if_python(fileName):
                filepath = os.path.join(i[0], fileName)
                controllerlist.append(filepath)
    return controllerlist


def save_controller_file(controller):
    filePath = os.path.join(sys.path[0],'all_controller.txt')
    theFile = open(filePath,'w')
    for i in controller:
        theFile.write(i+'\n')
    theFile.close()


if __name__ == '__main__':
    controller = create_controllerlist()
    save_controller_file(controller)