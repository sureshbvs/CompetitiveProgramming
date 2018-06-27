
import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;
import java.util.List;
import java.util.ArrayList;
import java.util.Stack;

import static org.junit.Assert.*;

public class Solution {

    public static class BinaryTreeNode {

        public int value;
        public BinaryTreeNode left;
        public BinaryTreeNode right;

        public BinaryTreeNode(int value) {
            this.value = value;
        }

        public BinaryTreeNode insertLeft(int leftValue) {
            this.left = new BinaryTreeNode(leftValue);
            return this.left;
        }

        public BinaryTreeNode insertRight(int rightValue) {
            this.right = new BinaryTreeNode(rightValue);
            return this.right;
        }
    }

   private static class NodeDepthPair 
{
    BinaryTreeNode node;
    int depth;
    NodeDepthPair(BinaryTreeNode node, int depth) 
    {
        this.node = node;
        this.depth = depth;
    }
}
public static boolean isBalanced(BinaryTreeNode treeRoot) 
{
    if (treeRoot == null) 
    {
        return true;
    }
    List<Integer> al = new ArrayList<>(3);
    Stack<NodeDepthPair> nodes = new Stack<>();
    nodes.push(new NodeDepthPair(treeRoot, 0));
    while (!nodes.empty()) 
    {
        NodeDepthPair nodeDepthPair = nodes.pop();
        BinaryTreeNode node = nodeDepthPair.node;
        int depth = nodeDepthPair.depth;
        if (node.left == null && node.right == null) 
        {
            if (!al.contains(depth)) 
            {
                al.add(depth);
                if (al.size() > 2 || (al.size() == 2
                        && Math.abs(al.get(0) - al.get(1)) > 1)) 
                {
                    return false;
                }
            }
        } 
        else 
        {
            if (node.left != null) 
            {
                nodes.push(new NodeDepthPair(node.left, depth + 1));
            }
            if (node.right != null) 
            {
                nodes.push(new NodeDepthPair(node.right, depth + 1));
            }
        }
    }

    return true;
}
    // tests

    @Test
    public void fullTreeTest() {
        final BinaryTreeNode root = new BinaryTreeNode(5);
        final BinaryTreeNode a = root.insertLeft(8);
        final BinaryTreeNode b = root.insertRight(6);
        a.insertLeft(1);
        a.insertRight(2);
        b.insertLeft(3);
        b.insertRight(4);
        final boolean result = isBalanced(root);
        assertTrue(result);
    }

    @Test
    public void bothLeavesAtTheSameDepthTest() {
        final BinaryTreeNode root = new BinaryTreeNode(3);
        root.insertLeft(4).insertLeft(1);
        root.insertRight(2).insertRight(9);
        final boolean result = isBalanced(root);
        assertTrue(result);
    }

    @Test
    public void leafHeightsDifferByOneTest() {
        final BinaryTreeNode root = new BinaryTreeNode(6);
        root.insertLeft(1);
        root.insertRight(0).insertRight(7);
        final boolean result = isBalanced(root);
        assertTrue(result);
    }

    @Test
    public void leafHeightsDifferByTwoTest() {
        final BinaryTreeNode root = new BinaryTreeNode(6);
        root.insertLeft(1);
        root.insertRight(0).insertRight(7).insertRight(8);
        final boolean result = isBalanced(root);
        assertFalse(result);
    }

    @Test
    public void bothSubTreesSuperbalancedTest() {
        final BinaryTreeNode root = new BinaryTreeNode(1);
        root.insertLeft(5);
        final BinaryTreeNode b = root.insertRight(9);
        b.insertLeft(8).insertLeft(7);
        b.insertRight(5);
        final boolean result = isBalanced(root);
        assertFalse(result);
    }

    @Test
    public void onlyOneNodeTest() {
        final BinaryTreeNode root = new BinaryTreeNode(1);
        final boolean result = isBalanced(root);
        assertTrue(result);
    }

    @Test
    public void treeIsLinkedListTest() {
        final BinaryTreeNode root = new BinaryTreeNode(1);
        root.insertRight(2).insertRight(3).insertRight(4);
        final boolean result = isBalanced(root);
        assertTrue(result);
    }

    public static void main(String[] args) {
        Result result = JUnitCore.runClasses(Solution.class);
        for (Failure failure : result.getFailures()) {
            System.out.println(failure.toString());
        }
        if (result.wasSuccessful()) {
            System.out.println("All tests passed.");
        }
    }
}
