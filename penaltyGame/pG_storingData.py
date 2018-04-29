import numpy as np
import pandas as pd

def save_result(gen_side, gen_height, inp_side, inp_height, scored):

    f = 'C:\\Users\\maksim.lebedev\\Desktop\\MachineLearning\\PythonHW\\projects\\penaltyGame\\data\\Scores_result.csv'
    df = pd.read_csv(f, sep=';')
    df_temp = pd.DataFrame(data={'Predicted Side':gen_side,
                                 'Predicted Height': gen_height,
                                 'Input Side': inp_side,
                                 'Input Height': inp_height,
                                 'Scored': scored},
                            columns=['Predicted Side', 'Predicted Height',
                                     'Input Side', 'Input Height', 'Scored'],
                           index = [0])
    df = df.append(df_temp, ignore_index=True)
    df.to_csv(f, sep=';', index=False)
