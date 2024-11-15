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

bool is_prime(int n) {
    if (n < 2) return false;
    if (n <= 3) return true;
    if (!(n % 2) || !(n % 3)) return false;
    for (int i = 5; i * i <= n; i += 6) {
        if (!(n % i) || !(n % (i + 2))) return false;
    }
    return true;
}

int get_prime_grid_count(VV<int>& grid, int n, int m, int row, int column) {
    if (row > n) return 1;
    if (column > m) return get_prime_grid_count(grid, n, m, row + 1, 0);

    int prime_grid_count = 0;

    int curr_row = 0, curr_col = 0;
    For(i, column) curr_row = curr_row*10 + grid[row][i];
    For(i, row) curr_col = curr_col*10 + grid[i][column];

    For(i, 10) {
        int r = curr_row*10 + i;
        int c = curr_col*10 + i;
        if (is_prime(r) && is_prime(c)) {
            grid[row][column] = i;
            prime_grid_count += get_prime_grid_count(grid, n, m, row, column + 1);
        }
    }

    return prime_grid_count;
}

int main() {
    cin.tie(0)->sync_with_stdio(0);

    int n, m;
    cin >> n >> m;
    VV<int> grid(n, vi(m, 0));
    cout << get_prime_grid_count(grid, n - 1, m - 1, 0, 0) << '\n';
}