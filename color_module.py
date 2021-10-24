class Color:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
    def __str__(self):
        return f"Color: R={self.red}, G={self.green}, B={self.blue}"