#!python3

"""
Create a class that will store a database for a veterinarian.
Your class will need the following properties:

animal (dog, cat, fish, bird, turtle, etc)
breed
name (the pet's name)
owner (the owner's name)
birthdate (of the pet, expressed as yyyy-mm-dd)

The constructor will need to ask for each of those values
for the database when the pet is instantiated

Methods:
display() - should show the name of the pet and type followed by their breed and owner


Main block should have a menu that has the following options:
1. Enter a new pet
2. Retrieve a pet
3. Exit

If they choose to retrieve a pet,
display the following:
Enter pet's name:
and then go through the list, looking for the name of the pet.
If the pet is found, it should call the display() method from the object

Example output:
1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? cat
Breed? Domestic Long Hair
Name? Benjamin
Owner? Chris
Birthdate? 20015-10-01

1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? dog
Breed? Shih-tzu
Name? Buster
Owner? Christy
Birthdate? 2008-10-16

1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? cat
Breed? Domestic Long Hair
Name? Casey
Owner? Chris
Birthdate? 20015-10-01

1. Enter a new pet
2. Retrieve a pet
3. Exit
2

Which Pet? Buster

Buster dog
Shih-tzu is owned by Christy
(10 points) 
"""
import os
pets=[]
class vet:
    animal = None
    breed = None
    name = None
    owner = None
    birthdate = None

    def __init__ (self,):
        self.name = input("What is your pets name? ")
        self.animal = input("What is your animal? ")
        self.breed = input("What is your animal's breed? ")
        self.owner = input("What is your name? ")
        self.birthdate= input("What is your animals birthdate? ")

    def display(self):
        print(self.name,self.animal)
        print(self.breed + " is owned by " + self.owner)


    def __del__(self):
        pass

def main():
    while True:
        os.system("cls")
        choice = input("1: Enter a new pet\n2: Retrive a pet\n3: Exit\n")
        if choice == "1":
            pets.append( vet() )
            
        elif choice == "2":
            pchoice = input("Name of pet ")

            for x in range(len(pets)):
                if pchoice == pets[x].name:
                    pets[x].display()
                    input()

                elif len(pets) == 0:
                    print("there are no pets here trying entering in one")
                    break
        else:
            print("Fine be that way")
            break

main()