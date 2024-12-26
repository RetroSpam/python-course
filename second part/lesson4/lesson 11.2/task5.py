def sales_schedule_with_range(days_in_month):

    sale_days = list(range(3, days_in_month + 1, 3))
    print(f"Дни распродаж: {sale_days}")

sales_schedule_with_range(30)
sales_schedule_with_range(31)