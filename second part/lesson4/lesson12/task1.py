def collect_data():

    data = [1, 2, 3, 4, 5]
    return process_data(data)

def process_data(data):

    if not data:
        return None
    average = sum(data) / len(data)
    return summarize_data(average)

def summarize_data(average):

    report = f"Result: Average: {average}"
    return report

result = collect_data()
print(result)