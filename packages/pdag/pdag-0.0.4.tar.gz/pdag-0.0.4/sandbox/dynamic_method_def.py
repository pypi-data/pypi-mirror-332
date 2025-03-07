from typing import ClassVar

from rich import print

import pdag.utils


class C(pdag.utils.MultiDef):
    a: ClassVar[list[int]] = [1, 2]

    def f(self) -> list[int]:
        return self.a

    # In a loop, define multiple versions of 'g'.
    for i in range(3):

        @pdag.utils.multidef(i)
        def g(self, i: int = i) -> int:
            return i


if __name__ == "__main__":
    c = C()
    print(c.g)
    assert c.g[0]() == 0
    assert c.g[0](i=1) == 1
    assert c.g[1]() == 1
    assert c.g[2]() == 2
    assert c.a == [1, 2]
