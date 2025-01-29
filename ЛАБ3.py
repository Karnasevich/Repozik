def calculak(a, b, operation="addd", *args, **kwargs):
    if operation == "addd":
        rezultat = a + b + sum(args)
    elif operation == "subtract":
        rezultat = a - b - sum(args)
    elif operation == "multipl":
        rezultat = a * b
        for num in args:
            rezultat *= num
    elif operation == "divide":
        if b == 0 or any(num == 0 for num in args):
            return "Не ділиться на 0"
        rezultat = a / b
        for num in args:
            rezultat /= num
    else:
        return "Помилка виконання програми"
    
    if "round" in kwargs:
        rezultat = round(rezultat, kwargs["round"])
    
    if kwargs.get("log", False):
        print(f"Operation: {operation}, rezultatult: {rezultat}")
    
    return rezultat
