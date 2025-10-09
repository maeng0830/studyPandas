import numpy as np
import pandas as pd

#  Pandas DataFrame의 사이즈가 큰 경우, 어떻게 화면에 출력 할지 설정
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.max_columns', None)


np1 = np.arange(1, 6)
np2 = np.arange(6, 11)
print(np1, np2)
# [1 2 3 4 5] [ 6  7  8  9 10]

s1 = pd.Series(np1)
s2 = pd.Series(np2)
s1_custom_index = pd.Series(np1, index=[1, 2, 3, 4, 5])
s2_custom_index = pd.Series(np2, index=[6, 7, 8, 9, 10])

# dict
data_fram_for_np = pd.DataFrame({'c1': np1, 'c2': np2})
data_fram_for_s = pd.DataFrame({'c1': s1, 'c2': s2})

print(data_fram_for_np)
#    c1  c2
# 0   1   6
# 1   2   7
# 2   3   8
# 3   4   9
print(data_fram_for_s)
#    c1  c2
# 0   1   6
# 1   2   7
# 2   3   8
# 3   4   9

print(pd.DataFrame({'c1': s1_custom_index, 'c2': s2_custom_index}))
#      c1    c2
# 1   1.0   NaN
# 2   2.0   NaN
# 3   3.0   NaN
# 4   4.0   NaN
# 5   5.0   NaN
# 6   NaN   6.0
# 7   NaN   7.0
# 8   NaN   8.0
# 9   NaN   9.0
# 10  NaN  10.0

################################################################

# list
data_fram_for_np = pd.DataFrame(
    [
        np1,
        np2
    ]
)

data_fram_for_s = pd.DataFrame(
    [
        s1,
        s2,
    ]
)

print(data_fram_for_np)
#    0  1  2  3
# 0  1  2  3  4
# 1  6  7  8  9
print(data_fram_for_s)
#    0  1  2  3
# 0  1  2  3  4
# 1  6  7  8  9

