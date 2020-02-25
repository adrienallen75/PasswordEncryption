import random
import os.path


class Encrypt():
    
    def encrypting(self):
        result = ''
        choice = ''
        
        characters_in_order = [chr(x) for x in range (32,127)]
        
        username = input('enter username:')
        password = input('enter password:')
        
        r_seed = input('enter an integer to use as a seed:')
        random.seed(r_seed)
        shuffled_list = [chr(x) for x in range (32,127)]
        random.shuffle(shuffled_list)
        for i in range (0,len(password)):
            result+= shuffled_list[characters_in_order.index(password[i])]
        print(result)
        
        print('Storing encrypted passwrod in a text file for security purposes!')
        
        f = open("password.txt","w")
        f.write(result)
        f.close()
        
        print(f.read())
        
print('Hello will you like to Encrypt enter E or exit enter 0 to exit the program:')

x = input()

if x == "E":
    p1 = Encrypt()
    e = p1.encrypting()
elif x =="0":
    print('Exiting program.......')
    exit(0)
            
            
