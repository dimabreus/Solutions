func = lambda a,b,h: print("Недосып") if h < a else print("Пересып") if h > b else print("Нормально")

func(8, 12, 3)
func(8, 12, 10)
func(8, 12, 15)
func(9, 8, 9)
