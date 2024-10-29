class VoteChecker:

    def __init__(self, voted_list):
        self.voted_list = voted_list

    def check_vote(self, name):
        if self.voted_list.get(name):
            print("Get", name, "out")
        else:
            self.voted_list[name] = True
            print("Ok.Let", name, "vote")
