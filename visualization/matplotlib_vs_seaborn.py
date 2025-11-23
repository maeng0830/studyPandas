import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.core.pylabtools import figsize

pd.set_option('display.float_format', lambda x: '%.2f' % x)

df = pd.read_csv("../my_data/Small_and_Big.csv", index_col=0, parse_dates=["date"])
print(df.head())

median_df = df.groupby(['date']).agg({'시가총액 (보통)(평균)(원)': 'median'})
median_df.columns = ["median_시가총액"]
print(median_df.head())
#               median_시가총액
# date
# 2000-07-31 34947000000.00
# 2000-08-31 33684000000.00
# 2000-09-30 33684000000.00
# 2000-10-31 30523000000.00
# 2000-11-30 30798000000.00

df = df.join(median_df, on="date")
df.loc[df['시가총액 (보통)(평균)(원)'] < df['median_시가총액'], 'size'] = "small"
df.loc[df['시가총액 (보통)(평균)(원)'] >= df['median_시가총액'], 'size'] = "big"

print(df.head())
#         date     종목명  PBR(IFRS-연결)  ...  시가총액 (보통)(평균)(원)    median_시가총액   size
# 0 2000-07-31     BYC          0.21  ...    27786000000.00 34947000000.00  small
# 1 2000-07-31      CJ          0.51  ...  1160889000000.00 34947000000.00    big
# 2 2000-07-31  CJ ENM          6.56  ...   400467000000.00 34947000000.00    big
# 3 2000-07-31  CJ대한통운          0.17  ...   194962000000.00 34947000000.00    big
# 4 2000-07-31   CJ씨푸드           NaN  ...     1987000000.00 34947000000.00  small

# count plot
## matplotlib
print(df['size'].value_counts())
df['size'].value_counts().plot(kind='bar')
plt.show()

## seaborn
sns.countplot(x='size', data=df)
plt.show()

# bar plot
df = df[df['date'] >= '2017-01-01']
## matplotlib
df.groupby(['date'])['수익률(%)'].mean().plot(kind='bar', figsize=(10, 5))
df['date'] = df['date'].dt.strftime('%Y-%m-%d')
plt.show()
## seaborn
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10, 5))
sns.barplot(data=df, x='date', y='수익률(%)', ax=ax, hue='size')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.show()

# relation plot <- seaborn
sns.relplot(data=df,
            x='PBR(IFRS-연결)',  # 1
            y='수익률(%)',  # 2
            col='size',  # 3
            hue='베타 (M,5Yr)',  # 4
            palette='coolwarm')
plt.show()

