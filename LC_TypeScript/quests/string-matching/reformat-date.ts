import assert from "node:assert";

const MONTHS = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
];

/**
 *
 * @param date Date in the format: "20th May 1960".
 * @returns Input date, in the format: "1960-05-20".
 */
function reformatDate(date: string): string {
    const regexp = /(\d+)\w+ (\w+) (\d+)/;
    const match = date.match(regexp);
    return (
        match![3] +
        "-" +
        (MONTHS.findIndex((x) => x === match![2]) + 1).toString().padStart(2, "0") +
        "-" +
        match![1].padStart(2, "0")
    );
}

assert.equal(reformatDate("20th May 1960"), "1960-05-20");
assert.equal(reformatDate("6th Jun 1933"), "1933-06-06");
assert.equal(reformatDate("26th May 1960"), "1960-05-26");
