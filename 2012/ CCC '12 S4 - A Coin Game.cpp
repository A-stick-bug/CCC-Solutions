// 15/15
// direct translation of my brute force BFS python code
// check the python file for improved bidirectional BFS solution

#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>
#include <string>

using namespace std;

int main() {
    int n;
    while (true) {
        cin >> n;
        if (n == 0) break;

        vector<vector<int>> coins(n);
        for (int i = 0; i < n; i++) {
            int coin;
            cin >> coin;
            coins[i].push_back(coin);
        }

        vector<vector<int>> end(n);
        for (int i = 0; i < n; i++) {
            end[i].push_back(i + 1);
        }

        auto store = [](const vector<vector<int>>& coins) {
            string s;
            for (const auto& stack : coins) {
                for (int coin : stack) {
                    s += to_string(coin);
                }
                s += ' ';
            }
            return s;
        };

        queue<pair<vector<vector<int>>, int>> q;
        q.push({coins, 0});
        unordered_set<string> used;
        used.insert(store(coins));

        bool found = false;
        while (!q.empty()) {
            auto [config, steps] = q.front();
            q.pop();

            if (config == end) {
                cout << steps << endl;
                found = true;
                break;
            }

            for (int i = 0; i < n; i++) {
                if (config[i].empty()) continue;

                if (i != 0 && (config[i - 1].empty() || config[i].back() < config[i - 1].back())) {
                    auto new_config = config;
                    int to_move = new_config[i].back();
                    new_config[i].pop_back();
                    new_config[i - 1].push_back(to_move);

                    string temp = store(new_config);
                    if (used.find(temp) == used.end()) {
                        q.push({new_config, steps + 1});
                        used.insert(temp);
                    }
                }

                if (i != n - 1 && (config[i + 1].empty() || config[i].back() < config[i + 1].back())) {
                    auto new_config = config;
                    int to_move = new_config[i].back();
                    new_config[i].pop_back();
                    new_config[i + 1].push_back(to_move);

                    string temp = store(new_config);
                    if (used.find(temp) == used.end()) {
                        q.push({new_config, steps + 1});
                        used.insert(temp);
                    }
                }
            }
        }

        if (!found) cout << "IMPOSSIBLE" << endl;
    }

    return 0;
}