#include <iostream>
#include <vector>
#include <unordered_map>
#include <cmath>
#include <algorithm>

using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef unordered_map<int, int> uimap;


void dfs(int node, int& curr_pos, vector<vi>& paths, vi& d, vector<bool>& visited) {
    visited[node] = true;
    // If we are at an end node with no children
    if (paths[node].size() == 0) {
        // We are able to say we can visit every node that we visited in our current path
        while (curr_pos < d.size() && visited[d[curr_pos]]) {
            curr_pos++;
        }
    } else {
        // because its sorted we can do it this way
        for (int child : paths[node]) {
            dfs(child, curr_pos, paths, d, visited);
        }
    }
    visited[node] = false;
}



int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, m;
    cin >> n >> m;

    //set<int> paths[10001];
    vector<vi> paths(n, vi());
    rep(i, 0, n-1) {
        int a, b;
        cin >> a >> b;
        paths[--a].push_back(--b);
    }
    
    rep(i, 0, n-1) {
        sort(paths[i].begin(), paths[i].end());
    }

    vi d;
    rep(i, 0, m) {
        int c;
        cin >> c;
        d.push_back(--c);
    }

    int current_pos = 0;
    vector<bool> visited(n);
    dfs(0, current_pos, paths, d, visited);
    
    cout << current_pos << endl;
}