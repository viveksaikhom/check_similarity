def check_similarity(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    duplicates = {}

    for i, line1 in enumerate(lines):
        if line1 not in duplicates:
            duplicates[line1] = [i + 1]
        else:
            duplicates[line1].append(i + 1)

    has_duplicates = False
    count = 0
    for line, indices in duplicates.items():
        if len(indices) > 1:
            has_duplicates = True
            print(f"Similar lines found at: {', '.join(map(str, indices))}:")
            print(line + '\n')
            count += 1
    print(count)

    if not has_duplicates:
        print("\nNo similarities found in your f**king file. Please check your content.\nStop wasting my time.")


check_similarity('input.txt')
