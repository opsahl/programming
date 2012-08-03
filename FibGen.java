public class FibGen{
    public FibGen(){
        a = 0;
        b = 1;
    }

    public long next(){
        temp = a;
        a = b;
        b = temp + a;
        
        return a;
    }

    public void reset(){
        a = 0;
        b = 1;
    }

    long a;
    long b;
    long temp;
}
