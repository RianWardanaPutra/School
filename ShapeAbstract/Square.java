package ShapeAbstracts;

public class Square extends Rectangle{
    protected double side=5;

    public Square(){
    }

    public Square(double side){
        this.side = side;
    }

    public Square(double side,String color,Boolean filled){
        this.side = side;
    }

    public double getSide(){
        return side;
    }

    public void setSide(double side){
        this.side=side;
    }

    public double setWidth(double width){
        this.width=width;
    }

    public double setLength(double length){
        this.length=length;
    }

    public String toString(){
        return "Square "+Square+" side= "+getSide();
    }
}