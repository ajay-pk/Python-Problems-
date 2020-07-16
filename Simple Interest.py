# Python3 program to find simple interest 
# for given principal amount, time and
# rate of interest.


def simple_interest(p,t,r):  #create a function
#let us print the inputs of the user
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is',r)

    si = (p * t * r)/100 #calculation and formula

    print('The Simple Interest is', si) #print the result or
    return si # return the result (optional)

p=float(input())
t=float(input())
r=float(input())

simple_interest(p,t,r) #call the function
