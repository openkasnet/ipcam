#!/usr/bin/env python3.6
import socket
import psycopg2
import sys
import time

date=time.strftime("%d-%m-%Y")
hour=time.strftime("%H:%M:%S")

try:
    con = psycopg2.connect(
    database="testmydb", 
    user="kasim", 
    password="10010010", 
    host="127.0.0.1", 
    port="5432"
    )
    print('Connected DB')
	
    cur = con.cursor()
    
    cur.execute('''CREATE TABLE ipaddress
					(id SERIAL PRIMARY KEY,
						ip INET NOT NULL,
                        port int NOT NULL,
						description VARCHAR(250),
						status boolean NOT NULL DEFAULT true,
						date date NOT NULL,
						time time NOT NULL,
						UNIQUE(ip)
						);
				

	''')
	#ALTER TABLE ipaddress ADD UNIQUE (ip);
    print("Table created successfully")
    con.commit()
    #cur.close()
    #con.close()
   	
    
    cur.execute('''INSERT INTO ipaddress(ip, port, description, status, date, time )
                VALUES('192.168.88.1', '80','Hovli','true','%s','%s') 
                ''' % (date,hour))
	
    con.commit()
    cur.close()
    con.close()



except psycopg2.DatabaseError as e:
	#print(f'Error {e}')
	print(e)
	sys.exit(1)





#finally:
#	if con:
#		con.close()

#ip = {'192.168.88.1':80,'192.168.1.3':53, '192.168.11.2': 78}


#if con:
#	print('\n'.join(ip))





"""
while 0 < 1:
	for i in ip:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(2)
		try:
			s.connect((i, ip[i]))
			print(i, 'Good')
		except socket.error:
			print("Not connet host %s"%(i))


"""
