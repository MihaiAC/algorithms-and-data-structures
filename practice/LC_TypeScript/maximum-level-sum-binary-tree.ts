class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = val === undefined ? 0 : val;
        this.left = left === undefined ? null : left;
        this.right = right === undefined ? null : right;
    }
}

function maxLevelSum(root: TreeNode | null): number {
    if (!root) return 0;

    let currNodes = [root];
    let currLevel = 1;
    let maxSum = root.val;
    let maxLevel = 1;

    while (currNodes.length > 0) {
        const nextLevel = [];
        let currSum = 0;

        for (const node of currNodes) {
            currSum += node.val;
            if (node.left) nextLevel.push(node.left);
            if (node.right) nextLevel.push(node.right);
        }

        currNodes = nextLevel;
        if (currSum > maxSum) {
            maxSum = currSum;
            maxLevel = currLevel;
        }

        currLevel += 1;
    }

    return maxLevel;
}
