from .base_image import BaseImage

class Square(BaseImage):
    def __init__(self, square_size=100):
        super().__init__()
        self.square_size = square_size

    def create_image(self):
        # Calculate the position of the square
        left = (self.width - self.square_size) // 2
        top = (self.height - self.square_size) // 2
        right = left + self.square_size
        bottom = top + self.square_size
        
        # Draw a black square
        self.draw.rectangle([(left, top), (right, bottom)], fill='black')
        return self.image
