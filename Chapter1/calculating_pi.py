# calculating_pi.py
# From Classic Computer Science Problems in Python Chapter 1
# Copyright 2018 David Kopec
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def calculate_pi(n_terms: int) -> float:
    """円周率をライプニッツの公式を使って計算する
    ライブニッツの公式 pi = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 -
    これは例でもっと効率的なコードで実装できる
    """
    # 公式では全ての項で分子は4
    numerator: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0
    pi: float = 0.0
    for _ in range(n_terms):
        pi += operation * (numerator / denominator)
        # 分母が2ずつ増えている
        # 加減算は交互
        denominator += 2.0
        operation *= -1.0
    return pi


if __name__ == "__main__":
    print(calculate_pi(1000000))
