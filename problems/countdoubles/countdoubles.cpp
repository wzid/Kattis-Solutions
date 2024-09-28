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
    int n, m;
    cin >> n >> m;
    vi vals;
    For(i, n) {
        int x;
        cin >> x;
        vals.push_back(x);
    }

    int count = 0;
    for (int i = 0; i < ((n - m) + 1); i++) {
        int even_count = 0;

        For(j, m) {
            if (vals[i + j] % 2 == 0) {
                even_count++;
            }
        }

        if (even_count >= 2) {
            count++;
        }
    }

    cout << count << endl;
    return 0;
}