// Deliberate bug for the Self-Healer live-fix demo.
// `multiply` should return the product of its two arguments, but it returns
// the sum instead. The unit test in test/calc.test.js expects real
// multiplication, so `npm test` fails until this is corrected.
// Self-Healer should detect this, fix it, and open a fix PR.
function multiply(a, b) {
  return a * b;
}

module.exports = { multiply };
