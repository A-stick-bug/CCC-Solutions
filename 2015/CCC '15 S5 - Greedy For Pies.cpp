/*
15/15
https://dmoj.ca/problem/ccc15s5

Extension of the house robber question, you can't take 2 pies in a row.
However, you are also given M pies that you can insert anywhere in the list.

For 40%, we can just try inserting M into every possible position.
For full marks, we consider the 5 options at each position (shown in solve function).

Note:
- we must sort the extra pieces so the ones we use as filling are the worst ones and the ones we actually
  take are the best. This is also the reason we need an extra DP state.
- K is 1-indexed, when k=0, it means we ran out of pies to insert
*/

#include <bits/stdc++.h>
using namespace std;

const int INF = 1 << 30;
int N, M;
vector<int> pie, extra;
vector<vector<vector<int>>> cache;

int solve(int i, int j, int k) {
    if (j - k > 1) return -INF;  // invalid state
    if (i >= N) return 0;  // finished
    if (cache[i][j][k] != -1) return cache[i][j][k];

    cache[i][j][k] = max({solve(i + 1, j, k),  // skip
                          solve(i + 2, j, k) + pie[i],  // take
                          solve(i + 1, j + 1, k) + pie[i], // take, use extra pie as filling so we can take 2 in a row
                          k > 0 ? solve(i + 1, j, k - 1) + extra[k - 1]: -INF,  // add extra pie, skip normal
                          k > 0 ? solve(i, j + 1, k - 1) + extra[k - 1]: -INF});  // add 1 extra pie, also skip one
    return cache[i][j][k];
}

int main() {
    cin >> N;
    pie.resize(N);
    for (int i = 0; i < N; i++)
        cin >> pie[i];

    cin >> M;
    extra.resize(M);
    for (int i = 0; i < M; i++)
        cin >> extra[i];
    sort(extra.begin(), extra.end());

    cache.resize(N, vector<vector<int>>(M + 2, vector<int>(M + 1, -1)));
    cout << solve(0, 1, M) << "\n";

    return 0;
}
