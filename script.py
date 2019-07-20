"""This is a simple script to scale our data by a factor of 10"""
import numpy

i = 1

while( i != 5):
    print(i)
    s = numpy.loadtxt('neon' + str(i) +'.txt')
    s = numpy.transpose(s)
    f = open('neon' + str(i) +'x10.txt', "w")

    EOF = False
    j = 0
    while(not EOF):
        try:
            f.write( " {:.2f}".format(s[0][j]*10) +' ' + str(s[1][j]) + '\n')
            j+= 1
        except:
            EOF = True
            f.close()
    i += 1

