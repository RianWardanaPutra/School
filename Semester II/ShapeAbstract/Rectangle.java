package ShapeAbstracts;

public class Rectangle implements Shape{
    protected double width=2;
    protected double length=3;

    public Rectangle(){
    }

    public Rectangle(double width,double length){
        this.width = width;
        this.length = length;
    }

    public Rectangle(double width,double length,String color,Boolean filled){
        this.width = width;
        this.length = length;
    }

    public double getWidth(){
        return width;
    }

    public double setWidth(double width){
        this.width=width;
    }

    public double getLength(){
        return length;
    }

    public double setLength(double length){
        this.length=length;
    }

    public double getArea(){
        return width*length;
    }

    public double getPerimeter(){
        return (2*width)+(2*length);
    }

    public String toString(){
        return "Rectangle "+Rectangle+" width= "+getWidth()+", length= "+getLength()+" area= "+getArea()+" perimeter= "+getPerimeter();
    }
}