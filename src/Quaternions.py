import math


class Quaternion:
    def __init__(self, real_part: float, i_part: float, j_part: float, k_part: float):
        self.r = real_part
        self.i = i_part
        self.j = j_part
        self.k = k_part

    def q_sum(self: 'Quaternion', q: 'Quaternion') -> 'Quaternion':
        return Quaternion(self.r + q.r, self.i + q.i, self.j + q.j, self.k + q.k)

    def hamilton_prod(self: 'Quaternion', q: 'Quaternion') -> 'Quaternion':
        r = (self.r * q.r) - (self.i * q.i) - (self.j * q.j) - (self.k * q.k)
        i = (self.r * q.i) + (self.i * q.r) + (self.j * q.k) - (self.k * q.j)
        j = (self.r * q.j) - (self.i * q.k) + (self.j * q.r) + (self.k * q.i)
        k = (self.r * q.k) + (self.i * q.j) - (self.j * q.i) + (self.k * q.r)
        return Quaternion(r, i, j, k)

    def conjugate(self: 'Quaternion') -> 'Quaternion':
        return Quaternion(self.r, -self.i, -self.j, -self.k)

    def to_string(self: 'Quaternion') -> str:
        return 'value: ' + str(self.r) + ' + ' + str(self.i) + 'i + ' + str(self.j) + 'j + ' + str(self.k) + 'k'

    def q_norm(self: 'Quaternion') -> float:
        return math.sqrt((self.r ** 2) + (self.i ** 2) + (self.j ** 2) + (self.k ** 2))

    def q_unitary(self: "Quaternion") -> 'Quaternion':
        norm = self.q_norm()
        return Quaternion(self.r/norm, self.i/norm, self.j/norm, self.k/norm)

    def q_mult_inverse(self: 'Quaternion'):
        res = self.conjugate()
        norm = (self.r ** 2) + (self.i ** 2) + (self.j ** 2) + (self.k ** 2)
        return Quaternion(res.r/norm, res.i/norm, res.j/norm, res.k/norm)

    def rotate(self: 'Quaternion', q: 'Quaternion') -> 'Quaternion':
        return q.hamilton_prod(self.hamilton_prod(q.conjugate()))


def rotation(angle: float, x: float, y: float, z: float) -> Quaternion:
    a: float = math.cos(angle / 2)
    b: float = math.sin(angle / 2)
    l: float = math.sqrt((x ** 2) + (y ** 2) + (z ** 2))
    return Quaternion(a, b * x / l, b * y / l, b * z / l)
