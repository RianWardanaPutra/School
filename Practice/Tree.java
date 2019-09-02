class Node {
    int data;
    Node left, right;

    public Node(int data) {
        this.data = data;
        left = right = null;
    }
}

class BSTree {
    Node root;

    public BSTree(Node root) {
        this.root = root;
    }

    public void insert(Node parent, Node child) {
        if(parent == null) {
            parent = child;
            return;
        }
        if(parent.data > child.data) {
            if(parent.left == null) {
                parent.left = child;
            } else {
                insert(parent.left, child);
            }
        } else {
            if(parent.right == null) {
                parent.right = child;
            } else {
                insert(parent.right, child);
            }
        }
    }

    public Node search(int key) {
        Node walk = this.root;
        if(walk == null) {
            return null;
        }
        while (walk.data != key) {
            if(key < walk.data) {
                walk = walk.left;
            } else {
                walk = walk.right;
            }
        }
        if(key == walk.data) {
            return walk;
        } else {
            return null;
        }
    }
}
