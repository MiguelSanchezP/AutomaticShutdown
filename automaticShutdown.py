import subprocess

ten = False
twenty = False
thirty = False

while (ten == False or twenty == False or thirty == False):
	subprocess.call("sar 1 600 | tail -1 > auxiliar.txt", shell=True)
	f = open ('./auxiliar.txt', 'r')
	line = ''
	for lines in f:
		line = lines
	value = float(line[19:29].replace(',', '.').lstrip())
	twenty = ten
	thirty = twenty
	if value < 1:
		ten = True
	else:
		ten = False

subprocess.call("sudo shutdown now", shell=True)
