/**
 * Solving project euler problem 1
 */
public class Euler1{

    public static void main(String[] args){
        System.out.println(solve(10));
        System.out.println(solve(1000));
    }

    public static long solve(int max){
        long sum = 0;
        
        for(int i = 0; i < max; i++){
            if(i % 3 == 0 || i % 5 == 0){
                sum += i;
            }
        }
        return sum;
    }
}
