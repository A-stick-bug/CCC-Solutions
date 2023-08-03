// my python code was too slow
// passes 50/50 test cases

#include <iostream>
#include <vector>
#include <bitset>
#include <array>

using namespace std;

const int MAXN = 18;
int n_nodes, n_roads;
vector<vector<pair<int, int>>> graph;
int max_dist = 0;
bitset<MAXN> state;
array<array<int, 1 << MAXN>, MAXN> max_dists;

void dfs(int node, bitset<MAXN> &path, int dist) {
    if (node == n_nodes - 1) {
        max_dist = max(max_dist, dist);
        return;
    }

    for (auto &[adj, adj_dist] : graph[node]) {
        int new_dist = dist + adj_dist;
        if (path[adj]) continue;

        bitset<MAXN> new_path = path;
        new_path[adj] = true;

        if (!max_dists[adj][new_path.to_ullong()] || new_dist > max_dists[adj][new_path.to_ullong()]) {
            max_dists[adj][new_path.to_ullong()] = new_dist;
            dfs(adj, new_path, new_dist);
        }
    }
}

int main() {
    cin >> n_nodes >> n_roads;
    graph.resize(n_nodes);

    for (int i = 0; i < n_roads; i++) {
        int a, b, dist;
        cin >> a >> b >> dist;
        graph[a].push_back({b, dist});
    }

    state[0] = true;

    dfs(0, state, 0);
    cout << max_dist << endl;

    return 0;
}
