def matrix_dot_vector(a: list[list[int | float]], b: list[int | float]) -> list[int | float] | int:
    """
    Computes the dot product of an n x m matrix 'a' and a vector 'b' of length m.
    
    Returns:
        list: The resulting vector of length n if valid.
        int: -1 if dimensions are incompatible.
    """
    # Check for empty matrix or vector
    if not a or not b or not a[0]:
        return -1

    num_cols = len(a[0])

    # Check if number of columns matches vector length and all rows have consistent length
    if num_cols != len(b) or any(len(row) != num_cols for row in a):
        return -1

    # Compute dot product for each row
    return [sum(row[i] * b[i] for i in range(num_cols)) for row in a]