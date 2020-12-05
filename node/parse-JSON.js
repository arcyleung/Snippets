const { performance } = require('perf_hooks');
const { shuffleArray, generateRandomStringArray, average } = require('./utils');
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
const numEntries = 100;
const stringifiedJsonObjects = jsonObjects.map(jso => JSON.stringify(jso))
const data = {};

const keys = generateRandomStringArray(4, null, numEntries);
let vals = generateRandomStringArray(50, null, numEntries - stringifiedJsonObjects.length);
console.log(vals);

vals = shuffleArray(vals.concat(stringifiedJsonObjects));
console.log(vals);


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

const quoteCheckParseIndexOf = (data) => {
    const ret = {};
    for (const [k, v] of Object.entries(data)) {
        if (v.indexOf('{') !== -1 && v.indexOf('[') !== -1) {
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

const quoteCheckParseStartsWith = (data) => {
    const ret = {};
    for (const [k, v] of Object.entries(data)) {
        if (!v.startsWith('{') && !v.startsWith('[')) {
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
const funcs = [
    tryCatchParse,
    quoteCheckParseIncludes,
    quoteCheckParseIndex,
    quoteCheckParseIndexOf,
    quoteCheckParseStartsWith
];

const timestamps = [[], [], [], [], []];

for (let trials = 0; trials < 10000; trials++) {
    const shuffledFuncsIdxs = shuffleArray(Array.from(Array(funcs.length).keys()));
    for (idx of shuffledFuncsIdxs) {
        const t0 = performance.now();
        const res = funcs[idx](data);
        const t1 = performance.now();
        // results.push(res)
        timestamps[idx].push(t1-t0);
    }
}



const averages = timestamps.map(times => average(times))

console.table(averages);
console.log(average([1,2,3,4,5,6]))

// assert.deepStrictEqual(results[0], results[1]);
// assert.deepStrictEqual(results[1], results[2]);
// assert.deepStrictEqual(results[2], results[0]);