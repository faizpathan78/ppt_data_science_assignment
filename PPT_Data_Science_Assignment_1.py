def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == s[::-1]

def find_largest_element(lst):
    return max(lst)

def count_occurrences(lst):
    occurrences = {}
    for item in lst:
        occurrences[item] = occurrences.get(item, 0) + 1
    return occurrences

def second_largest_number(lst):
    sorted_list = sorted(set(lst), reverse=True)
    return sorted_list[1]

def remove_duplicates(lst):
    return list(set(lst))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sort_list(lst):
    return sorted(lst)

def sum_of_numbers(lst):
    return sum(lst)

def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def all_permutations(s):
    if len(s) == 1:
        return [s]
    perms = []
    for i, c in enumerate(s):
        for perm in all_permutations(s[:i] + s[i + 1:]):
            perms.append(c + perm)
    return perms

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        while len(fib) < n:
            fib.append(fib[-1] + fib[-2])
        return fib

def median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n % 2 == 0:
        mid = n // 2
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[n // 2]

def is_sorted(lst):
    return lst == sorted(lst)

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def max_subarray_sum(lst):
    max_sum = current_sum = lst[0]
    for num in lst[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

def remove_vowels(s):
    vowels = "AEIOUaeiou"
    return ''.join([char for char in s if char not in vowels])

def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

def first_non_repeating_character(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    for char in s:
        if char_count[char] == 1:
            return char

def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

def merge_sorted_lists(lst1, lst2):
    merged_list = sorted(lst1 + lst2)
    return merged_list

def mode(lst):
    count_dict = {}
    for item in lst:
        count_dict[item] = count_dict.get(item, 0) + 1
    max_count = max(count_dict.values())
    return [item for item, count in count_dict.items() if count == max_count]

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def square_root(n):
    if n == 0 or n == 1:
        return n
    x = n
    y = 1
    while x > y:
        x = (x + y) // 2
        y = n // x
    return x

def valid_palindrome_ignore_non_alphanumeric(s):
    alphanumeric_s = ''.join(char.lower() for char in s if char.isalnum())
    return alphanumeric_s == alphanumeric_s[::-1]

def min_element_rotated_sorted_list(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        mid = (left + right) // 2
        if lst[mid] > lst[right]:
            left = mid + 1
        else:
            right = mid
    return lst[left]

def sum_of_even_numbers(lst):
    return sum(num for num in lst if num % 2 == 0)

def power_of_number(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / power_of_number(base, -exponent)
    else:
        return base * power_of_number(base, exponent - 1)

def remove_duplicates_preserve_order(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

def longest_common_prefix(strs):
    if not strs:
        return ""
    min_str = min(strs)
    max_str = max(strs)
    for i, char in enumerate(min_str):
        if char != max_str[i]:
            return min_str[:i]
    return min_str

def is_perfect_square(num):
    if num < 0:
        return False
    root = int(num ** 0.5)
    return root * root == num

def product_of_elements(lst):
    result = 1
    for num in lst:
        result *= num
    return result

def reverse_sentence_preserve_order(sentence):
    words = sentence.split()
    return ' '.join(words[::-1])

def missing_number(lst):
    n = len(lst) + 1
    total_sum = n * (n + 1) // 2
    current_sum = sum(lst)
    return total_sum - current_sum

def sum_of_digits(n):
    total_sum = 0
    while n > 0:
        total_sum += n % 10
        n //= 10
    return total_sum

def valid_palindrome_case_sensitive(s):
    return s == s[::-1]

def smallest_missing_positive_integer(lst):
    lst = [num for num in lst if num > 0]
    lst.sort()
    missing = 1
    for num in lst:
        if num == missing:
            missing += 1
        else:
            return missing
    return missing

def longest_palindrome_substring(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest_palindrome = ""
    for i in range(len(s)):
        odd_palindrome = expand_around_center(i, i)
        even_palindrome = expand_around_center(i, i + 1)
        longest_palindrome = max(longest_palindrome, odd_palindrome, even_palindrome, key=len)
    return longest_palindrome

def occurrences_of_element(lst, target):
    return lst.count(target)

def is_perfect_number(n):
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

def remove_duplicates_from_string(s):
    return ''.join(char for i, char in enumerate(s) if char not in s[:i])

def first_missing_positive(lst):
    n = len(lst)
    for i in range(n):
        while 1 <= lst[i] <= n and lst[lst[i] - 1] != lst[i]:
            lst[lst[i] - 1], lst[i] = lst[i], lst[lst[i] - 1]
    for i in range(n):
        if lst[i] != i + 1:
            return i + 1
    return n + 1


if __name__ == "__main__":
    
    sample_string = "hello"
    sample_list = [1, 2, 3, 4, 5, 3, 2, 1]
    sample_list2 = [5, 6, 7, 8, 9]
    sample_number = 12345
    sample_sentence = "This is a sample sentence."
    sample_string2 = "world"
    sample_rotated_list = [4, 5, 6, 7, 1, 2, 3]
    sample_num_list = [1, 2, 3, 4, 5, 6, 7]
    sample_str_list = ["apple", "banana", "orange", "apple", "grape"]
    sample_list3 = [10, 20, 30, 40, 50]

    print("1. Reverse String:", reverse_string(sample_string))
    print("2. Palindrome Check:", is_palindrome(sample_string))
    print("3. Largest Element in List:", find_largest_element(sample_list))
    print("4. Count Occurrences:", count_occurrences(sample_list))
    print("5. Second Largest Number:", second_largest_number(sample_list))
    print("6. Remove Duplicates from List:", remove_duplicates(sample_list))
    print("7. Factorial:", factorial(5))
    print("8. Prime Check:", is_prime(17))
    print("9. Sort List:", sort_list(sample_list))
    print("10. Sum of Numbers in List:", sum_of_numbers(sample_list))
    print("11. Common Elements:", common_elements(sample_list, sample_list2))
    print("12. Anagram Check:", is_anagram(sample_string, sample_string2))
    print("13. All Permutations of String:", all_permutations(sample_string))
    print("14. Fibonacci Sequence:", fibonacci(10))
    print("15. Median of List:", median(sample_list3))
    print("16. Non-decreasing Order Check:", is_sorted(sample_list))
    print("17. Intersection of Lists:", intersection(sample_list, sample_list2))
    print("18. Maximum Subarray Sum:", max_subarray_sum(sample_list3))
    print("19. Remove Vowels from String:", remove_vowels(sample_string))
    print("20. Reverse Order of Words in Sentence:", reverse_sentence(sample_sentence))
    print("21. Anagram Check (Case Sensitive):", is_anagram(sample_string, sample_string2))
    print("22. First Non-Repeating Character:", first_non_repeating_character(sample_string))
    print("23. Prime Factors of Number:", prime_factors(24))
    print("24. Power of Two Check:", is_power_of_two(64))
    print("25. Merge Sorted Lists:", merge_sorted_lists(sample_list, sample_list2))
    print("26. Mode of List:", mode(sample_list))
    print("27. Greatest Common Divisor (GCD):", gcd(48, 18))
    print("28. Square Root of Number:", square_root(16))
    print("29. Valid Palindrome (Ignoring Non-Alphanumeric):", valid_palindrome_ignore_non_alphanumeric(sample_sentence))
    print("30. Minimum Element in Rotated Sorted List:", min_element_rotated_sorted_list(sample_rotated_list))
    print("31. Sum of Even Numbers in List:", sum_of_even_numbers(sample_list))
    print("32. Power of Number using Recursion:", power_of_number(2, 5))
    print("33. Remove Duplicates from List (Preserve Order):", remove_duplicates_preserve_order(sample_str_list))
    print("34. Longest Common Prefix among Strings:", longest_common_prefix(sample_str_list))
    print("35. Perfect Square Check:", is_perfect_square(25))
    print("36. Product of Elements in List:", product_of_elements(sample_list))
    print("37. Reverse Order of Words in Sentence (Preserve Order):", reverse_sentence_preserve_order(sample_sentence))
    print("38. Missing Number in List of Consecutive Numbers:", missing_number(sample_num_list))
    print("39. Sum of Digits in Number:", sum_of_digits(sample_number))
    print("40. Valid Palindrome (Case Sensitive):", valid_palindrome_case_sensitive(sample_string))
    print("41. Smallest Missing Positive Integer in List:", smallest_missing_positive_integer(sample_num_list))
    print("42. Longest Palindrome Substring in String:", longest_palindrome_substring(sample_sentence))
    print("43. Occurrences of Element in List:", occurrences_of_element(sample_list, 3))
    print("44. Perfect Number Check:", is_perfect_number(28))
    print("45. Remove Duplicates from String:", remove_duplicates_from_string(sample_string))
    print("46. First Missing Positive in List:", first_missing_positive(sample_list3))

