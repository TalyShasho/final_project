import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
import statsmodels.api as sm



def analyze_music_type_vs_IS(df):
    """
    Analyze the relationship between 'music_type' and 'IS'.

    Parameters:
        df (pd.DataFrame): The input DataFrame containing 'music_type' and 'IS' columns.

    Returns:
        tuple: Correlation value and ANOVA table.
    """
    # 1. Correlation between 'music_type' and 'IS'
    df['music_type_numeric'] = df['music_type'].astype('category').cat.codes  # Convert music_type to numeric
    correlation = df['music_type_numeric'].corr(df['IS'])
    print(f"Correlation between music type and IS: {correlation}")

    # 2. ANOVA test for 'music_type' and 'IS'
    model = ols('IS ~ C(music_type)', data=df).fit()  # Fit the model
    anova_table = sm.stats.anova_lm(model, typ=2)  # Perform ANOVA
    print(anova_table)

    # 3. Graph of IS vs music_type
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='music_type', y='IS', data=df, palette="Set2")
    plt.title('IS by Music Type')
    plt.xlabel('Music Type')
    plt.ylabel('IS')
    plt.xticks(rotation=45)  # Rotate x labels for better visibility if necessary
    plt.show()

    return correlation, anova_table


