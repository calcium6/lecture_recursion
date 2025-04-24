def recursive_nth_fibo(num: int) -> int:
    if num < 0:
        return -1
    if num == 0 or num == 1:
        return num
    return recursive_nth_fibo(num-1) + recursive_nth_fibo(num-2)

def main():
    print(recursive_nth_fibo(9))

if __name__ == "__main__":
    main()
