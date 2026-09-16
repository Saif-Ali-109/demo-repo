// Intentionally unformatted for the Self-Healer lint/format demo.
// biome (single quotes + semicolons) will rewrite this file on ci-fix/<run-id>.
const greeting = "hello there"
const users = { count: 3, active: "yes" }
function greet(name) {
    return greeting + ", " + name + "!"
}
module.exports = { greet, users }