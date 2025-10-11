# Print a Trinomial Triangle.
# Author: Lucas Vazquez (github.com/lucasvazq)


def print_trinomial_triangle(rows: int):
    """
    Print the first `rows` of the Trinomial Triangle.

    The trinomial triangle is a triangular array of numbers similar to Pascal's triangle.
    The top row consists of a single 1, and each subsequent row contains 2 more numbers than the last row.
    Each number is the sum of the 3 numbers above it.

    Example:
        Row 0:       1
        Row 1:     1 1 1
        Row 2:   1 2 3 2 1
        Row 3: 1 3 6 7 6 3 1

    Args:
        rows: The number of rows to generate and print.
    """

    # Initialize the triangle-data structure.
    # Here we are going to store the rows of the triangle.
    data = []

    # Generate the specified number of rows for the Trinomial Triangle.
    for index in range(rows):

        # Initialize the current row.

        if index == 0:
            # The first Row (with index 0) is always just [1].
            data.append([1])

        else:
            # Each row has 2 more elements than the previous row.
            # For example:
            # - Row with index 1 has 3 elements.
            # - Row with index 2 has 5 elements.
            # - Row with index 3 has 7 elements.
            # - Row with index 4 has 9 elements.
            # - ...
            new_row_range = (index * 2) + 1

            new_row = []
            for subindex in range(new_row_range):
                # Each element is the sum of the three elements above it.
                # If there is no element above it (because we are at the edge of the triangle),
                # we treat that as a 0.
                new_row.append(sum(data[-1][max(subindex-2,0):subindex+1]))

            data.append(new_row)

        # Print the last processed row.
        print(" ".join(str(x) for x in data[-1]))

        # === Compressed version! ===
        # Here's a solution for Code Golf enthusiasts:
        # d=[1];[print(*(d:=[sum(d[max(s-2,0):s+1])for s in range(i*2+1)]))for i in range(20)]
