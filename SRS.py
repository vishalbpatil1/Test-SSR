
import statistics as s
import itertools as it

# Simple random sampling without replacment
def srs_wor(x,n):
    import itertools as it
    a=list(it.combinations(x,n))
    c=[];d=[]
    for i in a:
        b=list(i)
        import statistics as s
        mean=c.append(s.mean(b))
        var=d.append(s.variance(b))
    import pandas as pd
    z={'Sample':a,'sample_mean':c,'sample variance':d}
    df=pd.DataFrame(z)
    print(df)
    print('Estimate of population mean : ',s.mean(c))

# Simple random sampling with replacment



def srs_wr(x,n):
    a=list(it.product(x,repeat=n))
    c=[];d=[]
    for i in a:
        b=list(i)
        import statistics as s
        mean=c.append(s.mean(b))
        var=d.append(s.variance(b))
    import pandas as pd
    z={'Sample':a,'sample_mean':c,'sample variance':d}
    df=pd.DataFrame(z)
    print(df)
    print('Estimate of population mean : ',s.mean(c))


    ''' srs_wor([1,2,3,4],2)
     Sample  sample_mean  sample variance
0  (1, 2)          1.5              0.5
1  (1, 3)          2.0              2.0
2  (1, 4)          2.5              4.5
3  (2, 3)          2.5              0.5
4  (2, 4)          3.0              2.0
5  (3, 4)          3.5              0.5
Estimate of population mean :  2.5



srs_wr([1,2,3,4],2)

Sample  sample_mean  sample variance
0   (1, 1)          1.0              0.0
1   (1, 2)          1.5              0.5
2   (1, 3)          2.0              2.0
3   (1, 4)          2.5              4.5
4   (2, 1)          1.5              0.5
5   (2, 2)          2.0              0.0
6   (2, 3)          2.5              0.5
7   (2, 4)          3.0              2.0
8   (3, 1)          2.0              2.0
9   (3, 2)          2.5              0.5
10  (3, 3)          3.0              0.0
11  (3, 4)          3.5              0.5
12  (4, 1)          2.5              4.5
13  (4, 2)          3.0              2.0
14  (4, 3)          3.5              0.5
15  (4, 4)          4.0              0.0
Estimate of population mean :  2.5
'''