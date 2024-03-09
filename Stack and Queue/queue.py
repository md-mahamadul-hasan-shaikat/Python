from collections import deque

bank = deque(['Anis', 'karim', 'Rafi', 'Rakib'])
bank.popleft()
print(bank)
bank.popleft()
print(bank)

if not bank:
    print("No person left")