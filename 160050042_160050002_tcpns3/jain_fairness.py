import numpy as np
import matplotlib.pyplot as plt

def jf(x):
	return np.sum(x)**2/(len(x)*np.sum([i**2 for i in x]))
	
X = [2,4,6,8,10]
Y = [jf([114840,320040]), jf([274680, 111960, 298080, 186840]), jf([109080, 103320, 204840, 157320, 149760, 165240]), jf([73440, 173880, 119880, 178560, 190080, 124200, 66240, 65520]), jf([91080, 99720, 87840, 97200, 65520, 102240, 59760, 132120, 118440, 96840])]
print("(num_flows, JFI)")
print(list(zip(X,Y)))	
plt.plot(X,Y)
plt.title("Jain Fairness Index")
plt.xlabel("num_flows")
plt.ylabel("Jain Fairness index")
plt.show()
