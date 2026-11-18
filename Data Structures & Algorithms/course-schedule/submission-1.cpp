#include <unordered_map>
#include <unordered_set>
class Solution {
      unordered_map<int, vector<int>> preMap;
      unordered_set<int> visited;
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        // 2d array
        // dfs
        // turn array into dict, key = coures, val = prereq
        // not possible if there's a cycle
        // therefore if prerquisite of a turns out to be a, return False
        for (int i = 0; i < numCourses; i++) {
            preMap[i] = {};
        }
        for (auto& prereq: prerequisites) {
            preMap[prereq[0]].push_back(prereq[1]);
        }
        for (int c = 0; c < numCourses; c++) {
            if (!dfs(c)){
                return false;
            }
        }
        return true;
    }
    bool dfs(int c) {
        if (visited.count(c) > 0) {
            return false;
        }
        if (preMap[c].empty()) {
            return true;
        }
        visited.insert(c);
        for (int pre: preMap[c]) {
            if (!dfs(pre)) {
                return false;
            }
        }
        visited.erase(c);
        preMap[c].clear();
        return true;
    }
};
