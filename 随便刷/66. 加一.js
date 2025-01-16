/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    const arr = [0].concat(digits);
    arr[arr.length - 1] += 1;
    for (let i = arr.length - 1; i > 0; i -= 1) {
        if (arr[i] === 10) {
            arr[i] = 0;
            arr[i - 1] += 1;
        }
    }
    if (arr[0] === 0) arr.shift();
    return arr;
};