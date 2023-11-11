#include <iostream>
#include <vector>
#include <unordered_map>
#include <cmath>
#include <bitset>

using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef unordered_map<int, int> uimap;

const int MAX_PR = 10'000'000;
bitset<MAX_PR> isprime;
vi eratosthenesSieve(int lim) {
    isprime.set(); isprime[0] = isprime[1] = 0;
    for (int i = 4; i < lim; i += 2) isprime[i] = 0;
    for (int i = 3; i*i < lim; i += 2) if (isprime[i])
        for (int j = i*i; j < lim; j += i*2) isprime[j] = 0;
    vi pr;
    rep(i,2,lim) {
        if (isprime[i]) 
            pr.push_back(i);
        if (pr.size() > 100000) break;
    }
    return pr;
}

vi primes = eratosthenesSieve(1e7);

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int l, h;

    cin >> l >> h;
    string p;
    cin >> p;

    int sum = 0;
    rep(i, l, h+1) {
        int curr_prime = primes[i-1];
        string prime_str = to_string(curr_prime);
        if (prime_str.find(p) != string::npos) {
            sum++;
        }
    }
    cout << sum << endl;
}