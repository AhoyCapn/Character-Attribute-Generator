"""
Made by Preston Johnstone 
This program uses the random module to generate attributes for a character.
Last Updated 3/9/2019
Version 2.0
"""

import random

def attribute_program():

    def attribute_process(): # The process of both generating and printing the attributes.

        def print_attributes(attributelist): # The process of printing the attributes.
            hasList = ['Long Hair', 'Short Hair']

            print('\nYour Character...\n')
            for attribute in attributelist:
                if attribute in hasList:
                    print('has {}'.format(attribute))
                else:
                    print('is {}'.format(attribute))
    
        def generate_attributes(attributelist): # The process of generating the attributes.
        
            def attributeGenerator(storageList, listUsed): # The code that appends a new list by choosing a random element from another list.
                storageList.append(random.choice(listUsed))
        
            # These are the lists that describe attributes for the character.
            MorF = ['Male', 'Female']
            LngorShrtHair = ['Long Hair', 'Short Hair']
            TllorShrt = ['Tall', 'Short']
            FrndlyorUfrndly = ['Friendly', 'Unfriendly']
            Race = ['White', 'Black', 'Asian', 'Hispanic', 'Latino']


            # The generation of the attributes, being appended to the list.
            attributeGenerator(attributelist, MorF)
            attributeGenerator(attributelist, LngorShrtHair)
            attributeGenerator(attributelist, TllorShrt)
            attributeGenerator(attributelist, FrndlyorUfrndly)
            attributeGenerator(attributelist, Race)

        generatedAttributes = [] # The data structure that will hold the chosen attributes.

        generate_attributes(generatedAttributes)
        print_attributes(generatedAttributes)
        
   
    print('\nWelcome to the Attribute Generator')

    while True:
        print('\n1. Use Program (Y)\n')
        print('2. Exit Program (N)\n')
        choice = input('Input: ')
        print('----------------------------------------------------')
        if choice.lower() == 'y':
            attribute_process()
            print('----------------------------------------------------')
            continue
        elif choice.lower() == 'n':
            print('Program stopped. Goodbye!')
            break
        elif choice.lower() != 'n' or choice.lower() != 'y':
            print('\nInvalid input! Must be y or n!')

        

attribute_program()
