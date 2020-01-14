# I import some modules the two first are from py ofcurse
# the last two are games that i made and used on the game.
import random
import sys 
sys.path.insert(1, r"C:\Users\gusta\OneDrive\Escritorio\code")
sys.path.insert(1, r"C:\Users\gusta\OneDrive\Escritorio\code")
import guess_the_number
import rockpaperscisors


class Engine:

    # the Engine class is made to start the game and call the
    # next class once the first is finish.
    def __init__(self, location):

        self.location = location

    def start(self):
        
        self.location.start_location.enter()

        self.location.next_location()
      

class Place:

    # this is the father class of the Locations of the game
    # From this they inherit a help method
    print('\n')
    path_help = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\dialogue\help advise.txt")
    path_help = open(path_help, 'r+').read()

    print(path_help)
    

    def help(self):

        # this is help function, i use files to print information to the user, this is very commond on
        # this code.
        path_answers_location_1 = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\help ans\help L1.tx.txt")
        path_answers_location_2 = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\help ans\help L2.txt")
        path_answers_location_3 = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\help ans\help L3.txt")
        path_answers_location_4 = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\help ans\help L4.txt")

        location_1 = open(path_answers_location_1, 'r+').read()
        location_2 = open(path_answers_location_2, 'r+').read()
        location_3 = open(path_answers_location_3, 'r+').read()
        location_4 = open(path_answers_location_4, 'r+').read()

        print("""
        
        -Help mode:

            The n° 1 is 'k2_205'(Location 1)
            The n° 2 is 'Circuit_planet'(Location 2)
            The n° 3 is 'Toys_casttle'(Location 3)
            The n° 4 is 'k2_205_2'(Location 4)

        """)

        locatio_list = ['k2_205', 'Circuit_planet', 'Toys_casttle', 'k2_205_2']
        print(locatio_list, '\n'"1, 2, 3, 4")

        while True:

            player_help = input("> ")

            if player_help == '1':
                print("\nThe answers for location one are: \n\n", location_1)
                break

            elif player_help == '2':
                print("\nThe answers for location one are: \n\n", location_2)
                break

            elif player_help == '3':
                print("\nThe answers for location one are: \n\n", location_3)
                break
                
            elif player_help == '4':
                print("\nThe answers for location one are: \n\n", location_4)
                break
            
            else:
                print("Sorry but that isn't an option.")
                print("Try again.")
                continue
    

class k2_205(Place):# Done!

    # first class (Location) of the game! 
    def enter(self):

        #--------------------------------------------------------------------
        # This opens the answers list for this Location.
        path_answers = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\\answers\\answers_location_1.txt")

        path_answers_R1 = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\answers\rose answer L1\rose talk 1.txt")
        path_answers_P = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\answers\rose answer L1\prince ans to rose.txt")
        path_answers_R2 = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\answers\rose answer L1\rose ans talk 2.txt")

        path_answers_R3 = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\answers\rose answer L1\rose ans to 2 path.txt")

        path_answers_R4 = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\answers\rose answer L1\rose ans to jokes.txt")

        answers = open(path_answers, 'r+')

        path_answers_R1 = open(path_answers_R1, 'r+').read() 
        path_answers_P = open(path_answers_P, 'r+').read()
        path_answers_R2 = open(path_answers_R2, 'r+').read()        
        path_answers_R3 = open(path_answers_R3, 'r+').read() 
        path_answers_R4 = open(path_answers_R4, 'r+').read() 

        answer_list = []

        for word in answers:

            answer_list.append(word.strip())

        # this opens the dialogue file for this location.

        path_dialogue_1 = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\dialogue\Location_1\first part.txt")
        path_dialogue_2 = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\dialogue\Location_1\second part.txt")
        path_dialogue_3 = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\dialogue\Location_1\third part.txt")

        dialogue_1 = open(path_dialogue_1, 'r+').read()
        dialogue_2 = open(path_dialogue_2, 'r+').read()
        dialogue_3 = open(path_dialogue_3, 'r+').read()

        # This opens de dialogue file to read
        #----------------------------------------------------------
        # The fromat of above is very commond in this game 
        # this is just the way of this game to work
        print("""
        
        The little prince planet

        """)

        input("\nEnter\n")

        print(dialogue_1)
        input("\nEnter\n")

        print(dialogue_2)
        input("\nEnter\n")

        print(dialogue_3)
        input("\nEnter\n")

        while True:
            print("-You arrive to Rose-")
            print("\n-What do you tell her?-")

            player = input("\n>Talk: "); print('\n'); player = player.capitalize() 

            if player in answer_list[1:19]:

                print(path_answers_R1)
                input("\nEnter\n")

                print(path_answers_P)
                input("\nEnter\n")

                print(path_answers_R2)
                input("\nEnter\n")

                break

            elif player in answer_list[20:30]:

                print(path_answers_R3)
                input("\nEnter\n")

                print(path_answers_R1)
                input("\nEnter\n")

                print(path_answers_P)
                input("\nEnter\n")

                break
                
            elif player in answer_list[-4:-1]:

                print(path_answers_R4)
                input("\nEnter\n")

                continue

            elif player == 'Help':

                self.help()
                
                continue

            else:
                print("I'm sorry but i didn't understand that.\n")
                continue


