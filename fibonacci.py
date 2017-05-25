###Rabbits and Recurrence Relations ###
def fib(n,k):
    a, b = 1, 1
    for i in range (2,int(n)):
        a, b = b, int(k)*a + b #只需要保存最近两个月的数量即可
    print  b
