import { TreeNode } from "./TreeNode";

function sumRootToLeaf(root: TreeNode | null): number {
    const sumAux = (root: TreeNode, bin: string): number => {
        bin += root.val;
        if (root.left === null && root.right === null) return parseInt(bin, 2);

        let currSum = 0;
        if (root.left !== null) currSum += sumAux(root.left, bin);
        if (root.right !== null) currSum += sumAux(root.right, bin);

        return currSum;
    };

    if (!root) return 0;
    return sumAux(root, "");
}
