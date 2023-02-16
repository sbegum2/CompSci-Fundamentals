"""
  TODO: write Critter class
  Samira Begum
  April 2022
"""

#carefully read if one critter or all, i.e. sleep (all)
#i.e. if name is name? letter t
class Critter(object):

    def __init__(self, name, desc, personal, possesive, eat):
        """
        Constructor; parameters are intial string values for;
          name, desc, personal, possesive, eat
        """
        self.name = name
        self.desc = desc
        self.personal = personal
        self.possesive = personal
        self.eat = eat

    ###########################
    
    """
    Getter methods; each returns the value of the appropriate member variable
    """

    def get_name(self):
        return self.name

    ###########################
    """
    String method to print a message regarding the description and state
    of the critter
    """

    def __str__(self):
        return (("%s looks %s, %s, %s") % (self.personal, hunger_desc, play_desc, pet_desc)) 

    ##########################
    """
    Method to initialize a variable measuring how often the critter has 
    been fed. No parameters or return value.
    """

    def feed(self):
        print("The critter has been fed %d times" % (self.eat))

        hunger = 0
        hunger_desc = ""
        if (eat > 2):
            print("%s is over-full! %s doesn't want to eat anymore" % \
                    (self.name, self.personal))
            hunger = hunger + 1
            hunger_desc = "over-full"

        elif(eat == 1):
            print("%s is well-fed! %s could eat more." % \
                    (self.name, self.personal))
            hunger = hunger + 1
            hunger_desc = "well-fed"

        else:
            print("%s is hungry! Please feed %s" % (self.name, self.personal))
            hunger = hunger
            hunger_desc = "hungry"

    ###########################
    """
    Method to initialize an instance variable measuring how often the
    critter has been pet
    """
    pet_count = 0
    pet_desc = ""
    def pet(self):
        print("%s enjoys being pet!" , (self.name))
        pet_count = pet_count + 1
        if pet_count > 0:
            pet_desc = "happy"
        else:
            pet_desc = "sad"
    
    ############################

    """
    Method to initialize an instance variable measuring how often the 
    critter has been played with
    """
    playtime = 0
    play_desc = ""
    def play(self):
        print("%s is excited to play!" , (self.name))
        playtime = playtime + 1
        if playtime > 0:
            play_desc = playful
        else:
            play_desc = bored

    ############################

    """
    Modifier method to decrease critter's feeding, petting, and play levels 
    after sleeping 
    """
    
    def sleep(hunger, pet_count, playtime):
        print(("%s is going to sleep!") % (self.name))
        hunger = hunger - 1
        pet_count = pet_count - 1
        playtime = playtime - 1

##########################
# End of class definition
##########################
