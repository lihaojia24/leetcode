package com.hector.singleton;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution1333 {
    public List<Integer> filterRestaurants(int[][] restaurants, int veganFriendly, int maxPrice, int maxDistance) {
        Arrays.sort(restaurants, (a, b) -> a[1] == b[1] ? b[0] - a[0] : b[1] - a[1]);
        List<Integer> ans = new ArrayList<>();
        for (int[] res : restaurants){
            boolean can = veganFriendly == 0 ? true : res[2] == 1;
            can = can && (maxDistance >= res[4]);
            can = can && (maxPrice >= res[3]);
            if (can){
                ans.add(res[0]);
            }
        }
        return ans;
    }
}