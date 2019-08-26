console.log('*'.repeat(10));

const course_name = 'java script'

console.log(typeof (course_name));
console.log(course_name.length);
// first caracter
console.log(course_name[0]);
// last caracter
console.log(course_name.slice(-1));
console.log(course_name);


const message = "java \"script"
console.log(message);
const boolZero = new Boolean(0)
console.log('boolZero', boolZero)
const boolOne = new Boolean(1)
console.log('boolOne', boolOne)
const boolMinues = new Boolean(-1)
console.log('boolMinues', boolMinues)
const boolEmptyArr = new Boolean([])
console.log('boolEmptyArr', boolEmptyArr)
const boolEmptyObj = new Boolean({})
console.log('boolEmptyObj', boolEmptyObj)

const age = 50
if (22 < age < 65) {
    console.log('you are ok to get in')
}


const arr = ['timor', 'mosh', 'nadal']
const name = arr.find(str => str.startsWith('t'))
console.log(name);


function increment(number, by) {
    return number + by
}

console.log(increment(3, 4))


const nums = [1, 2, 3, 4, 5, 6, 7, 9]
const skip = nums.filter((num, i) => i % 3 === 0)
console.log(skip);
let [a, b, c, ...rest] = nums
console.log(a); // 1
console.log(b); // 2
console.log(c); // 3
console.log(rest); // rest numbers


const filtering = (num) => {
    return num > 5
}

nums.filter(filtering)

// val.toString().split('.')
const getValueWithTwoNumbersAfterPoint = (val) => {
    if (!val.toString().includes('.')) return val
    let [beforeDot, afterDot] = val.toString().split('.')
    beforeDot = Number(beforeDot)
    const afterDotString = afterDot.slice(0, 2)
    const afterDotNumber = Number(afterDot.slice(0, 2))
    if (afterDotNumber > 0) {
        const lastNumber = afterDotString.toString().length === 1 ? '0' : ''
        return `${beforeDot}.${afterDotString}${lastNumber}`
    } else {
        return beforeDot
    }
}

console.log(getValueWithTwoNumbersAfterPoint(8.50));
console.log('---------------');

