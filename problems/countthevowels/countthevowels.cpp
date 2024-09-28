#include <iostream>
#include <string>

using namespace std;

int main() {
    string s;
    getline(cin, s);
    int count = 0;
    char arr[] = {'a', 'e', 'i', 'o', 'u'};
    for (int i = 0; i < s.size(); i++) {
        for (char c : arr) {
            if (tolower(s[i]) == c) {
                count += 1;
            }
        }
    }
    cout << count << endl;
}