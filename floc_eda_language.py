import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

language_df = pd.read_csv('language.csv')
demo_df = pd.read_csv('demo_info.csv')
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
