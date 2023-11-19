#include <bits/stdc++.h>

using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sort_desc(x) sort(x.rbegin(), x.rend())
#define sz(x) (int)(x).size()
#define endl '\n'
template<typename T> using V=vector<T>;
template<typename T> using VV=vector<vector<T>>;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef unordered_map<int, int> uimap;

void rotate(VV<char>& matrix) {
    int size = matrix.size();
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < i; j++) {
            int temp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = temp;
        }
    }

    int iterations = size % 2 == 0 ? size / 2 : (size - 1) / 2;

    for (int i = 0; i < size; i++) {
        for (int j = 0; j < iterations; j++) {
            int temp = matrix[i][j];
            int j2 = (size - 1) - j;
            matrix[i][j] = matrix[i][j2];
            matrix[i][j2] = temp;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;
    rep(i, 0, n) {
        string s;
        cin >> s;
        // Get size
        int size = 0;
        rep(j, 0, 101) {
            if (s.length() <= j*j) {
                size = j;
                break;
            }
        }

        VV<char> matrix(size, vector<char>(size));
        for (int j = 0; j < s.length(); j++) {
            matrix[j / size][j % size] = s[j];
        }

        rotate(matrix);
        string result = "";
        for (int j = 0; j < size; j++) {
            for (int k = 0; k < size; k++) {
                if (matrix[j][k] != 0)
                    result += matrix[j][k];
            }
        }
        cout << result << endl;
    }
    return 0;

}
