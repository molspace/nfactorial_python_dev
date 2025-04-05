#Comments from mentor on bugs:

#Exercise 3: в функции pop, вместо вызова is_empty, было условие if self.is_empty, который евалуейтится как true всегда. Также не было ретурна

#Вот пример правильной реализации:

def pop(self):
    if self.is_empty:
        raise IndexError("Can't pop an empty stack.")
    return self._stack.pop()

# Exercise 8: перепутали знаки

# Exercise 10: Ваш код не хендлит кейс, где delay оверфлоуит, например, если departure "22:00" и вызываем delay(5), то у вас выходит "27:00"

# Exercise 12: substract и multiply не выполнены. Функция add написана неправильно. Вот пример правильной реализации:

def add(self, other):
    if other.rows != self.rows or other.cols != self.cols:
        raise ValueError(
            f"Matrix sizes don't match. Need: {self.rows} x {self.cols}"
        )
    new_matrix = [[0] * self.cols for _ in range(self.rows)]
    for row_idx in range(other.rows):
        for col_idx in range(other.cols):
            new_matrix[row_idx][col_idx] = (
                self.matrix[row_idx][col_idx] + other.matrix[row_idx][col_idx]
            )

    return Matrix(new_matrix)

# Exercise 14: Не учитывается, что передаваемый radius может быть отрицательным

# Exercise 17: Если есть две песни с одинаковым названием, то метод next_song выполнит задачу неправильно
