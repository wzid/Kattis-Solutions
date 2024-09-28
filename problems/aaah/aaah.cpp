#include <iostream>

using namespace std;

int main() {
    string s1;
    string s2;
    cin >> s1 >> s2;
    
    if (s1.length() >= s2.length()) {
        cout << "go" << endl;
    } else {
        cout << "no" << endl;
    }
    
    return 0;
}