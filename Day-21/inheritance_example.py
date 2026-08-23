class Animal():
    def __init__(self):
        self.num_eyes = 2
    def breathe(self):
        print("Enhale, Exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this Underwater")

    def swim(self):
        print("Swimming in water")

nemo = Fish()
nemo.breathe()
nemo.swim()