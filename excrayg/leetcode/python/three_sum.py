import random
import pprint

def get_rand_list(max_len):
    min_int, max_int = -50, 50
    test_list = []
    for i in range(max_len):
        test_list.append(random.randint(min_int, max_int))
        
    return test_list
    
def get_three_sum_to_k(test_list, k):
    test_list.sort()
    num_items = len(test_list)
    for a_idx in range(num_items-3+1):
        b_idx = a_idx + 1
        c_idx = num_items-1
        while b_idx < c_idx:
            a = test_list[a_idx]
            b = test_list[b_idx]
            c = test_list[c_idx]
            if a+b+c == k:
                return [a,b,c]
            elif a+b+c < k:
                b_idx += 1
            else:
                c_idx -= 1
                
    return []

num_test_cases = 10      
for test_case in range(num_test_cases):
    max_len_of_list = 10
    min_randk, max_randk = 0, 0  
    test_list = get_rand_list(max_len_of_list)
    k = random.randint(min_randk, max_randk)
    three_elem = get_three_sum_to_k(test_list, k)
    print("Test list: {} K: {}\nA,B,C: {}\n".format(test_list, k, three_elem))
    if three_elem:
        assert sum(three_elem) == k