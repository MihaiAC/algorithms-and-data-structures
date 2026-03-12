import assert from "node:assert";

function maskEmail(s: string): string {
    const atIdx = s.indexOf("@");
    const domain = s.slice(atIdx).toLowerCase();
    const email = s.slice(0, atIdx);

    return email[0]!.toLowerCase() + "*****" + email.at(-1)?.toLowerCase() + domain;
}

function splitNumber(st: string, offset: number): string {
    const splits = offset !== 0 ? ["*".repeat(offset)] : [];
    let idx;
    for (idx = offset; idx + 4 < st.length; idx += 3) {
        splits.push("***");
    }

    splits.push(st.slice(idx));
    return splits.join("-");
}

function maskPhoneNumber(s: string): string {
    const st = s.replaceAll(/[+\-() ]/g, "");
    return (st.length > 10 ? "+" : "") + splitNumber(st, st.length - 10);
}

function maskPII(s: string): string {
    if (s.includes("@")) return maskEmail(s);
    return maskPhoneNumber(s);
}

assert.equal(maskPII("LeetCode@LeetCode.com"), "l*****e@leetcode.com");
assert.equal(maskPII("AB@qq.com"), "a*****b@qq.com");
assert.equal(maskPII("1(234)567-890"), "***-***-7890");
assert.equal(maskPII("86-(10)12345678"), "+**-***-***-5678");
