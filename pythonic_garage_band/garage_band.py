from abc import abstractclassmethod

class Band:
    
    band_list = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.band_list.append(self.name)

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"

    def play_solos(self):
        solos = []
        return [member.play_solo() for member in self.members]

    @classmethod
    def to_list(cls):
        return cls.band_list


class Musician:

    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

    def __repr__(self):
        """This repr method from super class to make every sub class have repr method."""
        return f"{self.__class__.__name__} instance. Name = {self.name}"    

    def __str__(self):
        """This str method from super class to make every sub class have str method."""
        return f"My name is {self.name} and I play {self.instrument}"


class Guitarist(Musician):

    def __init__(self, name):
        super().__init__(name, "guitar")

    def get_instrument(self):
        """This get_instrument method from Guitarist."""
        return self.instrument

    def play_solo(self):
        """This play_solo method from  Guitarist."""
        return "face melting guitar solo"


class Bassist(Musician):

    def __init__(self, name):    
        super().__init__(name, "bass")

    def get_instrument(self):
        """This get_instrument method from Bassist."""
        return "bass"
    
    def play_solo(self):
        """This play_solo method from  Bassist."""
        return "bom bom buh bom"


class Drummer(Musician):
    
    def __init__(self, name):
        super().__init__(name, "drums")

    def get_instrument(self):
        """This get_instrument method from Drummer."""
        return "drums"

    def play_solo(self):
        """This play_solo method from  Drummer."""
        return "rattle boom crash"

# if __name__ == "__main__":
#   h=Drummer('azooz')