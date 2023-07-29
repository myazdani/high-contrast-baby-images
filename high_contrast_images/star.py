from .base_image import BaseImage
import math

class Star(BaseImage):
    def __init__(self, num_points=5, outer_radius=None, inner_radius=None):
        super().__init__()
        self.num_points = num_points
        self.outer_radius = outer_radius if outer_radius else min(self.width, self.height) // 3
        self.inner_radius = inner_radius if inner_radius else self.outer_radius // 2

    def create_image(self):
        center = (self.width // 2, self.height // 2)
        points = []
        for i in range(self.num_points * 2):
            if i % 2 == 0:
                radius = self.outer_radius
            else:
                radius = self.inner_radius
            angle = math.pi / self.num_points * i
            x = center[0] + radius * math.cos(angle)
            y = center[1] + radius * math.sin(angle)
            points.append((x, y))
        self.draw.polygon(points, fill='black')
        return self.image 
