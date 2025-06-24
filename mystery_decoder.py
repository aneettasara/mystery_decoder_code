# Mystery Word Grid Decoder
# Author: [Your Name]
# Description: Decodes a mystery word from a 5x5 character grid
# using reversed diagonals.

def get_grid():
    print("Enter 5 rows of letters, space-separated (e.g., a b c d e):")
    grid = []
    for i in range(5):
        while True:
            row = input(f"Row {i+1}: ").strip().split()
            if len(row) != 5:
                print("Please enter exactly 5 characters.")
                continue
            grid.append(row)
            break
    return grid

def decode_grid(grid):
    # Extract diagonals
    main_diag = [grid[i][i] for i in range(5)]
    anti_diag = [grid[i][4 - i] for i in range(5)]

    # Reverse them
    main_diag.reverse()
    anti_diag.reverse()

    # Combine and return the decoded word
    return ''.join(main_diag + anti_diag)

def main():
    grid = get_grid()
    decoded_word = decode_grid(grid)
    print("\nDecoded Word:", decoded_word)

if __name__ == "__main__":
    main()

