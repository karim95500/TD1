def top_three(values):
    return sorted(values, reverse=True)[:3]
 
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_arithmetic_sequence(lst):
    if len(lst) < 2:
        return True
    diff = lst[1] - lst[0]
    return all(lst[i] - lst[i - 1] == diff for i in range(2, len(lst)))
    
