"""
Закодировать любую строку по алгоритму Хаффмана.
"""

import collections


class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value


def get_code(root, binary_repr=None, code=''):

    if binary_repr is None:
        binary_repr = dict()
    if root is None:
        return

    if isinstance(root.value, str):
        binary_repr[root.value] = code
        return binary_repr

    get_code(root.left, binary_repr, code + '0')
    get_code(root.right, binary_repr, code + '1')

    return binary_repr


def get_tree(string):
    string_count = collections.Counter(string)
    if len(string_count) <= 1:
        node = Node(None)
        if len(string_count) == 1:
            node.left = Node([key for key in string_count][0])
            node.right = Node(None)
        string_count = {node: 1}

    while len(string_count) != 1:
        node = Node(None)
        spam = string_count.most_common()[:-3:-1]
        if isinstance(spam[0][0], str):
            node.left = Node(spam[0][0])
        else:
            node.left = spam[0][0]
        if isinstance(spam[1][0], str):
            node.right = Node(spam[1][0])
        else:
            node.right = spam[1][0]
        del string_count[spam[0][0]]
        del string_count[spam[1][0]]
        string_count[node] = spam[0][1] + spam[1][1]

    return [key for key in string_count][0]


def coding(string, binary_repr):
    res = ''
    for symbol in string:
        res += binary_repr[symbol]

    return res


def decoding(string, binary_repr):
    res = ''
    i = 0
    while i < len(string):
        for code in binary_repr:
            if string[i:].find(binary_repr[code]) == 0:
                res += code
                i += len(binary_repr[code])

    return res


if __name__ == '__main__':
    my_string = input('Enter a string to compress: ')
    tree = get_tree(my_string)

    codes = get_code(tree)
    print(f'Encoding: {codes}')

    coding_str = coding(my_string, codes)
    print('Compressed string: ', coding_str)

decoding_str = decoding(coding_str, codes)
print('Source string: ', decoding_str)
