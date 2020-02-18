public class Main{
    public static void main(String[] args) {
        BinaryTree bt = new BinaryTree();

        bt.addNode(new Node(10));
        bt.addNode(new Node(5));
        bt.addNode(new Node(12));
        bt.addNode(new Node(20));
        bt.addNode(new Node(7));
        bt.addNode(new Node(3));
        bt.addNode(new Node(4));

        System.out.println(BinaryTree.searchValue(bt.root, 3));

        System.out.println("\nIn order tree:");
        BinaryTree.displayInOrder(bt.root);
        System.out.println("\nPre order tree:");
        BinaryTree.displayPreOrder(bt.root);
        System.out.println("\nPost order tree:");
        BinaryTree.displayPostOrder(bt.root);
    }
}