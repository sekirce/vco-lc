import matplotlib.pyplot as plt 
import csv 

x = [] 
y = [] 
z = []

with open('C:/Users/Asus/Documents/GitHub/vco-lc/pyhton-plot-files/resultsS.csv','r') as csvfile: 
	lines = csv.reader(csvfile, delimiter=',') 
	for row in lines: 
		x.append(float(row[1]))
		z.append(float(row[2])) 
		y.append(float(row[4]))
        #  y.append(int(row[1])) 
        
x = x[2:]
z = z[2:]
y = y[2:]

plt.plot(x, y, color = 'g', linestyle = 'solid', 
		marker = 'o',label = "Plot of Amplitude = f(vbbias)") 

plt.xticks(rotation = 25) 
plt.xlabel('Vbbias (V)') 
plt.ylabel('Vp-p amplitude (V)') 
plt.title('Points for modelling', fontsize = 20) 
plt.grid() 
plt.legend() 
plt.show() 

plt.plot(x, z, color = 'g', linestyle = 'solid', 
		marker = 'o',label = "Plot of Amplitude = f(vbbias)") 

plt.xticks(rotation = 25) 
plt.xlabel('Vbbias (V)') 
plt.ylabel('Frequency (V)') 
plt.title('Points for modelling', fontsize = 20) 
plt.grid() 
plt.legend() 
plt.show() 

