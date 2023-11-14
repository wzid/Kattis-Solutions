#include <iostream>
#include <vector>
#include <unordered_map>
#include <cmath>
#include <algorithm>

using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef unordered_map<int, int> uimap;

// Used to fix when modding negative numbers
ll mod(ll x, ll m) {
    return ((x % m) + m) % m;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;
    rep(i, 0, n) {
        char roll;
        int D, H, M;

        cin >> roll >> D >> H >> M;

        int hours_to_change = floor(D / 60);
        int minutes_to_change = D % 60;

        if (roll == 'F') {
            int new_minutes = M + minutes_to_change;
            int new_hour = mod(H + hours_to_change, 24);
            
            if (new_minutes >= 60) {
                new_minutes = mod(new_minutes, 60);
                new_hour = mod(new_hour + 1, 24);
            }
            cout << new_hour << " " << new_minutes << '\n';
        } else {
            int new_minutes = M - minutes_to_change;
            int new_hour = mod(H - hours_to_change, 24);
            
            if (new_minutes < 0) {
                new_minutes = mod(new_minutes, 60);
                new_hour = mod(new_hour - 1, 24);
            }
            cout << new_hour << " " << new_minutes << '\n';
        }

    }
}