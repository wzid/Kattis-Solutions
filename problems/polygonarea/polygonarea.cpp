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
    rep(i, 0, x.size()- 1) {
        // determinant: https://en.wikipedia.org/wiki/Determinant
        result += (x[i] * y[i+1]) - (x[i+1] * y[i]);
    }
    return result / 2;
}

int main() {
    cin.tie(0)->sync_with_stdio(0);

    int n;
    cin >> n;

    while (n != 0) {
        vi x_i, y_i;
        For(i, n) {
            int x, y;
            cin >> x >> y;
            x_i.push_back(x);
            y_i.push_back(y);
        }
        x_i.push_back(x_i[0]);
        y_i.push_back(y_i[0]);

        double result = shoelace_formula(x_i, y_i);
        if (result < 0) {
            cout << fixed << setprecision(1) << "CW " << abs(result) << endl;
        } else {
            cout << fixed << setprecision(1) << "CCW " << result << endl;
        }
        cin >> n;
    }

    return 0;
}