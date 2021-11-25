# generating a random string of both letters and numbers
import random

# random password generator 

"""
when called a function will return a super secure password 
Yes it will look crazy and you won't be able to memorize it 
but that is not the point assuming it will just automatically
save your super secure unique password. 

The password will include things "asgdhgsahjgdsjh"
"--=-=-=-??././././././"
"16526352736278"
It will return a string 

class secret_password 
with methods that return different things 
(1) number 
(2) letters
(3) specail characters 
(4) will return a combination of these things 


"""

class Password:
    def __init__(self):
       
        self.letters = "abcdefghijklmnopqrstuvwxyz"
        self.characters = "-+=/;:',.%$#@!*"

    # first method return random number
    def number_options(self):
        return random.choice(range(10))

    # second method returns a random letter
    def letter_options(self):
        letters = []
        for let in self.letters:
            letters.append(let)
        return random.choice(letters)
        # yes now of course there are many way to do this so 
        # put your thinking cap on kay

    def special_character_option(self):
        special_characters = []
        for char in self.characters:
            special_characters.append(char)
        return random.choice(special_characters)

    def combine_randoms(self):
        secret_password = []
        counter = 0
        while counter < 6:
            secret_password.append(self.special_character_option())
            secret_password.append(str(self.number_options()))
            secret_password.append(self.letter_options())
            counter += 1
        # final_password = "".join(secret_password)
        # I am going to find a place to do this outside the loop 
        return print(secret_password)
            

        # return self.special_character_option() + self.letter_options() + str(self.number_options())


x = Password()

u = x.combine_randoms()
print(type(u))
