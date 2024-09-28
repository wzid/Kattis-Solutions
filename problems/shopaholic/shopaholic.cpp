#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int n;
    
    cin >> n;
    
    vector<int> items;
    
    for (int i = 0; i < n; i++) {
        int tmp;
        cin >> tmp;
        items.push_back(tmp);
    }
    
    sort(items.begin(), items.end());
    
    long savings = 0;
    while (items.size() / 3 > 0) {
        int a = items.back();
        
        items.pop_back();
        items.pop_back();
        int c = items.back();
        items.pop_back();
        
        savings += c;
    }
    
    cout << savings << endl;
}