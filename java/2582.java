class Solution{
    public int passThePillow(int n, int times){
        int time = times / (n -1);
        int res = times % (n - 1);
        if (time % 2 == 0){
            return res + 1;
        }
        return n - res;
    }
}