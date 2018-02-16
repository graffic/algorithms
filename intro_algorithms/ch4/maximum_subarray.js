/* Maximum subarray */
const LEFT = Symbol("left");
const RIGHT = Symbol("right");

/* Range [start, end)
 *
 * > Array.from(range(0, 10, false))
 * [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 * > Array.from(range(0, 10, true))
 * [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
 */
function* range(start, end, reversed) {
    if (!reversed) {
        for (let i=start; i<end; i++) yield i;
    }
    else {
        for(let i=end-1; i>=start; i--) yield i;
    }
}

/* Sliding maximum 
 * > sub_max([-1, 2, 3, 4, 5], 0, 3, LEFT)
 * [5, 1]
 * > sub_max([-1, 2, 3, 4, -5], 2, 5, RIGHT)
 * [7, 3]
 */
function sub_max(input, start, end, direction) {
    let max = -Infinity;
    let current = 0;
    let index;

    for(let i of range(start,end, direction == LEFT)) {
        current += input[i];
        if (current > max) {
            index = i;
            max = current;
        }
    }

    return [max, index];
}

/**
 * Find the maximum subarray that goes across left and right
 * 
 * @param {Array} input 
 * @param {number} start 
 * @param {number} end 
 * @param {number} mid 
 * 
 * > find_cross([1, 2], 0, 2, 1)
 * [3, 0, 1]
 * > find_cross([0, -1, 2, 5, 6, -7], 1, 6, 4)
 * [13, 2, 4]
 * > find_cross([-1, 2, 5, 6, -7, 40, -50], 0, 5, 2)
 * [13, 1, 3]
 */
function find_cross(input, start, end, mid) {
    const [left_sum, left_index] = sub_max(input, start, mid, LEFT);
    const [right_sum, right_index] = sub_max(input, mid, end, RIGHT);

    return [left_sum + right_sum, left_index, right_index];
}

/**
 * Find the maximum subarray in input starting at start and ending at end
 * 
 * @param {Array} input 
 * @param {number} start 
 * @param {number} end 
 * > find([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7], 0, 16)
 * [43, 7, 10]
 */
function find(input, start, end) {
    const relative_mid = Math.floor((end - start) / 2);
    if (relative_mid == 0) {
        return [input[0], start, start];
    }
    const mid = start + relative_mid;

    const [max_left, left_start, left_end] = find(input, start, mid);
    const [max_right, right_start, right_end] = find(input, mid, end);
    const [max_cross, cross_start, cross_end] = find_cross(input, start, end, mid);

    if (max_left >= max_right && max_left >= max_cross) {
        return [max_left, left_start, left_end];
    }
    else if (max_right >= max_left && max_right >= max_cross) {
        return [max_right, right_start, right_end];
    }
    return [max_cross, cross_start, cross_end];
}

/* Finds the maximum subarray of an array
 * > find_maximum_subarray([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7])
 * [43, 7, 10]
*/
function find_maximum_subarray(input) {
    // This is a wrapper function into the recursive find
    return find(input, 0, input.length);
}

exports = find_maximum_subarray;