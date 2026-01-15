# %%
import pandas as pd
import requests
import numpy as np
from bs4 import BeautifulSoup
import yfinance
import os
import pygsheets
from decimal import Decimal, ROUND_HALF_UP
import locale
from datetime import datetime, timedelta
import json
import datawrapper
import time
import io
#https://github.com/patrickloeber/python-github-action-template?tab=readme-ov-file
# Set the locale to English (United States)
locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')
#authorization
if "PYGSHEET" in os.environ:

    AUTH_DATA = os.environ["PYGSHEET"]
    whatever_json=json.loads(AUTH_DATA, strict=False)
    credentials = whatever_json

    gc = pygsheets.authorize(service_account_json=(json.dumps(whatever_json))
    )
else:

    gc = pygsheets.authorize(service_file='/Users/halukamaier-borst/Documents/trumptracker-459020-5b428916efa8.json')



# %%

# Get today's date
today = datetime.now()

# Get date 365 days ago
date_365_days_ago = today - timedelta(days=365)

# Format as string if needed
date_365_days_ago_str = date_365_days_ago.strftime("%Y-%m-%d")

print(date_365_days_ago_str)
today

# %%

GoldPrice = yfinance.download (tickers = "GC=F", start = date_365_days_ago_str, 
                              interval = "1d")
GoldPrice

# %%
msci_world = yfinance.download (tickers = "^990100-USD-STRD", start = date_365_days_ago_str, 
                              interval = "1d")
msci_world

# %%
bitcoin = yfinance.download (tickers = "BTC-USD", start = date_365_days_ago_str, 
                              interval = "1d")
bitcoin

# %%
def reduce_index(df,indexname):
    index_red=pd.DataFrame()
    df["Date"]=df.index
    index_red["Date"]=df["Date"]

    index_red[indexname]=df[df.columns[0]]

    index_red=index_red.reset_index(drop=True)
    return index_red


# %%
gold_red=reduce_index(GoldPrice,"GOLD")
msci_world_red=reduce_index(msci_world,"MSCI_WORLD")
bitcoin_red=reduce_index(bitcoin,"BITCOIN")
bitcoin_red

# %%
gold_msci=pd.merge(gold_red, msci_world_red, on="Date", how="outer")
gold_msci=gold_msci.fillna(method="ffill")
gold_msci

# %%
gold_msci_bitcoin=pd.merge(gold_msci, bitcoin_red, on="Date", how="outer")
gold_msci_bitcoin=gold_msci_bitcoin.fillna(method="ffill")
today_str=today.strftime("%Y-%m-%d")

gold_msci_bitcoin_without_today=gold_msci_bitcoin[gold_msci_bitcoin["Date"]!=today_str]
gold_msci_bitcoin_without_today=gold_msci_bitcoin_without_today.dropna()
gold_msci_bitcoin_without_today

# %%
for col in gold_msci_bitcoin_without_today.columns[1:]:
    gold_msci_bitcoin_without_today[col]= gold_msci_bitcoin_without_today[col].apply(lambda x: Decimal(str(x)))

    # Example: Perform precise rounding on the Decimal column
    gold_msci_bitcoin_without_today[col]= gold_msci_bitcoin_without_today[col].apply(lambda x: x.quantize(Decimal('1'), rounding=ROUND_HALF_UP))
gold_msci_bitcoin_without_today

# %%
gold_msci_bitcoin_without_today.to_csv("sofar.csv", index=False)

