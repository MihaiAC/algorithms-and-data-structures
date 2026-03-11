import { TreeNode } from "../TreeNode";

/**
 * Returns the lowest common ancestor of n1, n2.
 * n1 and n2 are assumed to be unique and present in the tree.
 * @param root Candidate LCA.
 * @param n1
 * @param n2
 * @returns LCA of n1, n2
 */
function lca(root: TreeNode | null, n1: number, n2: number): TreeNode | null {
    if (root === null) return null;
    if (root.val === n1 || root.val === n2) return root;

    const leftLca = lca(root.left, n1, n2);
    const rightLca = lca(root.right, n1, n2);

    // If true, means n1 and n2 are in different subtrees of the current node =>
    // current node is the lca.
    if (leftLca && rightLca) return root;

    return leftLca ? leftLca : rightLca;
}

function getMaxDepth(root: TreeNode | null, currDepth: number): number {
    if (root === null) return currDepth - 1;

    const leftDepth = getMaxDepth(root.left, currDepth + 1);
    const rightDepth = getMaxDepth(root.right, currDepth + 1);

    return Math.max(leftDepth, rightDepth);
}

function getNodesAtMaxDepth(
    root: TreeNode | null,
    currDepth: number,
    maxDepth: number
): TreeNode[] {
    if (root === null) return [];
    if (currDepth === maxDepth) return [root];

    const leftNodes = getNodesAtMaxDepth(root.left, currDepth + 1, maxDepth);
    const rightNodes = getNodesAtMaxDepth(root.right, currDepth + 1, maxDepth);

    return [...leftNodes, ...rightNodes];
}

function subtreeWithAllDeepest(root: TreeNode | null): TreeNode | null {
    const maxDepth = getMaxDepth(root, 0);
    const nodesAtMaxDepth = getNodesAtMaxDepth(root, 0, maxDepth);

    if (nodesAtMaxDepth.length === 0) return null;

    let currLca = nodesAtMaxDepth[0];
    for (const node of nodesAtMaxDepth.slice(1)) {
        currLca = lca(root, currLca.val, node.val)!;
    }

    return currLca;
}
