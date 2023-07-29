from .base_image import BaseImage

class Striped(BaseImage):
    def __init__(self, stripe_width=50):
        super().__init__()
        self.stripe_width = stripe_width

    def create_image(self):
        for i in range(0, self.width, self.stripe_width):
            color = 'black' if (i // self.stripe_width) % 2 == 0 else 'white'
            self.draw.rectangle([(i, 0), (i+self.stripe_width, self.height)], fill=color)
        return self.image
