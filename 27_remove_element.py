#  https://leetcode.com/problems/remove-element/

def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    len_nums = len(nums)
    i_swap = len_nums - 1 # индекс хвоста, куда можно сбрасывать лишний эл-т
    n_swap = 0            # кол-во лишних эл-ов
    i = 0                 # индекс текущего эл-та       

    for elem in nums:
        # цикл актуален, если еще не пересеклись индексы текущего и свалки
        if i <= i_swap:
            if elem == val:
                while (nums[i_swap] == val) & (i_swap >=0 ):
                    i_swap-=1
                    n_swap+=1
                if i <= i_swap:
                    nums[i], nums[i_swap] = nums[i_swap], nums[i]
                    n_swap+=1
                    i_swap-=1                
        i+=1
    if n_swap > 0:
        if n_swap >= len_nums:
            nums = []
        else:        
            nums = nums[0:len_nums-n_swap]
    return nums


        

def test():
    arr = [3, 2, 2, 3]
    val = 3
    assert removeElement(arr, val) == [2, 2]

    arr = [1]
    val = 1
    assert removeElement(arr, val) == []

    arr = [1]
    val = 0
    assert removeElement(arr, val) == [1]

    arr = [1, 1]
    val = 1
    assert removeElement(arr, val) == []

    arr = [1, 1]
    val = 0
    assert removeElement(arr, val) == [1, 1]

    arr = [4, 5]
    val = 4
    assert removeElement(arr, val) == [5]

    arr = [4, 5]
    val = 5
    assert removeElement(arr, val) == [4]

    arr = [0,1,2,2,3,0,4,2]
    val = 2
    assert removeElement(arr, val) == [0,1,4,0,3]


if __name__ == '__main__':
    test()