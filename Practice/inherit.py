class Properties:
    def __init__(self, color, border_wt):
        self.color = color
        self.border_wt = border_wt
        print("Setting Values of colour and Border weight in Parent class.\n")
    
    def print2(self):
        print(f"Colour = {self.color}, Border Size = {self.border_wt}. (Parent Class)")

class Polygon(Properties):
    def __init__(self, sides, color, border_wt):
        super().__init__(color, border_wt)  # Initialize the parent class
        self.no_of_sides = sides

    def print1(self):
        print(f"The polygon is of {self.no_of_sides} sides. (Child Class)\n")

def main():
    # The Polygon class now also requires color and border weight arguments
    obj = Polygon(4, 'Red', 5)
    obj.print1()
    obj.print2()

if __name__ == '__main__':
    main()
