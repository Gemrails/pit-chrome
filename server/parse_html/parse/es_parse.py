#!/usr/bin/python
#coding=utf-8

from bs4 import BeautifulSoup
from public_func import write_txt

class EsParse():
    def init(self):
        self.path = "/tmp"
        pass

    def parse(self, html_doc):
        soup = BeautifulSoup(html_doc)
        full_text = soup.get_text()
        mm = full_text.encode("UTF-8").split("导出PDF")[1]
        if len(mm)< 3:
            print "非es网页"
            return
        text = "\n".join(mm.split("\n\n\n\n"))
        try:
            write_txt(self.path, text)
        except Exception, e:
            print "write txt error, {}".format(str(e))