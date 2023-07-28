from PIL import Image, ImageDraw

class BaseImage:
    def __init__(self, width=500, height=500):
        self.width = width
        self.height = height
        self.image = Image.new('RGB', (width, height), 'white')
        self.draw = ImageDraw.Draw(self.image)

    def create_image(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def save(self, filename):
        self.create_image()
        self.image.save(filename)
