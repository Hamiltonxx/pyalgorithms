def box_stack_height(boxes):
    # Generate rotations
    rotations = []
    for box in boxes:
        l, w, h = box
        rotations.append((l, w, h))
        rotations.append((w, l, h))
        rotations.append((h, l, w))

    # Sort rotations in non-increasing order of base area
    rotations.sort(key=lambda x: x[0] * x[1], reverse=True)

    n = len(rotations)
    dp = [0] * n

    for i in range(n):
        dp[i] = rotations[i][2]  # Initialize with box height

        for j in range(i):
            if rotations[j][0] > rotations[i][0] and rotations[j][1] > rotations[i][1]:
                dp[i] = max(dp[i], dp[j] + rotations[i][2])

    return max(dp)

# Example usage
# boxes = [(1, 2, 3), (2, 3, 4), (3, 4, 5)]
boxes = [(3, 2, 1), (4, 3, 2), (5, 4, 3)]
max_height = box_stack_height(boxes)
print("Maximum height achievable:", max_height)