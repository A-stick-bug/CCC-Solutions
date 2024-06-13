// https://dmoj.ca/problem/cco15p2
// bitmask DP with DFS
// store the nodes we visited on the current path as a bitmask
// dp[i][mask]: longest path from the i-th node, already visited set bits in mask

#include <bits/stdc++.h>

#define pii pair<int, int>

using namespace std;

const int inf = 1000000000;
int N, M;
vector<vector<pii>> graph;
vector<vector<int>> dist;

int solve(int cur, int mask) {
    if (cur == N - 1)  // reached destination
        return 0;
    if (dist[cur][mask] != -1)  // cache
        return dist[cur][mask];
    int mx = -inf;
    for (auto [adj, adj_d]: graph[cur]) {
        if (mask & (1 << adj))  // already visited
            continue;
        mx = max(mx, adj_d + solve(adj, mask | (1 << adj)));
    }
    return dist[cur][mask] = mx;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M;
    graph.resize(N, vector<pii >());
    dist.resize(N, vector<int>(1 << N, -1));

    for (int i = 0; i < M; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        graph[a].emplace_back(b, c);
    }

    cout << solve(0, 1) << "\n";
    return 0;
}
