import pandas as pd
import numpy as np

df_testing_raw = pd.read_excel("C://Users//Matthew//Documents//Fall_2022//ISDS_7103//project_dataset.xlsx", sheet_name=2)

## Fix the origin column

def origin():
    origin_list = []
    Europe = ["Europe","europäisch"]
    US = ["U.S.","US","USA","Detroit"]
    Asia = ["Japan","Nippon"]

    ## Since all others are American cars, I simply use an else statement to change these all to "US".
    ## IF there were others that were coded as blank or ?, I would have altered the code to accommodate such cases.

    # other = ["?", None]
    # American_makers = ["GM", "Ford"]
    for i in df_testing_raw["origin"]:
        if i in Europe:
            origin_list.append("Europe")
        elif i in US:
            origin_list.append("US")
        elif i in Asia:
            origin_list.append("Asia")
        else:
            origin_list.append("US")

    return origin_list

df_testing_raw["origin"] = origin()

# print(df_testing_raw["origin"].head())


def year():
    year_list = []
    messy = [777]
    messy_yr = [1985,1987,1990]
    for i in df_testing_raw["yr"]:
        if i in messy:
            year_list.append(77)
        elif i in messy_yr:
            i = i - 1900
            year_list.append(i)
        else:
            year_list.append(i)

    return year_list

df_testing_raw["yr"] = year()

# print(df_testing_raw["yr"].head())

## Fixing the cylinders


correct_cyl = [3,4,5,6,8,12]
messy_cyl = []
for i in df_testing_raw["cyl"]:
    if i not in correct_cyl:
        messy_cyl.append(i)

# print(messy_cyl)
## Copy and paste values in the messy_cyl list into the function below

def cyl():
    messy_cyl = [444, 5, 'vier', 5, 'Eight', 'quattro', 5, 5, 'acht', 'sechs', 888, 5, 'four', 3, 5, 'quartre', 3, 3, 5, 'four', 3, 5]
    fours = [444,"four","quattro","quartre","vier"]
    sixes = ["sechs"]
    eights = ["Eight",888,"acht"]
    cyl_list = []
    for i in df_testing_raw["cyl"]:
        if i in messy_cyl:
            if i in fours:
                cyl_list.append(4)
            elif i in sixes:
                cyl_list.append(6)
            elif i in eights:
                cyl_list.append(8)
            else:
                cyl_list.append(i)
        else:
            cyl_list.append(i)

    return cyl_list

df_testing_raw["cyl"] = cyl()


def auto():
    auto_list = []
    for i in df_testing_raw["auto"]:
        if i == "manual":
            auto_list.append(0)
        else:
            auto_list.append(i)

    return auto_list

df_testing_raw["auto"] = auto()


## Recode the AC column to 0s and 1s

def ac():
    ac_list = []
    yes = ["O","yes"]
    no = ["X","no","none","nil"]
    for i in df_testing_raw["a/c"]:
        if i in no:
            ac_list.append(0)
        elif i in yes:
            ac_list.append(1)

    return ac_list

df_testing_raw["a/c"] = ac()

def fro():
    fro_list = []
    for i in df_testing_raw["fro"]:
        if i == "no":
            i = 0
            fro_list.append(i)
        elif i == "yes" or "Yes":
            i = 1
            fro_list.append(i)
        else:
            fro_list.append(i)

    return fro_list

df_testing_raw["fro"] = fro()



def weight():
    weight_list = []
    unknown = ["unknown","?"]
    strings = ["32k","3*1000"]
    for i in df_testing_raw["wght"]:
        if i in strings:
            if i == strings[0]:
                weight_list.append(3200)
            elif i == strings[1]:
                weight_list.append(3000)
            else:
                weight_list.append(i)
        elif i in unknown:
           if i == "unknown":
               weight_list.append(1999)
           elif i == "?":
                weight_list.append(1753)
           else:
               weight_list.append(i)
        else:
            weight_list.append(i)

    return weight_list


df_testing_raw["wght"] = weight()

# print(weight())

## Hard coding in the missing disp values - googled the cars' info

def disp():
    disp_list = []
    for i in df_testing_raw["disp"]:
        if i == "missing":
            i = 351.9
            disp_list.append(i)
        elif i == 'blank':
            i = 97.5
            disp_list.append(i)
        else:
            disp_list.append(i)

    return disp_list

