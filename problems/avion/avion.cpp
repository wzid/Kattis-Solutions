#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

int main() {

    
    bool found = false;
    for (int i = 0; i < 5; i++) {
        string x;
        cin >> x;
        if (x.find("FBI") != string::npos) {
            cout << i+1 << " ";
            found = true;
        }
    }

    if (!found) {
        cout << "HE GOT AWAY!" << endl;
    }

    return 0;
}