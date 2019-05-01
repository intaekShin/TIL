// Array Helper Methods

// case 1.
// ES5
// var colors = ['red', 'blue', 'green']

// for (var i = 0; i < colors.length; i++) {
//     console.log(colors[i]);
// }
// ES6+ - forEach : for 문을 이용하지 않고도 반복을 가능하게 함.
const colors = ['red', 'blue', 'green']

const f = function(color){ // callback function  f 를 콜백함수라 부름.(정의임)
    console.log(color)
}

colors.forEach(f)

// colors.forEach(function(color){ // callback function  f 를 콜백함수라 부름.(정의임)
//     console.log(color)
// }) // return 값이 없다. 반복만 하고 끝남.

// case 2.
// ES5
// var numbers = [1,2,3]
// var doubleNumbers = []

// for (var i = 0; i < numbers.length; i++) {
//     doubleNumbers.push(numbers[i] * 2)
// }

// console.log(doubleNumbers)

// ES6+ - map
const numbers = [1,2,3]

const doubleNumbers = numbers.map(function(number){
    return number * 2   // return으로 해줘야 제대로 작동함.
})

console.log(doubleNumbers)  // [2,4,6]

// case 3.
// ES6+ - filter : 특정한 조건을 만족하는 배열들로 다시 재배열하는 기능.
const products = [
    {name: 'cucumber', type: 'vegetable'},
    {name: 'banana', type: 'fruit'},
    {name: 'carrot', type: 'vegetable'},
    {name: 'apple', type: 'fruit'},
]

const fruitProducts = products.filter(function(product){
    return product.type === 'fruit' // 조건을 return해줘야 한다.
    // 해당 조건이 true일 경우, item을 가져와 배열에 넣음.
})

console.log(fruitProducts)

// case 4.
// ES6+ - find : 단 하나만 찾습니다. true, false만을 반환한다.

const users = [
    {name: 'nwith'},
    {name: 'admin'},
    {name: 'zzuli'},
]

const foundUser = users.find(function(user){
    return user.name === 'admin'
})

console.log(foundUser)

// case 5.
// ES6+ - every & some
const computers = [
    {name: 'macbook', ram: 16},
    {name: 'gram', ram: 8},
    {name: 'seies9', ram: 32},
]

const everyComputersAvailable = computers.every(function(computer){
    return computer.ram > 16    // 이 조건에 모두 부합하면 true (AND 간지)
})

const someComputersAvailable = computers.some(function(computer){
    return computer.ram > 16    // 하나라도 부합하면 true (OR간지)
})

console.log(everyComputersAvailable)
console.log(someComputersAvailable)

