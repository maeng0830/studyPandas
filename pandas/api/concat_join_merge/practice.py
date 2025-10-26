import numpy as np
import pandas as pd
from ccxt.static_dependencies.ecdsa.numbertheory import is_prime

pd.set_option('display.float_format', lambda x: '%.2f' % x)

######################################################################################
product_df = pd.read_csv('../../../my_data/product.csv', index_col=0)
review_df = pd.read_csv('../../../my_data/review.csv', index_col=0)

print(product_df.shape)  # (474, 4)
print(review_df.shape)  # (27008, 6)

print(product_df.head(2))
#     id  brand                                title    price
# 0  384  apple   apple iphone 6 (space grey, 32 gb) 23999.00
# 1  385  apple  apple iphone 6s (space grey, 32 gb) 33999.00
print(review_df.head(2))
#    product__id  ...        date
# 0          351  ...  2011-07-22
# 1          351  ...  2011-08-23


flipkart_df = pd.merge(product_df, review_df, left_on='id', right_on='product__id', how='right')
flipkart_df.drop(['id', 'product__id', 'author', 'date'], axis=1, inplace=True)
print(flipkart_df.shape)
# (27008, 6)
print(flipkart_df)
#           brand  ...                                            content
# 0      micromax  ...  Has anyone ordered yet ? Please tell us your e...
# 1      micromax  ...  I bought this phone and been using for last we...
# 2      micromax  ...  Excellent phone altogether. Only negative poin...
# 3      micromax  ...  Worth for the money..... How much you are payi...
# 4      micromax  ...  i am a regular user of ebay india, and i usual...
# ...         ...  ...                                                ...
# 27003  micromax  ...                                               Good
# 27004        mi  ...  very nice product\nthanks again for your time ...
# 27005        mi  ...  Camera quality ,battery is excellent,volte is ...
# 27006        mi  ...                                       Good product
# 27007        mi  ...                        just want to say incredible
#
# [27008 rows x 6 columns]
######################################################################################
amazon_df = pd.read_csv('../../../my_data/amazon_review1.csv', index_col=0)
print(amazon_df.shape)
# (42190, 6)
print(amazon_df.head())
#               brand  ... rating
# date                 ...
# 2013-06-25    apple  ...      5
# 2013-06-25  samsung  ...      5
# 2013-06-29  samsung  ...      5
# 2013-07-01  samsung  ...      5
# 2013-07-04  samsung  ...      1
#
# [5 rows x 6 columns]

########################################################################################
df = pd.concat([amazon_df, flipkart_df], axis=0)
print(df.shape)
# (69198, 7)
print(df.head())
#               brand  ... rating
# 2013-06-25    apple  ...   5.00
# 2013-06-25  samsung  ...   5.00
# 2013-06-29  samsung  ...   5.00
# 2013-07-01  samsung  ...   5.00
# 2013-07-04  samsung  ...   1.00
#
# [5 rows x 6 columns]