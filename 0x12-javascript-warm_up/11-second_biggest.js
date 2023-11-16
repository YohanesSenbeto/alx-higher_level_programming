#!/usr/bin/node
function findSecondLargestInteger (args) {
  const integers = args.map(Number).filter(Number.isInteger)

  if (integers.length < 2) {
    return 0
  }

  const sortedIntegers = integers.sort((a, b) => b - a)
  return sortedIntegers[1]
}

const args = process.argv.slice(2)
const result = findSecondLargestInteger(args)
console.log('The second biggest integer is:', result)
