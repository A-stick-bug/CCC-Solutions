// brute force recursion, with memoization
// similar to bounded knapsack DP

#include <bits/stdc++.h>

using namespace std;

int n;
vector<int> options;
map<pair<int, int>, int> memo;

int solve(int i, int amt) {
    if (i == n) {
        return abs(amt);
    }
    if (memo.find({i, amt}) != memo.end()) {
        return memo[{i, amt}];
    }
    if (abs(amt) > 200)  // optimization, the minimal difference is never more than the largest weight
        return 1000;
    return memo[{i, amt}] = min(solve(i + 1, amt + options[i]), solve(i + 1, amt - options[i]));
}

int main() {
    cin >> n;
    for (int i = 0; i < n; ++i) {
        int cnt, amt;
        cin >> cnt >> amt;
        while (cnt--) {
            options.push_back(amt);
        }
    }
    n = options.size();
    cout << solve(0, 0) << endl;
    return 0;
}
