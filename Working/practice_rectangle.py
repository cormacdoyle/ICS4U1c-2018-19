class Rectangle(object):
    def __init__(self):
        self.width = 0
        self.height = 0
def get_area(rec):
    return(rec.width *rec.height)

def main():
    rect1 = Rectangle()
    rect1.height = int(input("What is the height?"))
    rect1.width = int(input("What is the width?"))
    print(get_area(rect1))

main()

