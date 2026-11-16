class Solution {
public:
    bool mergeTriplets(vector<vector<int>>& triplets, vector<int>& target) {
        bool x = false; bool y = false; bool z = false;
        int a = target[0];
        int b = target[1];
        int c = target[2];
        for (const auto& t: triplets) {
            x |= (t[0] == a && t[1] <= b && t[2] <= c);
            y |= (t[0] <= a && t[1] == b && t[2] <= c);
            z |= (t[0] <= a && t[1] <= b && t[2] == c);
            if (x && y && z) {
                return true;
            }
        }
        return false;        
    }
};
