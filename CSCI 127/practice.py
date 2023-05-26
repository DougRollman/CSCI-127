import matplotlib.pyplot as plt
import pandas as pd

file = input("enter file to be read: ")
borough = input("enter name of borough: ")
save = input("Enter name to be saved as: ")


pop = pd.read_csv(file)

pop['Date of Interest'] = pop['date_of_interest']            
pop['Fraction'] = pop[borough] / pop["case_count"]
pop.plot(x = "Date of Interest", y = "Fraction")


print("Min: ", pop[borough].min())
print("Max: ", pop[borough].max())
print("Mean: ", round(pop[borough].mean(),3))
print("Median: ", pop[borough].median())
print("Standard Deviation: ",round(pop[borough].std(),3))

#Save to the file the user input in variable output
plt.show()
fig = plt.gcf()
fig.savefig(save)
