notes, max_pitch, good_samples = map(int, input().split())

ans = []
for i in range(notes):
    rem = notes - i - 1
    cur = min(good_samples - rem, max_pitch)
    if cur <= 0:
        break
    if cur > i:
        val = min(max_pitch, i + 1)
        cur = val
    else:
        val = ans[i - cur]

    ans.append(val)
    good_samples -= cur

if good_samples == 0 and len(ans) == notes:
    print(*ans)
else:
    print(-1)
