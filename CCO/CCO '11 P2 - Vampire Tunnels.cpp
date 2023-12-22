// dijkstra's algorithm with an extra variable
// for each node, we store the minimum distance to get there with s time in the sun
// similar to https://dmoj.ca/problem/ccc15s4

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int S, N, E;
    cin >> S >> N >> E;

    vector<vector<tuple<int, int, int>>> graph(N);
    for(int i = 0; i < E; i++) {
        int a, b, d, sun;
        cin >> a >> b >> d >> sun;
        graph[a].push_back({b, d, sun});
        graph[b].push_back({a, d, sun});
    }

    vector<vector<int>> dist(N, vector<int>(S + 1, 1<<30));
    dist[0] = vector<int>(S + 1, 0);

    priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<>> pq;
    pq.push({0, 0, 0});

    while(!pq.empty()) {
        auto [d, cur, sun] = pq.top();
        pq.pop();

        if(cur == N - 1) {
            cout << d << "\n";
            return 0;
        }

        for(auto [adj, new_dist, new_sun] : graph[cur]) {
            new_sun *= new_dist;
            if(sun + new_sun > S)
                continue;

            if(d + new_dist < dist[adj][sun + new_sun]) {
                dist[adj][sun + new_sun] = d + new_dist;
                pq.push({d + new_dist, adj, sun + new_sun});
            }
        }
    }
    cout << -1 << "\n";
    return 0;
}
