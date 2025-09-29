from itertools import combinations
def solution(relation):
    num_rows = len(relation)
    num_cols = len(relation[0])
    
    all_combs = []
    for i in range(1, num_cols + 1):
        all_combs.extend(combinations(range(num_cols), i))

    unique_keys = []
    for comb in all_combs:
        tmp_set = set()
        for row in relation:
            tmp_set.add(tuple(row[c] for c in comb))
        if len(tmp_set) == num_rows:
            unique_keys.append(comb)
    
    candidate_keys = []
    for u_key in unique_keys:
        is_minimal = True
        for c_key in candidate_keys:
            if set(c_key).issubset(set(u_key)):
                is_minimal = False
                break
        
        if is_minimal:
            candidate_keys.append(u_key)
            
    return len(candidate_keys)
    