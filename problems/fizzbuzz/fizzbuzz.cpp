#include <iostream>
#include <string>

using namespace std;

int main() {
    int x, y, n;
    cin >> x >> y >> n;
    
    for (int i = 1; i <= n; i++) {
        string output = "";
        if (i % x == 0) {
            output += "Fizz";
        }
        if (i % y == 0) {
            output += "Buzz";
        }
        
        if (output.size() == 0) {
            cout << i << endl;
        } else {
            cout << output << endl;
        }
    }
}