import numpy as np


def sumthr(x, M, thr, y):
    # x - input 1D array
    # M - size of sliding window
    # thr - specified threshold for average of sequence size M
    # y - previous mask of bad pixels (1=good, 0=bad)
    
    w = np.where(y == 1)[0]

    if not w.size:
        return x, M, thr, y
    
    xx = x[w]
    nxx = len(xx)
    if nxx < M:
        return x, M, thr, y
    
    xxa = np.zeros(nxx - M + 1)
    for i in range(M):
        xxa += xx[i:i+len(xxa)]
    
    p = np.ones((nxx,), dtype=int)
    wa = np.where(xxa > thr*M)[0]
    if wa.size:
        for i in range(M):
            p[wa + i] = 0
    
    y[w] = p
    return x, M, thr, y


# pro SumThr, x, M, thr, y
# ; x - input 1D array
# ; M - size of sliding window
# ; thr - specified threshold for average of sequence size M
# ; y - previous mask of bad pixels (1=good, 0=bad)
#
# w=where(y eq 1)
# if w(0) eq -1 then return
#
# xx=x(w) # only good pixels
# nxx=n_elements(xx)  # how many good pixels (e.g. 100)
# if nxx lt M then return
#
# xxa=fltarr(nxx-M+1)  # array with size (number of good pixels - len of window) (e.g. 100 - 25 = 75)
# for i=0,M-1 do xxa=xxa+xx(i:*)
# i = 0 : xxa += xx[0:74]
# i = 1 : xxa += xx[1:75]
# ...
# i = 24: xxa += xx[24:99]
#
# p=bytarr(nxx)+1
# wa=where(xxa gt thr*M)
# if wa(0) ne -1 then for i=0,M-1 do p(wa+i)=0
#
# y(w)=p
# return
# end