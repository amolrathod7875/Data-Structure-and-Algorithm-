class Solution {
public:
    int maxArea(vector<int>& height) {
        int left_limit = 0;
        int right_limit = height.size() -1;
        int max_water = 0;
        while(left_limit < right_limit)
        {
            int width = right_limit - left_limit;
            int limiting_height = min(height[right_limit],height[left_limit]);
            int current_water = width * limiting_height;
            max_water = max(current_water,max_water);
            height[left_limit] < height[right_limit] ? left_limit++ : right_limit--;

            
        }
        return max_water;
    }
};