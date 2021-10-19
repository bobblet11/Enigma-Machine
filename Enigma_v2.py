import numpy as np
import string
import random

alphabet = [char for char in string.ascii_lowercase]

def create_pairings(set_of_letters):
    already_paired=[]
    pairings = {}
    for letter in set_of_letters:
        while True:
            paired_letter = set_of_letters[random.randint(0,len(set_of_letters)-1)]
            if paired_letter == letter or paired_letter in already_paired:
                continue
            else:
                pairings[letter] = paired_letter
                already_paired.append(paired_letter)
                break
    return pairings

def configure_plugboard():
    removed = random.sample(alphabet,6)
    plugboard_letters = [letter for letter in alphabet if letter not in removed]
    plugboard_pairings = create_pairings(plugboard_letters)
    return plugboard_pairings

def transfer_to_plugboard(message,plugboard_pairings):
    encoded_message=[]
    for letter in message:
        if letter in plugboard_pairings.keys():
            
            encoded_message.append(plugboard_pairings[letter])
           
        else:
            encoded_message.append(letter)
    return encoded_message

def reflect(wheels):
    for i in wheels:
                reversed_pairing = {value : key for (key, value) in wheels[i].items()}
                wheels[i]= reversed_pairing
    return wheels

def create_wheels():
    wheels = {}
    wheel_count = 1
    while wheel_count <5:
        wheels[wheel_count] = create_pairings(alphabet)
        wheel_count+=1
    return wheels

def rotate_wheel(wheel_num, wheels,direction):
    values = list(wheels[wheel_num].values())
    rotated_values = values[direction:]+values[:direction]
    wheels[wheel_num] = dict(zip(alphabet,rotated_values))
    return wheels

def trasnfer_to_wheels(letter_of_message, wheels,encrypt):
    wheel_num = 1
    counter = 0
    j=1
    
    while counter !=7:
        if wheel_num == 4 and encrypt == False:
            j = -1
            wheels = reflect(wheels)
        pairings = wheels[wheel_num]
        
        output = pairings[letter_of_message]
        
        letter_of_message = output
        if wheel_num == 4 and encrypt == True:
            j = -1
            wheels = reflect(wheels)

        counter +=1
        wheel_num +=j
        continue
    wheels = reflect(wheels)
    return output
