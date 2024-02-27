# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 09:38:16 2024

@author: urmii
"""
#################################1 sample t test #################################################
import numpy as np
import pandas as pd
from scipy import stats
import scipy
import statsmodels.stats.descriptivestats as sd
import statsmodels.stats.weightstats
#1 sample sign test
#for given dataset check weather scores are equal or less than 80
#H0: scores are either are not equal and greater than 80
#H1: scores are either are equal and greater than 80
#whenever there is single sampleand data is not normal
marks=pd.read_csv('C:/9-ML/Hypothesis/hypothesis_datasets/Signtest.csv')
marks
#Normal QQ plot
import pylab
stats.probplot(marks.Scores,dist='norm',plot=pylab)
#data is not normal
#H0: data is normal
#H1: data is not normal
stats.shapiro(marks.Scores)
#p_value is 0.024>0.005 ,p is high then null fly
#decision: data is not normal
marks.Scores.describe()
#1 sample sign test
sd.sign_test(marks.Scores,mu=marks.Scores.mean())
#P_value 0.82>0.005,p is high null fly
#decision: scores are either equal or less tha n 80

########################################1 sample z-test##############################################
#importing a data
import statsmodels.stats.weightstats as stests
fabric=pd.read_csv('C:/9-ML/Hypothesis/hypothesis_datasets/Fabric_data.csv')
#calculate the normality test
print(stats.shapiro(fabric))
#0.1460 H0 true
#calculate the mean
np.mean(fabric)
#ztest
#parameters in z test,value is mean of data
ztest,pval=stests.ztest(fabric,x2=None,value=150)
print(float(pval))
#p-value=7.156241255356764e-06<0.05 so p low null go


###########################mann whitney test################################################
#vehicles with and without addictive
#H0: fuel additive does not impact the performance
#h1: fuel additive does impact the performance
fuel=pd.read_csv('C:/9-ML/Hypothesis/hypothesis_datasets/mann_whitney_additive.csv')
fuel
fuel.columns='Without_Additive','With_additive'
#noemality test
#H0: data is normal
print(stats.shapiro(fuel.Without_Additive))
print(stats.shapiro(fuel.With_additive))
#without additive is normal
#with additive is not normal
##when two samples are not normal then mannwhitney test
#non-parametric test case
#mann -whitney test
scipy.stats.mannwhitneyu(fuel.Without_Additive, fuel.With_additive)


################paired t test################################################################
#when two featured are normal then paired t test
#univariate test that test for a significant diff between

sup=pd.read_csv('C:/9-ML/Hypothesis/hypothesis_datasets/paired2.csv')
sup

#H0: there is no significant diff between of suppliers A and B
#H1: there is significant diff between means of suppliers of A and B
stats.shapiro(sup.SupplierA)
stats.shapiro(sup.SupplierB)
#data.are normal
import seaborn as sns
sns.boxplot(data=sup)
#Assuming the external conditions are same for both samples
#paired t test
ttest,pval=stats.ttest_rel(sup['SupplierA'],sup['SupplierB'])
print(pval)
#decision : pval<0.05  then H1 is accepted

#########################2-sample t test###########################################################

#load the data
prom=pd.read_excel('C:/9-ML/Hypothesis/hypothesis_datasets/Promotion.xlsx')
prom
#H0:InterestRateWaiver < StandardPromotion
#H1:InterstRateWaiver > StandardPromotion
prom.columns='InterestRateWaiver','StandardPromotion'
#normality test
stats.shapiro(prom.InterestRateWaiver)
print(stats.shapiro(prom.StandardPromotion))

#data are normal
#variance test
help(scipy.stats.levene)
#H0: Both columns have equal variance
#H1: both columns have unequal variance
scipy.stats.levene(prom.InterestRateWaiver,prom.StandardPromotion)

#p-value=0.27>0.05 so p high null fly=>equal variance

ttest,pval=stats.ttest_ind(prom.InterestRateWaiver,prom.StandardPromotion)
help(scipy.stats.ttest_ind)
print(pval)
#H0:equal means
#h1:unequal means
#p-value=0.024 <0.05 so p is low null go


########  ONW WAY ANOVA#################################################################
conn=pd.read_excel('C:/9-ML/Hypothesis/hypothesis_datasets/ContractRenewal_Data(unstacked).xlsx')
conn.columns='SupplierA','SupplierB','SupplierC'
#H0: All the 3 suppliers have equal mean transaction time
#H1: All the 3 suppliers have not equal mean transaction time
#normlity test
stats.shapiro(conn.SupplierA)  #shapiro test
#pvalue=0.89>0.005 SupplierA is normal
stats.shapiro(conn.SupplierB)
stats.shapiro(conn.SuppliersC)
#0.57>0.005,sipplier c is normal
#variance test
help(scipy.stats.levene)
#all 3 suppliers are being checked for variance
scipy.stats.levene(conn.SupplierA,conn.SupplierB,conn.SupplierC)
#the levene test tests the null hypothesis
#the all input samples are from populations with equal variance
help(scipy.stats.levene)
#all 3 suppliers are being checked for variance

scipy.stats.levene(conn.SupplierA,conn.SupplierB,conn.SupplierC)
#the levene test tests the null hypothesis
#that all input samples are from populations with equal variance
#pvalue =0.777>0.005,p is high null fly
#H0 all input sample from populations with equal variance
#one way anova
f,p=stats.f_oneway(conn.SupplierA,conn.SupplierB,conn.SupplierC)
# p value
p #p is high null fly
#p value 0.10>0.05 H0 is accepted

############################ 2 probation test #############################################
'''johnie talkers soft drinks division sales manager has been planiing to luanch a new sakes
incentive program for their sales executive the sales executive flet that adults wont buy children will And 
hence requated sales manager not to launch the program analayze the data and determine whater there is a '''

two_prob_test=pd.read_excel('C:/9-ML/Hypothesis/hypothesis_datasets/JohnyTalkers.xlsx')
two_prob_test
from statsmodels.stats.proportion import proportions_ztest
tab1=two_prob_test.Person.value_counts()
tab1
tab2=two_prob_test.Drinks.value_counts()

#crosstable table
count=np.array([58,152])
nobs=np.array([480,740])
stats,pval=proportions_ztest(count,nobs,alternative='two-sided')
print(pval)
#val=0.00

stats,pval=proportions_ztest(count,nobs,alternative='Larger')
print(pval)
#val=0.999

############################# chi squared test ############################################
bahaman=pd.read_excel('C:/9-ML/Hypothesis/hypothesis_datasets/Bahaman.xlsx')
bahaman
count=pd.crosstab(bahaman['Defective'], bahaman['Country'])
count
Chisquare_results=scipy.stats.chi2_contingency(count)
Chisquare=[['Test Statistics','p-value'],[Chisquare_results[0],Chisquare_results[1]]]
Chisquare


'''you use chi2 contigency when you want to test
weahter two (or more) groups have the same distribution'''

#H0 : Null hypothesis the two groups have
#no significant difference
#since p=0.63>0.05 Hance H0 is True


 

