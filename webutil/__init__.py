import json
import os

# get Data
def get(id):
  return json.loads(open(os.path.join("./data",id + ".json"),"r"))
  
def create(id,arch):
  d = open(os.path.join("./data",id + ".json"),"w+")
  d.write(json.dumps(arch))
  print("Created JSON data file.")
  return d
