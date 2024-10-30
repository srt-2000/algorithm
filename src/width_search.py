from collections import deque


class MSearcher:

    def __init__(self):
        self.person = None
        self.searched = None
        self.search_queue = None
        self.name = None
        self.graph_ = None

    def search_mango_seller(self, name, graph_):
        self.graph_ = graph_
        self.name = name
        self.search_queue = deque()
        self.search_queue += self.graph_[self.name]
        self.searched = []
        while self.search_queue:
            self.person = self.search_queue.popleft()
            if self.person not in self.searched:
                if self.person[-1] == "m":
                    print(self.person, "is mango seller")
                    print("I've already checked this friends:\n", self.searched)
                    return True
                else:
                    self.searched.append(self.person)
                    self.search_queue += graph_[self.person]
        print("I've already checked this friends:\n", self.searched)
        print(f"There are not mango-sellers in {self.name}s friends circle")
        return False
