# geometric_lib

![](https://repository-images.githubusercontent.com/58407107/d9543580-6f67-11e9-88f8-e2535c66675a)

Проект geometric_lib состоит из файлов:
- circle.py 
- rectangle.py 
- square.py 
- triangle.py 

Каждый файл состоит из функций для вычисления площадей и периметров различных геометрических фигур. 

## Математические формулы

| Фигура | Площадь | Периметр |
|--------|---------|----------|
| Круг | S = pi * r * r | P = 2 * pi * r |
| Прямоугольник | S = a * b | P = 2 * (a + b) |
| Квадрат | S = a * a | P = 4 * a |
| Треугольник | S = 1/2 * a * h | P = a + b + c |

## Коды функций 

### circle.py 

```python
import math

def area(r):
    return math.pi * r * r

def perimeter(r):
    return 2 * math.pi * r
```

### rectangle.py 

```python
def area(a, b): 
    return a * b 

def perimeter(a, b): 
    return 2 * (a + b)
```

### square.py 

```python
def area(a):
    return a * a

def perimeter(a):
    return 4 * a
```

### triangle.py 

```python
def area(a, h): 
    return 1/2 * a * h 

def perimeter(a, b, c): 
    return a + b + c 
```


## История коммитов
``` 
* commit 1890240312786d5fc999565e830020cc58caf292 (HEAD -> documentation)
| Author: Sofia Gorokhovskaya <gorsofart@yandex.ru>
| Date:   Mon Oct 13 16:44:34 2025 +0300
| 
|     A new branch was created and markdown files were added
| 
```