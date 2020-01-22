# trivial_compression.py
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


class CompressedGene:
    """A,C,G,Tからなるstrをビット列に変換したり戻したりする
    """
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        """A,C,G,Tを00,01,10,11のビット列に変換する
        """
        # 0b1を代入するのと同じはず。sentinelはガード
        self.bit_string: int = 1  # start with sentinel
        from sys import getsizeof
        print("initial bit_string: ", getsizeof(self.bit_string))
        for nucleotide in gene.upper():
            # 2ビットシフトして文字ごとに追加する2ビット分を確保する
            self.bit_string <<= 2  # shift left two bits
            if nucleotide == "A":  # change last two bits to 00
                # self.bit_string = self.bit_string | 0b00と同じ
                # 論理和なので元の情報は保存される
                self.bit_string |= 0b00
            elif nucleotide == "C":  # change last two bits to 01
                self.bit_string |= 0b01
            elif nucleotide == "G":  # change last two bits to 10
                self.bit_string |= 0b10
            elif nucleotide == "T":  # change last two bits to 11
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid Nucleotide:{}".format(nucleotide))

    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):  # - 1 to exclude sentinel
            # 2,4,6,...ビットを右シフトして１ビット目、２ビット目を取り出すことで途中のビットも取得できる
            # シフト演算子自体は破壊的ではない
            bits: int = self.bit_string >> i & 0b11  # get just 2 relevant bits
            # if文ではなく辞書を使用して参照する方法もある
            # 辞書ではハッシュ関数を利用するので性能が落ちる場合もある
            if bits == 0b00:  # A
                gene += "A"
            elif bits == 0b01:  # C
                gene += "C"
            elif bits == 0b10:  # G
                gene += "G"
            elif bits == 0b11:  # T
                gene += "T"
            else:
                raise ValueError("Invalid bits:{}".format(bits))
        # 読み込みが圧縮時とは逆方向なので[::-1]で反転する
        return gene[::-1]  # [::-1] reverses string by slicing backwards

    def __str__(self) -> str:  # string representation for pretty printing
        return self.decompress()


if __name__ == "__main__":
    from sys import getsizeof
    # original: str = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
    original: str = "ACGT" * 100
    # getsizeofで文字列のサイズだけでなく、そのほかの情報も含めたサイズを確認している
    print("original is {} bytes".format(getsizeof(original)))
    print("len(original):", len(original), " len(original.encode('utf-8')):", len(original.encode('utf-8')))
    compressed: CompressedGene = CompressedGene(original)  # compress
    print("compressed is {} bytes".format(getsizeof(compressed.bit_string)))
    # bit_stringはintなのでlenは使えない
    # print("len(original):", len(compressed.bit_string), " len(original.encode('utf-8')):", len(compressed.bit_string.encode('utf-8')))
    print(compressed)  # decompress
    print("original and decompressed are the same: {}".format(original == compressed.decompress()))
    print("整数として出力した場合: ", compressed.bit_string)