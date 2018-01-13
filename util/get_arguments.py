class Argument:
  id = ""
  long = ""
  args = []
  def __init__(self,id,long,args):
    self.id = id
    self.long = long
    self.args = args
  def get(self):
    if self.args.contains(self.id) or self.args.contains(self.long):
      i = 1
      while i < len(self.args):
        if self.args[i] == self.id:
          return True,self.args[i+1]
        elif self.args[i] == self.long:
          return True,True
        else:
          return False,"No argument found with the name " + self.long + " or the name " + self.id + "."
