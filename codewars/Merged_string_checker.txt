# def is_merge(s, part1, part2):
#     s = {v:idx for idx, v in enumerate(s)}
#     pt1 = [s.get(v, -1) for v in part1]
#     pt2 = [s.get(v, -1) for v in part2]
#     if pt1==sorted(pt1) and pt2==sorted(pt2) \
#             and sum(s.values())==sum(pt1+pt2):
#         return True
#     return False

def is_merge(s, part1, part2):
    s=list(s)
    part1=list(part1)
    part2=list(part2)
    while part1 and part2:
        a = s.pop(0)
        if part1[0]==a:
            part1.pop(0)
        elif part2[0]==a:
            part2.pop(0)
        else:
            break
    if s==part1+part2 :
        return True
    return False


    # s=list(s)
    # pt1_ch=[]
    # for e in part1:
    #     s.remove(e)
    #     pt1_ch.append(e)
    # if pt1_ch==list(part1) and s==list(part2):
    #     return True
    # return False
    # s=list(s)
    # for el in part1:
    #     s.remove(el)
    # if ''.join(s)==part2:
    #     return True
    # return False


# print([1]+[2])

# print(len('aaa'))

print(is_merge('codewars', 'cdw', 'oears'))
