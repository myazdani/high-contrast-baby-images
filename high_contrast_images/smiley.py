from .base_image import BaseImage

class Smiley(BaseImage):
    def __init__(self, stripe_width=50):
        super().__init__()
        self.stripe_width = stripe_width

    def create_image(self):
        # draw the outline of the face
        self.draw.ellipse([(50, 50), (450, 450)], outline='black', width=20)

        # draw two eyes
        self.draw.ellipse([(150, 200), (200, 250)], fill='black')
        self.draw.ellipse([(300, 200), (350, 250)], fill='black')

        # draw a smile
        self.draw.arc([(150, 250), (350, 350)], start=0, end=180, fill='black', width=20)

        return self.image
