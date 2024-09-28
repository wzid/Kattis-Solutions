#include <bits/stdc++.h>

using namespace std;

#define endl '\n'
typedef long long ll;

ll pow_mod(ll base, ll exp, ll mod) {
   base %= mod;
   ll result = 1;
   while (exp > 0) {
       if (exp & 1) result = (result * base) % mod;
       base = (base * base) % mod;
       exp >>= 1;
   }
   return result;
}

int main() {
    int c, r;
    cin >> r >> c;
    cout << r*pow_mod(r-1, c-1, 998244353) % 998244353 << endl;
    return 0;
}