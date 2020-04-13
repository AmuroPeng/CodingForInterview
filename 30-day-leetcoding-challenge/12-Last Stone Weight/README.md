# 12-Last Stone Weight
# 
-----------
# 题目链接


# 题目描述
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

 

Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
 

Note:

1 <= stones.length <= 30
1 <= stones[i] <= 1000

# 复杂度
1. 时间复杂度 O(nlogn)
2. 空间复杂度 O()

# 思路
1. 每次排序太慢了，可以用最大堆：对于排序数组需要多次操作（插入，修改，删除）的情况，堆排序很好用。
2. python的堆库：heapq
   - heap = []#建立一个常见的堆
   - heappush(heap,item)#往堆中插入一条新的值
   - item = heappop(heap)#弹出最小的值
   - item = heap[0]#查看堆中最小的值，不弹出
   - heapify(x)#以线性时间将一个列表转为堆
   - item = heapreplace(heap,item)#弹出一个最小的值，然后将item插入到堆当中。堆的整体的结构不会发生改变。
   - heappoppush()#弹出最小的值，并且将新的值插入其中
   - merge()#将多个堆进行合并
   - nlargest(n , iterbale, key=None)从堆中找出做大的N个数，key的作用和sorted( )方法里面的key类似，用列表元素的某个属性和函数作为关键字

> 这道题的数据规模不大，如果数据量变大的一遍遍排序肯定超时
> 因为每一次排序都需要O(nlogn)的时间复杂度
> 可是如果使用堆来存放数组，我们只有在建堆时需要O(1/2nlogn),剩下的插入和取最大值都只要O(logn)的复杂度
> 时间一下子就下了很多
> python有一个自带的heapq能创建小顶堆，我把数据变成负数就间接实现了大顶堆。

> 作者：ripple-zjw
> 链接：https://leetcode-cn.com/problems/last-stone-weight/solution/shi-yong-dui-dai-ti-pai-xu-geng-jia-de-kuai-by-rip/
> 来源：力扣（LeetCode）


0+0