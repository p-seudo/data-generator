import pandas as pd
from random import randint
import numpy as np
import argparse
from datetime import datetime, timedelta
import os


items = pd.read_csv('raw/raw_item.csv')
dc = pd.read_csv('raw/raw_dist.csv')
retailers = pd.read_csv('raw/raw_retailer.csv')

parser = argparse.ArgumentParser(prog='generator', description='Generates data for the given period, one file for each distributor')
parser.add_argument('-p', '--period')
args = parser.parse_args()
period = args.period.split('-')
month,year = int(period[0]),int(period[1])
input_month, input_year = month, year
start_date = datetime(input_year, input_month, 1)
end_date = datetime(input_year, input_month + 1, 1) - timedelta(days=1)
if not os.path.exists('sales_files'):
    os.makedirs('sales_files')
for city in dc['city_name'].unique():
    for _,dist in dc[dc['city_name']==city].iterrows():
        filtered_retailers = retailers[retailers['retailer_city']==city]
        for n in range((end_date - start_date).days + 1):
            current_date = start_date + timedelta(n)
            for _,row in filtered_retailers.iterrows():
                k = randint(1,len(items))
                sample_items = items.sample(n=k)
                sample_items['retailer_code'] = pd.Series(row['retailer_code']*sample_items.shape[0])
                sample_items['retailer_name'] = pd.Series(row['retailer_name']*sample_items.shape[0])
                sample_items['retailer_category'] = pd.Series(row['retailer_category']*sample_items.shape[0])
                sample_items['retailer_city'] = pd.Series(row['retailer_city']*sample_items.shape[0])
                sample_items['retailer_address'] = pd.Series(row['retailer_address']*sample_items.shape[0])
                sample_items['distributor_code'] = pd.Series(dist['distributor_code']*sample_items.shape[0])
                sample_items['dist_address'] = pd.Series(dist['dist_address']*sample_items.shape[0])
                sample_items['dc_code'] = pd.Series(dist['dc_code']*sample_items.shape[0])
                sample_items['dc_name'] = pd.Series(dist['dc_name']*sample_items.shape[0])
                sample_items['dc_address'] = pd.Series(dist['dc_address']*sample_items.shape[0])
                sample_items['city_name'] = pd.Series(dist['city_name']*sample_items.shape[0])
                total_cases = np.random.randint(1, 100, sample_items.shape[0])
                sample_items['total_cases'] = total_cases
            sample_items['date'] = [current_date]*sample_items.shape[0]
        if not os.path.exists(f"{dist.dc_code}"):
            os.makedirs(f"sales_files/{dist.dc_code}")
        sample_items.to_csv(f"sales_files/{dist.dc_code}/{current_date.strftime('%m%Y')}.csv",index=False)

