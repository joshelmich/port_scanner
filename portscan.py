#!/usr/bin/python
import socket
import subprocess
import sys
from datetime import datetime
from tcp_errors import tcp_error_print


# Using the range function to specify ports (here it will scans all ports between 1 and 1024)

# We also put in some error handling for catching errors
class port_scanner:
	
	def scan_ports(self, ip_address, port_list):
		# Check what time the scan started		
		t1 = datetime.now()
		try:			
			tcp_err = tcp_error_print()
			tcp_err.load_tcp_errors()			
			for portNo in range(1, len(port_list), 1):
				port = port_list[portNo]		
				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		
				result = sock.connect_ex((ip_address, port))		
				print "Port:", port, "result:", result, ", ", tcp_err.get_error_string(result)
				sock.close()

		except KeyboardInterrupt:
			print "You pressed Ctrl+C"
			sys.exit()

		except socket.gaierror:
			print 'Hostname could not be resolved. Exiting'
			sys.exit()

		except socket.error:
			print "Couldn't connect to server"
			sys.exit()

		# Checking the time again
		t2 = datetime.now()

		# Calculates the difference of time, to see how long it took to run the script
		total =  t2 - t1
		return total
		
def main(): 			

	# Clear the screen
	subprocess.call('clear', shell=True)
	cmd_line_imput = 0
	if len(sys.argv) == 2:
		if len(sys.argv[1].split(".")) == 4:
			remoteServerIP = sys.argv[1]
			cmd_line_imput = 1
	if cmd_line_imput == 0:
		# Ask for input
		remoteServer    = raw_input("Enter a remote host to scan: ")
		remoteServerIP  = socket.gethostbyname(remoteServer)
	# Print a nice banner with information on which host we are about to scan
	print "-" * 60
	print "Please wait, scanning remote host", remoteServerIP
	print "-" * 60
	# Printing the information to screen
	portList = [21, 22, 35, 43, 558, 795]
	ps = port_scanner()
	scan_time = ps.scan_ports(remoteServerIP, portList)
	print 'Scanning Completed in: ', scan_time


if __name__ == '__main__':	
	main()



