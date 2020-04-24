# LRU Cache
# 
-----------
# 题目链接
https://leetcode-cn.com/problems/lru-cache/

# 题目描述
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

# 复杂度
1. 时间复杂度 O()
2. 空间复杂度 O()

# 思路
1. 🌟不会，所以没具体写。经典题：LRU缓存
2. LRU需要用双链表+hash表
3. 或者用自带的有序字典：有一种叫做有序字典的数据结构，综合了哈希表和链表，在 Python 中为 OrderedDict，在 Java 中为 LinkedHashMap
4. 不能使用数组，因为：数组利用下标定位，时间复杂度为O(1)，链表定位元素时间复杂度O(n)；数组插入或删除元素的时间复杂度O(n)，链表的时间复杂度O(1)
5. 《浅谈单链表与双链表的区别（以及数组和链表的区别）》 https://blog.csdn.net/kangxidagege/article/details/80211225
6. https://leetcode-cn.com/problems/lru-cache/solution/shu-ju-jie-gou-fen-xi-python-ha-xi-shuang-xiang-li/

0+0