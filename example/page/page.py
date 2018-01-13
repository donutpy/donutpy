#!bin/python
print("data:text/html\n")
print("{name}\n{data}")
dat = donut.FieldStorage()
print(dat["name"])
