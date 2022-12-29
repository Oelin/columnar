from typing import Sequence
from dataclasses import dataclass
import numpy as np



def permute(sequence: Sequence, permutation: Sequence) -> Sequence:
    return [sequence[index] for index in permutation]


@dataclass
class ColumnarTranspositionCipher:

    alphabet: int = (0, 255)


    def encrypt(self, key: Sequence, data: Sequence) -> Sequence:

        columns = len(key)
        rows = len(data) // columns
        permutation = [key.index(x) for x in sorted(key)]

        padding = np.random.randint(*self.alphabet, len(data) % columns)
        plaintext = data + padding

        matrix = [plaintext[row : row + columns] for row in range(rows)]
        matrix = np.transpose(matrix)
        matrix = permute(matrix, permutation)
        ciphertext = matrix.flatten()

        return ciphertext


    def decrypt(self, key: Sequence, data: Sequence) -> Sequence:

        colums = len(key)
        rows = len(data) // columns
        permutation = [key.index(x) for x in sorted(key)]
        permutation = permute(sorted(permutation), permutation)

        matrix = data.reshape((rows, columns)).T
        plaintext = permute(matrix, permutation)

        return plaintext
