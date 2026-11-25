class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = size(position);
        map<int, double> posTime;
        stack<double> st;
        for (int i = 0; i < n; i++){
            posTime[position[i]] = static_cast<double>((target - position[i])) / speed[i];
        }
        int car_fleets = 0; 
        for (auto it = posTime.rbegin(); it != posTime.rend(); it++) {
            double time = it->second;
            if (!st.empty() && time <= st.top()) {
                continue;
            }
            st.push(time);
            car_fleets++;
        }
        return car_fleets;
    }
};
