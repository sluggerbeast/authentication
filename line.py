"""

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. 
Check if these points make a straight line in the XY plane.

example: 
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

example:
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
"""

class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:

        #y = mx+c
        # m = (y2-y1)/(x2-x1)
        if coordinates[1][0] - coordinates[0][0]!=0:
            m = (coordinates[1][1] - coordinates[0][1])/(coordinates[1][0] - coordinates[0][0])
        else:
            m = "inf"
        mc =0
        for i in range(len(coordinates)-1):
            
            if(coordinates[i+1][0] - coordinates[i][0])!=0:
                mc = (coordinates[i+1][1] - coordinates[i][1])/(coordinates[i+1][0] - coordinates[i][0])
            else:
                mc = "inf"
            if m!=mc:
                return False



        return True
    
new_sol = Solution()
coor = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
coor1 = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
val = new_sol.checkStraightLine(coor1)
print(val)