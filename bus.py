def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a // gcd(a, b)) * b

def together_times(a, b, how_many):
    step = lcm(a, b)
    return [i * step for i in range(1, how_many + 1)]

print("=== Bus Schedule Overlap Calculator ===")
print("Example schedules:")
for a, b in [(12, 18), (10, 15), (7, 5), (20, 80)]:
    print(f"• Buses every {a} & {b} mins -> Meet every {lcm(a, b)} mins | Next 4: {together_times(a, b, 4)}")

while True:
    print()
    try:
        text = input("Enter two bus intervals in minutes (e.g., 10 4) or 'q' to quit: ").strip()
    except EOFError:
        break

    if not text or text.lower() == 'q':
        print("Goodbye!")
        break

    parts = text.replace(",", " ").split()
    if len(parts) != 2 or not all(p.isdecimal() and 0 < int(p) <= 999999 for p in parts):
        print("Invalid input. Please enter two positive whole numbers (e.g., 12 18).")
    else:
        a, b = int(parts[0]), int(parts[1])
        next_meeting = lcm(a, b)
        upcoming = together_times(a, b, 4)
        print(f"-> Both buses leave together again after {next_meeting} minutes.")
        print(f"-> Next 4 meeting times (in minutes): {upcoming}")

# Time complexity of lcm is O(log(min(a, b))) because it calls gcd(a, b), which reduces the numbers by at least half every two steps, and then does one division and multiplication in O(1) time.
