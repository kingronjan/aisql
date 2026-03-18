import numpy as np


def get_dot(vec_a, vec_b):
    """获取两个向量的点积：两个向量的同维度数字乘积之和"""
    if len(vec_a) != len(vec_b):
        raise ValueError('vectors must be of the same length')

    dot_sum = 0
    for a, b in zip(vec_a, vec_b):
        dot_sum += a * b
    return dot_sum


def get_norm(vec):
    """获取单个向量的模长，对向量的每个数字求平方，再求和，再开根号"""
    sum_square = 0
    for num in vec:
        sum_square += num ** 2
    return np.sqrt(sum_square)


def cosine_similarity(vec_a, vec_b):
    """计算两个向量的余弦相似度：点积除以模长的乘积"""
    dot_product = get_dot(vec_a, vec_b)
    return dot_product / (get_norm(vec_a) * get_norm(vec_b))


if __name__ == '__main__':
    vec_a = [0.5, 0.5]
    vec_b = [0.7, 0.7]
    vec_d = [-0.6, -0.5]
    print(cosine_similarity(vec_a, vec_b))
    print(cosine_similarity(vec_a, vec_d))