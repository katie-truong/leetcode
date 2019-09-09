def longestVowelsOnlySubstring(S):
    vowels = set('aeiou')
    temp = 0
    aux = []

    for c in S + 'z':
        if c in vowels:
            temp += 1
        elif temp:
            aux.append(temp)
            temp = 0

    # If the first letter is not vowel, you must cut the head
    if S[0] not in vowels: 
        aux = [0] + aux
    # If the last letter is not vowel, you must cut the tail
    if S[-1] not in vowels: 
        aux += [0]

    return aux[0] + aux[-1] + max(aux[1:-1]) if len(aux) >= 3 else sum(aux)
    
print(longestVowelsOnlySubstring("abeaude"))