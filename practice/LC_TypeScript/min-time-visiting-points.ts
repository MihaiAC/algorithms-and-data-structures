function minTimeToVisitAllPoints(points: [number, number][]): number {
    const dist = (x: [number, number], y: [number, number]) => {
        const dx = Math.abs(y[0] - x[0]);
        const dy = Math.abs(y[1] - x[1]);

        return Math.max(dx, dy);
    };

    let time = 0;
    for (let ii = 0; ii < points.length - 1; ii++) {
        time += dist(points[ii], points[ii + 1]);
    }

    return time;
}
