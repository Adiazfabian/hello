import pylab as pl
import numpy as np

#Con SINC
k=np.arange(-20,20)
ak=(1/2.0)*np.sinc(k/2.0)*np.exp(-1j*k*np.pi/2.0)
m=np.abs(ak)
f=np.angle(ak)
#pylab.figure(2)
#pylab.stem(k,m,markerfmt=" ")
#pylab.show()
#Reconstruccion
t=np.linspace(-2,2,1000)
s_per=0
for k in range(-10,10):     
    #print s_per
    s_per=s_per+(1/2.0)*np.sinc(k/2.0)*np.exp(-1j*k*np.pi/2.0)*np.exp(1j*k*2*np.pi*t)    
pl.plot(t,s_per), pl.show()