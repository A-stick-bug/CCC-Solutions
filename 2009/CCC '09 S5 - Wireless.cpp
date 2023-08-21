// 15/15
// translation of my python solution to c++ because python is too slow

#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

int dist(int x, int r) {
    return floor(sqrt(pow(r, 2) - pow(x, 2)));
}

int main() {
    int ROWS, COLS, k;
    cin >> ROWS >> COLS >> k;
    vector<vector<int>> diff(ROWS, vector<int>(COLS + 1)); // difference array, +1 on columns to prevent going out of bounds

    for (int i = 0; i < k; i++) {
        int col, row, radius, rate;
        cin >> col >> row >> radius >> rate;
        col -= 1; // turn into 0-indexing
        row -= 1;

        for (int i = max(0, row - radius); i <= min(ROWS - 1, row + radius); i++) { // make sure we stay in range
            int r_dist = abs(i - row); // up-down distance
            int width = dist(r_dist, radius);

            int start = max(0, col - width);
            int end = min(COLS - 1, col + width);
            diff[i][start] += rate;
            diff[i][end + 1] -= rate;
        }
    }

    int cur = 0, greatest = 0, occurrences = 0;

    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS + 1; j++) {
            cur += diff[i][j];
            if (cur > greatest) {
                greatest = cur;
                occurrences = 1;
            } else if (cur == greatest) {
                occurrences += 1;
            }
        }
    }

    cout << greatest << endl;
    cout << occurrences << endl;

    return 0;
}
