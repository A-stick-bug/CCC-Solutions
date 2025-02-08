// https://dmoj.ca/problem/ccc10s5
// Tree DP with binary search
//
// Note: the pragmas play an important role here, we purposely use iterative bottom up DP
//       instead of top down to take full advantage of pragma optimizations
//
// DP state: [node index][enhancers remaining] = max value this node can send to the node above
//
// At each node with, children, we split the enhancers between the following
// - enhancing the edge above
// - giving the enhancers to children 1
// - giving the enhancers to children 2
// If you give too much to the children, the edge above won't let everything flow through
// If you give too much to the edge above, you are wasting useless capacity
// To find the right balance, we binary search how much we give to the edge above
// This works since as you give less to the edge above, the children always return more (thus monotonic)
//
// Time complexity analysis:
// N nodes, W enhancers -> NW DP states
// Binary search on enhancing edge above, split amongst children 1 and 2 -> WlogW transitions
// TC: O(N * W^2 * logW)

#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")

#include <bits/stdc++.h>

using namespace std;

const int MN = 102;     // max number of nodes
const int MS = 520000;  // max sum of values
const int ME = 725;     // small optimization: max enhancements to ever put on an edge

int find_next_end(int start, const string &s) {  // helper function for parsing tree
    for (int i = start; i < (int) s.size(); i++) {
        if (s[i] == ')' || s[i] == ' ')
            return i;
    }
    return s.size();
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    getline(cin, s);
    int X;
    cin >> X;

    int idx = 0;
    int node_idx = 0;
    vector<vector<int>> graph(MN);  // each node's children
    vector<int> amt(MN, 0);  // value for leaf nodes
    vector<bool> isLeaf(MN, false);

    // parse tree
    vector<int> stack;
    while (idx < (int) s.size()) {
        // print(idx, stack)
        if (s[idx] == '(') {  // start of group
            idx++;
        } else if (s[idx] == ' ') {  // empty space
            idx++;
        } else if (s[idx] == ')') {  // end group, add a parent for the 2 nodes
            int a = stack.back();
            stack.pop_back();
            int b = stack.back();
            stack.pop_back();
            graph[node_idx].push_back(a);
            graph[node_idx].push_back(b);
            stack.push_back(node_idx);
            node_idx++;
            idx++;
        } else {  // number (leaf node)
            int nxt_idx = find_next_end(idx, s);
            int num = stoi(s.substr(idx, nxt_idx - idx));
            stack.push_back(node_idx);
            amt[node_idx] = num;
            isLeaf[node_idx] = true;
            node_idx++;
            idx = nxt_idx;
        }
    }

    int root = node_idx - 1;
    int n = node_idx;  // number of nodes in the tree

    int dp[n][X + 1];
    memset(dp, -1, sizeof(dp));

    // iterative DP
    for (int cur = 0; cur < n; cur++) {
        if (graph[cur].empty() && !isLeaf[cur]) {  // empty node
            continue;
        }

        for (int rem = 0; rem <= X; rem++) {
            if (isLeaf[cur]) {  // base case: leaf
                int best = 0;
                int low = 0;
                int high = (cur != root ? min(rem, ME) : 0);

                while (low <= high) {
                    int mid = (low + high) / 2;
                    int to_top = mid;
                    int to_cur = rem - to_top;
                    int best_v = amt[cur] + to_cur;

                    if (cur == root)
                        best = max(best, best_v);  // root: no need to enhance edge above
                    best = max(best, min((1 + to_top) * (1 + to_top), best_v));

                    if ((1 + to_top) * (1 + to_top) >= best_v)  // spending excess on enhancing edge above
                        high = mid - 1;
                    else  // spending too little to enhance edge above
                        low = mid + 1;
                }

                dp[cur][rem] = best;
                continue;
            }

            // regular case
            int best = 0;
            int low = 0;
            int high = (cur != root ? min(rem, ME) : 0);
            while (low <= high) {
                int mid = (low + high) / 2;
                int to_top = mid;

                int to_child = rem - to_top;
                int c1 = graph[cur][0], c2 = graph[cur][1];
                int best_v = 0;
                // try all splits of enhancers to the 2 children
                for (int to_c1 = 0; to_c1 <= to_child; to_c1++) {
                    int to_c2 = to_child - to_c1;
                    int v1 = dp[c1][to_c1];
                    int v2 = dp[c2][to_c2];
                    best_v = max(best_v, v1 + v2);
                }

                if (cur == root)
                    best = max(best, best_v);  // root: no need to enhance edge above
                best = max(best, min((1 + to_top) * (1 + to_top), best_v));

                if ((1 + to_top) * (1 + to_top) >= best_v)  // spending excess on enhancing edge above
                    high = mid - 1;
                else  // spending too little to enhance edge above
                    low = mid + 1;
            }
            dp[cur][rem] = best;
        }
    }

    cout << dp[root][X] << "\n";
    return 0;
}