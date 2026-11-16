#include <map>
class Solution {
public:
    vector<int> partitionLabels(string s) {
        // since same letter can only be in one substring
        // seen set
        // dict key = let, val = final index
        // second for loop, if final index grater than current final index replace
        // if index = final index, add to result
        map<char, int> lastInd;
        for (int i = 0; i < size(s); i++) {
            lastInd[s[i]] = i;
        }
        vector<int> res;
        int maxInd = 0;
        int prevInd = -1;
        for(int i = 0; i < size(s); i++) {
            maxInd = max(lastInd[s[i]], maxInd);
            if (i == maxInd) { 
                cout << maxInd << endl;
                res.push_back(maxInd - prevInd);
                prevInd = maxInd;
            }
        }
        return res;
    }
};
