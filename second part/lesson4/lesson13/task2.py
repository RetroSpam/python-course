import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f'Execution {round(end-start, 2)} seconds')

    return wrapper


@timer
def create_design(Task, pause):
    time.sleep(pause)
    print(Task)


Task_1 = 'Логотип Васильевский рынок'
Task_2 = 'Макет сайта "Логомашины"'


create_design(Task_1, 2.45)
create_design(Task_2, 4.30)