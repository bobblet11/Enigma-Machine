# Enigma-Machine

This is my enigma machine. It encrypts and decrypts.

il go through the steps of what happens.
1. type a message and split chars into a list
2. create random plugboard configurations and 3 wheel configurations ( in the real enigma machine only 20 of the letters in alphabet were switched by plugboard so i also randomly removed 6 chars from alphabet to create plugboard configurations).
3. to create these conifgurations i used a dictionary and the zip fucntion 
4. then i looped through the list of chars in my message and passed it through the plug board, switchting letters that are paired
5. then i looped through the list of chars that passed through plugboard and passed it through the 3 wheels, reflector and again through wheels. causing the each char to change    7 times randomly
6. then i passed each char through the plug board again
7. finally i used the 'join' method combine all the characters into a string.
