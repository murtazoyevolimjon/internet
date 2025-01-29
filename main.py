import socket
import json


with open("domains.txt") as input_file:
    domains = input_file.read().split()

    result = []
    for domain in domains:
        ip = socket.gethostbyname(domain)
        
        result.append({
            'name': domain,
            'ip': ip
        })

with open("domains.json", "w") as output_file:
    result_json = json.dumps(result, indent=4)
    output_file.write(result_json)
