#include <bits/stdc++.h>
#define int long long
using namespace std;

signed main() {
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N,M ,Q;
    cin >> N >> M >> Q;
    vector<array<int, 2>> arr;
    for (int i = 0; i < N; i++){
        int a,b;
        cin >> a >> b;
        arr.push_back({a, b});
    }

    unordered_map<int, multiset<int>> vals;
    for (auto i: arr){
        vals[i[0]].insert(i[1]);
    }
    for (auto [k,v]: vals){
        vals[k].insert(-1);
    }

    multiset<int> minimum;  // maintain
    multiset<int> second;
    int total = 0;
    for (auto [k,v]: vals){
        minimum.insert(*--v.end());
        second.insert(*----v.end());
        total += *--v.end();
    }

    for (int q = 0; q <= Q; q++){
        if (q != 0){
            int t,i,x;
            cin >> t >> i >> x;
            i --;

            auto [old_c, old_v] = arr[i];
            if (t == 1) arr[i][0] = x;
            else arr[i][1] = x;
            auto [new_c, new_v] = arr[i];

            minimum.erase(minimum.find(*--vals[old_c].end()));
            second.erase(second.find(*----vals[old_c].end()));

            total -= *--vals[old_c].end();
            vals[old_c].erase(vals[old_c].find( old_v));

            if (old_c != new_c){
                minimum.erase(minimum.find(*--vals[new_c].end()));
                second.erase(second.find(*----vals[new_c].end()));
            }
            total -= *--vals[new_c].end();


            if (old_c != new_c){
                minimum.insert(*--vals[old_c].end());
                second.insert(*----vals[old_c].end());
            }

            total += *--vals[old_c].end();

            vals[new_c].insert(new_v);
            minimum.insert(*--vals[new_c].end());
            second.insert(*----vals[new_c].end());
            total += *--vals[new_c].end();
        }
        cout << total + max(0LL, *--second.end() - *minimum.begin()) << "\n";

    }

}
