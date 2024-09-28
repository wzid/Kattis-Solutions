#include <algorithm>
#include <iostream>
#include <unordered_map>

using namespace std;

int main() {
    unordered_map<string, int> m;

    string first;
    while (cin >> first) {
        
        if (first == "define") {
            int value;
            cin >> value;
            string key;
            cin >> key;

            m[key] = value;
        } else {
            string second, op, third;
            cin >> second >> op >> third;

            if (m.find(second) == m.end() 
                || m.find(third) == m.end()) {
                    cout << "undefined" << endl;
                continue;
            }

            bool result;
            if (op == "<") {
                result =(m[second] < m[third]);
            } else if (op == ">") {
                result = (m[second] > m[third]);
            } else if (op == "=") {
                result = (m[second] == m[third]);
            }
            
            cout << (result ? "true" : "false") << endl;
        }
    }

    return 0;
}