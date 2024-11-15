#include <bits/stdc++.h>

using namespace std;

#define rep(i, a, b) for (int i = a; i < (b); ++i)
#define For(i, a) for (int i = 0; i < (a); ++i)
#define all(x) begin(x), end(x)
#define is_in(x, s) ((s).find(x) != (s).end())
#define endl '\n'
#define pi acos(-1.0)
typedef long long ll;
template <class T>
using V = vector<T>;
template <class T>
using VV = vector<vector<T>>;
template <class K, class V>
using umap = unordered_map<K, V>;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef unordered_map<int, int> uimap;

const int MAX_PR = 70'000;
bitset<MAX_PR> isprime;
vi eratosthenes_sieve(int lim) {
    isprime.set();
    isprime[0] = isprime[1] = 0;
    for (int i = 4; i < lim; i += 2) isprime[i] = 0;
    for (int i = 3; i * i < lim; i += 2)
        if (isprime[i])
            for (int j = i * i; j < lim; j += i * 2) isprime[j] = 0;
    vi pr;
    rep(i, 2, lim) if (isprime[i]) pr.push_back(i);
    return pr;
}

vi primes = eratosthenes_sieve(50'000);

unordered_map<int, bool> happy_or_not;  // 8056075

bool is_happy(int n) {
    if (is_in(n, happy_or_not)) {
        return happy_or_not[n];
    }

    unordered_set<int> to_set;
    to_set.insert(n);
    while (n > 3) {
        int temp_n = n;
        int sum = 0;
        while (temp_n != 0) {
            sum += (temp_n % 10) * (temp_n % 10);
            // C++ rounds down in integer division which is what we want
            temp_n /= 10;
        }
        if (is_in(sum, to_set)) {
            for (auto &val : to_set) {
                happy_or_not[val] = false;
            }
            return false;
        }
        to_set.insert(sum);
        if (is_in(sum, happy_or_not)) {
            return happy_or_not[sum];
        }
        n = sum;
    }
    if (n == 1) {
        for (auto &val : to_set) {
            happy_or_not[val] = true;
        }
        return true;
    } else {
        for (auto &val : to_set) {
            happy_or_not[val] = false;
        }
        return false;
    }
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int p;
    cin >> p;

    For(i, p) {
        int k, m;
        cin >> k >> m;

        if (!isprime[m]) {
            cout << k << " " << m << " NO\n";
        } else {
            bool happy = is_happy(m);
            cout << k << " " << m << (happy ? " YES\n" : " NO\n");
        }
    }
}