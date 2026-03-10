function nextGreatestLetter(letters: string[], target: string): string {
    for (const letter of letters) {
        if (letter > target) return letter;
    }

    return letters[0]!;
}
