import { TreeNode } from "./TreeNode";

/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

type BalanceResult = {
    height: number;
    balanced: boolean;
};

function isBalanced(root: TreeNode | null): boolean {
    const heightBalanced = (root: TreeNode | null): BalanceResult => {
        if (root === null)
            return {
                height: 0,
                balanced: true,
            };

        const left = heightBalanced(root.left);
        const right = heightBalanced(root.right);
        if (
            !left?.balanced ||
            !right?.balanced ||
            Math.abs(left.height - right.height) > 1
        )
            return {
                height: 0,
                balanced: false,
            };

        return {
            height: 1 + Math.max(left.height, right.height),
            balanced: true,
        };
    };

    return heightBalanced(root).balanced;
}
