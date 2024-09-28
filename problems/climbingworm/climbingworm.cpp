#include <iostream>

using namespace std;

int main() {
    int a, b, h;
    cin >> a >> b >> h;
    
    int position = 0;
    int count = 0;
    while (true) {
        position += a;
        count++;
        if (position >= h)
            break;
        position -= b;
    }
    
    cout << count << endl;
    
    return 0;
}