df_testing_raw["disp"] = disp()



## Hard coding in the missing hp values - googled the cars' info

def hp():
    hp_list = []
    for i in df_testing_raw["hp"]:
        if i == "unknown":
            i = 228
            hp_list.append(i)
        elif i == 'blank':
            i = 98
            hp_list.append(i)
        else:
            hp_list.append(i)

    return hp_list

df_testing_raw["hp"] = hp()


## hard-coding in length based on googled values
def length():
    len_list = []
    for i in df_testing_raw["lngth"]:
        if i == 'blank':
            i = 199.8
            len_list.append(i)
        elif i == '?':
            i = 161.1
            len_list.append(i)
        else:
            len_list.append(i)

    return len_list

df_testing_raw["lngth"] = length()


## Hard-coding width using google
def width():
    wdth_list = []
    for i in df_testing_raw["wdth"]:
        if i == '?':
            i =79.5
            wdth_list.append(i)
        elif i == 'blank':
            i = 69.6
            wdth_list.append(i)
        else:
            wdth_list.append(i)

    return wdth_list

df_testing_raw["wdth"] = width()




## Hard coding in the one missing wb value - googled the car's info

def wb():
    wb_list = []
    for i in df_testing_raw["wb"]:
        if i == "missing":
            wb_list.append(100.5)
        else:
            wb_list.append(i)

    return wb_list

df_testing_raw["wb"] = wb()

def reli():
    reli_list = []
    messy_reli = ["**","***","five","two"]
    fixed_reli = [2,3,5,2]

    ## Is there a way to automatically iterate through the indexes of these lists?
    ## I hard-coded in the indexes with 4 di

    for i in df_testing_raw["reli"]:
        if i in messy_reli:
            if i == messy_reli[0]:
                i = fixed_reli[0]
                reli_list.append(i)
            elif i == messy_reli[1]:
                i = fixed_reli[1]
                reli_list.append(i)
            elif i == messy_reli[2]:
                i = fixed_reli[2]
                reli_list.append(i)
            elif i == messy_reli[3]:
                i = fixed_reli[3]
                reli_list.append(i)
        else:
            reli_list.append(i)

    return reli_list

# print(reli())

df_testing_raw["reli"] = reli()

## Fixing domestic


conditions = [(df_testing_raw["origin"] == "US"),
                  (df_testing_raw["origin"] != "US")]
values = [1,0]
df_testing_raw["dom"] = np.select(conditions,values)

# df_testing_raw["dom"].info()

conditions = [(df_testing_raw["origin"] == "Europe"),
                  (df_testing_raw["origin"] != "Europe")]
values = [1,0]
df_testing_raw["eur"] = np.select(conditions,values)


## What's left? sales, price, and markup

## There is one record that is missing sales. Can we predict sales based on the other features?
## For now, let's replace the sales with the median.

# median = df_testing_raw.median()
# print(median)
# df_testing_raw["sales"][df_testing_raw["sales"] == "?"] = np.nan
# median = df_testing_raw["sales"].median()
# print(median)

sales_list = []
for i in df_testing_raw["sales"]:
    if i == "?":
        sales_list.append(55500)
    else:
        sales_list.append(i)

df_testing_raw["sales"] = sales_list
# print(df_testing_raw["sales"].head(280))

price_list = []
messy_price = ["$50k","???","$38k"]
for i in df_testing_raw["price"]:
    if i in messy_price:
        if i == messy_price[0]:
            price_list.append(50000)
        elif i == messy_price[2]:
            price_list.append(38000)
        else:
            price_list.append(11159.97)
    else:
        price_list.append(i)

df_testing_raw["price"] = price_list


def markup():
    markup_list = []
    for i in df_testing_raw["markup"]:
        if i == "$6k":
            i = 6
            markup_list.append(i)
        elif i == "$2,500":
            i = 2.5
            markup_list.append(i)
        elif i == 2500:
            i = 2.5
            markup_list.append(i)
        else:
            markup_list.append(i)

    return markup_list

df_testing_raw["markup"] = markup()



## dropping the fid column

df_testing_raw.drop(labels='fid',axis=1,inplace=True)





df_testing_raw.info()


df_testing_clean = df_testing_raw.to_excel("df_testing_cleaned.xlsx")



