#include <bits/stdc++.h>

using namespace std;

#define rep(i, a, b) for (int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sort_desc(x) sort(x.rbegin(), x.rend())
#define sz(x) (int)(x).size()
#define endl '\n'
template <typename T>
using V = vector<T>;
template <typename T>
using VV = vector<vector<T>>;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef unordered_map<int, int> uimap;

int main()
{
    cin.tie(0)->sync_with_stdio(0);

    int real_n;
    cin >> real_n;

    int n;
    cin >> n;
    V<string> res;

    while (real_n > 0) {
        long long s = 0;
        rep(i, 0, n) {
            long long tmp;
            cin >> tmp;
            s += tmp % n;
        }
        if (s % n == 0) {
            res.push_back("YES");
        } else {
            res.push_back("NO");
        }

        real_n--;
        if (real_n != 0) {
            cin >> n;
        }

    }

    for (auto i : res) {
        cout << i << endl;
    }

    return 0;
}
