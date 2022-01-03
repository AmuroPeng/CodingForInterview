## 字符
1. ASCII码
```javascript
"ABC".charCodeAt(0) // returns 65 ("A")
"ABC".charCodeAt(1) // returns 66 ("B")
"ABC".charCodeAt(2) // returns 67 ("C")
"ABC".charCodeAt(3) // returns NaN
```

## 数组
1. 新建数组 填充0
    ```javascript
    new Array(n + 1).fill(0);
    ```
2. 任何数据结构 转成 Array
   ```javascript
   Array.from(xxx);
   ```
3. 遍历数组时取index和value两个值
   ```javascript
   let list = [5, 6, 7];
   for (let [index, value] of list.entries()) {
       console.log(index, value);
   }
   // 0 5
   // 1 6
   // 2 7
   ```
4. 左边增加元素
   ```javascript
   1. 从左增添: array.unshift("新元素")
   2. 从左删除：删除的元素 = array.shift()
   ```
   
5. 判断数组中是否存在某个值 `array.indexOf`  
   如果存在返回数组元素的下标，否则返回-1
   ```javascript
   let arr = ['something', 'anything', 'nothing', 'anything'];
   let index = arr.indexOf('nothing');
   // 结果：2
   ```
6. 二维数组 初始化
   ```javascript
   matrix = new Array(n).fill(0).map(() => new Array(n).fill(0));
   or
   matrix = new Array(n).fill(0).map(function () {
       return new Array(n).fill(0);
   })
   ```
   不能直接new里面套new，因为会导致每一行引用的都是同一个[0,0,0]
7. sort()
   ```javascript
   xxx.sort((a, b) => a - b) 
   //即使全是数字，也得这么排序
   //否则 就会是 [1,10,2,20,3,30]
   ```

## Map
1. Map里没有的key也可以get，得到undefined
```javascript
const map = new Map();
map.get("乱七八糟")||0  // 0
```

## Set
```javascript
let mySet = new Set();
mySet.add(1);
mySet.has(1); // true
mySet.delete(1);  // true
mySet.size;

for (let [key, value] of mySet.entries()) {
    console.log(key);
}
```

## 循环
1. 循环字符串
```javascript
let iterable = "boo";  
for (let value of iterable) {  
console.log(value);  
}
// "b"
// "o"
// "o"
```

## 查看对象的类型
```javascript
const map = new Map();
map.toString() // [object Map]
```