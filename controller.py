import Enigma_v2 as eng
message = [char.lower() for char in input("What message would you liek to encode?\n>")]
def encrypt(message):
    plugboard_pairings = eng.configure_plugboard()
    wheels = eng.create_wheels()
    pos1, pos2, pos3 = 1,1,1
    plugboard_pass_1 = eng.transfer_to_plugboard(message,plugboard_pairings)
    
    wheel_outputs = []
    for letter in plugboard_pass_1:
        if letter in eng.alphabet:
            wheel_output = eng.trasnfer_to_wheels(letter,wheels,encrypt=True)
            wheel_outputs.append(wheel_output)
            wheels = eng.rotate_wheel(1,wheels,1)
            pos1+=1
            if pos1 > 26:
                pos2 +=1
                wheels = eng.rotate_wheel(2,wheels,1)
                pos1 = 1
            if pos2 > 26:
                pos3+=1
                pos2 = 1
                wheels = eng.rotate_wheel(3,wheels,1)
            if pos3>26:
                pos3 = 1
        
        else:
            wheel_outputs.append(letter)
        
    plugboard_pass_2 = eng.transfer_to_plugboard(wheel_outputs,plugboard_pairings)
    key = {'positions':(pos1,pos2,pos3),
            'wheels': wheels,
            'plugboard_pairings':plugboard_pairings
    }
    return plugboard_pass_2, key


def decrypt(key, encoded_message):
    print(key)
    wheels, positions, plugboard_pairings = key['wheels'],key['positions'],key['plugboard_pairings']
    pos1,pos2,pos3 = positions[0],positions[1],positions[2]
    reflected_plugboard_pairings = {value : key for (key, value) in plugboard_pairings.items()}
    reversed_encoded_message = reversed(encoded_message)
    plugboard_pass_1 = eng.transfer_to_plugboard(reversed_encoded_message,reflected_plugboard_pairings)
    wheel_outputs = []
    for letter in plugboard_pass_1:
        if letter in eng.alphabet:
            pos1-=1
            wheels = eng.rotate_wheel(1,wheels,-1)
            wheel_output = eng.trasnfer_to_wheels(letter,wheels, encrypt=False)
            wheel_outputs.append(wheel_output)
            
            if pos1 <1:
                pos2 -=1
                wheels = eng.rotate_wheel(2,wheels,-1)
                pos1 = 26
            if pos2 < 1:
                pos3-=1
                wheels = eng.rotate_wheel(3,wheels,-1)
            if pos3<1:
                pos3 = 26
        else:
            wheel_outputs.append(letter)
        
    plugboard_pass_2 = eng.transfer_to_plugboard(wheel_outputs,reflected_plugboard_pairings)
    return reversed(plugboard_pass_2)
    
encoded_message , key = encrypt(message)
print(f"[{''.join(encoded_message)}]")
decoded_message = decrypt(key,encoded_message)
print(f"[{''.join(decoded_message)}]")
