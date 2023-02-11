# 중복 빼고 정렬하기
import sys

input = sys.stdin.readline

N = int(input())
num = sorted(set(map(int, input().split())))

print(*num)
