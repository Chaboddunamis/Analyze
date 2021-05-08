import pandas as pd
import numpy as np
import scipy.stats as stats
from pandas_profiling import ProfileReport



class analyze:
    def __init__(self, data):
        self.data = data
        
        
    def extract_categoricals(self):
        numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
        dataframe = self.data.select_dtypes(exclude=numerics)
        return dataframe.head(20)
        
    def extract_numericals(self):
        numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
        dataset = self.data.select_dtypes(include=numerics)
        return dataset.head(20)
        
    def intro(self):
        
        print('................................................')
        print('Here is the introductory information of your dataset:\n')
        print(self.data.info())  
        print('\n')
        
        
        
        
        print('................................................')
        print("The summary of your dataset's descripive statistics are:\n")
        print(self.data.describe())
        print('\n')
        
        
        
        
        print('................................................')
        print('The shape of your dataset is:\n')
        print(self.data.shape) 
        print('\n')
        
        
        
        
        print('................................................')
        print('The columns of your dataset are:\n')
        print(self.data.columns)  
        print('\n')
        
        
        
        
        print('................................................')
        print('The number of rows of your dataset is:\n')
        print(len(self.data))  
        print('\n')
        
        
        
        
        print('................................................')
        print('The data types of your dataset are:\n')
        print(self.data.dtypes)  
        print('\n')
        
        
        
        print('................................................')
        print('The number of unique/distinct entries in your dataset is:\n')
        print(self.data.nunique()) 
        print('\n')
        
        
        

        
        print('................................................')
        print('These are the missing values in your dataset:\n')
        print(self.data.isna().sum())  
        print('\n')
        
        
        print('................................................')
        print('The first 10 rows of your dataset are:\n')
        print(self.data.head(10))  
        print('\n')
        
        
    
    
    
    def analyze(self):
        minimum = self.data.min()
        tenth_percentile = self.data.quantile(0.1)
        tenth_percentile_without_missing_values = self.data.dropna().quantile(0.1)
        Q1 = self.data.quantile(0.25)
        Q1_without_missing_values = self.data.dropna().quantile(0.25)
        median = self.data.median()
        median_without_missing_values = self.data.dropna().median()
        Q3 = self.data.quantile(0.75)
        Q3_without_missing_values = self.data.dropna().quantile(0.75)
        ninetieth_percentile = self.data.quantile(0.9)
        ninetieth_percentile_without_missing_values = self.data.dropna().quantile(0.9)
        maximum = self.data.max()
        standard_deviation = self.data.std()
        standard_deviation_without_missing_values = self.data.dropna().std()
        variance = self.data.var()
        variance_without_missing_values = self.data.dropna().var()
        mean = self.data.mean()
        mean_without_missing_values = self.data.dropna().mean()
        kurtosis = self.data.kurtosis()
        skew = self.data.skew()
        mode = self.data.mode()
        correlation = self.data.corr()
        
        
       
        print('................................................')
        print('These are the categorical features in your dataset:\n')
        print(analyze.extract_categoricals(self))  
        print('\n')
        
        
        
        
        
        print('................................................')
        print('These are the numerical features in your dataset:\n')
        print(analyze.extract_numericals(self))  
        print('\n')
        
        
        
        
        
        
        print('................................................')
        print('The minimum values for each column in the dataset are:\n')
        print(minimum)  
        print('\n')
        
        
        
        
        
        print('................................................')
        print('The 10th percentile values for each column in the dataset are:\n')
        print(tenth_percentile)  
        print('\n')
    
    
    
    
    
    
        print('................................................')
        print('The 10th percentile values for each column in the dataset without missing values are:\n')
        print(tenth_percentile_without_missing_values)  
        print('\n')
        
        
        
        
        
        
        print('................................................')
        print('The first quartile values of your dataset are:\n')
        print(Q1)  
        print('\n')
        
        
        
        
        
        
        print('................................................')
        print('The first quartile values of your dataset without missing values are:\n')
        print(Q1_without_missing_values)  
        print('\n')
        
        
        
        
        
        print('................................................')
        print('The median values for each column of your dataset are:\n')
        print(median)  
        print('\n')
        
        
        
        
        
        print('................................................')
        print('The median values for each column of your dataset without missing values are:\n')
        print(median_without_missing_values)  
        print('\n')
        
        
        
        
        print('................................................')
        print('The third quartile values for each column of your dataset are:\n')
        print(Q3) 
        print('\n')
        
        
        
        
    
        print('................................................')
        print('The third quartile values for each column of your dataset without missing values are:\n')
        print(Q3_without_missing_values)  
        print('\n')
        
        
        
        
    
        print('................................................')
        print('The 90th percentile values for each column of your dataset are:\n')
        print(ninetieth_percentile)  
        print('\n')
        
        
        
        
        
        print('................................................')
        print('The 90th percentile values for each column of your dataset without missing values are:\n')
        print(ninetieth_percentile_without_missing_values) 
        print('\n')
        
        
        
        
        print('................................................')
        print('The maximum values for each columns of your dataset are:\n')
        print(maximum)  
        print('\n')
        
        
        
        
        
        
        print('................................................')
        print('The standard deviation values for each column of your dataset are:\n')
        print(standard_deviation)  
        print('\n')
        
        
        
        
        
        
        print('................................................')
        print('The standard deviation values for each column of your dataset without missinh values are:\n')
        print(standard_deviation_without_missing_values) 
        print('\n')
        
        
        
        
        
        print('................................................')
        print('The variance values of your dataset are:\n')
        print(variance)  
        print('\n')
        
        
        
        
        
        print('................................................')
        print('The variance values of your dataset without missing values are:\n')
        print(variance_without_missing_values)  
        print('\n')
        
        
        
        print('................................................')
        print('The mean values for each column of your dataset are:\n')
        print(mean)  
        print('\n')
        
        
        
        
        
        print('................................................')
        print('The mean values for each column of your dataset without missing values')
        print(mean_without_missing_values)  
        print('\n')
        
        
        
        
        
        print('................................................')
        print('The kurtosis of your dataset is:\n')
        print(kurtosis)  
        print('\n')
        
        
        
        
        print('................................................')
        print('The skew of your dataset is:\n')
        print(skew) 
        print('\n')
        
        
        
        
        
        print('................................................')
        print('The modal values of your dataset columns are:\n')
        print(mode[:20])  
        print('\n')
        
        
        
        
        print('................................................')
        print('The correlation of your dataset is:\n')
        print(correlation)  
        print('\n')
        
        
        
        interquartile_range = self.data.quantile(0.75) - self.data.quantile(0.25)
        print('................................................')
        print('The interquartile ranges of your dataset columns is:\n')
        print(interquartile_range)  
        print('\n')
        
        
        
        interquartile_range_without_missing_data = self.data.dropna().quantile(0.75) - self.data.dropna().quantile(0.25)
        print('................................................')
        print('The interquartile ranges of your dataset columns without missing data are:\n')
        print(interquartile_range_without_missing_data)  
        print('\n')
        
        
        
        
        coeff_var = (np.std(analyze.extract_numericals(self), ddof=1) / np.mean(analyze.extract_numericals(self))) * 100
        print('................................................')             
        print('The coefficients of variation of your dataset columns are:\n')
        print(coeff_var)  
        print('\n')
        
        
        
    
        coeff_var_without_missing_values = (np.std(analyze.extract_numericals(self).dropna(), ddof=1) / np.mean(analyze.extract_numericals(self).dropna())) * 100
        print('................................................')             
        print('The coefficients of variation of your dataset columns without missing values are:\n')
        print(coeff_var_without_missing_values)  
        print('\n')


        print('Do you want to generate a distribution report of your dataset to properly understand the statistical distributions and assumptions of your data?')
        response = input('[y/n]: ').lower()
        
        if response == 'y' or response == 'yes':
            print("Generating report...", '\n')
            print('Do you want to generate a distribution report for the whole dataset or just a specific column?')
            response = input('[type y for whole or n for specific]: ').lower()
            if response == 'y' or response == 'yes':
                print("Generating report...", '\n')
                for col in analyze.extract_numericals(self).dropna().columns:
                    get_dist(analyze.extract_numericals(self).dropna()[col])
                  
            elif response == 'n' or response == 'specific':
                action = str(input("Type the column you want to analyze as written on the dataset e.g PassengerId:"))
                if action in self.data.columns:
                    print("Generating report...", '\n')
                    get_dist(analyze.extract_numericals(self).dropna()[action])
                
                else:
                    print('Invalid column. Please check the spelling and confirm that the column is in the dataset')
            else:
                  print("Invalid command")
                  
        elif response == 'n' or response == 'no':
                  print("Summarized analysis complete")
        else:
                  print("Summarized analysis complete")

        print('Do you want to generate a detailed report on the exploration of your dataset?')
        response = input('[y/n]: ').lower()

        if response == 'y' or response == 'yes':
            print("Generating report...", '\n')
            prof = ProfileReport(self.data)
            prof.to_file(output_file='report.html')
            print('Your Report has been generated and saved as \'report.html\'')
        elif response == 'n' or response == 'no':
            print('Process Completed')
        else:
            print('Process Completed')



