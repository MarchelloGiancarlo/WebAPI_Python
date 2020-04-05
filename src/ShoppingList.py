class ShoppingList:
    def __init__(self):
        self.elementList = []

    def getElementListCount(self):
        return len(self.elementList)

    def addElement(self, name, quantity):
        for element in self.elementList:
            if element.name == name:
                element.quantity = int(element.quantity) + int(quantity)
                return "increased quantity in a existing element"
        self.elementList.append(Element(name, quantity))
        return "inserted new element"

    def getElementQuantity(self, name):
        for element in self.elementList:
            if element.name == name:
                return element.quantity
        return 0

    def getElementList(self):
        return self.elementList


class Element:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def getName(self):
        return self.name

    def getQuantity(self):
        return self.quantity


if __name__ == "__main__":
    print("Started directly ShoppingList.py")
