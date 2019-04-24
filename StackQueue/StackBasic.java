public class StackBasic{
    public static void main(String[] args) {
        String a = "Kasur rusaK";
        String b = "";
        String c = "";
        StackInit s = new StackInit(a.length());
        for(int i = 0; i < a.length(); i++){
            s.push(a.charAt(i));
        }

        for (int i = 0; i < a.length(); i++){
            char popped = s.pop();
            b += popped;
            //System.out.println(s.pop());
        }

        if(a.equals(b))
            System.out.println("palindrome");
        else
            System.out.println("not a palindrome");

        System.out.println(" ");
    }
}