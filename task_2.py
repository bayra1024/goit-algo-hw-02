from collections import deque


def is_palindrome(s):
    s = s.lower().replace(" ", "")
    char_queue = deque(s)
    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            print(f'Рядок "{s}" - не паліндром.')
            return False
    print(f'Рядок "{s}" - паліндром.')
    return True
