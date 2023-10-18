#include <iostream>
#include <vector>
using namespace std;

int solve(int i, int ball, vector<vector<int>>& cache, vector<int>& scores, int W) {
    if (cache[i][ball] != -1) {
        return cache[i][ball];
    }
    if (ball == 0 || i >= scores.size()) {
        return 0;
    }
    cache[i][ball] = max(scores[i] + solve(i + W, ball - 1, cache, scores, W), solve(i + 1, ball, cache, scores, W));
    return cache[i][ball];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;

    while (T--) {
        int N, K, W;
        cin >> N >> K >> W;

        vector<int> arr(N + W);
        for (int i = 0; i < N; i++) {
            cin >> arr[i];
        }
        for (int i = N; i < N + W; i++) {
            arr[i] = 0;
        }

        N += W;

        vector<int> scores(N - W + 1);
        scores[0] = 0;
        for (int i = 0; i < W; i++) {
            scores[0] += arr[i];
        }
        for (int i = 1; i < scores.size(); i++) {
            scores[i] = scores[i - 1] + arr[i + W - 1] - arr[i - 1];
        }

        vector<vector<int>> cache(N + 1, vector<int>(K + 1, -1));

        cout << solve(0, K, cache, scores, W) << endl;
    }

    return 0;
}