# %%
def retrieve_from_investing(index):
    index_to_shortform_dict={"MSCI_WORLD":"indices/msci-world-historical-data","GOLD":"commodities/gold-historical-data","BITCOIN":"crypto/bitcoin/historical-data"}
    now = datetime.now()
    formatted_date = now.strftime("%m/%d/%Y")
    index_shortform=index_to_shortform_dict[index]


    url=f"https://www.investing.com/{index_shortform}#:~:text=Daily-,Download,-{formatted_date}"
    print(url)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    response = requests.get(url, headers=headers)



    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the first table on the page
        table = soup.find('table', class_="freeze-column-w-1 w-full overflow-x-auto text-xs leading-4")

        # Extract rows from the table
        rows = table.find_all('tr')

        # Extract data from each row
        table_data = []
        for row in rows:
            cells = row.find_all(['td', 'th'])  # Get all cells (both <td> and <th>)
            cell_data = [cell.get_text(strip=True) for cell in cells]  # Extract text
            table_data.append(cell_data)

        # Return the extracted table data
        return(table_data)
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

# %%
filepath = "https://www.cryptodatadownload.com/cdd/Binance_BTCUSDT_d.csv"


# Now we want to create a dataframe and use Pandas' to_csv function to read in our file
df = pd.read_csv(filepath, skiprows=1)  # we use skiprows parameter because first row contains our web address

# Now that we have loaded our data into the dataframe, we can preview it using the print & .head() function
df_red=df[["Date","Close"]]
df_red["Date"]=pd.to_datetime(df_red["Date"])
df_red["Close"]=df_red["Close"].apply(lambda x: Decimal(str(x)))
df_red=df_red.dropna(how="all")
crosscheck_data_red=df_red
crosscheck_data_red=crosscheck_data_red.dropna(subset=["Date"])
crosscheck_data_red.columns=["Date","Bitcoin"+"check"]
crosscheck_data_red

# %%
df_to_check=gold_msci_bitcoin_without_today.copy()
columns_to_round = ['GOLD','MSCI_WORLD','BITCOIN']
    
