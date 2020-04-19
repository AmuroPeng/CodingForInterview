class Solution:
    def displayTable(self, orders: list) -> list:
        title_list = []
        dict_ = {}
        for i in orders:
            if i[2] not in title_list:
                title_list.append(i[2])
        title_list=[sorted(title_list)]
        title_list[0]=["Table"]+title_list[0]
        print(title_list[0])
        for i in orders:
            # print(title_list[0].index(i[2]))
            if int(i[1]) not in dict_.keys():
                dict_[int(i[1])] = ['0']*len(orders)
            # print(i[2])
            # print(str(dict_[int(i[1])])+'  '+str([title_list[0].index(i[2])]))
            # print(dict_[int(i[1])][title_list[0].index(i[2])-1])
            dict_[int(i[1])][title_list[0].index(i[2])-1] = str(1+int(dict_[int(i[1])][title_list[0].index(i[2])-1]))
            # print(dict_)
        # dict_.sort()
        # print(sorted(dict_.keys()))
        for k in sorted(dict_.keys()):
            title_list.append([str(k)]+dict_[k][:len(title_list[0])-1])
        print(title_list)
        return title_list


if __name__ == "__main__":
    s = Solution()
    print(s.displayTable([["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]]))
