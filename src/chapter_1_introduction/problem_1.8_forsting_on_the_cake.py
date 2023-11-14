"""
Iskander the Baker is decorating a huge cake by covering the rectangular surface
of the cake with frosting. For this purpose, he mixes frosting sugar with lemon
juice and beetle juice, in order to produce three kinds of frosting: yellow, pink and
white. These colours are identified by the numbers 0 for yellow, 1 for pink and 2
for white.
To obtain a nice pattern, he partitions the cake surface into vertical stripes of width
A1,A2, . . . ,An centimeters, and horizontal stripes of height B1,B2, . . . ,Bn centimeters,
for some positive integer n. These stripes split the cake surface into n × n
rectangles. The intersection of vertical stripe i and horizontal stripe j has colour
number (i + j ) mod 3 for all 1 ≤ i,j ≤ n, see Figure 1.8. To prepare the frosting,
Iskander wants to know the total surface in square centimeters to be coloured for each
of the three colours, and asks for your help.

Input
The input consists of the following integers:
• on the first line: the integer n,
• on the second line: the values of A1, . . . ,An, n integers separated by single spaces,
• on the third line: the values of B1, . . . ,Bn, n integers separated by single spaces.

Limits
The input satisfies 3 ≤ n ≤ 100 000 and 1 ≤ A1, . . . ,An,B1, . . . ,Bn ≤ 10 000.

Output
The output should consist of three integers separated by single spaces, representing
the total area for each colour 0, 1 and 2.


Sample Input
3
1 1 1
1 1 1
Sample Output
3 3 3


Sample Input
7
6 2 4 5 1 1 4
2 5 1 4 2 3 4
Sample Output
155 131 197


Catch:
the index starts with 1
so the first cell is (1,1)
and colour is (1+1)%3 --> 2 --> white
"""

from functools import lru_cache

def read_input():
    partition = int(input())
    vertical_stripes = list(map(int, input().split()))
    horizontal_stripes = list(map(int, input().split()))
    
    assert len(vertical_stripes) == partition, "Check vertical stripes input"
    assert len(horizontal_stripes) == partition, "Check horiontal stripes input"
    print(f"Partitions: {partition}")
    print(f"Vertical Stripes: {vertical_stripes}")
    print(f"Horizontal Strips: {horizontal_stripes}")
    return partition, vertical_stripes, horizontal_stripes

def fake_input_1():
    return 3, [1,1,1], [1, 1, 1]


def fake_input_2():
    return 7, [6,2,4,5,1,1,4], [2,5,1,4,2,3,4]

@lru_cache
def memo(v,h):
    return v*h

if  __name__ == "__main__":
    p, vs, hs = fake_input_2()
    
    output = [0]*3
    for i, v in enumerate(vs, start=1):
        for j, h in enumerate(hs, start=1):
            colour = ( i+j) % 3
            output[colour] += memo(v,h)

    print(" ".join(list(map(str,output))))


