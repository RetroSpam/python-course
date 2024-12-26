from functools import lru_cache

@lru_cache(maxsize=None)
def calculate_project_cost(project_type, business_size):
    
    if project_type == 'Логотип' and business_size == 'малый бизнес':
        return 3000


print(f"Посчитали цену: {calculate_project_cost('Логотип', 'малый бизнес')}")
print(f"Загрузили из кеша: {calculate_project_cost('Логотип', 'малый бизнес')}")