#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

vector<string> split(string x, char delimeter) {
    vector<string> result;
    stringstream ss(x);

    string current;
    while (getline(ss, current, delimeter)) {
        result.push_back(current);
    }

    return result;
}

int main() {
    string x;
    cin >> x;

    vector<string> res = split(x, '-');

    string result;
    for (auto& s : res) {
        cout << s[0];
    }

    cout << endl;

    return 0;
}