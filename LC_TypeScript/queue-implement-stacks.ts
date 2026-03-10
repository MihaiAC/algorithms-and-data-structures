class MyQueue {
    private stack1: number[];
    private stack2: number[];

    constructor() {
        this.stack1 = [];
        this.stack2 = [];
    }

    push(x: number): void {
        this.stack1.push(x);
    }

    pop(): number {
        if (this.stack2.length === 0) {
            this.spill();
        }

        return this.stack2.pop()!;
    }

    spill(): void {
        while (this.stack1.length > 0) {
            this.stack2.push(this.stack1.pop()!);
        }
    }

    peek(): number {
        if (this.stack2.length === 0) {
            this.spill();
        }

        return this.stack2.at(-1)!;
    }

    empty(): boolean {
        return this.stack1.length === 0 && this.stack2.length === 0;
    }
}
