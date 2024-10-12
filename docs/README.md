
# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

# L-03
- Circle and square added (8ba9aeb)
- Docs added (d078c8d)
- Docs added (6adb962)

# L-04
- Triangle added (d080c78)
- Doc updated for triangle (51c40eb)
- Add calculate.py (d76db2a)
- Update docs for calculate.py (b5b0fae)
- Add rectangle.py (3049431)

# L-05
- Add user agreement (438b89a)
- Update Docs. Add user agreement info (86edb1c)

# Program Circle 
Функция _area_ принимает значение радиуса круга ``` def area(r):```,
после чего возвращает значение его площади ```return math.pi * r * r```.
Пример работы функции:
```
def area(r):
    return math.pi * r * r
    
print(area(2)) 
```
Результатом работы функции будет 12.56.

Функция _perimeter_ принимает значение радиуса круга ``` def perimeter(r):```,
после чего возвращает значение его периметра ```return 2 * math.pi * r```.
Пример работы функции:
```
def perimeter(r):
    return 2 * math.pi * r
    
print(perimeter(3)) 
```
Результатом работы функции будет 18.84.

# Program Square
Функция _area_ принимает значение стороны квадрата ``` def area(a):```,
после чего возвращает значение его площади ```return a * a```.
Пример работы функции:
```
def area(a):
    return return a * a
    
print(area(6)) 
```
Результатом работы функции будет 36.

Функция _perimeter_ принимает значение стороны квадрата ``` def perimeter(a):```,
после чего возвращает значение его периметра ```return 4 * a```.
Пример работы функции:
```
def perimeter(a):
    return return 4 * a
    
print(perimeter(5))
```
Результатом работы функции будет 20.

# Program Triangle
Функция _area_ принимает значение трёх сторон треугольника ``` def area(a, b, c):```,
после чего возвращает значение его полупериметра ```return (a + b + c) / 2```.
Пример работы функции:
```
def area(a, b, c):
    return (a + b + c) / 2
    
print(area(1, 2, 3)) 
```
Результатом работы функции будет 3.

Функция _perimeter_ принимает значение трёх сторон треугольника ``` def perimeter(a, b, c):```,
после чего возвращает значение его периметра ```return a + b + c```.
Пример работы функции:
```
def perimeter(a, b, c):
    return a + b + c
    
print(perimeter(5, 3, 2))
```
Результатом работы функции будет 10.

# Program Calculate
Сначала мы импортируем модули для работы с кругами и квадратами
```
import circle
import square
```
Глобальные переменные: 
- **figs** - список содержимых геометрических фигур.
- **funcs** - список поддерживаемых типов вычислений.
- **sizes** - словарь, определяющий количество параметров, необходимых для каждой комбинации функции и фигуры.

Функция _calc_:
```
def calc(fig, func, size):
	assert fig in figs
	assert func in funcs

	result = eval(f'{fig}.{func}(*{size})')
	print(f'{func} of {fig} is {result}')
```
Функция _calc_ принимает название геометрической фигуры **fig**, тип вычисления **func** (например _perimeter_ или _area_) и **size** - список размеров, необходимых для вычисления.

Функциональность:

- Проверяет, что указанная фигура ```assert fig in figs``` и функция ```assert func in funcs```поддерживаются.
- Динамически вызывает соответствующую функцию из соответствующего модуля с помощью eval ```result = eval(f'{fig}.{func}(*{size})')```.
- Выводит результат вычисления ```print(f'{func} of {fig} is {result}')```.

Основной блок выполнения функции:
```
if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	calc(fig, func, size)
```
Процесс:
1) Выбор фигуры:
Запрашивает у пользователя ввод названия фигуры до тех пор, пока не будет введено допустимое значение из списка figs.
2) Выбор функции:
Запрашивает у пользователя ввод типа вычисления до тех пор, пока не будет введено допустимое значение из списка funcs.
3) Ввод размеров:
Запрашивает у пользователя ввод необходимых размеров, разделенных пробелами.
Количество ожидаемых размеров определяется значением в словаре sizes для комбинации функции и фигуры. Если значение отсутствует, по умолчанию ожидается один размер.
4) Вычисление:
Вызывает функцию calc с предоставленными параметрами для выполнения вычисления и вывода результата.

Таким образом, например, если пользователь введет **circle** как название фигуры, выберет **area** для вычисление площади, укажет радиус **r = 3**,
то результатом работы программы будет ```area of circle is 78.53981633974483```

