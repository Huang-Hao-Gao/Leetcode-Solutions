int findMaxConsecutiveOnes(int* nums, int numsSize) {
    int max = 0;
    int acc = 0;
    for(int i = 0; i < numsSize; i++)
    {
        if(nums[i] == 1)
        {
            acc += 1;
            if(acc > max)
            {
                max = acc;
            }
        }
        else
        {
            acc = 0;
        }
    }
    return max;
}
