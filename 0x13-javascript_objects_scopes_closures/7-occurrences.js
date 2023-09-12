#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let n = 0; n < list.length; n++) {
    if (list[n] === searchElement) {
      count++;
    }
  }
  return (count);
};
