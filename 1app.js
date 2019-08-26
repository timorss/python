

// console.log(Array(10));

console.time('label');
[...Array(10)].map((v, i) => i + 1)

console.timeEnd('label');

console.time('label0');
Array(10).fill().map((v, i) => i + 1)

console.timeEnd('label0');

console.time('label1');
const arr = []
for (let i = 50; i <= 200; i++) {
    arr.push(i);
}
console.timeEnd('label1');


console.time('label2');
const arr1 = []
const start = 50
for (let i = 0; i <= 200 - start; i++) {
    arr1[i] = i +start;
}
console.timeEnd('label2');
