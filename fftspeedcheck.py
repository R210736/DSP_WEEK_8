import numpy as np
x=np.array([1,-1,2,4])
N=len(x)
def fft(x):
    N=len(x)
    if N==1:
        return x
    else:
        xe=x[0::2]
        xo=x[1::2]
        Xe=fft(xe)
        Xo=fft(xo)
        Wn=np.exp(-1j*2*np.pi*np.arange(0,N/2)/N)
        X=np.concatenate([Xe+Wn*Xo,Xe-Wn*Xo])
        return X
print(fft(x))