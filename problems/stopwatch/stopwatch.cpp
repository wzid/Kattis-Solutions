#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    bool stopped = true;
    int last = 0;
    int sum = 0;
    
    if (n % 2 != 0) {
        cout << "still running" << endl;
        return 0;
    }
    
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        
        if (stopped) {
            last = x;
        } else {
            sum = sum + (x - last);
        }
        stopped = !stopped;
    }
    
    cout << sum << endl;
}