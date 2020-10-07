# put it all in a nifty function
import numpy as np 
from scipy.stats import t 

def t_statistic(tails, control,treatment,alpha):
    control_mean = np.mean(control)
    treatment_mean = np.mean(treatment)
    control_stddev = np.std(control)
    treatment_stddev = np.std(treatment)
    N1 = len(control)
    N2 = len(treatment)

    #relative_difference = (np.mean(treatment) - np.mean(control)) / np.mean(control)* 10
    observed_t = (treatment_mean - control_mean)/ np.sqrt( (control_stddev)**2/N1 + (treatment_stddev)**2/N2 )

    top =  (control_stddev)**2/N1 + (treatment_stddev)**2/N2 
    bottom = 1/(N1-1)*(control_stddev**2/N1) + 1/(N2-1)*(treatment_stddev**2/N2)

    df = top/bottom

    #calculate the p-value 
    #1-the area under the curve (using, cumulative distribution function)
    
    #one-tailed
    if tails == 1:
        p=(1-t.cdf(observed_t, df))
    else:
    #two tailed
        p=(1-t.cdf(observed_t, df))*2
    
    #critical value can be calculated by using ppf : Percent point function (inverse of cdf — percentiles).
    critical_value = t.ppf(1.0 - alpha/2, df)
    
    return (round(observed_t,3),np.floor(df), round(p,3), round(critical_value,3))

