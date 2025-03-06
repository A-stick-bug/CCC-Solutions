/*
 https://dmoj.ca/problem/ccc14s5
 Dynamic programming on edges of a graph
 States: [node index] = max number of treats
 - To optimize transitions, we loop all pairs of nodes (edges) in order of distance
 - That way, any transition from a previous state is guaranteed to be a valid one

 Sample case visualization: https://www.desmos.com/calculator/2ziyxrgcnp
 TC: O(n^2 * log(n)), from sorting all pairs of nodes
*/

#include <bits/stdc++.h>

using namespace std;

int N;
vector<pair<int, int>> nodes;
vector<array<int, 3>> edges;
const int inf = 1 << 30;

int dist(pair<int, int> a, pair<int, int> b) {
    return (a.first - b.first) * (a.first - b.first) + (a.second - b.second) * (a.second - b.second);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;

    nodes.push_back({0, 0});
    for (int i = 1; i <= N; i++) {
        int a, b;
        cin >> a >> b;
        nodes.push_back({a, b});
    }
    for (int i = 0; i <= N; i++)
        for (int j = i + 1; j <= N; j++)
            edges.push_back({-dist(nodes[i], nodes[j]), i, j});
    sort(edges.begin(), edges.end());  // sort by distance, largest ones first

    int dp[N + 1];
    for (int i = 0; i <= N; i++)
        dp[i] = -inf;
    dp[0] = 0;  // base case

    for (int idx = 0; idx < edges.size();) {
        int cur = idx;
        unordered_map<int, int> new_dp;

        // group all edges with the same distance together, so we don't
        // accidentally transition from an equal distance
        while (cur < edges.size() and edges[cur][0] == edges[idx][0]) {
            auto [_, a, b] = edges[cur];
            int best_a = dp[a];
            int best_b = dp[b];
            if (b != 0 and best_a != -inf)
                new_dp[b] = max(new_dp[b], best_a + 1);
            if (a != 0 and best_b != -inf)
                new_dp[a] = max(new_dp[a], best_b + 1);
            cur++;
        }

        // update dp with the new values
        for (auto [k, v]: new_dp) {
            dp[k] = max(dp[k], v);
        }
        idx = cur;
    }

    cout << *max_element(dp, dp + N + 1) << "\n";

    return 0;
}