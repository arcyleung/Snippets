const { performance } = require('perf_hooks');
const { shuffleArray, generateRandomStringArray } = require('./utils');
const jsonObjects = require('./test-files/large.json');
const assert = require('assert');

/*
 * This is an experiment to see whether it is faster (and how much faster)
 * to check whether a string has an opening curly/ square brace
 * before calling JSON.parse()
 * 
 * 
 * Input: Object with string properties, some of which could be parsed as JSON objects but we don't know which ones ahead of time
 * { foo: 'blah', bar: '{"baz":2,"qux":"oof"}' }
 * 
 * Output: Object with both string and Object properties
 * { foo: 'blah', bar: { baz: 2, qux: 'oof' } }
 */

// Set up test data
const numEntries = 1000;
const stringifiedJsonObjects = jsonObjects.map(jso => JSON.stringify(jso))
const data = {};

const keys = generateRandomStringArray(4, null, numEntries);
let vals = generateRandomStringArray(50, null, numEntries - stringifiedJsonObjects.length);
vals = shuffleArray(vals.concat(stringifiedJsonObjects));

for (let ix = 0; ix < numEntries; ix++) {
    data[keys[ix]] = vals[ix];
}

// console.log(data);

const tryCatchParse = (data) => {
    const ret = {};
    for (const [k, v] of Object.entries(data)) {
        try {
            ret[k] = JSON.parse(v);
        } catch (ex) {
            ret[k] = v;
        }
    }
    return ret;
};

const quoteCheckParseIncludes = (data) => {
    const ret = {};
    for (const [k, v] of Object.entries(data)) {
        if (!v.includes('{') && !v.includes('[')) {
            ret[k] = v;
            continue;
        }
        try {
            ret[k] = JSON.parse(v);
        } catch (ex) {
            ret[k] = v;
        }
    }
    return ret;
};

const quoteCheckParseIndex = (data) => {
    const ret = {};
    for (const [k, v] of Object.entries(data)) {
        if (v[0] !== '{' && v[0] !== '[') {
            ret[k] = v;
            continue;
        }
        try {
            ret[k] = JSON.parse(v);
        } catch (ex) {
            ret[k] = v;
        }
    }
    return ret;
};

// Test each method
const funcs = [tryCatchParse, quoteCheckParseIncludes, quoteCheckParseIndex];
const stats = [];
const results = [];
for (f of funcs) {
    const t0 = performance.now();
    const res = f(data);
    const t1 = performance.now();
    results.push(res)
    console.log(res);
    stats.push((t1-t0).toFixed(2));
}

console.table(stats);

assert.deepStrictEqual(results[0], results[1]);
assert.deepStrictEqual(results[1], results[2]);
assert.deepStrictEqual(results[2], results[0]);