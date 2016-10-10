class stack(object):
    def __init__(self):
        self.lst=[]

    def isEmpty(self):
        return len(self.lst)==0

    def top(self):
        if not isEmpty(self.lst):
            return self.lst[-1]

    def getSize(self):
        return len(self.lst)

    def pop(self):
        if not isEmpty(self.lst):
            A=self.lst
            self.lst.pop()
            return A
    
