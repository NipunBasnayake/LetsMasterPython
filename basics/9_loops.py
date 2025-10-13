count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

total = 0
while True:
    user_input = input("enter a number (type 'exit' to stop): ")
    if user_input.lower() == "exit":
        break
    total += int(user_input)
    print(f"total: {total}")

counts = 0
while counts < 5:
    print(f"Count: {counts}")
    counts += 1
else:
    print("Loop completed successfully")