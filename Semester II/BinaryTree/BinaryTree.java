class Node{
    private int value;
    public Node leftChild;
    public Node rightChild;

    Node(int value){
        this.value = value;
    }

    public int getValue(){
        return this.value;
    }
}

public class BinaryTree{
    public Node root;

    public void addNode(Node node){
        if(root == null){
            root = node;
        }else{
            insertNode(root, node);
        }
    }

    private void insertNode(Node parent, Node child){
        if(child.getValue() < parent.getValue()){
            if(parent.leftChild == null){
                parent.leftChild = child;
            }else{
                insertNode(parent.leftChild, child);
            }
        }else{
            if(parent.rightChild == null){
                parent.rightChild = child;
            }else{
                insertNode(parent.rightChild, child);
            }
        }
    }

    public static boolean searchValue(Node root, int value){
        if(root == null){
            return false;
        }else{
            if(root.getValue() == value){
                return true;
            }else if(root.getValue() > value){
                return searchValue(root.leftChild, value);
            }else{
                return searchValue(root.rightChild, value);
            }
        }
    }

    public static void displayInOrder(Node root){
        if(root != null){
            displayInOrder(root.leftChild);
            System.out.print(root.getValue() + " ");
            displayInOrder(root.rightChild);
        }
    }
    
    public static void displayPreOrder(Node root){
        if(root != null){
            System.out.print(root.getValue() + " ");
            displayInOrder(root.leftChild);
            displayInOrder(root.rightChild);
        }
    }
    
    public static void displayPostOrder(Node root){
        if(root != null){
            displayInOrder(root.leftChild);
            displayInOrder(root.rightChild);
            System.out.print(root.getValue() + " ");
        }
    }

    public boolean delete (int key){
        Node parent = root;
        Node current = root;
        boolean isLeftChild = false;
        boolean isRightChild = false;
        if(parent.getValue() == key){
            if(parent.leftChild == null ){

            }
        }
        return false;
    }
}