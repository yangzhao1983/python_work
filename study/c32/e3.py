from study.c32.e2 import MyList
class SubMyList(MyList):
    count = 0
    def __init__(self, start=[]):
        self.adds = 0
        MyList.__init__(self, start)
