class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        // dist / speed = time taken to reach target
        // map position to time
        // stack and counter
        // regular map presorts keys but has worse lookup
        int n = size(position);
        map<int, double> posTime;
        for (int i = 0; i < n; i++) {
            posTime[position[i]] = static_cast<double>((target - position[i])) / speed[i];
        }
        int fleet_count = 0;
        stack<double> st;
        for (auto it = posTime.rbegin(); it != posTime.rend(); it++) {
            double time = it->second;
            if (!st.empty() && time <= st.top()) {
                continue;
            }
            st.push(time);
            fleet_count++;
        }
    return fleet_count;
    }
};
