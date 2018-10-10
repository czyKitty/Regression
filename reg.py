import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plot
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from numpy import *
from numpy.linalg import *
import sys

set_printoptions(suppress=True)

#get data from the file
def readFile(xSet,ySet,fileName):
    fileData = open(fileName)
    line = fileData.readline().split()
    
    while (len(line) > 1):
        xSet.append(float(line[0]))
        ySet.append(float(line[1]))
        line = fileData.readline().split()
    fileData.close()
    return (xSet,ySet)

#validation data
def validation(validationFile, w, n,regData,regX):
    dataSet = readFile([],[],validationFile)

    xData = matrix(dataSet[0]).T
    yData = matrix(dataSet[1]).T

    X = ones((len(dataSet[0]),1))
    for i in range(1,n+1):
        X = column_stack((X, power((2*xData - xData.max() - xData.min())/(xData.max() - xData.min()), i)))

    #Plot validation data
    plot.plot(xData,yData,'go', markersize=3)
    
    #Draw regression line
    plot.plot(regData,regX*w, color='blue',linewidth=1)
    
    function = "y="+str(round(w.item(0),2))
    for i in range(1,n+1):
        if w.item(i)>0:
            function += "+"
        if i == 1:
            function += str(round(w.item(i),2))+"x"
        else:
            function += str(round(w.item(i),2))+"x^"+str(i)
    print("Function: ",function)

    mse = float(1.0/len(xData)*(X*w-yData).T*(X*w-yData))
    print("MSE:",mse)

    plot.draw()
    input("<type to continue>")

#train data
def train(trainFile, n):
    dataSet = readFile([],[],trainFile)
    
    xData = matrix(dataSet[0]).T
    yData = matrix(dataSet[1]).T

    X = ones((len(dataSet[0]),1))
    for i in range(1,n+1):
        X = column_stack((X, power((2*xData - xData.max() - xData.min())/(xData.max() - xData.min()), i)))
    
    w = (X.T*X).I*X.T*yData

    #Plot training data
    plot.ion()
    plot.axis([min(dataSet[0])-1,max(dataSet[0])+1,min(dataSet[1])-10,max(dataSet[1])+10])
    plot.plot(dataSet[0],dataSet[1], 'go', color='grey', markersize=1)


    regData = matrix(arange(min(dataSet[0]),max(dataSet[0]),0.5)).T
    regX = ones((len(regData),1))

    for i in range(1,n+1):
        regX = column_stack((regX, power((2*regData - xData.max() - xData.min())/(xData.max() - xData.min()), i)))

    return(w,regData,regX)

def main():
    trainFile = sys.argv[1]
    validationFile = sys.argv[2]
    degree = sys.argv[3]
    trained = train(trainFile,int(degree))
    validation(validationFile, trained[0], int(degree),trained[1],trained[2])

main()
