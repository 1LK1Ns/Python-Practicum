def main():
    s1 = input()
    s2 = input()
    s3 = input()
    mi = 'яя'
    if 'зайка' in s1:
        mi = s1
    if 'зайка' in s2:
        mi = min(s2, mi)
    if 'зайка' in s3:
        mi = min(s3, mi)
    print(mi, len(mi))
if __name__ == "__main__":
    main()
