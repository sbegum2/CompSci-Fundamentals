"""
To find the perimeter of a square using user-inputted length

Samira Begum
February 2022
"""

def main():

  l = int((input("What's the side length? ")))
  print("Perimeter is: " + str(l*4)) 
  print("Area is: " + str(l**2))   

  for i in range(l):
     print("= "*(l))

main()
