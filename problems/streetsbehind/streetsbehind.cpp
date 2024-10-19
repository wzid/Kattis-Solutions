#include <bits/stdc++.h>

using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define For(i, a) for(int i = 0; i < (a); ++i)
#define all(x) begin(x), end(x)
#define is_in(x, s) ((s).find(x) != (s).end())
#define endl '\n'
#define pi acos(-1.0)
typedef long long ll;
template<class T> using V=vector<T>;
template<class T> using VV=vector<vector<T>>;
template<class K, class V> using umap=unordered_map<K, V>;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef unordered_map<int, int> uimap;

ll ceil_div(ll n, ll d) {
    return (n + d - 1) / d;
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int t;
    cin >> t;

    For(i, t){
        ll n, k, a, b;
        cin >> n >> k >> a >> b;

        ll iterations = 0;
        bool failed = false;
        ll d = b - a;
        while (k > 0) {
            ll top = n * d;
            ll convert = top / a;
            if (convert == 0) {
                failed = true;
                break;
            }

            if (top % a != 0) {
                ll x = (a - top + convert*a) / (convert * d);
                x = max(1LL, min(x, ceil_div(k, convert)));
                
                iterations += x;
                ll conversion = min(k, x * convert);
                k -= conversion;
                n += conversion;
            } else {
                convert = min(k, convert);
                n += convert;
                k -= convert;
                iterations += 1;
            }

        }

        if (failed) {
            cout << "-1\n";
        } else {
            cout << iterations << '\n';
        }

    }

}