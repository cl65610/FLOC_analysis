import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

math_df = pd.read_csv('https://raw.githubusercontent.com/cl65610/FLOC_analysis/master/Data/math.csv')
demo_df = pd.read_csv('https://raw.githubusercontent.com/cl65610/FLOC_analysis/master/Data/demo_info.csv')
# Get rid of that unnecessary first column
math_df.drop('Unnamed: 0', axis=1, inplace=True)

# Rename the math_df columns to be more useful and malleable
math_df.columns
math_cols = ['name', 'date_pre_test', 'start_grade', 'date_post_test', 'end_grade',
            'calc_pre', 'calc_diff_pre', 'calc_post', 'calc_diff_post', 'calc_improve',
            'calc_gc', 'fluency_pre', 'fluency_diff_pre', 'fluency_post', 'fluency_diff_post',
            'fluency_improve', 'fluency_gc', 'avg_pre', 'avg_diff_pre', 'avg_post',
            'avg_diff_post', 'avg_improve', 'avg_gc', 'hrs_received']
math_df.columns = math_cols

#Rename the demo columns
demo_cols = ['name', 'grade', 'income', 'program', 'ward', 'first_gen', 'ethnicity',
            'free_and_reduced', 'highest_edu']
demo_df.columns = demo_cols

# Merge the two dataframes together

math_merged = math_df.merge(demo_df, how = 'left', left_on='name', right_on='name')

# Remap the ethnicity values so they can be graphed

ethnicities = {'Hispanic/Latino':'Hispanic', 'African American/Black':'African American',
                'Black/African American (non Hispanic)':'African American', 'Multi-racial':'Multi-racial',
                'Other':'Other'}

math_merged.ethnicity = math_merged.ethnicity.map(ethnicities)
math_merged.columns
plt.style.use('seaborn-bright')
sns.pairplot(data = math_merged, x_vars = ['calc_diff_pre', 'fluency_diff_pre',
                                            'avg_diff_pre', 'hrs_received', 'grade',
                                             'ward'],
                                y_vars = ['calc_improve', 'calc_gc', 'fluency_improve',
                                            'fluency_gc', 'avg_improve', 'avg_gc'], kind = 'reg')
plt.savefig('math_pairplot.png')


sns.jointplot(data = math_merged, x = 'hrs_received', y= 'avg_improve')

print plt.style.available
