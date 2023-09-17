# def findMinArrowShots(points):
#     points.sort()
#     right = points[0][1]
#     cnt = 1
#     for p in points[1:]:
#         if right < p[0]:
#             right = p[1]
#             cnt += 1
#         else:
#             right = min(right, p[1])
#     return cnt


def findMinArrowShots(points):
    points.sort(key=lambda x:x[1])
    cnt, shot = 1, points[0][1]
    for p in points:
        if p[0] > shot:
            cnt, shot = cnt+1, p[1]
    return cnt 