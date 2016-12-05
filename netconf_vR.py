import getpass
import paramiko
import time

#Set var
address = "0.0.0.0"
naddress = "0.0.0.0"
message = 100
firstcon = 1
ans = '1'
count = 0

#Set standard messages
HELLO = """
<?xml version="1.0" encoding="UTF-8"?>
	<hello xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
		<capabilities>
			<capability>urn:ietf:params:netconf:base:1.0</capability>
		</capabilities>
	</hello>
]]>]]>
"""

PING ="""
<rpc message-id="r_msg" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
	<ping xmlns="urn:vyatta.com:mgmt:vyatta-op:1">
		<host>r_add</host>
		<count>5</count>
		<ttl>3</ttl>
	</ping>
</rpc>
]]>]]>
"""
ROUTE ="""
<rpc message-id="r_msg" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
	<route xmlns="urn:vyatta.com:mgmt:vyatta-op:1">
		<destination>r_add</destination>
	</route>
</rpc>
]]>]]>
"""

CLOSE ="""
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
<close-session/>
</rpc>
]]>]]>
"""

#get dynamic credentials                                                            
hostname = raw_input('Hostname: ')
username = raw_input('Username: ')
password = getpass.getpass('Password: ')

#initiate ssh connection 
ssh = paramiko.SSHClient()
#ignore missing hostkey
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=username,password=password, port=22) 

#get transport from previous ssh connection
trans = ssh.get_transport() 
#create channel for netconf 
chan = trans.open_session()
name = chan.set_name('netconf')
chan.invoke_subsystem('netconf')
data = chan.recv(2048)
print data

while not chan.exit_status_ready(): #while server as not acknowledge end of connection
	if not chan.recv_ready(): #test if buffered data
		if firstcon == 1:
			chan.send(HELLO)
			firstcon = 0
			print HELLO
		print 'Do you want to pass some netconf command ?'
		while (ans != 'y' and ans != 'n'):
			ans = raw_input('y/n ?')
		if ans == 'y':
			while (ans != 'p' and ans != 'r'):
				ans = raw_input('Ping (p) or Route (r) p/r ?:')
			if ans == 'p':
				PING_T = PING.replace('r_add',raw_input('X.X.X.X:')).replace('r_msg',str(message+1))
				message = message + 1
				chan.send(PING_T)
				print PING_T
			elif ans == 'r':
				ROUTE_T = ROUTE.replace('r_add',raw_input('X.X.X.X:')).replace('r_msg',str(message+1))
				chan.send(ROUTE_T)
				message = message + 1
				print ROUTE_T
		elif ans == 'n':
			chan.send(CLOSE)
			print CLOSE
		data = chan.recv(2048)
		print data
	else: 
		data = chan.recv(2048)
		print data
chan.close()
ssh.close()
print 'connection ended'


