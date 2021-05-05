from pythonic_garage_band.garage_band import Musician, Guitarist, Drummer, Bassist


class Band:
    band_names = []

    def __init__(self, name,):
        self.name = str(name)
        self.members = Musician.all_members()
        Band.band_names.append(self.members)

    def play_solo(self):
        members = Musician.all_members()
        solo_players = []
        solo_players.append(
            f' "i am { self.name } and i am a solo player from the class Band'
        )
        return solo_players

    def __str__(self):
        return f"str method from band class {self.name}"

    def __repr__(self):
        return f"repr method from band class {self.name}"

    @classmethod
    def to_list(cls):
        return cls.band_names


if __name__ == "__main__":

    metallica = Drummer("Metallica")
    print(Metallica)
    print(Metallica.get_instrument())
    print(Metallica.play_solo())

    black_pink = Guitarist("BlackPink")
    print(BlackPink)
    print(BlackPink.get_instrument())
    print(BlackPink.play_solo())

    scorpions = Bassist("Scorpions")
    print(Scorpions)
    print(Scorpions.get_instrument())
    print(Scorpions.play_solo())
    print(Musician.__str__)

    the_weekend = Band("TheWeekend")
    print(the_weekend.play_solo())
    print(Musician.all_members())
    print(Band.band_names)
