from .base_image import BaseImage

class Checkerboard(BaseImage):
    def __init__(self, cell_size=50):
        super().__init__()
        self.cell_size = cell_size

    def create_image(self):
        for i in range(0, self.width, self.cell_size):
            for j in range(0, self.height, self.cell_size):
                if (i // self.cell_size % 2 == 0) ^ (j // self.cell_size % 2 == 0):
                    color = 'black'
                else:
                    color = 'white'
                self.draw.rectangle([(i, j), (i+self.cell_size, j+self.cell_size)], fill=color)
        return self.image
