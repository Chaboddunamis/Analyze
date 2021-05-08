## Analyze
---
Analyze is a python module that provides comprehensive statistical analysis of a dataframe in 5 lines of code. It creates significant insight for data scientists, analysts and machine learning engineers, enabling quick understanding of a dataset..
---
### Installation

#### Install the package
```bash
pip install Analyze
```
---
#### Import the package into your code
```python
from Analyze import analyze, get_dist
```
---
#### Read your dataset into a variable and make it a dataframe 
```python
data = pd.read_csv('file.csv') # Use the appropriate file extension
```
---
#### Create an instance of the analyze class
```python
Datavalue = analyze(data)
```
---

#### Explore the comprehensive statistical value of your dataset using the analyse method.
```python
Datavalue.analyze()
```
---
#### Sample Output
```python
................................................
These are the categorical features in your dataset:

                                                 Name     Sex  \
0                             Braund, Mr. Owen Harris    male   
1   Cumings, Mrs. John Bradley (Florence Briggs Th...  female   
2                              Heikkinen, Miss. Laina  female   
3        Futrelle, Mrs. Jacques Heath (Lily May Peel)  female   
4                            Allen, Mr. William Henry    male   
5                                    Moran, Mr. James    male   
6                             McCarthy, Mr. Timothy J    male   
7                      Palsson, Master. Gosta Leonard    male   
8   Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)  female   
9                 Nasser, Mrs. Nicholas (Adele Achem)  female   
10                    Sandstrom, Miss. Marguerite Rut  female   
11                           Bonnell, Miss. Elizabeth  female   
12                     Saundercock, Mr. William Henry    male   
13                        Andersson, Mr. Anders Johan    male   
14               Vestrom, Miss. Hulda Amanda Adolfina  female   
15                   Hewlett, Mrs. (Mary D Kingcome)   female   
16                               Rice, Master. Eugene    male   
17                       Williams, Mr. Charles Eugene    male   
18  Vander Planke, Mrs. Julius (Emelia Maria Vande...  female   
19                            Masselmani, Mrs. Fatima  female   

              Ticket Cabin Embarked  
0          A/5 21171   NaN        S  
1           PC 17599   C85        C  
2   STON/O2. 3101282   NaN        S  
3             113803  C123        S  
4             373450   NaN        S  
5             330877   NaN        Q  
6              17463   E46        S  
7             349909   NaN        S  
8             347742   NaN        S  
9             237736   NaN        C  
10           PP 9549    G6        S  
11            113783  C103        S  
12         A/5. 2151   NaN        S  
13            347082   NaN        S  
14            350406   NaN        S  
15            248706   NaN        S  
16            382652   NaN        Q  
17            244373   NaN        S  
18            345763   NaN        S  
19              2649   NaN        C  



................................................
The 10th percentile values for each column in the dataset are:

PassengerId    90.00
Survived        0.00
Pclass          1.00
Age            14.00
SibSp           0.00
Parch           0.00
Fare            7.55
Name: 0.1, dtype: float64





................................................
The median values for each column of your dataset without missing values are:

PassengerId    457.0
Survived         1.0
Pclass           1.0
Age             36.0
SibSp            0.0
Parch            0.0
Fare            57.0
dtype: float64


................................................
The interquartile ranges of your dataset columns is:

PassengerId    445.0000
Survived         1.0000
Pclass           1.0000
Age             17.8750
SibSp            1.0000
Parch            0.0000
Fare            23.0896
dtype: float64




................................................
The coefficients of variation of your dataset columns without missing values are:

PassengerId     56.618895
Survived       109.330348
Pclass          36.083963
Age             63.499659
SibSp          137.349175
Parch          217.198066
Fare            76.676637
dtype: float64


------------------------------------
................................................
These are the numerical features in your dataset:

    PassengerId  Survived  Pclass   Age  SibSp  Parch     Fare
0             1         0       3  22.0      1      0   7.2500
1             2         1       1  38.0      1      0  71.2833
2             3         1       3  26.0      0      0   7.9250
3             4         1       1  35.0      1      0  53.1000
4             5         0       3  35.0      0      0   8.0500
5             6         0       3   NaN      0      0   8.4583
6             7         0       1  54.0      0      0  51.8625
7             8         0       3   2.0      3      1  21.0750
8             9         1       3  27.0      0      2  11.1333
9            10         1       2  14.0      1      0  30.0708
10           11         1       3   4.0      1      1  16.7000
11           12         1       1  58.0      0      0  26.5500
12           13         0       3  20.0      0      0   8.0500
13           14         0       3  39.0      1      5  31.2750
14           15         0       3  14.0      0      0   7.8542
15           16         1       2  55.0      0      0  16.0000
16           17         0       3   2.0      4      1  29.1250
17           18         1       2   NaN      0      0  13.0000
18           19         0       3  31.0      1      0  18.0000
19           20         1       3   NaN      0      0   7.2250

------------------------------------

................................................
The skew of your dataset is:

credit.policy        -1.539621
int.rate              0.164420
installment           0.912522
log.annual.inc        0.028668
dti                   0.023941
fico                  0.471260
days.with.cr.line     1.155748
revol.bal            11.161058
revol.util            0.059985
inq.last.6mths        3.584151
delinq.2yrs           6.061793
pub.rec               5.126434
not.fully.paid        1.854592
dtype: float64


------------------------------------
................................................
The mean values for each column of your dataset are:

PassengerId    446.000000
Survived         0.383838
Pclass           2.308642
Age             29.699118
SibSp            0.523008
Parch            0.381594
Fare            32.204208
dtype: float64


------------------------------------

................................................
The kurtosis of your dataset is:

PassengerId    -1.200000
Survived       -1.775005
Pclass         -1.280015
Age             0.178274
SibSp          17.880420
Parch           9.778125
Fare           33.398141
dtype: float64



------------------------------------
Distributions listed by Betterment of fit for int.rate:
............................................
   Distribution  chi_square
4      invgauss    1.029833
6         gamma    1.343415
8       lognorm    1.445072
1          norm    1.458848
3          beta    1.755474
5       uniform    2.043826
10       triang    5.287520
7         expon   14.766634
0   weibull_min   37.608865
2   weibull_max   74.688672
9      pearson3  398.094255


------------------------------------
Generating report... 

<scipy.stats._continuous_distns.weibull_min_gen object at 0x11e0699a0>
(0.44201093944372993, 1.9999999999999996, 6.268594297720819)

<scipy.stats._continuous_distns.norm_gen object at 0x11dd94a30>
(28.0, 17.2490408940528)

<scipy.stats._continuous_distns.weibull_max_gen object at 0x11e069d00>
(0.2488410231665656, 58.000000000000014, 1.5915689505857427)

<scipy.stats._continuous_distns.beta_gen object at 0x11e046400>
(1.0527932282858297, 0.8439361636930744, -7.839143943009921, 65.83914394300993)

<scipy.stats._continuous_distns.invgauss_gen object at 0x11e0951c0>
(0.03838006670625667, -62.95941618248101, 2367.692288500255)

<scipy.stats._continuous_distns.uniform_gen object at 0x11e0f53d0>
(2.0, 56.0)

<scipy.stats._continuous_distns.gamma_gen object at 0x11e07cd90>
(54.156927130881755, -98.49677304019752, 2.334748847288054)

<scipy.stats._continuous_distns.expon_gen object at 0x11e05c460>
(2.0, 26.0)

<scipy.stats._continuous_distns.lognorm_gen object at 0x11e0b13d0>
(4.3245955568716274, 1.9999999876441796, 1.595318052251119)

<scipy.stats._continuous_distns.pearson3_gen object at 0x11e0cd8b0>
(0.4767375399624638, 28.000022387906775, 17.488900591625978)

<scipy.stats._continuous_distns.triang_gen object at 0x11e0e1a00>
(0.9999999999942933, -16.926163961990795, 74.92616396492964)




------------------------------------

................................................
The variance values of your dataset are:

PassengerId    66231.000000
Survived           0.236772
Pclass             0.699015
Age              211.019125
SibSp              1.216043
Parch              0.649728
Fare            2469.436846
dtype: float64


------------------------------------
```
---

#### Maintainers: 
[Henry Uwakwe](https://www.linkedin.com/in/ikechukwu-henry-uwakwe-6916a5b6/) 