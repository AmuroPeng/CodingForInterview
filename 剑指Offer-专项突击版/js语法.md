## 数组
1. 新建数组 填充0
```javascript
new Array(n + 1).fill(0);
```

## Map
1. Map里没有的key也可以get，得到undefined
```javascript
const map = new Map();
map.get("乱七八糟")||0  // 0
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