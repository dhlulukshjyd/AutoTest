# -*- coding:utf-8 -*-
# Author: jiangchunxiao

import os
from datetime import datetime
from lxml import etree
from lxml import html
import LogAndResultPath
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class TestReport(object):
    """description of class"""
    def __init__(self):
        # format = "%Y%m%d%H%M%S"
        # currentday = datetime.now().strftime(format)
        logandresultpath = LogAndResultPath.GetLogAndResultDirectory()
        resultpath = logandresultpath[1]
        #self.reportfile = resultpath + "\TestResult" + currentday + ".html"
        self.reportfile = resultpath + "\TestResult.html"

    # 创建测试html报告
    def CreateHtmlFile(self):
        if os.path.exists(self.reportfile) is False:
            f = open(self.reportfile, 'w')
            message = """<html>
            <head>    
                <title>Automation Test Result</title>
                <style>
                    table {
                            border-collapse: collapse;
                            padding: 15px;
                            font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
                            }
                    th{
                        background-color: green;
                        color: white;
                        border: 1px solid #ddd;
                        padding-bottom: 15px;
                        padding-top: 15px;
                    }
                    tr{
                        border: 1px solid #008000;
                        padding-bottom: 8px;
                        padding-top: 8px;
                        text-align: left;
                    }
                    td{
                        border: 1px solid #008000;
                    } 
                </style>
            </head>
            <body>
                <h1>Automation Test Result</h1>
                <table>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Owner</th>
                        <th>Result</th>
                        <th>StartTime</th>
                        <th>EndTime</th>
                        <th>Duration(s)</th>
                        <th>ErrorMessage</th>
                   </tr>
                </table>
            </body>
            </html>
            """
            f.write(message)
            f.close()

    def WriteHTML(self, testcaseinfo):
        # 创建Html文件
        self.CreateHtmlFile()

        f = open(self.reportfile, "r")

        htmlcontent = f.read()
       # print htmlcontent
        f.close()
        # tree = mytree.fromstring(str(htmlcontent))
        htmlcontent.encode('utf-8')
        tree = html.fromstring(htmlcontent)
        tableElem = tree.find(".//table")
        if testcaseinfo.result == "Failed":
            mytablerow = "<tr><td>{0}</td><td>{1}</td><td>{2}</td><td bgcolor=\"#FF0000\">{3}</td><td>{4}</td><td>{5}</td><td>{6}</td><td>{7}</td></tr>".format(
                testcaseinfo.id, testcaseinfo.name, testcaseinfo.owner, testcaseinfo.result, testcaseinfo.starttime,
                testcaseinfo.endtime, testcaseinfo.secondsDuration, testcaseinfo.errorInfo)
        else:
            mytablerow = "<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td><td>{5}</td><td>{6}</td><td>{7}</td></tr>".format(
                testcaseinfo.id, testcaseinfo.name, testcaseinfo.owner, testcaseinfo.result, testcaseinfo.starttime,
                testcaseinfo.endtime, testcaseinfo.secondsDuration, testcaseinfo.errorInfo)
        tableElem.append(etree.HTML(str(mytablerow)))

        f = open(self.reportfile, "w")
        # html.tostring
        newContent = repr(html.tostring(tree, method="html", pretty_print=True))
        newContent = newContent.replace(r"\n", "").replace(r"\t", "").replace("'", " ")
        newContent = newContent[:len(newContent) - 1]
        f.write(newContent)
        f.close()