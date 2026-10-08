def solution(s):
    answer = []
    groups = []

    s = s[2:-2].split("},{")

    for group in s:
        nums = list(map(int, group.split(",")))
        groups.append(nums)

    groups.sort(key=len)

    for group in groups:
        for num in group:
            if num not in answer:
                answer.append(num)

    return answer