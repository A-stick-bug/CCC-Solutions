/*
https://dmoj.ca/problem/ccc19s5
Basically implementing the editorial: https://dmoj.ca/problem/ccc19s5/editorial

Using max 2D BIT, after figuring out that you have to align the triangle to the right,
the problem becomes mostly implementation

Align triangle like this for max BIT queries
      3
    1 2
  4 2 1
6 1 4 2
*/

#include <bits/stdc++.h>

using namespace std;

const int MN = 3002;
int bit[MN][MN];

void update(int r, int c, int diff) {
    for (; r < MN; r += r & -r)
        for (int col = c; col < MN; col += col & -col)
            bit[r][col] = max(bit[r][col], diff);
}

int query(int r, int c) {
    int total = 0;
    for (; r > 0; r -= r & -r)
        for (int col = c; col > 0; col -= col & -col)
            total = max(total, bit[r][col]);
    return total;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, K;
    cin >> N >> K;

    vector<vector<int>> triangle(N, vector<int>(N));
    for (int i = 0; i < N; i++) {
        for (int j = 0; j <= i; j++) {
            cin >> triangle[i][j + (N - i - 1)];  // right align
        }
    }

    long long total = 0;

    for (int i = N - 1; i >= 0; i--) {
        int j = N - 1;
        int ti = i;
        while (ti < N) {  // update cells on the right most anti-diagonal that hasn't been updated yet
            update(ti + 1, j + 1, triangle[ti][j]);
            ti++;
            j--;
        }
        if (N - i >= K) {  // we have enough cells to query for max
            j = N - K;
            ti = i;
            while (ti < N - K + 1) {
                total += query(ti + K, j + K);
                ti++;
                j--;
            }
        }
    }

    cout << total << "\n";
    return 0;
}

