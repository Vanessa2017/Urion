#include <bits/stdc++.h>

def primo(self):  prime[prime_cont++] = 2

    isprime.set()
    for(lli i=3; i<=lim; i+=2) 
        if(isprime[i]) 
            prime[prime_cont++] = i

            for(j = i + i; j <= lim; j+= i) 
                isprime.reset(j)



inline ll fatora(ll n)
    i = 0
    ans = 1
    ll div
    while (n > 1 and i < prime_cont)
        div = 0
        while(n > 1 and n % prime[i] == 0)
            n/= prime[i]
            div++

        i++
        if i > 1) ans*= (div + 1:

    return ans


def main(self):
    ll n
    primo()

    while(cin >> n)
        if (not n) return 0
        cout << fatora(n) << '\n'


