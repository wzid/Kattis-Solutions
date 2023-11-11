#include <iostream>
#include <vector>
#include <unordered_map>
#include <cmath>

using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef unordered_map<int, int> uimap;

ll euclid(ll a, ll b, ll &x, ll &y) {
    if (!b) return x = 1, y = 0, a;
    ll d = euclid(b, a % b, y, x);
    return y -= a/b * x, d;
}

int main() {
    int n;
    cin >> n;
    rep(i, 0, n) {
        ll kids, bags;
        cin >> kids >> bags;
        
        if (bags == 1 && kids > 1) {
            cout << kids + 1 << endl;
            continue;
        }

        if (kids == 1 && bags == 1) {
            cout << 2 << endl;
            continue;
        }

        if (kids == 1 && bags > 1) {
            cout << 1 << endl;
            continue;
        }

        ll x, y;
        ll d = euclid(bags, kids, x, y);
        
        if (x == 0 || d!= 1) {
            cout << "IMPOSSIBLE" << endl;
            continue;
        } else {
            ll nee = (x % kids + kids) % kids;
            cout << nee << endl;
        }
    }
}