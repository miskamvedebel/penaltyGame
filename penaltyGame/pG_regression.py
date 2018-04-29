import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

f = 'C:\\Users\\maksim.lebedev\\Desktop\\MachineLearning\\PythonHW\\projects\\penaltyGame\\data\\Scores_result.csv'

poss_var = pd.DataFrame({'Input Side': [0, 0, 0, 1, 1, 1, 2, 2, 2],
                         'Input Height': [3, 6, 9, 3, 6, 9, 3, 6, 9]}, 
                        columns=['Input Side', 'Input Height'])

def create_random_train(len_of_array=10000):
    res = pd.DataFrame(data=np.zeros(shape=(len_of_array, 5)), columns=['Predicted Side', 
                                     'Predicted Height', 
                                     'Input Side', 'Input Height', 'Scored'])
    for i in range(len_of_array):
        gen = np.random.randint(0, 3, size=(1,2))
        inp = np.random.randint(0, 3, size=(1,2))
        take = gen == inp
        res.loc[i, 'Predicted Side'] = gen[0][0]
        res.loc[i, 'Predicted Height'] = gen[0][1]
        res.loc[i, 'Input Side'] = inp[0][0]
        res.loc[i, 'Input Height'] = inp[0][1]
        res.loc[i, 'Scored'] = np.where((take[0][0] * take[0][1]) == False, 1, 0)
    for c in ['Predicted Height', 'Input Height']:
        res[str(c)] = res[str(c)].map({0:3, 1:6, 2:9})
    return res

def merge_dataset(rand, df):
    return rand.append(df, ignore_index=True)

def load_ds():
    f = 'C:\\Users\\maksim.lebedev\\Desktop\\MachineLearning\\PythonHW\\projects\\penaltyGame\\data\\Scores_result.csv'
    return pd.read_csv(f, sep=';') 

def train_model(X_train, y_train, 
                X_test=poss_var.loc[:, ['Input Side', 'Input Height']]):
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    score = lr.predict(poss_var.loc[:, ['Input Side', 'Input Height']])
    return score

def out_(score_rand):
    poss_var['Scored'] = score_rand
    out = poss_var[['Input Side', 'Input Height']][poss_var['Scored'] == np.max(poss_var['Scored'])]
    return out.iloc[0, 0], out.iloc[0, 1]



