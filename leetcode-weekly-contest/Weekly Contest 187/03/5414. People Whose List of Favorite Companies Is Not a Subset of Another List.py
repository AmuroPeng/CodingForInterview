import collections


class Solution:
    def peopleIndexes(self, favoriteCompanies: list) -> list:
        # dict_ = {}
        # for i in range(len(favoriteCompanies)):
        #     if len(favoriteCompanies[i]) not in dict_:
        #         dict_[len(favoriteCompanies[i])] = [i]
        #     else:
        #         dict_[len(favoriteCompanies[i])].append(i)
        # for k, v in collections.OrderedDict(sorted(dict_.items(), reverse=True, key=lambda t: t[0])).items():
            
        list_ = set()
        for i in range(len(favoriteCompanies)):
            for j in range(i+1,len(favoriteCompanies)):
                if len(favoriteCompanies[j])>len(favoriteCompanies[i]):
                    pass
                else:
                    print(j,favoriteCompanies[j],i,favoriteCompanies[i])
                    if not [False for c in favoriteCompanies[j] if c not in favoriteCompanies[i]]:
                        list_.add(j)
                    elif not [False for c in favoriteCompanies[i] if c not in favoriteCompanies[j]]:
                        list_.add(i)
                    elif favoriteCompanies[i] == favoriteCompanies [j]:
                        list_.add(i)
                        list_.add(j)
        list1=[]
        for i in range(len(favoriteCompanies)):
            if i not in list_:
                list1.append(i)
        return list1
        

if __name__ == "__main__":
    # pass
    s = Solution()
    print(s.peopleIndexes([["leetcode", "google", "facebook"], [
          "google", "microsoft"], ["google", "facebook"], ["google"], ["amazon"]]))

# 错的