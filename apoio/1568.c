#include <bits/stdc++.h>

using namespace std;

typedef long long int lli;
typedef lli ll;

bitset<30000002> isprime;
lli prime[30000002], prime_cont = 0;
lli lim = 30000001;

void primo() {
  prime[prime_cont++] = 2;

    isprime.set();
    for(lli i=3; i<=lim; i+=2) 
    {
        if(isprime[i]) 
        {
            prime[prime_cont++] = i;

            for(lli j = i + i; j <= lim; j+= i) 
                isprime.reset(j);
        }
    }
}
inline ll fatora(ll n)
{
    ll i = 0;
    ll ans = 1;
    ll div;
    while (n > 1 && i < prime_cont)
    {
        div = 0;
        while(n > 1 && n % prime[i] == 0)
        {
            n/= prime[i];
            div++;
        }
        i++;
        if (i > 1) ans*= (div + 1);
    }
    return ans;
}

int main()
{
    ll n;
    primo();

    while(cin >> n)
    {
        if (!n) return 0;
        cout << fatora(n) << '\n';
    }
}
