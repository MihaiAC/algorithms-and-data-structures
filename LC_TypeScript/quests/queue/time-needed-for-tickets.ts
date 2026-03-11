import assert from "node:assert";

function timeRequiredToBuy(tickets: number[], k: number): number {
    const kTickets = tickets[k];
    let requiredTime = 0;

    for (let idx = 0; idx < tickets.length; idx++) {
        if (idx <= k) {
            requiredTime += Math.min(tickets[idx], kTickets);
        } else if (idx > k) {
            requiredTime += Math.min(tickets[idx], kTickets - 1);
        }
    }

    return requiredTime;
}

assert.equal(timeRequiredToBuy([2, 3, 2], 2), 6);
assert.equal(timeRequiredToBuy([5, 1, 1, 1], 0), 8);
