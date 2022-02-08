class priority_queue:
    def __init__(self):
        self.value_of = {}
        self.size = 0

    def add(self,value,item):
        ## check if its in the queue already
        try:
            value2 = self.value_of[hash(item.key())][0]
            if value2 > value:
                self.value_of[hash(item.key())] = (value,item)
        except KeyError:
            self.value_of[hash(item.key())] = (value,item)
            self.size+=1

    def get(self):
        min = 100000
        min_item = None
        for hashed_item in self.value_of.keys():
            current_cost, current_item = self.value_of[hashed_item]
            if current_cost < min:
                min_item = current_item
        self.size-=1
        del self.value_of[hash(min_item.key())]
        return min_item
