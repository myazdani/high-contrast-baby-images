from .base_image import BaseImage

class Spiral(BaseImage):
    def __init__(self):
        super().__init__()

    def create_image(self):
        for i in range(0, min(self.width, self.height)//2, 25):
            if i // 25 % 2 == 0:
                color = 'black'
            else:
                color = 'white'
            self.draw.arc([(i, i), (self.width-i, self.height-i)], start=0, end=360, fill=color, width=25)
    
        return self.image
