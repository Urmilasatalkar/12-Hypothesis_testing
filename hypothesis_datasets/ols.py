# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 16:10:11 2024

@author: urmii
"""

import pandas as pd
import numpy as np
wcat=pd.read_csv('C:/2-datasets/wc-at.csv')
#EDA
#measure the central tendency
#measure the dispersion
#third momont business decision
#fouth moment business decison
wcat.info()
wcat.describe()

#graphical representation
import matplotlib.pyplot as plt
plt.bar(height=wcat.AT,x=np.arange(1,110,1))
plt.hist(wcat.AT)
plt.boxplot(wcat.AT)

#data is right skewed
#scatter plot
plt.scatter(x=wcat['waist'],y=wcat['AT'],color='green')

#direction position linearly moderrate strenght:poor
#now let us calculate corelation coefficient
np.corrcoef(wcat.Waist,wcat.AT)[0,1]
#now let us check direction using cover factor
cov_output=np.cov(wcat.Waist,wcat.AT)[0,1]
cov_output

import stmodels.formula.api as smf
#all machine learning algorithms are implemented using sklearn
#but for his statmodels
#prectice is being because it give you
#backened calculation is bita=0 and bita=1
model=smf.ols('AT-Waist',data=wcat).fit()
model.summary()
#ols helps to find best fit model which cause
#least square error
#fisrt you check R squared value=0.670 if R square =0.8
#means that model is best fit
#fit if R-Squared 0.8 to 0.6 moderate fit
#next you check p->t  means less than alpha
#id alpha is 0.05 heance the model is accepted

#regression line
pred1=model.predict(pd.DataFrame(wcat['waist']))
plt.scatter(wcat.Waist,wcat.AT)
plt.plot(wcat.Waist,pred1,'r')
plt.show()

#error calculation
res1=wcat.AT.pred1
np.mean(res1)
#it must be zero and here it 
res_sqrl=res1*res1
rmsel=np.mean(res_sqrl)
rmsel

#32,76,76lesser the value better the model
#how to improve this model transformation of 
plt.scatter(x=np.log(wcat['Waist']),y=wcat['AT'],color='brown')
np.corrcoef(np.log(wcat.Waist),wcat.AT)
#r value is 0.82<0.85 hence moderate linerly
model2=smf.ols('AT~np.log(Waist)',data=wcat).fit()
model2.summary()

#again check the R square value 0.67 which is less than 0.8 
#p value is 0 less than 0.05
pred2=model2.predict(pd.DataFrame(wcat.Waist),wcat.AT)
#check wcat and pred2 from variale explorer
#scatter diagram
plt.scatter(np.log(wcat.Waist),wcat.AT)
plt.plot(np.log(wcat.Waist),pred2,'r')
plt.legend(['predicted line','observed data'])


#error calculation
res2=wcat.AT.pred2
np.mean(res2)
#it must be zero and here it 
res_sqrl2=res2*res2
rmsel2=np.mean(res_sqrl)
rmsel2

plt.scatter(x=wcat['Waist'], y=np.log(wcat['AT']),color='orange')

np.corrcoef(np.log(wcat.Waist),wcat.AT)
#r value is 0.82<0.85 hence moderate linerly
model3=smf.ols('np.log(AT)~Waist',data=wcat).fit()
model3.summary()

#again check the R square value 0.67 which is less than 0.8 
#p value is 0 less than 0.05
pred3=model3.predict(pd.DataFrame(wcat.Waist),wcat.AT)
pred3_at=np.exp(pred3)
#check wcat and pred2 from variale explorer
#scatter diagram
plt.scatter(np.log(wcat.Waist),wcat.AT)
plt.plot(np.log(wcat.Waist),pred3,'r')
plt.legend(['predicted line','observed data'])
plt.show()


#error calculation
res3=wcat.AT.pred3
np.mean(res3)
#it must be zero and here it 
res_sqrl3=res3*res3
rmsel3=np.mean(res_sqrl3)
rmsel3

plt.scatter(x=wcat['Waist'], y=np.log(wcat['AT']),color='orange')

np.corrcoef(np.log(wcat.Waist),wcat.AT)
#r value is 0.82<0.85 hence moderate linerly
model3=smf.ols('np.log(AT)~Waist',data=wcat).fit()
model3.summary()

#again check the R square value 0.67 which is less than 0.8 
#p value is 0 less than 0.05
pred3=model3.predict(pd.DataFrame(wcat.Waist),wcat.AT)
pred3_at=np.exp(pred3)
#check wcat and pred2 from variale explorer
#scatter diagram
plt.scatter(np.log(wcat.Waist),wcat.AT)
plt.plot(np.log(wcat.Waist),pred3,'r')
plt.legend(['predicted line','observed data'])
plt.show()










