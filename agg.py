import pandas as pd

top10 = pd.read_csv('Data/global_0703.csv', parse_dates=['week'])

def create_agg_week(top10):
    agg_week = top10[['week', 'weekly_hours_viewed']].groupby('week').sum()
    agg_week.to_csv('Data/agg_week.csv')
    

def create_agg_category(top10):
    agg_category = top10[['week', 'category', 'weekly_hours_viewed']].groupby(['week', 'category']).sum()
    agg_category.to_csv('Data/agg_category.csv')


def main():
    create_agg_week(top10)
    create_agg_category(top10)


if __name__ == '__main__':
    main()
