#include <iostream>

using namespace std;

int main() {
    int x, y, n;
    cin >> x >> y >> n;
    
    string s;
    for (int i = 1; i <= n; i++) {
        s = "";
        if (i % x == 0) {
            s += "Fizz";
        }
        if (i % y == 0) {
            s += "Buzz";
        }
        
        if (!s.length()) {
            cout << i << endl;
        } else {
            cout << s << endl;
        }
    }
}