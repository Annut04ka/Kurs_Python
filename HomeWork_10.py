import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
# Использование функции get_dummies для преобразования DataFrame в one-hot вид
one_hot_data1 = pd.get_dummies(data['whoAmI'])

#Перевод DataFrame в one-hot вид без использования get_dummies
one_hot_data = pd.DataFrame()
one_hot_data['robot'] = (data['whoAmI'] == 'robot').astype(int)
one_hot_data['human'] = (data['whoAmI'] == 'human').astype(int)

one_hot_data.head()