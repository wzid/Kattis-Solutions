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
    string s;
    cin >> s;
    
    int b = 0, k = 0;

    for (char &c : s) {
        if (c == 'b')
            b++;
        if (c == 'k')
            k++;
    }
    
    if (b > k) {
        cout << "boba" << endl;
    } else if (k > b) {
        cout << "kiki" << endl;
    } else if (k == b && k != 0) {
        cout <<"boki" << endl;
    } else if (k == 0 && b == 0) {
        cout << "none" << endl;
    }
    return 0;
}