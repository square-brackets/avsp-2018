import sys
import copy
import operator
import math
from decimal import Decimal, ROUND_HALF_UP

NO_RATING = 'X'

def normalize(matrix, averages):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != NO_RATING:
                matrix[i][j] = matrix[i][j] - averages[i]

    return matrix

def calculate_matrix_average(matrix):
    averages = []
    for i in range(len(matrix)):
        sum_of_ratings = 0
        num_of_ratings = 0

        for j in range(len(matrix[i])):
            rating = matrix[i][j]
            if rating != NO_RATING:
                sum_of_ratings += rating
                num_of_ratings += 1

        averages.append(sum_of_ratings * 1.0 / num_of_ratings)

    return averages

def create_matrixes(n, m):
    user_item_matrix = [[0] * m for ni in range(n)]
    user_item_matrix_T = [[0] * n for mi in range(m)]

    for i in range(n):
        matrix_line = sys.stdin.readline().replace('\n', '').split(' ')
        for j in range(len(matrix_line)):
            item = matrix_line[j]
            if item != NO_RATING:
                item = int(item)
            user_item_matrix[i][j] = item
            user_item_matrix_T[j][i] = item

    return user_item_matrix, user_item_matrix_T

if __name__ == '__main__':
    n, m = sys.stdin.readline().split(' ')
    n = int(n)
    m = int(m)

    user_item_matrix, user_item_matrix_T = create_matrixes(n, m)

    average_item_ratings = calculate_matrix_average(user_item_matrix);
    average_user_ratings = calculate_matrix_average(user_item_matrix_T);

    def algorithm(item_index, user_index, k, data, normalized_matrix):
        similarities = []

        if len(data) == 0:
            return

        for i in range(len(data)):
            sum_of_multiplication = 0
            sum_of_owner_ratings = 0
            sum_of_other_ratings = 0

            if i == item_index:
                result = 1
            else:
                for j in range(len(data[0])):
                    owner_rating = normalized_matrix[item_index][j]
                    other_rating = normalized_matrix[i][j]

                    if owner_rating == NO_RATING:
                        owner_rating = 0

                    if other_rating == NO_RATING:
                        other_rating = 0

                    sum_of_multiplication += owner_rating * other_rating
                    sum_of_owner_ratings += owner_rating**2
                    sum_of_other_ratings += other_rating**2

                result = sum_of_multiplication / math.sqrt(sum_of_other_ratings * sum_of_owner_ratings)

            similarities.append((i, result))

        similarities = sorted(similarities, key=operator.itemgetter(1))
        similarities.reverse()

        cardinal_number = 0
        total_similar_values = 0
        total_values_with_grade = 0

        for similar_position, similar_value in similarities:
            if cardinal_number == k:
                break

            if similar_value > 0:
                grade = data[similar_position][user_index]

                if similar_position != item_index and grade != NO_RATING:
                    total_similar_values += similar_value
                    total_values_with_grade += grade * similar_value
                    cardinal_number += 1

        result = Decimal(Decimal(total_values_with_grade / total_similar_values).quantize(Decimal('.001'), rounding=ROUND_HALF_UP))
        print(result)

    q = sys.stdin.readline()
    q = int(q)

    for i in range(q):
        i, j, t, k = sys.stdin.readline().split(' ')
        i = int(i) - 1
        j = int(j) - 1
        k = int(k)

        if t == '0':
            # item-item
            matrix = copy.deepcopy(user_item_matrix)
            normalized_matrix = normalize(matrix, average_item_ratings)
            algorithm(i, j, k, user_item_matrix, normalized_matrix)
        elif t == '1':
            # user-user
            matrix = copy.deepcopy(user_item_matrix_T)
            normalized_matrix = normalize(matrix, average_user_ratings)
            algorithm(j, i, k, user_item_matrix_T, normalized_matrix)

# 5 5
# 1 2 X 2 4
# 2 X 3 X 5
# 3 1 X 4 X
# X 2 4 X 4
# 1 X 3 4 X
# 3
# 1 3 0 1
# 4 1 0 2
# 5 5 1 3

# 5 5
# 1 2 X 2 4
# 2 X 3 X 5
# 3 1 X 4 X
# X 2 4 X 4
# 1 X 3 4 X
# 1
# 5 5 1 3
