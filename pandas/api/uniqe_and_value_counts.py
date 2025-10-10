import numpy as np
import pandas as pd

pd.set_option('display.float_format', lambda x: '%.2f' % x)

df = pd.read_csv('../../my_data/naver_finance/2015_12.csv')

# For DataFrame <= nunique()
# nan은 count의 대상이 아님을 주의하자.
print(df.nunique())
# ticker       681
# 매출액(억원)      680
# 영업이익률(%)     667
# 순이익률(%)      672
# 당기순이익(억원)    680
# ROE(%)       655
# ROA(%)       650
# ROIC(%)      610
# EPS(원)       681
# BPS(원)       681
# SPS(원)       681
# PER(배)       668
# PBR(배)       680
# PSR(배)       668
# price        628
# price2       620
# dtype: int64

# For Series <= unique(), nunique(), value_counts()
# nan은 count의 대상이 아님을 주의하자.
print(df['ticker'].unique())
# ['AK홀딩스' 'BGF' 'BNK금융지주' 'BYC' 'CJ' 'CJ CGV' 'CJ대한통운' 'CJ씨푸드' 'CJ제일제당'
#  'CS홀딩스' 'DB' ....
#  '황금에스티' '효성' '효성 ITX' '후성' '휠라홀딩스' '휴니드테크놀러지스' '휴비스' '휴스틸' '휴켐스' '흥국화재'
#  '흥아해운']
print(df['ticker'].nunique())
# 681
print(df['ticker'].value_counts())
# ticker
# AK홀딩스      1
# BGF        1
# BNK금융지주    1
# BYC        1
# CJ         1
#           ..
# 휴비스        1
# 휴스틸        1
# 휴켐스        1
# 흥국화재       1
# 흥아해운       1
# Name: count, Length: 681, dtype: int64

############################################################
# index_col=0은 첫번째 컬럼을(즉 첫번째 series)를 인덱스로 사용하겠다는 의미이다.
df = pd.read_csv('../../my_data/symbol_sector.csv', index_col=0)
print(df.head())
#                  Sector
# AJ네트웍스  산업용 기계 및 장비 임대업
# AJ렌터카          운송장비 임대업
# AK홀딩스            기타 금융업
# AP우주통신         전자부품 제조업
# BGF              종합 소매업
