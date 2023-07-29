from .base_image import BaseImage
import math

class Hourglass(BaseImage):
    def __init__(self):
        super().__init__()

    def create_image(self):
        self.draw.polygon([(100, 100), (400,100),(100, 400), (400, 400)], outline='black', fill='black')

        # save the image
        return self.image
