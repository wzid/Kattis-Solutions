#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    bool stopped = true;
    int lastStart = 0;
    int time = 0;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        if (stopped == false) {
            time += x - lastStart;
        } else {
            lastStart = x;
        }
        stopped = !stopped;
    }
    if (stopped) {
        cout << time << endl;
    } else {
        cout << "still running" << endl;
    }
}