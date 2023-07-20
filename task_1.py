import random
import csv
import json


def generate_random_csv(filename, num_rows):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(num_rows):
            row = [random.randint(1, 1000) for _ in range(3)]
            writer.writerow(row)


def quadratic_equation_decorator(func):
    FILENAME = 'abc.csv'

    def wrapper():
        results = []
        with open(FILENAME, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                a, b, c = map(int, row)
                result = func(a, b, c)
                print(f'Equation: {a}x^2 + {b}x +{c} = 0')
                print('Roots:', result)
                results.append({'equasion': f'{a}x^2 + {b}x + {c} = 0',
                                'result': result})
            return results
    return wrapper


def save_to_json(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, 'w') as file:
                json.dump(result, file, indent=4)
            return result
        return wrapper
    return decorator



@save_to_json('result.json')
@quadratic_equation_decorator
def solve_quadratic_equation(*args):
    a, b, c, *other = args
    discriminant = b**2 - 4*a*c
    root1 = (-b + discriminant**(0.5)) / (2*a)
    root2 = (-b - discriminant**(-0.5)) / (2*a)
    return str(root1), str(root2)


if __name__ == "__main__":
    generate_random_csv('abc.csv', 10)
    solve_quadratic_equation()


