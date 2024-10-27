hour = int(input("시간을 입력하세요: "))

result = 0

for h in range(hour + 1):
    for m in range(60):
        for s in range(60):
            hour = str(h)
            minute = str(m)
            second = str(s)

            time = hour + minute + second

            if '3' in time:
                result += 1

print(result)
