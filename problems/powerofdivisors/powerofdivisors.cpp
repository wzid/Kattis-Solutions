#include <iostream>
#include <iomanip>
#include <bitset>
#include <cmath>
#include <vector>
#include <array>
#include <unordered_map>
#include <algorithm>

using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef unordered_map<int, int> umap;

const int MAX_PR = 5'000'000;
bitset<MAX_PR> isprime;
vi eratosthenesSieve(int lim) {
    isprime.set(); isprime[0] = isprime[1] = 0;
    for (int i = 4; i < lim; i += 2) isprime[i] = 0;
    for (int i = 3; i*i < lim; i += 2) if (isprime[i])
        for (int j = i*i; j < lim; j += i*2) isprime[j] = 0;
    vi pr;
    rep(i,2,lim) if (isprime[i]) pr.push_back(i);
    return pr;
}

vi primes = eratosthenesSieve(1e6);

const static int primes_length = sizeof(primes) / sizeof(primes[0]);

int number_of_divisors(ll x) {
    unordered_map<ll, ll> divisors;
    ll ans = 1;
    int prime_index = 0;

    while (x > 1) {
        int curr_prime = primes[prime_index];

        if (x % curr_prime == 0) {
            x /= curr_prime;
            divisors[curr_prime]++;
        } else {
            prime_index++;
            if (prime_index >= primes.size()) {
                divisors[x]++;
                break;
            }
            
        }
    }
    
    for (auto [k, v] : divisors) {
        ans *= (v + 1);
    }
    return ans;
}

bool is_perfect_ith_root(ll x, ll i) {
    ll root = round(pow(x, (long double)1/i));
    ll xn = 1, pn = i;
    while (pn--) {
        xn *= root;
    }
    return xn == x;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    ll x;
    cin >> x;

    if (x == 1) {
        cout << 1 << endl;
        return 0;
    } 
    unordered_map<ll, ll> roots;
    ll smallest_value = 0;
    for (ll i = 2; i <= 60; i++) {
        if (is_perfect_ith_root(x, i)) {
            ll v = round(pow(x, 1.0 / i));
    
            if (number_of_divisors(v) == i) {
                if (smallest_value == 0) {
                    smallest_value = v;
                } else {
                    smallest_value = min(smallest_value, v);
                }
            }
        }
    }

    // if there results
    if (smallest_value != 0) {
        cout << smallest_value << endl;
    } else {
        cout << -1 << endl;

    }

    
}