class Circuit_planet(Place):# Done!

    def enter(self):
          
        #--------------------------------------------------------------------
        # This opens the answers list for this Location.
        path_answers = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\answers\answers_location_2.txt")

        path_answers_R1 = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\answers\robot answers L2\Roboto ans 1.txt")
        path_answers_R2 = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\answers\robot answers L2\Roboto ans 2.txt")

        path_answers_R3 = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\answers\robot answers L2\looking for oil.txt")
        path_answers_R4 = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\answers\robot answers L2\you say no.txt")

        path_answers_R5 = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\answers\robot answers L2\grab oil.txt")
        path_answers_R6 = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\answers\robot answers L2\dont grab oil.txt")

        path_answers_R7 = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\answers\robot answers L2\roboto tells hat.txt")
        path_answers_R8 = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\answers\robot answers L2\prince going out.txt")

        path_answers_R9 = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\answers\robot answers L2\jokes ans.txt")
        path_answers_R10 = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\answers\robot answers L2\pankcakes ans.txt")

        answers = open(path_answers, 'r+')

        path_answers_R1 = open(path_answers_R1, 'r+').read() 
        path_answers_R2 = open(path_answers_R2, 'r+').read()        
        path_answers_R3 = open(path_answers_R3, 'r+').read() 
        path_answers_R4 = open(path_answers_R4, 'r+').read() 
        path_answers_R5 = open(path_answers_R5, 'r+').read() 
        path_answers_R6 = open(path_answers_R6, 'r+').read() 
        path_answers_R7 = open(path_answers_R7, 'r+').read()
        path_answers_R8 = open(path_answers_R8, 'r+').read()
        path_answers_R9 = open(path_answers_R9, 'r+').read()
        path_answers_R10 = open(path_answers_R10, 'r+').read()

        answer_list = []

        for word in answers:

            answer_list.append(word.strip())

        # this opens the dialogue file for this location.

        path_dialogue_1 = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\dialogue\Location_2\intro to circuit.txt")
        path_dialogue_2 = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\dialogue\Location_2\robot work.txt")

        dialogue_1 = open(path_dialogue_1, 'r+').read()
        dialogue_2 = open(path_dialogue_2, 'r+').read()

        # This opens de dialogue file to read
        #----------------------------------------------------------

        print("""
        
        The Circuit Planet!

        """)

        input("\nEnter\n")

        print(dialogue_1)
        input("\nEnter\n")

        loop_swich = True
        while loop_swich:

            print("-You approach to the robot and ask.-")
            print("\n-What do you tell?-")

            player = input("\n>Talk: "); print('\n'); player = player.capitalize() 

            if player in answer_list[1:13]: # ask bout hat

                print(dialogue_2)
                input("\nEnter\n")

                continue

            elif player in answer_list[14:28]: # How is he doing?

                print(dialogue_2)
                input("\nEnter\n")

                continue

                
            elif player in answer_list[29:42]: # how it is name

                print(dialogue_2)
                input("\nEnter\n")

                continue


            elif player in answer_list[43:57]: # This is the help one 
                
                print(path_answers_R1)
                input("\nEnter\n")

                print(path_answers_R2)

                not(loop_swich)

                loop_swich = True
                while loop_swich:

                    player = input("\n>Answer: "); print('\n'); player = player.capitalize() 

                    if player == 'Yes':

                        print(path_answers_R3)
                        input("\nEnter\n")
                        loop_swich = False

                        loop_swich = True
                        while loop_swich:

                            player = input("\n>Answer: "); print('\n'); player = player.capitalize() 

                            if player == 'Grab it':

                                print(path_answers_R5)
                                input("\nEnter\n")
                                loop_swich = False

                                loop_swich = True
                                while loop_swich:

                                    player = input("\n>Answer: "); print('\n'); player = player.capitalize() 

                                    if player in answer_list[1:13]: # ask bout hat 

                                        print(path_answers_R7)
                                        input("\nEnter\n")

                                        print(path_answers_R8)

                                        loop_swich = False
                                        break

                                    elif player == 'Help':

                                        self.help()
                                        
                                        continue

                                    else:
                                        print("\nSorry Roboto didn't hear well.")
                                        continue

                            elif player == 'Leave it':

                                print(path_answers_R6)
                                input("\nEnter\n")
                                continue

                            elif player == 'Help':

                                self.help()
                
                                continue

                            else:
                                print("\nSorry Roboto didn't hear well.")
                                continue

                    elif player == 'No':
                        
                        print(path_answers_R4)
                        input("\nEnter\n")
                        continue

                    elif player == 'Help':

                        self.help()
                
                        continue

                    else:
                        print("\nSorry Roboto didn't hear well.")
                        continue


            elif player in answer_list[58:61]: # jokes

                print(path_answers_R9)
                input("\nEnter\n")

                continue
                
            elif player in answer_list[62:71]: # pankcakes
                
                print(path_answers_R10)
                input("\nEnter\n")

                continue

            elif player == 'Help':

                self.help()
                
                continue

            else:
                print("I'm sorry but i didn't understand that.\n")
                continue


