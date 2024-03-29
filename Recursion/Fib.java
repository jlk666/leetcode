public class Fib{
    // 1. what type of input? what type of value? 
    public int fib(int n){
        // 3. base case, the end of recursion
        if (n <= 2){
            return n-1;
        }
        return fib (n-1)+fib(n-2);
        //2. the relationship between this level and level before
        
    }
}