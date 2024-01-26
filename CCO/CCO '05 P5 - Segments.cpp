// simple recursion using memoization
// check python code for bottom up version

#include <bits/stdc++.h>

using namespace std;

int n;
vector<pair<int, int>> arr;
map<pair<int, int>, int> memo;

int solve(int i, int loc) {
    if (i == n) {
        return n - loc;  // distance to walk to corner
    }
    pair<int, int> key = make_pair(i, loc);
    if (memo.find(key) != memo.end()) {
        return memo[key];
    }
    int l = arr[i].first, r = arr[i].second;
    int result = min(abs(loc - l) + (r - l) + solve(i + 1, r),
                     abs(r - loc) + (r - l) + solve(i + 1, l));
    memo[key] = result;
    return result;
}

int main() {
    cin >> n;
    arr.resize(n);
    for (int i = 0; i < n; ++i) {
        cin >> arr[i].first >> arr[i].second;
    }
    cout << solve(0, 1) + n - 1 << endl;  // add time to drop down levels
    return 0;
}