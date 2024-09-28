#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    int* arr = new int[n];
    int towers = 0;
    cin >> arr[0];
    int last = arr[0];

    for (int i = 1; i < n; i++) {
        cin >> arr[i];

        if (arr[i] > last) {
            towers += 1;
        }
        last = arr[i];
    }
    
    cout << towers + 1 << endl;
}