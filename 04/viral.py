"""
  Program to estimate revenue of a viral Tiktok video

  Samira Begum
  February 2022
"""

def main():

    likes = int(input("Enter number of likes: "))

    if(likes < 10000):
        rev = 0

    if(likes >= 10000):
        rev = ((likes//1000)*3)

    if(likes > 1000000):
        rev = ((rev) + 2500)

    if(likes > 10000000):
        rev = ((rev) +  10000)

    print("Your viral video with " +  str(likes) + " likes could earn $" + str(rev))

main()
