#Platform: HackerRank
#Problem: Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    student_mark = student_marks[query_name]
    
    avg = sum(student_mark)/len(student_mark)
    print(f"{avg:.2f}")
