import statsmodels.api as sm
from statsmodels.formula.api import ols
import numpy as np
import pandas as pd
# masukkan Datanya
x = [9.3,8.95,14.12,10.22,13.22,9.51] # satu varible aja kalau 2 maka [[a,b],...]
y = [5,2,6,3,5,2]

x,y = np.array(x),np.array(y)
pendata =pd.DataFrame({'x':x,'y':y})
model = ols('y ~ x',pendata).fit()
tabel = sm.stats.anova_lm(model,typ=2)

print(tabel)

print(model.summary())