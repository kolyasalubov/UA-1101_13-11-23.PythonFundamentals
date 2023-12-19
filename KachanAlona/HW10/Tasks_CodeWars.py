# I. Ball-super-ball
class Ball(object):
    """
    Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
    If no arguments are given, ball objects should instantiate with a "ball type" of "regular.
    """
    def __init__(self, ball_type='regular'):
        self.ball_type = ball_type


# II. Color-ghost
class Ghost(object):
    def __init__(self):
        color = ['white', 'yellow', 'purple', 'red']
        from random import randint
        num = randint(0, 3)
        self.color = color[num]


# III. Basic-subclasses-Adam-and-Eve

# IV. Classy-classes
#
# V. Building Spheres
#
# VI. Dynamic Classes