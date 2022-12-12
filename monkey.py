class monkey:
    # monkey class constructor initializes and sets variables and makes inspections equal to 0
    def __init__(self, items, operation, test, true, false):
        self.items = items
        self.operation = operation
        self.test = test
        self.true = true
        self.false = false
        self.inspections = 0
    # addItem function adds x to items list
    def addItem(self, x):
        self.items.append(x)
    # removeItem removes the last element in the items list and returns it
    def removeItem(self):
        return self.items.pop(-1)