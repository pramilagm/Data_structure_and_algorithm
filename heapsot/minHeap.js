// const minHeap = arr => {
//   let temp = arr[0];
//   arr[0] = arr[arr.length - 1];
//   arr[arr.length - 1] = arr[0];
//   arr.pop();
//   heapify(arr, 0);
// };

// const parentIdx = idx => {
//   return Math.floor(idx - 1 / 2);
// };
// const heapify = (arr, idx) => {
//   if (idx == arr.length - 1) {
//     return;
//   }
//   let left = 2 * idx;
//   let right = 2 * idx + 1;

//   if (arr[left] > arr[parentIdx(idx)] && arr[left] < arr[right]) {
//     [arr[left], arr[minimum]] = [arr[minimum], arr[left]];
//     heapify(arr, arr[parentIdx(idx)]);
//   }
//   //   if (arr[left] < arr[minimum] && arr[left] < arr.length) {
//   //     minimum = arr[left];
//   //   }
//   //   if (arr[right] < arr[minimum] && arr[right] < arr.length) {
//   //     minimum = arr[right];
//   //   }

//   if (arr[right] > arr[parentIdx(idx)] && arr[right] < arr[left]) {
//     [arr[right], arr[parentIdx(idx)]] = [arr[parentIdx(idx)], arr[right]];
//     heapify(arr, arr(parentIdx(idx)));
//   }
//   return arr;
// };
// var arr = [-1, 0, 1, 2, 3, 4, 5];

// console.log(minHeap(arr));
// console.log("Hello");
// function allLongestStrings(inputArray) {
//   var longestWord = [];
//   var longest = string(inputArray[0]);
//   for (let i = 0; i < inputArray.length; i++) {
//     if (longest === string(inputArray[i])) {
//       longestWord.push(inputArray[i]);
//     }
//     if (longest < string(inputArray[i])) {
//       longestWord.push(inputArray[i]);
//     }
//   }

//   return longestWord;
// }

// function string(word) {
//   var new_str = word.split(",");
//   var count = 0;
//   for (let i = 0; i < word.length; i++) {
//     count += 1;
//   }
//   return count;
// }
// var inputArray = ["aba", "aa", "ad", "vcd", "aba"];
// console.log(inputArray.slice(0, 2));
// console.log(allLongestStrings(inputArray));
// var a = ["pramila", "bb", "ghartilolo"];

// // console.log(longestWord);
// function max(arr) {
//   len = arr.length;
//   for (let i = 0; i < len; i++) {
//     console.log("----------", i);
//     for (let j = i; j < len; j++) {
//       console.log("--------------", arr[j]);
//       for (let k = i; k <= j; k++) {
//         console.log("--------------------------------------");
//         console.log(arr[k]);
//       }
//       console.log(" ");
//     }
//   }
// }
// var arr = [3, 3, -10, 9, 5];
// var arrA = [1, 2, 3];
// console.log(max(arr));
// console.log(maxSumSubarray(arr, 7));
// console.log(maxSumSubarray(arrA, 2));

// function maxSumSubarray(arr, m) {
//   let max_end_here = 0;
//   let max_so_far = 0;
//   for (let i = 0; i < arr.length; i++) {
//     max_end_here += arr[i];
//     if (max_end_here < 0) {
//       max_end_here = 0;
//     }
//     if (max_so_far % m < max_end_here % m) {
//       max_so_far = max_end_here;
//     }
//   }
//   return max_so_far;
// }

var fizbuzz = n => {
  for (var i = 0; i < n; i++) {
    if (i % 5 == 0 || i % 3 == 0) {
      console.log("fizzbuzz");
    }
    if (i % 3 == 0) {
      console.log("Fizz");
    }
    if (i % 5 === 0) {
      console.log("Buzz");
    } else {
      console.log(i);
    }
  }
};
fizbuzz(100);
function addStrings(string1, string2) {
  let result = String();
  let i = string1.length - 1;
  let j = string2.length - 1;
  let carry = 0;
  while (i >= 0 || j >= 0) {
    let sum = carry;
    if (i > 0) {
      sum += string1.charAt(i) + "0";
      i--;
    }
    if (j > 0) {
      sum += string1.charAt(j) + "0";
      j--;
    }

    carry = sum / 10;
  }
  if (carry != 0) {
    result.push(carry);
  }
  return result.reverse().toString();
}

console.log(addStrings("3.14", "0.9"));
a = "5";
console.log(a);
