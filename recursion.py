def countdown(n):
    if n == 0: # n == 0, countdown(0)
        print("Liftoff!") 
        return # ends function execution
    print(n) # print 5 , print 4, print 3, print 2, print 1
    countdown(n - 1) #countdown(4), countdown(3), countdown(2), countdown(1), countdown(0)

countdown(5)


def countup(n): 
    if n == 0: # n == 0, countup(0)
        return
    countup(n - 1) # countup(2), countup(1), countup(0) # if it continues to call countup(n-1) how does it reach the print(n) statementt? 
    print(n) 

countup(3)
print()
def sO(n):
    if n <= 5:
        print("done")
        return
    sO(n - 2)
    sO(n / 2)
    print(n)

sO(10)
print()

def total(n):
    if n == 0:
        return 0
    return n + total(n - 1)

print(total(3))   # 6