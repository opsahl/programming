import java.util.ArrayList;

public class Euler2{

    public static long solve(long top){
        ArrayList<Long> fibs = new ArrayList<Long>();
        FibGen fibGen = new FibGen();
        
        long newfib = fibGen.next();
        while(newfib < top){
            fibs.add(newfib);
            newfib = fibGen.next();
        }
        
        long sum = 0;
        for(long num : fibs){
            if(num % 2 == 0){
                sum += num;
            }
        }

        return sum;
        
    }

    public static void main(String[] args){
        System.out.println(solve(4000000));
    }
}
