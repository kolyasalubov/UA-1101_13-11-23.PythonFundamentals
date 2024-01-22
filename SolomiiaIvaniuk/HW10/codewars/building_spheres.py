class Sphere(object):
    """Constructor of Sphere. Calculates volume, surface area and density."""
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        from math import pi
        self.volume = 4 / 3 * pi * self.radius ** 3
        return round(self.volume, 5)

    def get_surface_area(self):
        from math import pi
        surf_area = 4 * pi * self.radius ** 2
        return round(surf_area, 5)

    def get_density(self):
        from math import pi
        density = self.mass / self.volume
        return round(density, 5)

