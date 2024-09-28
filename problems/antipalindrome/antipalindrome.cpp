#include <bits/stdc++.h>

using namespace std;

#define rep(i, a, b) for (int i = a; i < (b); ++i)
#define For(i, a) for (int i = 0; i < (a); ++i)
#define all(x) begin(x), end(x)
#define is_in(x, s) ((s).find(x) != (s).end())
#define endl '\n'
#define pi acos(-1.0)
typedef long long ll;
template <class T>
using V = vector<T>;
template <class T>
using VV = vector<vector<T>>;
template <class K, class V>
using umap = unordered_map<K, V>;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef unordered_map<int, int> uimap;

string clean(string x) {
    string ret;
    for (auto c : x) {
        if (isalpha(c)) ret += tolower(c);
    }
    return ret;
}

int main() {
    string x;
    getline(cin, x);

    
    For(i, x.size()-1) {
        rep(j, i+1, x.size()) {
            if (tolower(x[i]) == tolower(x[j])) {
                string tmp = clean(x.substr(i, (j-i)+1));
                string rev = tmp;
                reverse(rev.begin(), rev.end());
                // cout << tmp << " " << rev << endl;
                if (rev == tmp) {
                    cout << "Palindrome" << endl;
                    return 0;
                }
            }
        }    
    }
    

    cout << "Anti-palindrome" << endl;

    return 0;
}