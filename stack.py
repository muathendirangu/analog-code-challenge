class MaxStack:
    def __init__(self):
        self.items = []
        self.trackMaxItem = []

    def push(self, item):
        self.items.append(item)
        if (len(self.items) == 1):
            self.trackMaxItem.append(item)

        if (item > self.trackMaxItem[-1]):
            self.trackMaxItem.append(item)

        else:
            self.trackMaxItem.append(self.trackMaxItem[-1])

    def pop(self):
        self.items.pop()
        self.trackMaxItem.pop()

    def is_empty(self):
        if self.items == []:
            return None

    def max(self):
        return self.trackMaxItem[-1]


if __name__ == "__main__":
    s = MaxStack()
    s.push(1)
    s.push(4)
    s.push(7)
    s.push(2)
    print(s.max())

    s.pop()
    s.pop()
    print(s.max())
