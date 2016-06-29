import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

language_df = pd.read_csv('https://raw.githubusercontent.com/cl65610/FLOC_analysis/master/Data/language.csv')
demo_df = pd.read_csv('https://raw.githubusercontent.com/cl65610/FLOC_analysis/master/Data/demo_info.csv')
language_df.columns
language_cols = ['ethnicity', 'name', 'pre_test_date', 'start_grade',
                'post_test_date', 'end_grade', 'wa_pre_score', 'wa_pre_diff',
                'wa_post_score', 'wa_post_diff', 'wa_improve', 'wa_gc', 'id_pre',
                'id_pre_diff', 'id_post', 'id_post_diff', 'id_improve', 'id_gc',
                'pc_pre', 'pc_pre_diff', 'pc_post', 'pc_post_diff', 'pc_improve',
                'pc_gc', 'hrs_received']

language_df.columns = language_cols
language_df.head()

demo_df.columns


demo_cols = ['name', 'grade', 'income', 'program', 'ward', 'first_gen', 'ethnicity',
            'free_and_reduced', 'highest_edu']
demo_df.columns = demo_cols
language_df[language_df.name == 'Anya Blakney']
demo_df[demo_df.name == 'Anya Blakney']
# Merge the demographic column with the language curriculum data
lan_merged = language_df.merge(demo_df, how = 'left', left_on='name', right_on='name')

lan_merged.columns
value_cols = ['wa_post_diff', 'wa_improve', 'wa_gc', 'id_improve', 'id_gc', 'pc_improve',
                'pc_gc']
plt.style.use('ggplot')
sns.pairplot(lan_merged, x_vars = ['hrs_received', 'grade'], y_vars = value_cols)
plt.savefig('pairplot.png')

sns.swarmplot(data = lan_merged, x = 'ethnicity_y', y='pc_improve', hue='grade')

lan_merged.id_improve.mean()
lan_merged.hrs_received.mean()

sns.jointplot(lan_merged.wa_improve, lan_merged.pc_improve)

plot = sns.swarmplot(data = lan_merged, x='ethnicity_y', y='wa_improve', hue='first_gen')
plt.xticks(rotation=30)
plt.show()


lan_merged.ethnicity_y.value_counts()
# Map more simple ethnicity values onto the appropriate column
ethnicities = {'Hispanic/Latino':'Hispanic', 'African American/Black':'African American',
                'Black/African American (non Hispanic)':'African American', 'Multi-racial':'Multi-racial',
                'Other':'Other'}
lan_merged.ethnicity_y = lan_merged.ethnicity_y.map(ethnicities)
lan_merged.ethnicity_y.value_counts()

sns.barplot(x='ethnicity_y', y='wa_improve', data = lan_merged)

g = sns.PairGrid(lan_merged[lan_merged.ethnicity_y != 'Other'], x_vars = 'ethnicity_y', y_vars = ['wa_improve', 'id_improve', 'pc_improve'], size = 6)
g.map(sns.barplot, palette = 'Set2')
plt.xticks(rotation=25)
plt.xlabel('Ethnicity')
plt.title('Average Improvement by Ethnicity')
plt.savefig('ethnicity_and_lang.png')


sns.pairplot(data = lan_merged, x_vars = ['wa_pre_diff', 'id_pre_diff', 'pc_pre_diff',
                                        'hrs_received'],
                                y_vars = ['wa_improve', 'wa_gc', 'id_improve', 'id_gc',
                                        'pc_improve', 'pc_gc'], kind='reg')
plt.savefig('lan_pairplot.png')

# Do the number of hours of tutoring someone receieves have a significant effect on their performance
sns.jointplot(data = lan_merged[lan_merged.hrs_received >=20], x='hrs_received', y='id_improve')
sns.jointplot(data = lan_merged[lan_merged.hrs_received <=20], x='hrs_received', y='id_improve')
sns.jointplot(data = lan_merged[lan_merged.wa_pre_diff >=-3], x='hrs_received', y = 'pc_improve')
