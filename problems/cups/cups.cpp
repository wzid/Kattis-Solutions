#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

bool is_number(string x) {
    int index = 0;
    if (x[0] == '-') {
        index = 1;
    }
    for (;index < x.length(); index++) {
        if (!isdigit(x[index])) {
            return false;
        }
    }

    return true;
}

bool cmp(pair<string, int>& a, pair<string, int>& b) {
    return a.second < b.second;
}

int main() {
    int n;
    cin >> n;
    vector<pair<string, int>> cups;
    for (int i = 0; i < n; i++) {
        string x, y;
        cin >> x >> y;

        if (is_number(x)) {
            int x_int = stoi(x);
            cups.push_back(make_pair(y, x_int / 2));
        } else {
            int y_int = stoi(y);
            cups.push_back(make_pair(x, y_int));
        }
    }

    sort(cups.begin(), cups.end(), cmp);

    for (auto& cup : cups) {
        cout << cup.first << endl;
    }
}