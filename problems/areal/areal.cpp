#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int main() {
    long long a;
    cin >> a;
    double perimeter = sqrt(a);
    cout << fixed << perimeter*4 << endl;
}