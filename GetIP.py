import socket
import csv
import sys




ping_results = []

def ping_request(server_name):
 ping_answer=socket.gethostbyname(server_name)
 return ping_answer

with open(sys.argv[1], mode='r') as hostnames:
		hostnames = csv.DictReader(hostnames, delimiter=",", fieldnames=['dns'])
		for row in hostnames:
			server_name = row['dns']
			print(server_name)
			try:
				ping_results.append([server_name,ping_request(server_name)])
			except Exception as e:
				ping_results.append([server_name,e])


with open("results.csv", mode='w') as csv_file:
    csv_writer = csv.writer(csv_file,delimiter=",")
    csv_writer.writerows(ping_results)

