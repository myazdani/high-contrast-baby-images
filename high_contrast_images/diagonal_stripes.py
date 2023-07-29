from .base_image import BaseImage

class DiagonalStripes(BaseImage):
    def __init__(self):
        super().__init__()

    def create_image(self):
        for i in range(-self.height, self.width, 50):
            if i // 50 % 2 == 0:
                color = 'black'
            else:
                color = 'white'
            self.draw.polygon([(i, 0), (i+50, 0), (i+50+self.height, self.height), (i+self.height, self.height)], fill=color)

        return self.image
