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
typedef vector<int> vi;
typedef unordered_map<int, int> uimap;
typedef tuple<int, int, int, int> Tree;
typedef pair<int, int> Point;



int cross(const Point& o, const Point& a, const Point& b) {
    return (a.first - o.first) * (b.second - o.second) - (a.second - o.second) * (b.first - o.first);
}

vector<Point> convex_hull(vector<Point>& points) {
    if (points.size() <= 1) return points;

    vector<Point> lower, upper;
    for (const auto& p : points) {
        while (lower.size() >= 2 && cross(lower[lower.size() - 2], lower.back(), p) <= 0) {
            lower.pop_back();
        }
        lower.push_back(p);
    }

    for (auto it = points.rbegin(); it != points.rend(); ++it) {
        while (upper.size() >= 2 && cross(upper[upper.size() - 2], upper.back(), *it) <= 0) {
            upper.pop_back();
        }
        upper.push_back(*it);
    }

    lower.pop_back();
    upper.pop_back();
    lower.insert(lower.end(), upper.begin(), upper.end());
    return lower;
}

double polygon_perimeter(const vector<Point>& points) {
    double perimeter = 0.0;
    int num_points = points.size();
    for (int i = 0; i < num_points; i++) {
        int x1 = points[i].first, y1 = points[i].second;
        int x2 = points[(i + 1) % num_points].first, y2 = points[(i + 1) % num_points].second;
        perimeter += sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
    }
    return perimeter;
}

int main() {
    while (true) {
        int n;
        cin >> n;
        if (n == 0) break;

        vector<Tree> trees;
        int total_val = 0, total_wood = 0;

        For(i, n) {
            int x, y, v, l;
            cin >> x >> y >> v >> l;
            trees.push_back({x, y, v, l});
            total_val += v;
            total_wood += l;
        }

        sort(all(trees));

        double minValLost = numeric_limits<double>::infinity();

        rep(i, 1, 1 << trees.size()) {
            vector<Point> perm;
            int valueLost = 0, woodChopped = 0;

            For(j, trees.size()) {
                if (i & (1 << j)) {
                    auto [x, y, v, l] = trees[j];
                    perm.emplace_back(x, y);
                    valueLost += v;
                    woodChopped += l;
                }
            }

            valueLost = total_val - valueLost;
            woodChopped = total_wood - woodChopped;

            if (polygon_perimeter(convex_hull(perm)) <= woodChopped) {
                minValLost = min(minValLost, static_cast<double>(valueLost));
            }
        }

        cout << "The lost value is " << minValLost << "." << endl;
    }

    return 0;
}