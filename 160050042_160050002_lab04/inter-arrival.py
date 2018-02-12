import os
import subprocess
import matplotlib.pyplot as plt 
import numpy as np

PATH_TO_NS3 = '/home/yash/Downloads/ns-3.27'
SIMTIME = 10
DATA_RATE = '10Mbps'

NODES = [1, 50, 100]

def main():

	os.chdir(PATH_TO_NS3)
	inter_arrival = {}
	total = {}
	for n in NODES:
		inter_arrival[n] = []
		total[n] = 0
		command = ["./waf", "--run", "nsta-udp --nodes={0} --simtime={1} --dataRate={2}".format(n,SIMTIME,DATA_RATE)]
		subprocess.call(command)
		
		command2 = 'tshark -r AccessPoint-0-0.pcap -Y \"ip.src==10.0.0.2\" > temp.txt'
		os.system(command2)

		with open("temp.txt") as f:
			total[n] += 1
			t_prev = float(f.readline().split()[1])
			for line in f:
				total[n] += 1
				t_now = float(line.split()[1])
				inter_arrival[n].append(t_now-t_prev)
				t_prev = t_now

	# Plotting routine
	y1,binEdges1=np.histogram(inter_arrival[1])
	bincenters1 = 0.5*(binEdges1[1:]+binEdges1[:-1])

	y50,binEdges50=np.histogram(inter_arrival[50])
	bincenters50 = 0.5*(binEdges50[1:]+binEdges50[:-1])

	y100,binEdges100=np.histogram(inter_arrival[100])
	bincenters100 = 0.5*(binEdges100[1:]+binEdges100[:-1])

	plt.xlabel("Time interval")
	plt.ylabel("Probability")
	plt.title("inter-arrival")
	plt.plot(bincenters1, y1/(total[1]-1))
	plt.plot(bincenters50, y50/(total[50]-1))
	plt.plot(bincenters100, y100/(total[100]-1))
	plt.savefig('inter-arrival.pdf')

if __name__ == '__main__':
	main()