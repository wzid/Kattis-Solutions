#include <bits/stdc++.h>

using namespace std;

int main() {
    int l, r;
    cin >> l >> r;
    if (sqrt(l*l+l*l) > r*2)
        cout << "nope";
    else
        cout << "fits";
}