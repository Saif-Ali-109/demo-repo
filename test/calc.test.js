const { test } = require("node:test");
const assert = require("node:assert");
const { multiply } = require("../src/calc");

test("multiply returns the product", () => {
	assert.strictEqual(multiply(2, 3), 6);
});