# Apply Decimal rounding to the specified columns
df_to_check[columns_to_round] = df_to_check[columns_to_round].applymap(lambda x: Decimal(str(x)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

for index_name in gold_msci_bitcoin_without_today.columns[1:]:
    print(index_name)
    if index_name!="BITCOIN":
        array=retrieve_from_investing(index_name)
        crosscheck_data=pd.DataFrame(array)
        crosscheck_data.replace("",np.nan,inplace=True)
        crosscheck_data=crosscheck_data.dropna(how="all")
        crosscheck_data[0]=pd.to_datetime(crosscheck_data[0], format="%b %d, %Y", errors="coerce")
        crosscheck_data_red=crosscheck_data[[0,1]]
        crosscheck_data_red=crosscheck_data_red.dropna(subset=[0])
        crosscheck_data_red.columns=["Date",index_name+"check"]
        crosscheck_data_red=crosscheck_data_red.sort_values(by="Date", ascending=True)
        crosscheck_data_red[index_name+"check"]=crosscheck_data_red[index_name+"check"].str.replace(",","")
        crosscheck_data_red[index_name+"check"]=crosscheck_data_red[index_name+"check"].astype(float)
        crosscheck_data_red[index_name+"check"]= crosscheck_data_red[index_name+"check"].apply(lambda x: Decimal(str(x)))
    else:
        filepath = "https://www.cryptodatadownload.com/cdd/Binance_BTCUSDT_d.csv"


        # Now we want to create a dataframe and use Pandas' to_csv function to read in our file
        df = pd.read_csv(filepath, skiprows=1)  # we use skiprows parameter because first row contains our web address

        # Now that we have loaded our data into the dataframe, we can preview it using the print & .head() function
        df_red=df[["Date","Close"]]
        df_red["Date"]=pd.to_datetime(df_red["Date"])
        df_red["Close"]=df_red["Close"].apply(lambda x: Decimal(str(x)))
        df_red=df_red.dropna(how="all")
        crosscheck_data_red=df_red
        crosscheck_data_red=crosscheck_data_red.dropna(subset=["Date"])
        crosscheck_data_red.columns=["Date","BITCOINcheck"]
        crosscheck_data_red
    # Example: Perform precise rounding on the Decimal column
    crosscheck_data_red[index_name+"check"] = crosscheck_data_red[index_name+"check"].apply(lambda x: x.quantize(Decimal('1'), rounding=ROUND_HALF_UP))
    print("crosscheckdata")
    print(crosscheck_data_red.tail(5))
    print("df_to_check")

    print(df_to_check.tail(5))

#    df_to_check=pd.merge(df_to_check,crosscheck_data_red, on="Date", how="outer", suffixes=["_raw","_crosscheck"])

    df_to_check=pd.merge(df_to_check,crosscheck_data_red, on="Date", how="outer", suffixes=["_raw","_crosscheck"])
df_to_check=df_to_check.fillna(method="ffill")
df_to_check


# %%
for index_name in gold_msci_bitcoin_without_today.columns[1:]:

    df_to_check[index_name+"overlap"]=df_to_check[index_name]/df_to_check[index_name+"check"]
df_to_check

# %%
overlap_cols=df_to_check.columns[df_to_check.columns.str.contains("overlap")]
overlap_cols

# %%
df_enough_overlap=df_to_check[((df_to_check[overlap_cols]>0.99) & (df_to_check[overlap_cols]<1.01)).all(axis=1)]
df_enough_overlap

# %%
checked_df_red=df_enough_overlap[df_enough_overlap.columns[:4]]
checked_df_red["Date"]=checked_df_red["Date"].dt.strftime("%Y-%m-%d")
checked_df_red

# %%
#Open the google spreadsheet
sh = gc.open('TrumptrackerRaw')
sheet_name = "Assets"  # Replace with the name of the sheet you want to select
wks = sh.worksheet_by_title(sheet_name)


#Get the data from the Sheet into python as DF
read_indices = wks.get_as_df()
read_indices_red=read_indices[read_indices.columns[:4]]
read_indices_red

# %%
read_plus_new_checked=pd.concat([read_indices_red,checked_df_red], axis=0, ignore_index=True)

read_plus_new_checked.drop_duplicates(subset=["Date"], keep="first", inplace=True)
read_plus_new_checked.reset_index(drop=True, inplace=True)
read_plus_new_checked

# %%
read_plus_new_checked["Date"]=pd.to_datetime(read_plus_new_checked["Date"])
read_plus_new_checked=read_plus_new_checked[read_plus_new_checked["Date"]>date_365_days_ago]
read_plus_new_checked.sort_values(by="Date", ascending=True, inplace=True)
read_plus_new_checked

# %%
def converter_perc(index_name):
    df_perc=pd.DataFrame()
    df_perc["Date"]=read_plus_new_checked["Date"]
    col_important=read_plus_new_checked[index_name]
    base_value=col_important.iloc[0]
    df_perc[index_name+"_perc"]=(col_important-base_value)*100/base_value
    df_perc[index_name+"_perc"] = df_perc[index_name+"_perc"].apply(lambda x: float(Decimal(str(x)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)))

    return(df_perc)

# %%
for col in read_plus_new_checked.columns[1:]:
    df_perc=converter_perc(col)
    read_plus_new_checked=pd.merge(read_plus_new_checked,df_perc,on="Date",how="outer",suffixes=["_abs","_perc"])
read_plus_new_checked 

# %%



#open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
sh = gc.open('TrumptrackerRaw')

sheet_name = "Assets"  # Replace with the name of the sheet you want to select
wks = sh.worksheet_by_title(sheet_name)

wks.set_dataframe(read_plus_new_checked,(0,0))


# %%
if "DWKEY" in os.environ:

    DWKEY = os.environ["DWKEY"]
    print(len(DWKEY))


else:
    data=pd.read_csv("/Users/halukamaier-borst/Documents/Keys.csv")
    DWKEY=data.APIKey.iloc[1]

# %%
dw_connection = datawrapper.Datawrapper(access_token = DWKEY)
allcharts=dw_connection.get_charts(limit=500)

dw_connection.publish_chart(chart_id="NH3ER")

# %%



