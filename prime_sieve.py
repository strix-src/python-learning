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
        count+=1
        print(i,end=' ')
        if count%20==0:
            print()
    print()

if __name__=='__main__':
    while True:
        try :    
            a=int(input("请输入数字:"))
            if a<2:
                print("请输入大于2的整数")
                continue
            break
        except ValueError:
            print("请输入数字不是其他")
    result_list=isprime_sieve(a)
    print_primes(result_list)
    print(f"在{a}之内一共有{len(result_list)}个素数")
