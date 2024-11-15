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


double dist(pii p, pii q) {
    return sqrt(((p.first - q.first) * (p.first - q.first)) + ((p.second - q.second) * (p.second - q.second)));
}


int main() {
    cin.tie(0)->sync_with_stdio(0);

    int n;
    cin >> n;

    For(i, n) {
        int s, h;
        cin >> s >> h;
        V<pii> points(h);
        For(j, h) {
            cin >> points[j].first >> points[j].second;
        }

        bool works = false;

        rep(x, 1, s) {
            rep(y, 1, s) {
                works = true;
                for (auto &[px, py] : points) {
                    if (px == x && py == y) {
                        works = false;
                        break;
                    }

                    double d = dist({px, py}, {x, y});
                    if (x + d > s || x - d < 0 || y - d < 0 || y + d > s) {
                        works = false;
                    }
                }
                if (works) {
                    cout << x << " " << y << '\n';
                    break;
                }
            }
            if (works)
                break;
        }
        if (!works)
            cout << "poodle\n";
    }
}