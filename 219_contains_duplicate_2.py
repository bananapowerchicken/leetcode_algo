class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        count_dict = dict.fromkeys(set(nums), 0)

        for n in nums:
            count_dict[n] += 1
        
        print(count_dict)

        for el in count_dict:
            num, amount = el, count_dict[el]
            if amount >= 2: 
                i = nums.index(num)
                j = nums.index(num, i + 1) # need to add reversing the list and count from end
                print(abs(i - j), k)
                if abs(i - j) <= k:
                    return True
        
        return False