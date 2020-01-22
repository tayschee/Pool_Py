class   GotCharacter :
    def __init__(self, first_name, is_alive=True) :
        self.first_name = first_name
        self.alive = is_alive
    def bebe(self) :
        print("abc")

class   Stark(GotCharacter) :
    def __init__(self, first_name=None, is_alive=True) :
        super().__init__(first_name, is_alive)
        self.family_name = "Stark"
        self.house_word = "Jarvis"
    def print_house_words(self) :
        print(self.house_word)
    def die(self) :
        self.alive = False

