package ShapeAbstracts;

public class Circle implements Shape{
    protected double radius=7;

    public Circle(){
    }

    public Circle(double radius,String color,boolean filled){
        this.radius = radius;
    }

    public double getRadius(){
        return radius;
    }

    public void setRadius(double radius){
        this.radius=radius;
    }

    public double getArea(){
        return (radius*radius)*(22/7);
    }

    public double getPerimeter(){
        return (radius*2)*(22/7);
    }

    public String toString(){
        return "Circle"+Circle+" radius= "+getRadius()+", area= "+getArea()+", perimeter= "+getPerimeter();
    }
}