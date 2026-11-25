class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
      // montonic stack dependent on the second iterator where we store position and height in a stack<pair<int, int>>
      //multiply i - pair position by height, keep track of max
      int n = size(heights);
      stack<int> st;
      int m = 0;
      int prev_h;
      int h;
      int width;
      //monotonic ascending stack
      for (int i = 0; i <= n; i++) {
        while (!st.empty() && (i == n || heights[st.top()] >= heights[i])) {
            prev_h = heights[st.top()];
            st.pop();
            width = st.empty() ? i : i - st.top() - 1;
            m = max(m, prev_h*width);
        }
        st.push(i);
      }
      return m;
    }
};
