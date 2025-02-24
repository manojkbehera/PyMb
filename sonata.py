# Alphabet Soup
# You have a bowl of letters (Alphabet soup). 
# Please write a method that outputs how many times you would be able to spell PENNYMAC 
# from the letters in the bowl. If you are unable to spell it, please return 0

from collections import Counter

def count_pennymac(soup):
    target_word = "PENNYMAC"
    target_count = Counter(target_word)  # Get frequency of each letter in "PENNYMAC"
    soup_count = Counter(soup)  # Get frequency of letters in the soup
    
    # Find the max number of times we can form "PENNYMAC"
    return min(soup_count[char] // target_count[char] for char in target_count)

# Example Usage:
soup = "PNENYAMCPENYMACPENNYMACPENN"
print(count_pennymac(soup))  # Output: 3
