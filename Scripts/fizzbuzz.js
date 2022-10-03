// Print fizzbuzz from 1 to the input number

const N = process.argv[2]
if (N === undefined) {
  console.error('Missing a number argument!')
  process.exit(1)
}

const FIZZBUZZ = {
  3: 'fizz',
  5: 'buzz',
}

for (let i = 1; i <= N; i++) {
  let fizzbuzz = ''

  Object.keys(FIZZBUZZ).forEach((key) => {
    if (i % key === 0) {
      fizzbuzz += FIZZBUZZ[key]
    }
  })

  if (fizzbuzz.length === 0) {
    fizzbuzz += i
  }

  console.log(fizzbuzz)
}