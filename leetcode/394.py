# stack = [['',1]]
# subs, k = stack.pop()
# print(subs,k)


def decodeString(s: str) -> str:
    stack = [['', 1]]
    num = ''
    for c in s:
        if c.isdigit():
            num += c
        elif c == '[':
            stack.append(['', int(num)])
            num = ''
        elif c == ']':
            subs, k = stack.pop()
            print("subs*k",subs*k)
            stack[-1][0] += subs * k
            print("stack[%s][%d]"%(subs,k))
        else:
            stack[-1][0] += c
    return stack[0][0] * stack[0][1]

s = "3[a]2[bc]"
results = decodeString(s)
print(results)