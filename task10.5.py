import math

class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        volume = (4 / 3) * math.pi * math.pow(self.radius, 3)
        return round(volume, 5)

    def get_surface_area(self):
        surface_area = 4 * math.pi * math.pow(self.radius, 2)
        return round(surface_area, 5)

    def get_density(self):
        density = self.mass / self.get_volume()
        return round(density, 5)

ball = Sphere(2, 50)
print("Radius:", ball.get_radius())
print("Mass:", ball.get_mass())
print("Volume:", ball.get_volume())
print("Surface Area:", ball.get_surface_area())
print("Density:", ball.get_density())
