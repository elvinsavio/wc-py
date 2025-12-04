def print_table(rows, headers=None):
    """
    rows: list of rows, each a list/tuple of cell strings
    headers: optional list/tuple of header strings
    """
    if not rows and not headers:
        print("(empty)")
        return

    # Combine headers and rows to measure widths
    all_rows = []
    if headers:
        all_rows.append(headers)
    all_rows.extend(rows)

    col_widths = [
        max(len(str(row[i])) for row in all_rows)
        for i in range(len(all_rows[0]))
    ]

    def format_row(row):
        return " | ".join(str(cell).ljust(col_widths[i]) for i, cell in enumerate(row))

    # Print header
    if headers:
        print(format_row(headers))
        print("-" * (sum(col_widths) + 3 * (len(col_widths) - 1)))

    # Print rows
    for row in rows:
        print(format_row(row))

    print("-" * (sum(col_widths) + 3 * (len(col_widths) - 1)))
