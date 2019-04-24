class StackInit{
    private final int maxSize;
    private final char[] stackArray;
    private int top;

    StackInit(int s){
        maxSize = s;
        stackArray = new char[maxSize];
        top = -1;
    }

    void push(char j){
        stackArray[++top] = j;
    }

    char pop(){
        return stackArray[top--];
    }

    //<E> pop(){
    //    return stackArray[top--];
    //}
    
    boolean isEmpty(){
        return (top == -1);
    }
}