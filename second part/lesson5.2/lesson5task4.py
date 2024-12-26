new_descriptions = [
    "Design is everywhere. Design is life",
    "Design your life"
]

def count_design_occurrences(descriptions):
    count = 0
    for description in descriptions:
        count += description.count("Design")
    return count


total_design_count = count_design_occurrences(new_descriptions)

print(f'The word "Design" appears {total_design_count} times in the new descriptions.')
