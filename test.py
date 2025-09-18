def reverse(s, idx):
    if idx < 0:
        return
    print(s[idx])
    reverse(s, idx - 1)

s = input()

reverse(s, len(s) - 1)
