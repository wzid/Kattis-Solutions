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
    int n;
    cin >> n;
    V<pair<int, int>> ranges(n);
    For(i, n) {
        int l, u;
        cin >> l >> u;
        ranges[i] = make_pair(l, u);
    }

    sort(all(ranges));
    V<pii> results;
    For(i, n) {
        int l = ranges[i].first;
        int u = ranges[i].second;
        int found = -1;
        int shrink_l = -1, shrink_u = -1;
        For(j, results.size()) {
            pii r = results[j];
            if (l >= r.first && l <= r.second) {
                shrink_u = min(r.second, u);
                shrink_l = max(r.first, l);
                found = j;
                break;
            }
        }
        if (found == -1) {
            results.push_back(make_pair(l, u));
        } else {
            results[found] = make_pair(shrink_l, shrink_u);
        }
    }

    cout << results.size() << endl;
    return 0;
}