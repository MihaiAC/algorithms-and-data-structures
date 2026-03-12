import assert from "node:assert";

function licenseKeyFormatting(s: string, k: number): string {
    const letters = Array.from(s).flatMap((letter) => {
        return letter !== "-" ? [letter.toUpperCase()] : [];
    });

    if (letters.length < k) return letters.join("");

    const [modK, divK] = [letters.length % k, Math.floor(letters.length / k)];
    let prefix = letters.slice(0, modK).join("");
    const chunks = Array.from({ length: divK }, (_, idx) =>
        letters.slice(modK + idx * k, modK + (idx + 1) * k).join("")
    );

    if (modK > 0) prefix += "-";
    return prefix + chunks.join("-");
}

assert.equal(licenseKeyFormatting("5F3Z-2e-9-w", 4), "5F3Z-2E9W");
assert.equal(licenseKeyFormatting("2-5g-3-J", 2), "2-5G-3J");
assert.equal(licenseKeyFormatting("2", 2), "2");
assert.equal(licenseKeyFormatting("-----------", 100), "");
