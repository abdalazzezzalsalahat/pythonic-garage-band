from abc import abstractclassmethod


class Musician:
    members = []

    def __init__(self, name,):
        self.name = name
        Musician.members.append(self)

    @abstractclassmethod
    def __str__(self):
        """
        This str method from super class to make every sub class have str method.
        """
        return f"Musican class  str <{self.name} >"

    @abstractclassmethod
    def __repr__(self):
        """
        This repr method from super class to make every sub class have repr method.
        """
        return f"{self.name} "

    @abstractclassmethod
    def get_instrument(self):
        """
        This get_instrument method from super class to make every sub class have
        get_instrument method.
        """
        return "Instrument from the Musician class."

    @abstractclassmethod
    def play_solo(self):
        """
        This play_solo method from super class to make every sub class have
        play_solo method.
        """
        return "play_solo from the Musician class."

    def all_members():
        return Musician.members


class Guitarist(Musician):

    def __init__(self, name,):
        super().__init__(name)

    def __str__(self):
        """
        This str method from Guitarist class.
        """
        return f" class   <{self.name} >"

    def __repr__(self):
        """
        This repr method from Guitarist class.
        """
        return f"{self.name} "

    def get_instrument(self):
        """
        This get_instrument method from Guitarist.
        """
        return "guitar"

    def play_solo(self):
        """
        This play_solo method from
        """
        return "guitar"


class Bassist(Musician):

    def __init__(self, name,):
        super().__init__(name)

    def __str__(self):
        """
        This str method from Bassist class.
        """
        return f" class   <{self.name} >"

    def __repr__(self):
        """
        This repr method from Bassist class.
        """
        return f"{self.name} "

    def get_instrument(self):
        """
        This get_instrument method from Bassist.
        """
        return "bass"

    def play_solo(self):
        """
        This play_solo method from Bassist.
        """
        return "bass"


class Drummer(Musician):

    def __init__(self, name,):
        super().__init__(name)

    def __str__(self):
        """
        This str method from the Drummer class.
        """
        return f" class   <{self.name} >"

    def __repr__(self):
        """
        This repr method from the Drummer class.
        """
        return f"{self.name} "

    def get_instrument(self):
        """
        This get_instrument method from Drummer.
        """
        return "drums"

    def play_solo(self):
        """
        This play_solo method from  Drummer.
        """
        return "drums"
