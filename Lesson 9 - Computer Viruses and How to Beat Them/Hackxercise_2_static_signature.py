"""
Implement the function sign so that given a line (in bytes), returns a unique signature of that line that is 20 characters long;
Implement the scan function that, given a list of paths and a signature, reads them line by line, 
and returns a list of all the paths that have a line that matches the static signature.
Any line in a file might end with a ‘\n’. Remember to remove it.

Don’t leave open files.

SHA1 is a good way to get a digest of a string (Remember hashlib?).



"""
from hashlib import sha1

def sign(line):
    sha1_inst = sha1()
    sha1_inst.update(line)
    uniq_sign = sha1_inst.hexdigest()
    return uniq_sign[0:20]

def scan(paths, signature):
    malicious_paths = []
    for path in paths:
        lines = open(path,'r').readlines()
        for line in lines:        
            line = line.rstrip('\n').encode('utf-8')
            if signature == sign(line): #suspicous agent found
                malicious_paths.append(path)
    return malicious_paths
