input_descriptions = [
    "Art is everywhere",
    "Art and Culture"
]

def replace_art_with_design(descriptions):
    return [description.replace("Art", "Design") for description in descriptions]

output_descriptions = replace_art_with_design(input_descriptions)

for input_text, output_text in zip(input_descriptions, output_descriptions):
    print(f'Input: "{input_text}" -> Output: "{output_text}"')
