const allowed_next = new Map([
    ["(", ")"],
    ["{", "}"],
    ["[","]"]
]);

/**
 * Checks if a series of brackets are open and closed in the right order and balanced.
 * 
 * @param {string} brackets 
 * @return {bool} true in case the brackets are right.
 * 
 * > validBrackets("{{[[(())]]}}")
 * true
 * > validBrackets("{[(])}")
 * false
 * > validBrackets("()")
 * true
 * > validBrackets("[({})](")
 * false
 */
function validBrackets(brackets) {
    const pending = [];
    for(let i=0; i<brackets.length; i++) {
        const current = brackets[i];
        
        if (allowed_next.has(current)) {
            pending.push(allowed_next.get(current));
            continue;
        }
        
        const expected = pending.pop();
        if (expected !== current) {
            return false;
        }
        
    }

    return pending.length == 0;
}

exports = validBrackets;