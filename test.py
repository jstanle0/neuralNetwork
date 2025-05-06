class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        if (y < -.25*x**2 + 5):
            self.state = 'bad'
        else:
            self.state = 'good'

    def __str__(self):
        return f"[{self.x}, {self.y}, {self.state}]"
    
if __name__ == '__main__':
    for x in range(10):
        for y in range(10):
            print(Point(x,y))