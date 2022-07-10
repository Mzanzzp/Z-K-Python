class Circle:
    def __init__(self, promien):
        self.promien = promien
        # self.srednice = srednice
        # self.pole = pole

    def set_promien(self, value):
        self.__promien = value
    @property
    def promien(self):
        return self.__promien
    @promien.setter
    def promien(self, value):
        self.__promien = value

    @promien.setter
    def promien(self, value):
        if value < 0: raise ValueError("promien ujemny")
        self._promien = value

