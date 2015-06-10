import math
from scipy.stats import truncnorm
from scipy.stats import uniform
from scipy import integrate
import numpy as np
from numpy import rate

sqrt = math.sqrt
e = math.e
pi = math.pi
alpha = .4748


#q=475922286169261325753349249653048451545124879242694725395555128576210262817955800483758081


#n=128.0


for i in range(1,10):
    n=2**i

    #q=n**3
    q=475922286169261325753349249653048451545124879242694725395555128576210262817955800483758081
    
    m=math.ceil(n*math.log(q,2))
    
    v=sqrt(m)
    
    d=math.ceil( 2*n*math.log(q)/math.log(v) )
    
    delta=(v/q**(n/d))**(1/d)
    
    print n, int(m), int(d), float(delta)

