class WordFinder:

    def __init__(self):
        self.word_table = {}
        self.word = None

    def find_world(self, word, word_table):
        self.word = word
        self.word_table = word_table
        if self.word in self.word_table:
            print("this world is on page -", self.word_table[self.word])
        if self.word not in self.word_table:
            print("there is no this word on our pages, sorry")
