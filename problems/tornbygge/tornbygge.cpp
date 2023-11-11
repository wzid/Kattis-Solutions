#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    
    int towers = 0;
    int j;
    cin >> j;
    
    int last = j;
    for (int i = 1; i < n; i++) {
        cin >> j;
        
        if (j > last) {
            towers += 1;
        }
        last = j;
    }
    
    cout << towers + 1 << endl;
}