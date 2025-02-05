def fix_case(s):
    uppercase_count = sum(1 for c in s if c.isupper())
    lowercase_count = len(s) - uppercase_count


    if uppercase_count > lowercase_count:
        return s.upper()
    else:
        return s.lower()


s = input().strip()

print(fix_case(s))
