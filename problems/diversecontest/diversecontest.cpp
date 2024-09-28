#include <bits/stdc++.h>

using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define For(i, a) for(int i = 0; i < (a); ++i)
#define all(x) begin(x), end(x)
#define is_in(x, s) ((s).find(x) != (s).end())
#define endl '\n'
#define pi acos(-1.0)
typedef long long ll;
template<class T> using V=vector<T>;
template<class T> using VV=vector<vector<T>>;
template<class K, class V> using umap=unordered_map<K, V>;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef unordered_map<int, int> uimap;

VV<int> find_permutations(int n, int k) {
    VV<int> res;
    For(i, 1<<n) {
        if (__builtin_popcount(i) == k) {
            V<int> temp;
            For(j, n) {
                if (i & (1<<j)) {
                    temp.push_back(j);
                }
            }
            res.push_back(temp);
        }
    }
    return res;
}

int main() {
    int n, k;
    
    cin >> n >> k;
    umap<string, int> m;
    VV<string> problems(n);
    For(i, n) {
        int a;
        cin >> a;
        // don't add the leading spaces
        
        For(j, a) {
            string s;
            cin >> s;
            problems[i].push_back(s);
        }
    }

    VV<int> perms = find_permutations(n, k);
    int max_of_each_top = k / 2;
    int count = 0;
    for(auto& perm : perms) {
        umap<string, int> tmp;
        bool b = false;
        for (auto& ind : perm) {
            for (auto& topic : problems[ind]) {
                if (tmp[topic] + 1 > max_of_each_top) {
                    b = true;
                    break;
                } else {
                    tmp[topic]++;
                }
            }
            if (b) break;
        }
        if (!b) count++;
    }

    cout << count << endl;


    return 0;
}