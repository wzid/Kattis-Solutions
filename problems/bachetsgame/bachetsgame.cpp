#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, m;
    
    while (cin >> n >> m) {
        int d[1000002] = {0};
        vector<int> moves;
        for (int i = 0; i < m; i++) {
            int a;
            cin >> a;
            moves.push_back(a);
        }
        sort(moves.begin(), moves.end());
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < m; j++) {
                int k = moves[j];
                if (i-k < 0) {
                    break;
                }
                if (d[i-k] == 0) {
                    d[i] = 1;
                }
            }
        }
        
        if (d[n] == 1) {
            cout << "Stan wins" << endl;
        } else {
            cout << "Ollie wins" << endl;
        }
    }
}