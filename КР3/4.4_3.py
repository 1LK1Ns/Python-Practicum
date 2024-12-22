def find_pair(*numbers, div=6):
    maxx = 0
    r = 0
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if (numbers[i] + numbers[j]) % div == 0 and (numbers[i] + numbers[j]) >= maxx:
                if (numbers[i] + numbers[j] == maxx and j >= r) or numbers[i] + numbers[j] > maxx:
                    maxx = numbers[i] + numbers[j]
                    r = j
                    res = (numbers[i], numbers[j])
    return res
