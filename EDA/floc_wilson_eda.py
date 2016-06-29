import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

# Read in the data and clean up the columns
wilson_df = pd.read_csv('https://raw.githubusercontent.com/cl65610/FLOC_analysis/master/Data/wilson.csv')
demo_df = pd.read_csv('https://raw.githubusercontent.com/cl65610/FLOC_analysis/master/Data/demo_info.csv')
wilson_cols = [ 'name', 'pre_test_date', 'start_grade',
                'post_test_date', 'end_grade', 'wa_pre_score', 'wa_pre_diff',
                'wa_post_score', 'wa_post_diff', 'wa_improve', 'wa_gc', 'id_pre',
                'id_pre_diff', 'id_post', 'id_post_diff', 'id_improve', 'id_gc',
                'pc_pre', 'pc_pre_diff', 'pc_post', 'pc_post_diff', 'pc_improve',
                'pc_gc', 'hrs_received']
wilson_df.columns = wilson_cols
demo_cols = ['name', 'grade', 'income', 'program', 'ward', 'first_gen', 'ethnicity',
            'free_and_reduced', 'highest_edu']
demo_df.columns = demo_cols


#Merge the demogrpahic info with the wilson testing data
wilson_merged = wilson_df.merge(demo_df, how = 'left', left_on='name', right_on='name')

# Remap the ethnicity values to be more graph friendly
ethnicities = {'Hispanic/Latino':'Hispanic', 'African American/Black':'African American',
                'Black/African American (non Hispanic)':'African American', 'Multi-racial':'Multi-racial',
                'Other':'Other', 'Asian/Pacific Islander': 'Asian'}
wilson_merged.ethnicity = wilson_merged.ethnicity.map(ethnicities)
wilson_merged.ethnicity.value_counts()


sns.pairplot(data = wilson_merged, x_vars = ['wa_pre_diff', 'id_pre_diff', 'pc_pre_diff',
                                                'hrs_received'],
                                    y_vars = ['wa_improve', 'wa_gc', 'id_improve', 'id_gc',
                                            'pc_improve', 'pc_gc'], kind='reg')
plt.savefig('wilson_pairplot.png')

sns.jointplot(data = wilson_merged, x='hrs_received', y='id_improve')

from sklearn.preprocessing import LabelEncoder
encode columns = ['first_gen', 'ethnicity', 'free_and_reduced', 'highest_edu']
wilson_merged.columns
sns.barplot(x='income', y='pc_gc', data = wilson_merged)

wilson_merged.income.value_counts()
