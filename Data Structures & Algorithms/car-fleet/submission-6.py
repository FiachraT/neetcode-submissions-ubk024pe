class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # car fleet = group of cars travelling at the same positon and same speed. A single car counts as one fleet
        # the variable in the i
        # return number of car fleets
       
       # what determines if a car joins a fleet? If it catches the car ahead before or at the target. How can we determine if it catches? Number of loops aka time taken to reach target
       # therefore (target - pos) / speed = time
       # make it easy to track by sorting cars pos first
       
       pos_time = {}
       l = len(position)
       for i in range(l):
         time = (target - position[i]) / speed[i]
         pos_time[position[i]] = time
       position = sorted(position, key = lambda x: -x)
       time_order = [0] * l
       for i, c in enumerate(position):
        time_order[i] = pos_time[c]
       stack = []
       for c in time_order:
        if not stack or c > stack[-1]:
           stack.append(c)
       return len(stack)



       
       
       

       


