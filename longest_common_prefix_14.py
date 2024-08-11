# https://leetcode.com/problems/longest-common-prefix
# complexity: 

def find_max_cmn_prefix(strs) -> str:
    res = ""
    
    if strs[0] != "":
        curr_res = strs[0][0]
    else:
        return res
    len_strs = len(strs)
    ind = 0

    if len_strs == 1:
        print("Only 1 elem in list -> res = ", res)
        return strs[0]    
    elif curr_res == "":
        print("1st elem is empty -> res = ", res)
        return res
    else:
        while 1:
            print("res = ", res)
            print("ind = ", ind)
            print("curr_res = ", curr_res)
            for elem in strs:
                print("Current elem", elem)
                if elem == "":
                    return ""
                if elem[0:ind+1] != curr_res:
                    return res
            ind+=1
            res = curr_res
            leng = len(strs[0])
            if ind < len(strs[0]):
                curr_res+=strs[0][ind]
            else:
                return res
            
            




def test():
    strs = ["flower","flower","flower","flower"]
    target = "flower"
    assert find_max_cmn_prefix(strs) == target
    


if __name__ == '__main__':
    test()
