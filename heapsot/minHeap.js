const minHeap = arr => {
  let temp = arr[0];
  arr[0] = arr[arr.length - 1];
  arr[arr.length - 1] = arr[0];
  arr.pop();
  heapify(arr, 0);
};

const parentIdx = idx => {
  return Math.floor(idx - 1 / 2);
};
const heapify = (arr, idx) => {
  if (idx == arr.length - 1) {
    return;
  }
  let left = 2 * idx;
  let right = 2 * idx + 1;

  if (arr[left] > arr[parentIdx(idx)] && arr[left] < arr[right]) {
    [arr[left], arr[minimum]] = [arr[minimum], arr[left]];
    heapify(arr, arr[parentIdx(idx)]);
  }
  //   if (arr[left] < arr[minimum] && arr[left] < arr.length) {
  //     minimum = arr[left];
  //   }
  //   if (arr[right] < arr[minimum] && arr[right] < arr.length) {
  //     minimum = arr[right];
  //   }

  if (arr[right] > arr[parentIdx(idx)] && arr[right] < arr[left]) {
    [arr[right], arr[parentIdx(idx)]] = [arr[parentIdx(idx)], arr[right]];
    heapify(arr, arr(parentIdx(idx)));
  }
  return arr;
};
var arr = [-1, 0, 1, 2, 3, 4, 5];

console.log(minHeap(arr));
console.log("Hello");
function allLongestStrings(inputArray) {
  var longestWord = [];
  var longest = string(inputArray[0]);
  for (let i = 0; i < inputArray.length; i++) {
    if (longest === string(inputArray[i])) {
      longestWord.push(inputArray[i]);
    }
    if (longest < string(inputArray[i])) {
      longestWord.push(inputArray[i]);
    }
  }

  return longestWord;
}

function string(word) {
  var new_str = word.split(",");
  var count = 0;
  for (let i = 0; i < word.length; i++) {
    count += 1;
  }
  return count;
}
var inputArray = ["aba", "aa", "ad", "vcd", "aba"];
console.log(inputArray.slice(0, 2));
console.log(allLongestStrings(inputArray));
var a = ["pramila", "bb", "ghartilolo"];

// console.log(longestWord);
