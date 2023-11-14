#include <iostream>
#include <vector>
#include <unordered_map>
#include <cmath>
#include <algorithm>
#include <bitset>

//#pragma GCC target ("avx2")

//#pragma GCC optimize ("Ofast")

using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define repll(i, a, b) for(ll i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef unordered_map<int, int> uimap;

const int LIM = 32768;
vector<int> primes;
bitset<LIM>p;
void sieve(){
    p.set();
    repll(i, 2, LIM) {
        if(!p[i]) continue;
        primes.push_back(i);
        for(ll j = i*i; j<LIM; j+=i){
            p[j] = 0;
        }
    }
}


ll eulerPhi(int x){
    ll ret = x;
    for(int i =0; i<primes.size() && primes[i]*primes[i]<=x; ++i){
        if(x%primes[i]==0){
            ret-=ret/primes[i];
            while(x%primes[i]==0){
                x/=primes[i];
            }
        }
    }
    if(x>1){
        ret-=ret/x;
    }
    return ret;
}


int main() {
    ll n;
    cin >> n;
    sieve();
    while (n != 0) {
        cout << eulerPhi(n) << '\n';
        cin >> n;

    }
}