#include <iostream>
#include <vector>
#include <unordered_map>
#include <cmath>
#include <algorithm>

using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef unordered_map<int, int> uimap;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t;
    cin >> t;
    rep(i, 0, t) {
        ll n;
        cin >> n;
        ll total_candy = 0;
        rep(j, 0, n) {
            ll x;
            cin >> x;
            total_candy += x % n;
            total_candy %= n;
        }
        if (total_candy % n == 0) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    }
}