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

const int LIM = 1'000'000;
int phi[LIM];

void calculatePhi() {
	rep(i,0,LIM) phi[i] = i&1 ? i : i/2;
	for (int i = 3; i < LIM; i += 2) if(phi[i] == i)
		for (int j = i; j < LIM; j += i) phi[j] -= phi[j] / i;
}

ll euclid(ll a, ll b, ll &x, ll &y) {
    if (!b) return x = 1, y = 0, a;
    ll d = euclid(b, a % b, y, x);
    return y -= a/b * x, d;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    calculatePhi();
    int t;
    cin >> t;

    rep(i, 0, t) {
        int n, e;
        cin >> n >> e;
        int totient = phi[n];
        ll x, y;
        euclid(e, totient, x, y);
        ll result = (x % totient + totient) % totient;
        cout << result << endl;
    }
}