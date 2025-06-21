def max_profit(prices: list):
    max_profit = 0 # max profit so far
    
    for left_pointer in range(len(prices)-1): #5
        for right_pointer in range(left_pointer+1, len(prices)):
            max_profit = max(prices[right_pointer] - prices[left_pointer], max_profit)

    return max_profit


def longest_substring(s: str) -> int:
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


