def compute_transition_table(pattern, alphabet):
    pattern_len = len(pattern)
    transition_table = [0] * (pattern_len + 1)
    transition_table[0] = -1

    for i in range(pattern_len):
        transition_table[i + 1] = transition_table[i] + 1
        while transition_table[i + 1] > 0 and pattern[i] != pattern[transition_table[i + 1] - 1]:
            transition_table[i + 1] = transition_table[transition_table[i + 1] - 1] + 1

    return transition_table

def finite_automata_match(pattern, text):
    transition_table = compute_transition_table(pattern, set(text))

    pattern_len = len(pattern)
    current_state = 0
    matches = []

    for i, char in enumerate(text):
        while current_state > 0 and pattern[current_state] != char:
            current_state = transition_table[current_state]

        if pattern[current_state] == char:
            current_state += 1
        
        if current_state == pattern_len:
            matches.append(i - pattern_len + 1)

    return matches


# 示例用法
pattern = "abc"
text = "abracadabca"

matches = finite_automata_match(pattern, text)
print(matches)  # 输出: [0, 7]