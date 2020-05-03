class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        set_=set(J);
        count=0
        for i in S:
            if i in set_:
                count+=1
        return count

if __name__ == "__main__":
    s=Solution()
    print(s.numJewelsInStones("aA","aAAbbbb"));

