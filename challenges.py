class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]


@Memoize
def lcs(strA, strB):
    if len(strA) == 0 or len(strB) == 0:
        return 0
    elif strA[-1] == strB[-1]: # if the last characters match
        return 1 + lcs(strA[:-1], strB[:-1])
    else: # if the last characters don't match
        return max(lcs(strA[:-1], strB), lcs(strA, strB[:-1]))


def lcs_dp(strA, strB):
    """Determine the length of the Longest Common Subsequence of 2 strings."""
    rows = len(strA) + 1
    cols = len(strB) + 1

    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    for row in range(1, rows):

        for col in range(1, cols):
            dp_table[row][col] = (dp_table[row - 1][col - 1] + 1
                                  if strA[row-1] == strB[col-1]
                                  else max(dp_table[row][col - 1],
                                           dp_table[row - 1][col]))
    return dp_table[rows-1][cols-1]

def knapsack(items, capacity):
    """Return the maximum value that can be stored in the knapsack using the
    items given."""
    if 0 in (len(items), capacity):
        return 0
    other_items = items[1:]
    if items[0][1] > capacity:
        return knapsack(other_items, capacity)
    return max(items[0][2] + knapsack(other_items, capacity - items[0][1]),
               knapsack(other_items, capacity))

def knapsack_dp(items, capacity):
    """Return the maximum value that can be stored in the knapsack using the
    items given."""
    rows = len(items) + 1
    cols = capacity + 1
    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    for row in range(1, rows):

        for col in range(1, cols):

            dp_table[row][col] = (dp_table[row - 1][col]
                                  if items[row - 1][1] > col
                                  else max(items[row - 1][2] +
                                           dp_table[row - 1][col - items[row - 1][1]],
                                           dp_table[row - 1][col]))
    return dp_table[rows-1][cols-1]

@Memoize
def edit_distance(str1, str2):
    """Compute the Edit Distance between 2 strings."""
    if 0 in (len(str1), len(str2)):
        return max(len(str1), len(str2))
    if str1[-1] == str2[-1]:
        return edit_distance(str1[:-1], str2[:-1])
    return 1 + min(edit_distance(str1[:-1], str2),
                   edit_distance(str1, str2[:-1]),
                   edit_distance(str1[:-1], str2[:-1]))

def edit_distance_dp(str1, str2):
    """Compute the Edit Distance between 2 strings."""
    rows = len(str1) + 1
    cols = len(str2) + 1
    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    for row in range(1, rows):

        for col in range(1, cols):
            dp_table[row][col] = (dp_table[row - 1][col - 1]
                                  if str1[row - 1] == str2[col - 1]
                                  else 1 + min(dp_table[row - 1][col],
                                               dp_table[row][col - 1]))
    print(dp_table)
    return dp_table[rows-1][cols-1]