class Toys_casttle(Place): # done!

    def enter(self):

        #--------------------------------------------------------------------
        # This opens the answers list for this Location.
        path_answers = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\answers\answers_location_3.txt")

        path_answers_R1 = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\answers\bb king ans L3\bad manners.txt")
        path_answers_R2 = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\answers\bb king ans L3\apologise.txt")
        path_answers_R3 = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\answers\bb king ans L3\not apologise.txt")

        path_answers_R4 = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\answers\bb king ans L3\accepted play.txt")
        path_answers_R5 = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\answers\bb king ans L3\rock paper scirsors rules.txt")

        path_answers_R6 = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\answers\bb king ans L3\you win.txt")
        path_answers_R7 = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\answers\bb king ans L3\you lose.txt")
        path_answers_R8 = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\answers\bb king ans L3\deny.txt")

        answers = open(path_answers, 'r+')

        path_answers_R1 = open(path_answers_R1, 'r+').read() 
        path_answers_R2 = open(path_answers_R2, 'r+').read()        
        path_answers_R3 = open(path_answers_R3, 'r+').read() 
        path_answers_R4 = open(path_answers_R4, 'r+').read() 
        path_answers_R5 = open(path_answers_R5, 'r+').read()
        path_answers_R6 = open(path_answers_R6, 'r+').read()
        path_answers_R7 = open(path_answers_R7, 'r+').read()
        path_answers_R8 = open(path_answers_R8, 'r+').read()

        answer_list = []

        for word in answers:

            answer_list.append(word.strip())

        # this opens the dialogue file for this location.

        path_dialogue_1 = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\dialogue\Location_3\entering to planet.txt")
        path_dialogue_2 = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\dialogue\Location_3\you find bb king.txt")
        path_dialogue_3 = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\dialogue\Location_3\scream.txt")
        path_dialogue_4 = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\dialogue\Location_3\gigle.txt")
      
        dialogue_1 = open(path_dialogue_1, 'r+').read()
        dialogue_2 = open(path_dialogue_2, 'r+').read()
        dialogue_3 = open(path_dialogue_3, 'r+').read()
        dialogue_4 = open(path_dialogue_4, 'r+').read() 

        # This opens de dialogue file to read
        #----------------------------------------------------------

        print("""
        
        The Toy's Castte 

        """)

        input("\nEnter\n")

        print(dialogue_1)
        
        loop_swich = True
        while loop_swich:

            player = input("\n>Talk: "); print('\n'); player = player.capitalize() 

            if player in answer_list[1:17]: # this is the guess the number game

                print("-You grab an old pice of game tech and start playing with it. . .")
                
                old_game = guess_the_number
                old_game.random_number()

                continue

            elif player in answer_list[18:47]: # looking for bb king 

                print(dialogue_2)
                input("\nEnter\n")

                print("Bb King is playing with his toys.\n")
                
                False

                loop_swich = True
                while loop_swich:

                    player = input("\n>Talk: "); print('\n'); player = player.capitalize() 

                    if player in answer_list[40:60]: # ask for hat 

                        print(path_answers_R1)
                        input("\nEnter\n")

                        False

                        loop_swich = True
                        while loop_swich:

                            player = input("\n>Talk: "); print('\n'); player = player.capitalize()

                            if player in answer_list[61:70]: # apologise

                                print(path_answers_R2)
                                False

                                loop_swich = True
                                while loop_swich:

                                    player = input("\n>Talk: "); print('\n'); player = player.capitalize()

                                    if player == 'Accept':

                                        print(path_answers_R4)
                                        input("\nEnter\n")

                                        print(path_answers_R5)
                                        input("\nEnter\n")

                                        rps_game = rockpaperscisors
                                        rps_game.game()                                
                                        loop_swich = False

                                        print('\n', path_answers_R6)
                                        input("\nEnter\n")

                                        break

                                    elif player == 'Deny':

                                        print(path_answers_R8)
                                        input("\nEnter\n")

                                        continue

                                    else:
                                        print("\nI didn't understand that.")
                                        continue
                                

                            elif player in answer_list[71:95]: # No apologise

                                print(path_answers_R3)
                                input("\nEnter\n")

                                continue

                            elif player == 'Help': # this is help

                                self.help()
                                continue

                            else:
                                print("\nSorry but i don't know what do you mean.")
                                continue

                    elif player in answer_list[96:120]: # call for his atention

                        print(dialogue_3)
                        input("\nEnter\n")

                        continue

                    elif player in answer_list[120:124]: # tell jokes!

                        print(dialogue_4)
                        input("\nEnter\n")

                        continue

                    elif player == 'Help': # this is help

                        self.help()
                        continue

                    else:
                        print("\nSorry but i don't know what do you mean.")
                        continue

            elif player == 'Help': # this is help

                self.help()
                continue

            else:
                print("\nSorry but i don't know what do you mean.")
                continue


