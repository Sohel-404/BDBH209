#Lab_1 3 Jan 2025

# 1.1
x<-2.7/2
print(x)

#1.2.1
x<-2.7 %/% 2
print(x)

#1.2.2
x<-2.7 %%2
print(x)

#1.3
x<-10+5i/2
print(x)

#1.4
a<-2.5
print(round(a))

#1.5
b<--2.5
print(round(b))

#1.6
c<-2 %/% 4-1
print(c)

#1.7
d<-3*2**2
print(d)

#1.8
e<-3**2*2
print(e)

#1.9
f<-7 %/% 4
print(f)

#1.10
g<-7%%4
print(g)

#1.11
h<--7%%4
print(h)

#1.12
i<-trunc(5.7)  #The trunc() function removes the decimal part
print(i)

#1.13
j<-trunc(-5.7) #The trunc() function removes the decimal part
print(j)

#2 
x<-5.7
print(ceiling(x))

f1<-function(x)floor(x+1)  # Adding 1 ensures that any fractional part will push 
f1(5.7)                    # the value to the next integer if it's positive.

#3
a<-1
b<-2
c<-4

#3.1
x<-(a&&b)   # '&&' is used for element-wise logical AND.
print(x)    # a and b are non-zero (treated as TRUE), the result is TRUE.

#3.2
x<-!(a<b) || (c>b) # Evaluating ' not(!) a<b or(||) c>b '
print(x)

#4.1
x<-c(5,3,7,8) # Creating a numeric vector x containing values 5,6,7,8.
print(x)      # datatype 'double'.

#4.2
is.integer(x) # FALSE. Since datatype of is double.

#4.3
is.numeric(x) # TRUE. Since numeric type includes both double and integer.

#4.4
x<-integer(x) # Doesn't convert the datatype to integer. 
print(x)      # initializes x as an integer vector of zeros.

#4.5
x<-c(5,3,7,8) 
print(x)

is.integer(x)

is.numeric(x)

x<-as.integer(x) #  converts x from type double (numeric) to type integer.
is.integer(x)    #  return TRUE, as x is of type integer.

#5.1
x<-sqrt(2) # square root of two is computed and assigned to x.
print(x)

#5.2
x*x==2 # comparison '==' checks for exact equality, so it returns FALSE.

#5.3
x*x-2 # computes magnitude of the error caused by floating point representation.

#5.4
all.equal(x*x,2) # compare numeric values, checks if two values are nearly equal.
                  











