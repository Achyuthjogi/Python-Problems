#Platform: HackerRank
#Problem: Swapcase
def swap_case(s):
    swap_case = s.swapcase()
    return swap_case

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
