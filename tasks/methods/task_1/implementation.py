class Coffee:
    def __init__(self, espresso=0, milk=0, milk_foam=0, ice_cream=0):
        self.espresso = espresso
        self.milk = milk
        self.milk_foam = milk_foam
        self.ice_cream = ice_cream

    @classmethod
    def get_cappucino(cls, *args, **kwargs):
        cappucino = cls(espresso=30,
                        milk=120,
                        milk_foam=50, )

        return cappucino

    @classmethod
    def get_latte(cls, *args, **kwargs):
        latte = cls(espresso=30,
                    milk=150,
                    milk_foam=20, )

        return latte

    @classmethod
    def get_glasse(cls, *args, **kwargs):
        glasse = cls(espresso=60,
                     ice_cream=140, )

        return glasse

    def get_recep(self):
        return {ingridient: ml for ingridient, ml in self.__dict__.items()}

    pass


test_latte = Coffee.get_latte()
print(test_latte.get_recep())
