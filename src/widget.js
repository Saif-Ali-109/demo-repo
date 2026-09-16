// Intentionally unformatted for the Self-Healer lint/format demo.
// The fixer (npx @biomejs/biome check --write .) will rewrite:
//   double quotes → single, adds semicolons, fixes indentation.
const greeting = "hello there"
const users = { count: 3, active: "yes" }
function greet(name) {
    return `hi ${name}!`
}
module.exports = { greet, users }