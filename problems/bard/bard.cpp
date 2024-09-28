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

double shoelace_formula(vector<int>& x, vector<int>& y) {
    double result = 0;
    rep(i, 0, x.size() - 1) {
        // determinant: https://en.wikipedia.org/wiki/Determinant
        result += (x[i] * y[i + 1]) - (x[i + 1] * y[i]);
    }
    return result / 2;
}

int main() {
    cin.tie(0)->sync_with_stdio(0);

    int n;
    cin >> n;
    int e;
    cin >> e;

    int bard_songs = 0;
    vi villagers(n + 1, 0);

    vi was_there;
    For(i, e) {
        int k;
        cin >> k;

        For(i, k) {
            int v;
            cin >> v;
            was_there.push_back(v);
        }

        bool bard_was_present = false;
        for (auto v : was_there) {
            if (v == 1) {
                bard_was_present = true;
                break;
            }
        }

        if (bard_was_present) {
            bard_songs++;
            for (auto v : was_there) {
                villagers[v - 1]++;
            }
        } else {
            for (auto v : was_there) {
                villagers[v - 1] = bard_songs;
            }
        }
        was_there.clear();
    }

    For(i, villagers.size()) {
        int songs_known = villagers[i];
        if (songs_known == bard_songs) {
            cout << i + 1 << endl;
        }
    }
    return 0;
}