#include <iostream>

using namespace std;

bool isVowel(char c) {
    return c == 'a' || c == 'i' || c == 'o' || c == 'u' || c == 'e';
}

int main() {
    string s;
    getline(cin, s);
    int sum = 0;
    for (char c : s) {
        sum += isVowel(tolower(c));
    }
    
    cout << sum << endl;
}