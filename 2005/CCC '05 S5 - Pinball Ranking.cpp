// 85/100 on DMOJ, unsure of how this would score on CCC because it's not on CCC grader

#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

int main() {
    int n;
    std::cin >> n;
    std::vector<int> scores;
    double total = 0;

    for (int i = 1; i <= n; i++) {  // i is how many elements are in scores during this iteration
        int score;
        std::cin >> score;

        // find ranking of this score
        int rank = std::upper_bound(scores.begin(), scores.end(), score) - scores.begin();
        scores.insert(scores.begin() + rank, score);
        total += i - rank;  // reverse rank because scores is in increasing order
    }

    // get 2 decimal place average
    std::cout << std::fixed << std::setprecision(2) << total / n << std::endl;
    return 0;
}
