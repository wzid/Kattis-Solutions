#include <iostream>
#include <algorithm>
#include <unordered_set>

using namespace std;

int main() {

    int n;
    cin >> n;
    unordered_set<string> s;
    cin.ignore();
    for (int i = 0; i < n; i++) {
        string x;
        getline(cin, x);

        // replace all hyphens with spaces
        for (auto& c : x) {
            if (c == '-')
                c = ' ';
            c = tolower(c);
        }

        s.insert(x);
    }

    cout << s.size() << endl;

    return 0;
}