from math import pi

class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
        self.volume = 4 / 3 * pi * self.radius ** 3
        self.surface = 4 * pi * self.radius ** 2

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        return self.volume

    def get_surface_area(self):
        return self.surface

    def get_density(self):
        return self.mass / self.get_volume()
