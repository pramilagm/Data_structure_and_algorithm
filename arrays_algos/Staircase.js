function staircase(n) {
  let printStaircase = "";
  for (var i = 1; i <= n; i++) {
    if (i < n) {
      printStaircase += " ".repeat(n - i) + "#".repeat(i) + "\n";
    } else {
      printStaircase += "#".repeat(i) + "\n";
    }
  }
  if (printStaircase.length > 1) {
    console.log(printStaircase);
  }
}
staircase(5);

function BirthdayCakeCandles(ar) {
  var maxCandlesHeight = ar[0];
  var maxCandleCount = 0;
  for (let i = 0; i < ar.length; i++) {
    if (ar[i] == maxCandlesHeight) {
      maxCandleCount++;
    }
    if (ar[i] > maxCandlesHeight) {
      maxCandlesHeight = ar[i];
      maxCandleCount = 1;
    }
  }
  return maxCandleCount;
}
var ar = [6, 3, 2, 6, 6, 6];
console.log(BirthdayCakeCandles(ar));

function vowelsAndConsonants(s) {
  var vowel = "aeiou";
  var consonant = "";
  // console.log("hello");
  for (let i = 0; i < s.length; i++) {
    if (!vowel.includes(s[i])) {
      consonant += s[i] + "\n";
    } else {
      console.log(s[i]);
    }
  }
  console.log(consonant);
}

var word = "javascriptloops";
vowelsAndConsonants(word);
