#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    string x, y;

    cin >> x >> y;

    reverse(x.begin(), x.end());
    reverse(y.begin(), y.end());

    int x_int = stoi(x);
    int y_int = stoi(y);

    cout << max(x_int, y_int) << endl;

    return 0;
}