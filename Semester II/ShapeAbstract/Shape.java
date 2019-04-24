package ShapeAbstracts;

abstract class Shape{
    protected String color="Blue";
    protected Boolean filled=false;

    public Shape(){
    }

    public Shape(String color,boolean filled){
        this.color = color;
        this.filled = filled;
    }

    public String getColor(){
        return color;
    }

    public void setColor(String color){
        this.color=color;
    }

    public Boolean isFilled(){
        return filled;
    }

    public void setFilled(Boolean filled){
        this.filled=filled;
    }

    public double getArea(){
        return getArea();
    }

    public double getPerimeter(){
        return getPerimeter();
    }

    public String toString(){
        return toString();
    }
}