// Intentionally unformatted for the Self-Healer lint/format demo.
// The fixer (npx @biomejs/biome check --write .) will rewrite:
//   var → const, double quotes → single, adds semicolons, fixes indentation.
var greeting = "hello there";
var users = { count: 3, active: 'yes' };
function greet(name) {
  return `${greeting}, ${name}!`;
}
module.exports = { greet, users };
