#Platfrom: HackerRank
#Problem: Finding runner-up score

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    unique_arr = set(arr)
    sort_arr = sorted(unique_arr)
    
    print(sort_arr[-2])
