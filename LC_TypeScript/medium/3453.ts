function separateSquares(squares: number[][]): number {
    let [minY, maxY] = [squares[0]![1]!, squares[0]![1]! + squares[0]![2]!];
    let total_area = 0;
    for (const square of squares) {
        const bottomY = square[1]!;
        const topY = bottomY + square[2]!;

        minY = Math.min(minY, bottomY);
        maxY = Math.max(maxY, topY);
        total_area += square[2]! ** 2;
    }

    const check = (yCand: number) => {
        let area = 0;
        for (const [_, y, l] of squares) {
            if (y < yCand) {
                area += l * Math.min(yCand - y, l);
            }
        }
        return area >= total_area / 2;
    };

    const eps = 1e-5;
    while (Math.abs(maxY - minY) > eps) {
        const midY = (maxY + minY) / 2;
        if (check(midY)) {
            maxY = midY;
        } else {
            minY = midY;
        }
    }

    return maxY;
}
