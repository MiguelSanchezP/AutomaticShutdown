import matplotlib.pyplot as plt
import numpy as np

def plot(files):
	figurecount = 1
	for file in files:
		f = open("./files/" + file, 'r')

		lines = []
		userusage = []
		niceusage = []
		systemusage = []
		iowaitusage = []
		stealusage = []
		idleusage = []

		i = 0
		for line in f:
			if not i<3 and not line[19:29] == '':
				lines.append(line)
				userusage.append(float(line[19:29].lstrip().replace(',', '.')))
				niceusage.append(float(line[29:39].lstrip().replace(',', '.')))
				systemusage.append(float(line[39:49].lstrip().replace(',', '.')))
				iowaitusage.append(float(line[49:59].lstrip().replace(',', '.')))
				stealusage.append(float(line[59:69].lstrip().replace(',', '.')))
				idleusage.append(float(line[69:79].lstrip().replace(',', '.')))
			i = i+1

		f.close()

		useravg.append(userusage[len(userusage)-1])
		niceavg.append(niceusage[len(niceusage)-1])
		systemavg.append(systemusage[len(systemusage)-1])
		iowaitavg.append(iowaitusage[len(iowaitusage)-1])
		stealavg.append(stealusage[len(stealusage)-1])
		idleavg.append(idleusage[len(idleusage)-1])
		x = np.arange(len(userusage)-4)
		plt.figure(figurecount)
		figurecount = figurecount + 1
		plt.title(file)
		plt.plot(x, userusage[3:len(userusage)-1])
		plt.plot(x, niceusage[3:len(niceusage)-1])
		plt.plot(x, systemusage[3:len(systemusage)-1])
		plt.plot(x, iowaitusage[3:len(iowaitusage)-1])
		plt.plot(x, stealusage[3:len(stealusage)-1])
		plt.legend(["User", "Nice", "System", "IOWait", "Steal"])
		#plt.plot(x, idleusage[3:len(idleusage)-1])
		#plt.axis('equal')
	plt.show()


useravg = []
niceavg = []
systemavg = []
iowaitavg = []
stealavg = []
idleavg = []
datasets = ["monitoringRest.txt", "monitoringRest2.txt", "monitoringRest3.txt", "monitoringPlex.txt", "monitoringSSHFS.txt", "monitoringDownload.txt", "monitoringUpdate.txt"]
plot (datasets)
print ("USER")
for i in range (len(datasets)):
	print (datasets[i] + ": " + str(useravg[i]))

print ("NICE")
for i in range (len(datasets)):
	print (datasets[i] + ": " + str(niceavg[i]))

print ("SYSTEM")
for i in range (len(datasets)):
	print (datasets[i] + ": " + str(systemavg[i]))

print ("IOWAIT")
for i in range (len(datasets)):
	print (datasets[i] + ": " + str(iowaitavg[i]))

print ("STEAL")
for i in range (len(datasets)):
	print (datasets[i] + ": " + str(stealavg[i]))

print ("IDLE")
for i in range (len(datasets)):
	print (datasets[i] + ": " + str(idleavg[i]))
