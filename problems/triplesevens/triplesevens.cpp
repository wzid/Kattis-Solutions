#include <bits/stdc++.h>

using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define For(i, a) for(int i = 0; i < (a); ++i)
#define all(x) begin(x), end(x)
#define is_in(x, s) ((s).find(x) != (s).end())
#define endl '\n'
#define pi acos(-1.0)
typedef long long ll;
template<typename T> using V=vector<T>;
template<typename T> using VV=vector<vector<T>>;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef unordered_map<int, int> uimap;

int main() {
    int n, a;
    cin >> n;

    for (int i = 0; i < 3; i++) {
        bool flag = false;
        for (int j = 0; j < n; j++) {
            cin >> a;
            if (a == 7)
                flag = true;
        }
        if (!flag) {
            cout << 0;
            return 0;
        }
    }

    cout << 777;
}