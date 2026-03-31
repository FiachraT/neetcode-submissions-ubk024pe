class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
      # board doesn't have to be full to be valid
      # can't use set to check right away because "." is valid
      #Create list of all charaters except ".". See if any are notdigits, zero or have duplicate numbers:
      # scanning row first for zeros and non-digits sufficient for rest

        # iterate through rows first. All checks. Build an array of all characters except "."
        set_arr = set()
        for r in range(9):        #Check all rows
            for c in range(9):
                d = board[r][c]  # d is a string
                if d.isdigit() and d != "0" and d not in set_arr or d == ".":
                    if d != ".":
                        set_arr.add(d)
                else:
                    return False
            set_arr.clear()
        # if made it through above loop, therefore all characters must be 1-9 digits or "."
        # Now just need to check if there are duplicaes vertically or in3 x 3
        for c in range(9):
            for r in range(9):  # check all verticle columns
                d = board[r][c]
                if d != ".":
                    if d not in set_arr:set_arr.add(d)
                    else: return False
            set_arr.clear()
        # now need to check 3x 3
        # 3 double for loops needed
        rf = 0
        rl = 3
        cf = 0
        cl = 3
        while rf != 9:
            for r in range(rf, rl): 
                for c in range(cf, cl):
                    d = board[r][c]
                    if d != ".":
                        if d not in set_arr:
                            set_arr.add(d) 
                            print(d)
                        else: return False
            set_arr.clear()
            if cf == 6:
                rf +=3
                rl +=3
                cf = 0
                cl = 3
            else:
                cf+=3
                cl+=3
        return True


