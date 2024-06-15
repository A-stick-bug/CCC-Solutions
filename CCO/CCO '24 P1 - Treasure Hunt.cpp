/*
 https://dmoj.ca/problem/cco24p1
 Standard multi-source Dijkstra's problem

 Solve the question in reverse:
 - Start Dijkstra's from all nodes (destinations), sorted by descending treasure amount
 - At each edge, we minus the cost to travel the edge
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    cin >> N >> M;

    vector<int> val(N);
    for(int i = 0; i < N; i++) {
        cin >> val[i];
    }

    vector<vector<pair<int, int>>> graph(N);
    for(int i = 0; i < M; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        a--; b--;
        graph[a].push_back({b, c});
        graph[b].push_back({a, c});
    }

    vector<int> best = val;
    priority_queue<pair<int, int>> pq;
    for(int i = 0; i < N; i++) {
        pq.push({val[i], i});
    }

    while(!pq.empty()) {
        auto [v, cur] = pq.top();
        pq.pop();

        for(auto [adj, cost] : graph[cur]) {
            int new_cost = v - cost;
            if(best[adj] < new_cost) {
                best[adj] = new_cost;
                pq.push({new_cost, adj});
            }
        }
    }

    for(int i = 0; i < N; i++) {
        cout << best[i] << "\n";
    }

    return 0;
}
