class Solution:
    def pathSum(self, root, targetSum: int) -> int:
        def dfs(node, current_sum, path_count):
            if not node:
                return 0

            # Update the current sum
            current_sum += node.val

            # Number of paths that end at the current node and sum to targetSum
            num_paths = path_count.get(current_sum - targetSum, 0)

            # Update the path count for the current sum
            path_count[current_sum] = path_count.get(current_sum, 0) + 1

            # Recur for left and right children
            num_paths += dfs(node.left, current_sum, path_count)
            num_paths += dfs(node.right, current_sum, path_count)

            # After the recursive call, remove the current sum from the path_count
            # to backtrack
            path_count[current_sum] -= 1

            return num_paths

        # Dictionary to store the prefix sums and their counts
        path_count = {0: 1}

        return dfs(root, 0, path_count)
