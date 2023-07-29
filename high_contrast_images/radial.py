from .base_image import BaseImage

class Radial(BaseImage):
    def __init__(self, max_radius=None):
        super().__init__()
        if max_radius is None:
            self.max_radius = int((self.width**2 + self.height**2)**0.5)

    def create_image(self):
        for radius in range(self.max_radius, 0, -50):  # start from outside and move inward
            if radius // 50 % 2 == 0:
                color = 'white'
            else:
                color = 'black'

            self.draw.ellipse([(self.width//2 - radius, self.height//2 - radius), 
                        (self.width//2 + radius, self.height//2 + radius)], 
                        fill=color)
        return self.image
