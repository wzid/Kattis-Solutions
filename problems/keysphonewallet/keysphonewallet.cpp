#include <bits/stdc++.h>

using namespace std;

enum Items { KEYS = 1, PHONE = 2, WALLET = 4 };
int bitmask = 0;

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        string x;
        cin >> x;
        if (x == "keys") {
            bitmask |= KEYS;
        } else if (x == "phone") {
            bitmask |= PHONE;
        } else if (x == "wallet") {
            bitmask |= WALLET;
        }
    }
    
    if (bitmask == (KEYS | PHONE | WALLET)) {
        cout << "ready" << endl;
    } else {
        if (!(bitmask & KEYS)) {
            cout << "keys" << endl;
        }
        if (!(bitmask & PHONE)) {
            cout << "phone" << endl;
        }
        if (!(bitmask & WALLET)) {
            cout << "wallet" << endl;
        }
    }
}