class k2_205_2(Place):

    def enter(self):
        
        #--------------------------------------------------------------------
        # This opens the answers list for this Location.
        path_answers = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\answers\answers_location_4.txt")

        path_answers_R1 = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\answers\rose L4\rose thanks.txt")
        path_answers_R2 = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\answers\rose L4\why the hat.txt")
        path_answers_R3 = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\answers\rose L4\new ppl.txt")

        answers = open(path_answers, 'r+')

        path_answers_R1 = open(path_answers_R1, 'r+').read() 
        path_answers_R2 = open(path_answers_R2, 'r+').read()        
        path_answers_R3 = open(path_answers_R3, 'r+').read()

        answer_list = []

        for word in answers:

            answer_list.append(word.strip())

        # this opens the dialogue file for this location.

        path_dialogue_1 = (r"C:\Users\gusta\OneDrive\Escritorio\code\Little Price game\dialogue\Location_4\welcome back.txt")

        dialogue_1 = open(path_dialogue_1, 'r+').read()

        # This opens de dialogue file to read
        #----------------------------------------------------------

        print("""
        
        Home sweet home.

        """)

        input("\nEnter\n")

        print(dialogue_1)

        loop_swich = True
        while loop_swich:

            player = input("\n>Talk: "); print('\n'); player = player.capitalize()

            if player in answer_list[1:23]: # give the hat

                print(path_answers_R1)
                input("\nEnter\n")
                loop_swich = False

                while True:

                    player = input("\n>Talk: "); print('\n'); player = player.capitalize()

                    if player in answer_list[24:28]: # why  hat

                        print(path_answers_R2)
                        input("\nEnter\n")

                        print("""
                        
                        *The End*

                        """)
                        False
                        break

                    elif player in answer_list[29:41]: # new ppl

                        print(path_answers_R3)
                        input("\nEnter\n")

                        continue

                    elif player == 'Help': # this is help

                        self.help()
                        continue

                    else:
                        print("\nSorry but i don't know what do you mean.")
                        continue


            elif player == 'Help': # this is help

                self.help()
                continue

            else:
                print("\nSorry but i don't know what do you mean.")
                continue
                

class Map:
    # this is where magic happens, kind of
    # first we have a dict that attach a string the respective class

    location_dict = {
        'k2_205': k2_205(),
        'Circuit_planet': Circuit_planet(),
        'Toys_casttle': Toys_casttle(),
        'k2_205_2': k2_205_2()
        }

    def __init__(self, start_location):

        self.start_location = start_location
        
        self.start_location = self.location_dict.get(start_location)        

    def next_location(self):

        '''This method call the next class/function in value of dict
        excluding the first.'''


        # fun part i set a var (locatioo_list) to method sorted that calls the dict keys, 
        # this is so i can iterate over the dict and get the keys.

        self.start_location

        i = 1

        locatioo_list = sorted(self.location_dict.keys())

        # Iteration ! ! !
        for key in enumerate(locatioo_list):

            # this excludes the first key that is the one used 
            # to call the program (The start class)
            self.start_location = key[+1]
            i += 1

            if self.start_location == 'k2_205':
                self.start_location = None
                continue

            # this is looking the key iterated in dict and bc we geta key then we can
            # access to the value that are the clases
            self.start_location = self.location_dict[self.start_location]

            # This is a handy thing that prints a random message in the list of
            # below everytime you pass a class (Location)
            opening_message_list = [
                "You have arrive to the next planet.",
                "You are in another planet!.",
                "Welcome to the planet.",
                "You are in another planet."
            ]

            opening_message = random.choice(opening_message_list)
            print('\n', opening_message, '\n')

            self.start_location.enter()


test = Map('k2_205')
start = Engine(test)
start.start()