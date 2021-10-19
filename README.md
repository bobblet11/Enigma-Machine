# Enigma-Machine

This is my enigma machine. It encrypts and decrypts.
ENCRYPT - 
il go through the steps of what happens.
1. type a message and split chars into a list
2. create random plugboard configurations and 3 wheel configurations ( in the real enigma machine only 20 of the letters in alphabet were switched by plugboard so i also randomly removed 6 chars from alphabet to create plugboard configurations).
3. to create these conifgurations i used a dictionary and the zip fucntion 
4. then i looped through the list of chars in my message and passed it through the plug board, switchting letters that are paired
5. then i looped through the list of chars that passed through plugboard and passed it through the 3 wheels, reflector and again through wheels. causing the each char to change    7 times randomly
6. Each time a character passes through wheels the wheel rotates, shifting its dictionary values one place.
7. For Each full loop of the first wheel, the second wheel rotates. for each full loop of second wheel, the thrid wheel rotates. (full loop = 26 rotations)
8. then i passed each char through the plug board again
9. finally i used the 'join' method combine all the characters into a string.

DECRYPT-
to decrypt i did everything previously mentioned by in reversed order. Im not sure if this is how that real enigma machine actually did it.
