function noSpace(x) {
    let res = x.replace(/ /g, '')
    return res
}
console.log(noSpace('8aaaaa dddd r     '))

function solve(s) {
    let res = []
    let arr = s.split('')
    arr.forEach((char, i) => {
        let firstNumber = !isNaN(Number(char))
        console.log(firstNumber);

        let afterNumber = !isNaN(Number(arr[i + 1]))
        if (firstNumber) {
            res.push(Number(char))
        } else {
            res.push(false)
        }
    })

    return s.replace(/[^0-9/]/g, ' ')
};


console.log(solve('gh12cdy695m1'))


let arr = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'I'], ['j', 'k', 'L']]
console.log('index', arr[1].indexOf(arr[1][2]));

console.log(arr)
if (0) {
    console.log('yesssssss');

}

function duplicateEncode(word) {
    const _word = word.toLowerCase()
    let obj = {}
    let res = ''
    for (char of _word) {
        if (obj[char]) {
            res += ')'
        } else {
            res += '('
        }
        return res
    }
}