class AddWords():
    def __init__(self, word):
        self.word = word

    def __str__(self):
        print(f"\nWord >>>\t{self.word}")

    def left_insert(self):
        left_add = input("Add : ")
        self.word = left_add + self.word

    def right_insert(self):
        right_add = input("Add : ")
        self.word = self.word + right_add

    def side_ask(self):
        while True:
            self.__str__()
            count = 0
            ask_side = input(f"Which side you want to add R / L\n{count}. Turn.: ")
            count += 1
            if ask_side.upper() == "R":
                self.right_insert()
            elif ask_side.upper() == "L":
                self.left_insert()

word = input("Lets begin >>> ")
scrabble = AddWords(word)
scrabble.side_ask()