def get_dist(column):
        df = column
        size = len(df)
        chi_square_statistics = []
        stat_bins = np.linspace(0,100,11)
        stat_cutoffs = np.percentile(df, stat_bins)
        visible_freq, bins = (np.histogram(df, bins=stat_cutoffs))
        total_freq = np.cumsum(visible_freq)
        dist_types = ['weibull_min','norm','weibull_max','beta',
              'invgauss','uniform','gamma','expon',   
              'lognorm','pearson3','triang']

        for name in ['weibull_min','norm','weibull_max','beta',
              'invgauss','uniform','gamma','expon',   
              'lognorm','pearson3','triang']:
            dist = getattr(stats, name)
            param = dist.fit(df)
            print("{}\n{}\n".format(dist, param))


            cdf_fit = dist.cdf(stat_cutoffs, *param)
            extant_freq = []
            for bin in range(len(stat_bins)-1):
                cdf_area = cdf_fit[bin+1] - cdf_fit[bin]
                extant_freq.append(cdf_area)


            extant_freq = np.array(extant_freq) * size
            total_extant_freq = np.cumsum(extant_freq)
            ss = sum (((total_extant_freq - total_freq) ** 2) / total_freq)
            chi_square_statistics.append(ss)


        results = pd.DataFrame()
        results['Distribution'] = dist_types
        results['chi_square'] = chi_square_statistics
        results.sort_values(['chi_square'], inplace=True)


        print ('\nDistributions listed by goodness of fit for {}:'.format(column.name))
        print ('............................................')
        print (results)