def maxpool_forward(X, pool_size, stride):
    """
    Compute the forward pass of 2D max pooling.
    """

    n_row = len(X)
    n_col = len(X[0])

    lst = []
    for row in range(0, n_row - pool_size + 1, stride):
        new_row = []
        for col in range(0, n_col - pool_size + 1, stride):
            val = -10**10
            for i in range(row, row + pool_size):
                for j in range(col, col + pool_size):
                    val = max(val, X[i][j])
            new_row.append(val)
        lst.append(new_row)

    return lst
