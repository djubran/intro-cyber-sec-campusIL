import time
import sys # ignore
sys.path.insert(0,'.') # ignore
from Root.pswd import real_password

def check_password(password): # Don't change it
    if len(password) != len(real_password):
        return False
    for x, y in zip(password, real_password):
        time.sleep(0.1) # Simulates the wait time of the safe's mechanism
        if int(x) != int(y):
            return False
    return True
   
def crack_password():
    start_time1 = time.time()
    for dig1 in range (0,9):
        passwrd=str(dig1)+'000'
        start_time = time.time()
        check_password(passwrd)
        end_time =time.time()
        diff = end_time - start_time
        if diff>0.2: #if function ran for more than 0.2 it means first digit was correct and we moved to check the next one
            break
    
    
    for dig2 in range (0,9):
        passwrd=str(dig1)+str(dig2)+'00'
        start_time = time.time()
        check_password(passwrd)
        end_time =time.time()
        diff = end_time - start_time
        if diff>0.3: #if function ran for more than 0.3 it means second digit was correct and we moved to check the next one
            break
    
        
    
    for dig3 in range (0,9):
        passwrd=str(dig1)+str(dig2)+str(dig3)+'0'
        start_time = time.time()
        check_password(passwrd)
        end_time =time.time()
        diff = end_time - start_time
        if diff>0.4:
            break
    
    
    for dig4 in range (10):
        passwrd=str(dig1)+str(dig2)+str(dig3)+str(dig4)
        if check_password(passwrd): #last digit check by brute forcing  (won't move on to a next digit to campare times)
            break
    
    return passwrd
    
#takes 8 sec




