class Solution {
public:
    bool mergeTriplets(vector<vector<int>>& triplets, vector<int>& target) {
        // elimanate elemnts where any of their values are bigger than the corresponding target values
        // of remaining triplets check if any of the triplets have the target value in the corresponding position
        bool x = false; bool y = false; bool z = false;
        int a;
        int b;
        int c;
        for (const auto& t: triplets) {
            a = target[0];
            b = target[1];
            c = target[2];
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
