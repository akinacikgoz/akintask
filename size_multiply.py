def find_max(t, z):
    max_value = 0
    for i in range(len(t)):
        for j in range(i + 1, len(t) + 1):
            substring = t[i:j]
            count = z.count(substring)
            max_value = max(max_value, len(substring) * count)
    return max_value

if __name__ == '__main__':
    print(find_max("acldm1labcdhsnd", "shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa"))