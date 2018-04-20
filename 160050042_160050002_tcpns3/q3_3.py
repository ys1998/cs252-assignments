import matplotlib.pyplot as plt

X = [1,2,4,7,10]
Y = [193.8, 140.06, 64.03, 25.66, 8.54]

plt.plot(X,Y)
plt.title("Average throughput vs. loss rate")
plt.xlabel("Loss rate (%)")
plt.ylabel("Avg. throughput (Kbps)")
plt.show()
