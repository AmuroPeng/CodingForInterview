class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        set_=set()
        for i in range(pow(k,2)):
            if len(bin(i)) != len(bin(k)):
                print("0"*(len(bin(k))-len(bin(i)))+bin(i)[2:])
                set_.add("0"*(len(bin(k))-len(bin(i)))+bin(i)[2:])
            else:
                print(bin(i)[2:])
                set_.add(bin(i)[2:])
        print(f"set_",set_,"\n")
        p = 0
        set_2 = set()
        while p != len(s)-p+len(bin(k))+2:
            print(s[p:p+len(bin(k))-2])
            set_2.add(s[p:p+len(bin(k))-2])
            p += 1
        print(f"set_2",set_2)

        return set_ == set_2

if __name__ == "__main__":
    s = Solution()
    print(s.hasAllCodes("00110", 2))
