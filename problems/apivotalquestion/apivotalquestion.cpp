#include <bits/stdc++.h>

using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
#define endl '\n'
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef unordered_map<int, int> uimap;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    // min heap
    int n;
    cin >> n;
    vi nums(n+1), max_left(n+1), min_right(n+1);

    rep(i, 0, n) {
        cin >> nums[i];
        
        if (i > 0) {
            max_left[i] = max(nums[i-1], max_left[i-1]);
        } else {
            max_left[i] = nums[i];
        }
    }

    for (int i = n-1; i > -1; --i) {
        if (i < n-1) {
            min_right[i] = min(nums[i+1], min_right[i+1]);
        } else {
            min_right[i] = nums[i];
        }
    }

    vi values;
    rep(i, 0, n) {
        if (nums[i] >= max_left[i] && nums[i] <= min_right[i]) {
            values.push_back(nums[i]);
        }
    }

    cout << sz(values) << " ";
    rep(i, 0, min(100, sz(values)) ) {
        cout << values[i] << " ";
    }

    cout << endl;
}
