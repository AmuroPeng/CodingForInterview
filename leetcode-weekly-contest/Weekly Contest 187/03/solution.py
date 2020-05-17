class Solution(object):
    def peopleIndexes(self, favoriteCompanies):
        """
        :type favoriteCompanies: List[List[str]]
        :rtype: List[int]
        """
        ansll = []
        for i in range(len(favoriteCompanies)):
            set1 = set(favoriteCompanies[i])
            flag = 1
            for j in range(len(favoriteCompanies)):
                set2 = set(favoriteCompanies[j])
                comm = set1.intersection(set2)
                if (comm == set1 and i != j):
                    flag = 0
            if (flag):
                ansll.append(i)
        return ansll