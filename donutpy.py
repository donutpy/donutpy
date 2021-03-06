import os
import util.getarguments
import sys
import glob
import json
from util.getarguments import *

def initiate():
  if os.path.isdir("./page"):
    print("Folder PAGE exists.")
    if os.path.isdir("./data"):
      print("Folder DATA exists.")
    else
      print("Creating folder DATA.")
      mkdirs("./data")
  else:
    print("Creating folder PAGE.")
    mkdirs("./page")
    if os.path.isdir("./data"):
      print("Folder DATA exists.")
    else
      print("Creating folder DATA.")
      mkdirs("./data")

def buildPages():
  exists1,var1 = Argument("-bp","--buildPages",sys.argv)
  if var1 == True:
    for file in glob.glob("./data/*.json"):
      d = json.loads(open(file,"r"))
      for page in glob.glob("./page/*.py"):
        x = open(page[:-3] + ".cgi",w+)
        exec(compile("import cgi\nimport donutpy.webutil as donut\n from donut import *\nGET={}\n args=os.getenv(\"QUERY_STRING\").split('&')\n for arg in args: \nt=arg.split('=') \nif len(t)>1: k,v=arg.split('='); GET[k]=v\n" + open(page,"r").read()))
