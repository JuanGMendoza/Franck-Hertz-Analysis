"""This program generates a plot of the Franck Hertz experiment and finds the peaks in the data"""
import numpy
import matplotlib.pyplot as pyplot

def main(): 

    dataHG = dict()
    dataNE = dict()

    for i in range(0,4):
        dataHG[i] = numpy.transpose(numpy.loadtxt('trial' + str(i + 1) + 'x10.txt'))
        dataNE[i] = numpy.transpose(numpy.loadtxt('neon' + str(i + 1) + '.txt'))

    for i in range(0,4):
           
        pyplot.errorbar(dataNE[i][0],dataNE[i][1], xerr = .1, yerr = .2, fmt = 'none', label = ('trial ' + str(i)))
    
    
    pyplot.xlabel('Accelerating Voltage (V)')
    pyplot.ylabel('\"Current\"(V)')
    pyplot.legend()
    pyplot.show()
    
    k = 0
    while(k != 4):
        
        i = 1
        peaks = numpy.zeros(4)
        max_x = numpy.zeros(4)
        max_xes = numpy.zeros([4,4])
        j = 0
        while(i != 5):
           
            peaks[j] = numpy.max(dataHG[k][1][0:i*47])
            j += 1
            i += 1
        
        i = 0
        j = 0
        while(j != 4):
            
            found = False
            
            while(not found):
                if(peaks[j] == dataHG[k][1][i]):
                    max_x[j] = dataHG[k][0][i]
                    i = 0
                    j += 1
                    found = True
                
                else:
                    i+=1
        max_xes[k] = max_x
        
        print(max_x)

        
        k +=1
    
        
main()

    
