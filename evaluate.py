import os
import sys
import re

def getData(dataFile):
    lineTotal = 0
    dataString = ''
    
    dataSet = open(dataFile,'r')
    line = dataSet.readline()
    
    while(len(line)>1):
        dataString += line
        line = dataSet.readline()
        lineTotal += 1
    
    dataSet.close()

    return(dataString,lineTotal)

def main():
    dataFile = sys.argv[1]
    degree = sys.argv[2]
    dataSet = getData(dataFile)
    dataString = dataSet[0]
    numLine = int(dataSet[1])
    numTemp = int(numLine/10)

    for i in range(0,10):
        trainData = open("train"+str(i),'w')
        validationData = open("validation"+str(i),'w')
        for j in range(numLine):
            if j>=i*numTemp and j<i*numTemp+numTemp:
                validationData.write(dataString.split('\n')[j]+'\n')
            else:
                trainData.write(dataString.split('\n')[j]+'\n')
        trainData.close()
        validationData.close()
        os.system("python3 reg.py train"+str(i)+" validation"+str(i)+" "+degree)

main()