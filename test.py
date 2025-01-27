import math
from itertools import count

import matplotlib.pyplot as plt

def arithmetic_mean(data,n):
    mean = sum(data)/n
    return mean


def geometric_mean(data,n):
    prod = math.prod(data)
    mean = prod**(1/n)
    return mean


def harmonic_mean(data,n):
    data = [ 1/x  for x in data ]
    mean = n/sum(data)
    return mean


def median(data,n):
    if len(data)%2==0:
        m1 = int(n/2)
        m2 = int((n/2)+1)
        # return data[m1-1], data[m2-1]
        med = (data[m1-1]+data[m2-1])/2
        return med
    else:
        i =  int(n/2)
        return data[i]

def mode(data):
    data = [ str(i) for i in data ]
    c = {i:data.count(i) for i in data}
    mod = max(c,key=lambda x:c[x])
    if all(x==1 for x in c.values()) is True:
        return 1
    else:
        return mod


def mean_deviation_u(a_mean,data,n):
    num = [ abs(i-a_mean) for i in data ]
    md_u = sum(num)/n
    return md_u


def mean_deviation_med(med,data,n):
    num = [ abs(i-med) for i in data ]
    md_med = sum(num)/n
    return md_med

# def standard_deviation():
    

def plot(data):
    plt.hist(data,edgecolor='black')
    plt.show()


def main():
    data = [44,46,49,52,55,62,67,72,77,80,83,86,88,90,92,94,99,100,101,106]
    print('Data: ',data)
    n = len(data)
    a_mean = arithmetic_mean(data,n)
    print('Arithmetic mean: ',round(a_mean,2))
    g_mean = geometric_mean(data,n)
    print('Geometric mean',round(g_mean,2))
    h_mean = harmonic_mean(data,n)
    print('Harmonic mean',round(h_mean,2))
    med = median(data,n)
    print('Median: ',med)
    # plot(data)
    mod = mode(data)
    print('Mode: ',mod)
    md_u = mean_deviation_u(a_mean,data,n)
    print('Mean deviation around mean: ',md_u)
    md_med = mean_deviation_med(med, data, n)
    print('Mean deviation around median: ', md_med)


if __name__ == '__main__':
    main()