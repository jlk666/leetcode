public class BST_no_recursion_v {
    public int findPosition(int[] integer_list, int target){
        int start = 0;
        int end = integer_list.length -1;

        if (integer_list == null || integer_list.length == 0){
            return -1;
        }

        while (start < end){
            int mid = (start+end)/2;
            if (integer_list[mid] == target){
                return mid;
            }
            if(integer_list[mid] < target){ // target 大，往👉🏻走
                start = mid+1;
            }
            if(integer_list[mid] > target){ //target 小， 往左走
                end = mid-1;                
            }
        }
        if(integer_list[start] == target){
            return start;
        }

        return -1;
    }
}
