// const sumAverage = (arr) => {
//     let result = 0
//     arr.forEach(smallArr => {
//         let sumOfSmallArr = 0

//         smallArr.forEach(num => {
//             sumOfSmallArr += num
//         })
//         let average = sumOfSmallArr / smallArr.length
//         result += average
//         console.log('sumOfSmallArr', sumOfSmallArr);
//         console.log('result', result);
//         console.log('arr.length', arr.length);
//     });
//     return result;
// }
// console.log(sumAverage([[3, 4, 1, 3, 5, 1, 4], [21, 54, 33, 21, 77]]))

// const makeUnique = arr => {
//     return [...new Set(arr)]
// }

// console.log(makeUnique(['A', 'A', 0]))

// const makeUnique2 = arr => {
//     return arr.filter((item, i) => {
//         console.log('arr.indexOf(item)', arr.indexOf(item));

//         return arr.indexOf(item) === i
//     })
// }

// console.log(makeUnique2(['A', 'A', 0]))

const makeUnique2 = arr => {
    let sum = 0
    for (item of arr) {
        sum += item
    }
    return sum
}

console.log(makeUnique2([1, 2, 3, 4, 5, 6]))