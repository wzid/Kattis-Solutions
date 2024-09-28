#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define For(i, a) for(int i = 0; i < (a); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
#define is_in(x, s) ((s).find(x) != (s).end())
#define endl '\n'
typedef long long ll;
typedef long double ld;
template<typename T> using V=vector<T>;
template<typename T> using VV=vector<vector<T>>;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef unordered_map<int, int> uimap;


int main() {
    cin.tie(0)->sync_with_stdio(0);
    priority_queue<int, vector<int>, greater<int>> values_to_use; // min heap

    int n;
    cin >> n;
    uimap degree;
    vi input(n);

    For (i, n) {
        int a;
        cin >> a;
        input[i] = a;
        degree[a]++;
    }

    if (input[n-1] != n+1) {
        cout << "Error\n";
        return 0;
    }



    rep (i, 1, n+2) {
        if (!is_in(i, degree)) values_to_use.push(i);
    }


    vi result(n);

    For (i, n) {

        result[i] = values_to_use.top();
    
        // decrease degree
        degree[input[i]]--;

        values_to_use.pop();
        // if the degree of the value is no longer in our input then we can use it
        if (degree[input[i]] == 0) { 
            values_to_use.push(input[i]);
        }
    }

    for (auto i : result) {
        cout << i << '\n';
    }

    return 0;
}