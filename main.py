"""
TODO:
    - Add functionality to not have to press enter on input.
    - Add functionality for multiple notes (?)
"""
import random
import time
import datetime
from time import sleep
import json

def add_note_and_print(replaceable_element,row_string):
    row_list = list(row_string)
    row_list[replaceable_element] = "O"
    print("".join(row_list))

def staff(clef_type = 'treble',width = 60):
    """
    Function to create the staff with a random note somewhere on it. 
    Also returns the numerical value of 0 through 10 on which line or space the note was generated
    """
    # Create a line and a space row without note symbols
    # 1. Generate lists
    line = []
    [line.append("-") for x in range(width)]

    space = []
    [space.append(" ") for x in range(width)]

    # 2. Turn lists into printable strings
    line_string = "".join(line)
    space_string = "".join(space)

    # Put all the rows into a staff

    staff = []
    if clef_type == 'bass':
        staff.append(space_string)
        staff.append(space_string)
    staff.append(line_string)
    staff.append(space_string)
    staff.append(line_string)
    staff.append(space_string)
    staff.append(line_string)
    staff.append(space_string)
    staff.append(line_string)
    staff.append(space_string)
    staff.append(line_string)
    if clef_type == 'treble':
            staff.append(space_string)
            staff.append(space_string)


    horizontal = random.randint(0,width-1)
    vertical = random.randint(0,10)


    i = 0
    for row in staff:
        if i == vertical:
            add_note_and_print(horizontal,row)
        else:
            print(row)
        i+=1
    return vertical

def main_test(which_clef='treble'):
    """
    This function deals with handling and processing inputs,
    comparing, compiling and storing results
    """

    # Clef definitions to compare inputs with the staff
    treble_clef = {10:'c', 9:'d', 8:'e', 7:'f', 6:'g', 5:'a', 4:'b', 3:'c', 2:'d', 1:'e', 0:'f'}
    bass_clef =   {10:'g', 9:'a', 8:'b', 7:'c', 6:'d', 5:'e', 4:'f', 3:'g', 2:'a', 1:'b', 0:'c'}

    # Data structure for stats
    attempt = {'attempted':'', 'correct':'', 'response_time':999999, 'timestamp':''}
    attempts = {}

    # Selecting the correct clef
    if which_clef == 'treble':
        clef = treble_clef
    elif which_clef == 'bass':
        clef = bass_clef
    else:
        raise Exception('Unknown clef as argument to main_test')

    # Endless loop for testing
    session_index = 0
    while True:
        print("press q to exit")
        inp_message = "In " + which_clef + " clef, which A to G note is this\n"

        val = staff(clef_type=which_clef) # A clef is generated with a random note
        
        # User input and timing user input for stats
        start = time.time()
        user = input(inp_message)
        end = time.time()
        
        # End of session to break loop naturally and to save results
        if user == 'q':
            if attempts != {}: #No need to store empty results
                date = time.strftime("%Y_%m_%d_%H_%M")
                fname = 'results/'+ date  + '.json'
                attempts['session'] = date
                with open(fname,'w+') as f:
                    f.write(json.dumps(attempts))
                f.close()
            print("Goodbye!")
            break

        # empty input  to clear up the screen
        if user == '' or user == ' ':
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            continue
        

        response_time = end - start
        attempts[session_index] = {'attempted': user, 'correct':clef[val], 'response_time':response_time, 'timestamp':time.time()}

        if clef[val] == user:
            session_index+=1
            print("\n\n\n                           YASSSS\n\n\n")
        else:
            session_index+=1
            print("\n\n                              NOPE\n\n")

main_test('treble')