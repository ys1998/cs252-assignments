import os
import subprocess
import matplotlib.pyplot as plt 
import random

PATH_TO_NS3 = '/home/yash/Downloads/ns-3.27'
SIMTIME = 10
DATA_RATE = '10Mbps'
NUM_NODES = 5
NODES = [2**n for n in range(NUM_NODES+1)]

def main():
	os.chdir(PATH_TO_NS3)

	throughput_values = []
	jain_fairness_1 = []
	jain_fairness_10 = []

	for n in sorted(NODES):
		command = ["./waf", "--run", "nsta-udp --nodes={0} --simtime={1} --dataRate={2}".format(n,SIMTIME,DATA_RATE)]
		subprocess.call(command)
		running_sum = 0.0
		with open("out-nsta-udp.txt") as f:
			f.readline()
			first_line = f.readline()
			sum_x = sum(map(float,first_line.split()[1:]))
			running_sum += sum_x
			sum_x_2 = sum(map(lambda x: float(x)**2, first_line.split()[1:]))
			jf = sum_x/(n*sum_x_2)
			jain_fairness_1.append(jf)
			for line in f:
				sum_x = sum(map(float,line.split()[1:]))
				running_sum += sum_x
				sum_x_2 = sum(map(lambda x: float(x)**2, line.split()[1:]))
				jf += sum_x/(n*sum_x_2)

			jain_fairness_10.append(jf/SIMTIME)
		tp = running_sum/SIMTIME
		throughput_values.append(tp)

	# Plotting routine
	plt.figure(1)
	plt.xlabel("log(N)")
	plt.ylabel("Total throughput (Mbps)")
	plt.title("throughput-numnodes")
	plt.plot(list(range(NUM_NODES+1)),throughput_values)
	plt.show()

	plt.figure(2)
	plt.xlabel("log(N)")
	plt.ylabel("Jain Fairness")
	plt.title("fairness-1sec-numnodes")
	plt.plot(list(range(NUM_NODES+1)),jain_fairness_1)
	plt.show()

	plt.figure(3)
	plt.xlabel("log(N)")
	plt.ylabel("Jain Fairness")
	plt.title("fairness-10sec-numnodes")
	plt.plot(list(range(NUM_NODES+1)),jain_fairness_10)
	plt.show()

if __name__ == '__main__':
	main()