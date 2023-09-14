# def scheduleCourse(courses):
#     courses.sort(key=lambda x:x[1])
#     print(courses)
#     ans = []
#     start = 0
#     for du,de in courses:
#         if start+du <= de:
#             ans.append([start,start+du])
#             start = start+du
#     print(ans)
#     return len(ans)

import heapq 
def schedule_courses(courses):
    courses.sort(key=lambda x:x[1])
    hp, cur = [], 0
    for du, dl in courses:
        heapq.heappush(hp, -du)
        cur += du
        if cur > dl:
            cur += heapq.heappop(hp)
    return len(hp)

# courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
# courses = [[1,2]]
# courses = [[3,2],[4,3]]
courses = [[5,5],[4,6],[2,6]]
# print(scheduleCourse(courses))
print(schedule_courses(courses))


