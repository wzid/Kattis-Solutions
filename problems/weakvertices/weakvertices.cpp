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
    int n;
    cin >> n;
    while (n != -1) {
        unordered_map<int, vi> m;
        For(i, n) {
            For(j, n) {
                int x;
                cin >> x;
                if (x == 1) {
                    m[i].push_back(j);
                }
            }
        }

        vi weak;

        For(i, n) {
            unordered_set<int> needs;
            bool success = false;
            for (auto index : m[i]) {
                if (needs.find(index) != needs.end()) {
                    success = true;
                    break;
                } else {
                    for (auto ind : m[index]) {
                        needs.insert(ind);
                    }
                }
            }
            
            if (!success) {
                weak.push_back(i);
            }
        }

        sort(all(weak));

        // print a line of all the weak vertices
        for (int i = 0; i < weak.size(); i++) {
            cout << weak[i];
            if (i != weak.size() - 1) {
                cout << " ";
            }
        }
        cout << '\n';
        cin >> n;
    }
    return 0;
}