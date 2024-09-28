#include <iostream>
#include <set>

using namespace std;

int main() {
    int start, end;
    
    cin >> start >> end;
    int combos = 0 ;
    for (int i = start; i <= end; i++) {
        string value = to_string(i);

        if (value.length() != 6)
            continue;
        set<int> digits;
        bool should_continue = false;
        for (auto& c : value) {
            if (c == '0') {
                should_continue = true;
                break;
            }
                
            digits.insert(c - '0');
        }

        // cout << "i: " << i << endl;

        // for (auto& v : digits) {
        //     cout << "V: " << v << endl;
        // }



        if (should_continue)
            continue;
        
        if (digits.size() != 6)
            continue;

        
        for (auto& v : digits) {
            if (i % v != 0) {
                should_continue = true;
                break;
            }
        }

        if (should_continue)
            continue;

        combos++;
    }

    cout << combos << endl;
}