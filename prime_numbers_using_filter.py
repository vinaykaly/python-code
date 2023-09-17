
numbers = range(2,1000)

def prime(num):

    for i in range(2,num):    #checking whether prime or not 

      if num%i == 0:
        return False

    return True

res = list(filter(prime,numbers))     # filter (fun,var)       

print(res)


