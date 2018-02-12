import os
import subprocess
import matplotlib.pyplot as plt 
import random
import re

PATH_TO_NS3 = '/home/rupesh/ns-3.27'
SIMTIME = 2
DATA_RATE = '10Mbps'

NODES = list(range(1,16))
#NODES.extend([n*n for n in range(4,12)])

def main():
	os.chdir(PATH_TO_NS3)

	fraction_retries = []

	for n in NODES:
		command = ["./waf", "--run", "nsta-udp --nodes={0} --simtime={1} --dataRate={2}".format(n,SIMTIME,DATA_RATE)]
		subprocess.call(command)
#		tp = running_sum/SIMTIME
#		================================================================================
		count1 = 0
		"""
		command2 = ["tshark", "-r", "Station-1-0.pcap", "-z", "conv,wlan,wlan.fc.retry==1",">temp1.txt"]
		subprocess.call(command2)
		"""
		command1 = "tshark -r Station-1-0.pcap -z conv,wlan,wlan.fc.retry==1 >temp1.txt"
		os.system(command1)
		with open("temp1.txt") as f:
			while(f.readline()[0]!="="):
				pass
			for i in range(4):
				f.readline()
			line = f.readline()
			
			while line[0] is not "=":
				count1 += int(line.split()[7])
				line = f.readline()

		count0 = 0
		command2 = "tshark -r Station-1-0.pcap -z conv,wlan,wlan.fc.retry==0 >temp0.txt"
		os.system(command2)
		with open("temp0.txt") as f:
			while(f.readline()[0]!="="):
				pass
			for i in range(4):
				f.readline()
			line = f.readline()
			
			while line[0] is not "=":
				count0 += int(line.split()[7])
				line = f.readline()

		fraction_retries.append(count1*100/(count1+count0))

	# Plotting routine
	plt.figure(1)
	plt.xlabel("Number of nodes")
	plt.ylabel("Percentage of retries")
	plt.title("retry-numnodes")
	plt.plot(NODES,fraction_retries)
	plt.show()



if __name__ == '__main__':
	main()