## 字符
1. ASCII码
```javascript
"ABC".charCodeAt(0) // returns 65 ("A")
"ABC".charCodeAt(1) // returns 66 ("B")
"ABC".charCodeAt(2) // returns 67 ("C")
"ABC".charCodeAt(3) // returns NaN
```
2. Math库
   - `Math.floor()` 向下取整

## 字符串
### 去掉两端的空格 trim
```javascript
str.trim()
// "   abc   "
// "abc"
```

### 正则
```javascript
str = "a b c"
str.split(/\s+/) // "abc"
```
- **\s**: 匹配一个空白字符，包括**空格**、制表符、换页符和**换行符**
- **+**: 匹配`1`个或多个
- **星号***：匹配`0`个或多个

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
let str = "boo";  
for (let value of str) {  
console.log(value);  
}
// "b"
// "o"
// "o"
```

## 类型
### 查看对象的类型
```javascript
1. (最好用)
function isArray(myArray) {
   return myArray.constructor.toString().indexOf("Array") > -1;
   // true|false
}
2. 
const map = new Map();
map.toString() // [object Map]
```
### 强制类型转换
   - `Number()`
   - `String()` = `.toString()`
   - `parseInt()` & `parseFloat()`

