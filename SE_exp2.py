import numpy as np
import pandas as pd


yq_in_df = pd.read_csv('yq_in.txt', encoding='ansi', sep='\t', names=['省','市','人数'])  # 读入csv文件
del yq_in_df['省']  # 删除省名列


# 将整个dataframe按省份分成若干个小的dataframe，并写入文件
df1 = yq_in_df.iloc[0:12]
df1.to_csv('D:\SE\yq_out.txt', sep='\t', index=False, header=['浙江省', ''])
df2 = yq_in_df.iloc[12:24]
df2.to_csv('D:\SE\yq_out.txt', mode='a+', sep='\t', index=False, header=['江西省', ''])
df3 = yq_in_df.iloc[24:45]
df3.to_csv('D:\SE\yq_out.txt', mode='a+', sep='\t', index=False, header=['广东省', ''])
df4 = yq_in_df.iloc[45:58]
df4.to_csv('D:\SE\yq_out.txt', mode='a+', sep='\t', index=False, header=['江苏省', ''])
df5 = yq_in_df.iloc[58:72]
df5.to_csv('D:\SE\yq_out.txt', mode='a+', sep='\t', index=False, header=['湖南省', ''])
df6 = yq_in_df.iloc[72:88]
df6.to_csv('D:\SE\yq_out.txt', mode='a+', sep='\t', index=False, header=['安徽省', ''])
df7 = yq_in_df.iloc[88:101]
df7.to_csv('D:\SE\yq_out.txt', mode='a+', sep='\t', index=False, header=['陕西省', ''])
df8 = yq_in_df.iloc[101:120]
df8.to_csv('D:\SE\yq_out.txt', mode='a+', sep='\t', index=False, header=['河南省', ''])
df9 = yq_in_df.iloc[120:]
df9.to_csv('D:\SE\yq_out.txt', mode='a+', sep='\t', index=False, header=['贵州省', ''])

