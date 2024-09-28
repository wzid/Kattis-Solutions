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

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, min, max;

    cin >> n >> min >> max;
    bool found_max = false;
    bool found_min = false;
    For(i, n-1) {
        int x;
        cin >> x;
        if (x == max)
            found_max = true;
        
        if (x == min)
            found_min = true;
    }

    if (!found_max && !found_min) {
        cout << -1 << endl;
    } else if (!found_max) {
        cout << max << endl;
    } else if (!found_min) {
        cout << min << endl;
    } else {
        rep(i, min, max +1) {
            cout << i << endl;
        }
    }

    return 0;
}