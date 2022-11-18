from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
t = int(input())

n, m = map(int, input().split())
graph = []
bread = []
time = []
for i in range(n) :
    graph.append(list(map(int, input().split())))
for i in range(m):
    bread.append(list(map(int, input().split())))



