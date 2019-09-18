import csv
import pandas as pd

# csv
def loadCsv(filename):
	dataSet = []
	with open(filename,'r') as file:
		csvReader = csv.reader(file)
		for line in csvReader:
			dataSet.append(line)
	return dataSet

# pandas
def loadCsv_pd(filename):
	result = pd.read_csv(filename,'r',header=None,sep='\t')


