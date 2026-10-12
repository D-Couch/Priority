import assert from 'node:assert/strict';
import {linkableCitations} from './static/citations.mjs';
const sources = [{id:'CR 510.1c'}, {id:'CR 702.19d'}];
assert.equal(linkableCitations('Rule 510.1c; trample (702.19d).', sources), '[CR 510.1c]; trample ([CR 702.19d]).');
assert.equal(linkableCitations('[CR 510.1c] and [C1]', sources), '[CR 510.1c] and [C1]');
assert.equal(linkableCitations('Rule 999.1; Rule 510.1ca; 1510.1c', sources), 'Rule 999.1; Rule 510.1ca; 1510.1c');
console.log('Citation presentation checks passed.');
