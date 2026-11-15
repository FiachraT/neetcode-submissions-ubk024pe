# include <map>
class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        // Add early break if size hand % group != 0
        // create frequency dict of cards from hand
        // find smallest key, val -1, see if +1 exists, if so val -1. Comtinue until size of group created
        // for next group find smallest key for which val != 0 and repeat
        // return False if +1 doesn't exist, else if it runs all the way through return true
        int n = size(hand);
        if (n % groupSize != 0) {
            return false;
        }
        int groups = n / groupSize;
        map<int, int> mymap;
        for (int card: hand){
            mymap[card]++;
        }
        int smallest;
        while (groups > 0) {
            while (!mymap.empty() && mymap.begin()->second <= 0) {
                    mymap.erase(mymap.begin());
            }
            smallest = mymap.begin()->first;
            for (int i = smallest; i < groupSize + smallest; i++) {
                if (mymap[i] <= 0) {
                    return false;
                }
                mymap[i]--;
            }
            groups--;
        }
        return true;
    }
};
