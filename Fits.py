"""This program reads in data and tries to find a gaussian fit to a slice of it"""
import numpy
import matplotlib.pyplot as pyplot
from scipy.optimize import curve_fit
from scipy import asarray as ar,exp

def main():

    dataHG, dataNE = loadData()
    
    slicedData1 = numpy.zeros([2,15])
    slicedData1[0] = dataHG[0][0][29:44]
    slicedData1[1] = dataHG[0][1][29:44]
    pyplot.scatter(slicedData1[0],slicedData1[1])

    popt,pcov = curve_fit(gaus,slicedData1[0],slicedData1[1])
    pyplot.plot(slicedData1[0],gaus(slicedData1[0],*popt),'ro:',label='fit')
    
    pyplot.show()


def gaus(x,a,x0,sigma):
        return a*exp(-(x-x0)**2/(2*sigma**2))

def loadData():
    dataHG = dict()
    dataNE = dict()

    for i in range(0,4):
        dataHG[i] = numpy.transpose(numpy.loadtxt('trial' + str(i + 1) + 'x10.txt'))
        dataNE[i] = numpy.transpose(numpy.loadtxt('neon' + str(i + 1) + '.txt'))

    return dataHG, dataNE

main()
