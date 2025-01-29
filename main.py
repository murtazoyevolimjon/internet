import socket
import json
# import time

socket.gethostbyname("google.com")
file = [] 
f = open("domains.txt", "r") 
word = ""
for i in f:
    a = i.strip()
    p = socket.gethostbyname(a)
    x = {
        "name": a,
        "ip": p 
    }
    # y = json.dumps(x)
    file.append(x)
y = json.dumps(file, indent=4)
json_file = open("domains.json", "w")
json_file.write(y)
# print(file)
    
    

            


