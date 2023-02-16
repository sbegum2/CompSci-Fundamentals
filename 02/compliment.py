"""
Program to generate a compliment you can give to someone

Samira Begum
February 2022
"""

def main():

    print("Let's create a compliment for your friend! Can you tell me a bit about them?")
    name = input("Their name: ")
    noun = input("Noun: ")
    adj = input("Adjective: ")
    verb = input("Verb ending with -ing: ")

    print(name)
    print("You are a lovely " + noun)
    print("I love that you love " + verb + " in such a " + adj + " way!")

main()
