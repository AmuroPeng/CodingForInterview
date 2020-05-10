class Solution:
    def checkStraightLine(self, coordinates: list) -> bool:
        if len(coordinates)<=2:
            return True
        if coordinates[1][0]-coordinates[0][0]==0 or coordinates[1][1]-coordinates[0][1]==0:
            if coordinates[1][1]-coordinates[0][1]==0 and coordinates[1][1]-coordinates[0][1]==0:
                pass
            else:
                return False
        angle=(coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
        print(angle)
        for i in range(2,len(coordinates)):
            if coordinates[i][0]-coordinates[0][0]==0 or coordinates[i][1]-coordinates[0][1]==0:
                if coordinates[i][1]-coordinates[0][1]==0 and coordinates[i][1]-coordinates[0][1]==0:
                    pass
                else:
                    return False
            elif angle==(coordinates[i][1]-coordinates[0][1])/(coordinates[i][0]-coordinates[0][0]):
                print(coordinates[i][1]-coordinates[0][1])
                print(coordinates[i][0]-coordinates[0][0])
                pass
            else:
                return False
        return True

if __name__ == "__main__":
    s=Solution()
    print(s.checkStraightLine([[-7,-3],[-7,-1],[-2,-2],[0,-8],[2,-2],[5,-6],[5,-5],[1,7]]))