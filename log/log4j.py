# coding=UTF-8
import os
import datetime

class Log4j(object):
    def writelog(self,path,content):
        filename=path
        now_time=datetime.datetime.now().strftime('%F %T')
        writeDate="时间："+now_time+"---"+content
        with open(filename,"a") as file_object:
            file_object.write(writeDate+"\n")


if __name__=='__main__':
    path="E:/Python/WeiboYouth/log4j.txt"
    content="null"
    log4j=Log4j()
    log4j.writelog(path,content)