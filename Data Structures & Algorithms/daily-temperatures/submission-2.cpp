class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures)
    {
        //monotonic stack = stack is always in decreasing order
        int n = size(temperatures);
        vector<int> res(n, 0);
        stack<int> st;
        int cur;
        for (int i = 0; i < n; i++) {
            cur = temperatures[i];
            while (!st.empty() && cur > temperatures[st.top()]) {
                res[st.top()] = i - st.top();
                st.pop();
            }
            st.push(i);
        }
        return res;
    }
};
