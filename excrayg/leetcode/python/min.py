def find_max_min(ip):
    if len(ip) ==1:
        return int(ip[0])
        
    val1 = float("-inf")
    # val2 = float("inf")
    for i in range(1, len(ip), 2):
        if ip[i] == '+':
            val1 = max(val1, find_max_min(ip[:i]) + find_max_min(ip[i+1:]))
        else:
            val1 = max(val1, find_max_min(ip[:i]) - find_max_min(ip[i+1:]))
            
    return val1

def find_max_min1(ip, d, s, e):
    if e-s == 1:
        return int(ip[s])
        
    val1 = float("-inf")
    # val2 = float("inf")
    for i in range(1, e-s, 2):
        if ip[i] ==  '+':           
        	val1 = max(val1, find_max_min1(ip, d, s, i) + find_max_min1(ip, d, i+1, e))
        else:
            val1 = max(val1, find_max_min1(ip[:i]) - find_max_min1(ip[i+1:]))
            
    return val1

print(find_max_min1("1+3−2−5+1−6+7"))

print(find_max_min("1+3−2−5+1−6+7"))