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

    int n, s;
    cin >> n >> s;

    int temp_s = s;

    int res = 0;

    rep(i, 0, n) {
        string shots;
        cin >> shots;
        int shots_int = 0;
        
        if (int index = shots.find("L") != string::npos) {
            shots_int = stoi(shots.substr(0, index));
            shots_int++;
        } else {
            shots_int = stoi(shots);
        }

        if (shots_int > s) {
            res++;
            s = temp_s - shots_int;
        } else {
            s -= shots_int;
        }
    }

    cout << res << endl;

    return 0;
}
