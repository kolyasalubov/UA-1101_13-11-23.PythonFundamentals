def God():
    Adam = Man("Adam")
    Eve = Woman("Eve")
    return [Adam, Eve]

class Human:
    def __init__(self, name):
        self.name = name


class Man(Human):
    def __init__(self, name):
        super().__init__(name)


class Woman(Human):
    def __init__(self, name):
        super().__init__(name)


