def isprime_sieve(a):
    if a<2:return []
    isprime=[True]*(a+1)
    isprime[0]=isprime[1]=False
    for i in range(2,int(a**0.5)+1):
        if isprime[i]:
            for j in range(i*i,a+1,i):
                isprime[j]=False
    primes=[i for i in range(2,a+1) if isprime[i]]
    return primes

def print_primes(result_list):
    count=0
    for i in result_list:
        print(i,end=' ')
        count+=1
        if count%10==0:
            print()
    print()

if __name__=='__main__':
    a=int(input("请输入数字:"))
    result_list=isprime_sieve(a)
    print_primes(result_list)
