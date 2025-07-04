//  marks = [25, 65, 88]
//  console.log(marks[-1])
//  marks[1]=9999
//  console.log(marks)
//  Object.freeze(marks)
//  marks[0]=0
//  console.log(marks)

// const a = ["virat", "rohit", "Hardik", "pant", "rahul"];

// let i = 0;
// while (i < a.length) {
//   console.log(a[i]);
//   i++;
// }

// i = 0;
// while (i <= 10) {
//   console.log(i);
//   i++;
// }




const arr1=[25,26]
const arr2=[66,88]

const arr=[arr1,arr2]
let f=arr[0]
 f.push(999)
console.log(arr)

let str="hello"
let k=str
k=k+ "man"
console.log(k)
console.log(str)