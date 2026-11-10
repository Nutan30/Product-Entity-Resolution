import re
import pandas as pd
import numpy as np


def clean_text(text):
    if pd.isnull(text):
        return ""

    text = str(text).lower()
    text = re.sub(r"<[^>]*(>|$)", " ", text)
    text = re.sub(r"&[a-z]+;", " ", text)
    text = text.replace("&", " and ")
    text = text.replace("'", "")


    text = re.sub(r"[^a-z0-9.\s]", " ", text)
    text = re.sub(r"(?<!\d)\.|\.(?!\d)", " ", text)

    text = re.sub(r"\s+", " ", text).strip()
    return text

def clean_price(price):
    if pd.isnull(price):
        return np.nan

    price = re.sub(r"[^0-9.]", "", str(price))
    if price == "":
        return np.nan

    try:
        value = float(price)
    except ValueError:
        return np.nan

    if value == 0:
        return np.nan
    return value

def clean_amazon(df):
    df = df.copy()
    df["name_clean"] = df["title"].apply(clean_text)
    df["desc_clean"] = df["description"].apply(clean_text)
    df["manu_clean"] = df["manufacturer"].apply(clean_text)
    df["price_clean"] = df["price"].apply(clean_price)
    return df

def clean_google(df):
    df = df.copy()
    df["name_clean"] = df["name"].apply(clean_text)
    df["desc_clean"] = df["description"].apply(clean_text)
    df["manu_clean"] = df["manufacturer"].apply(clean_text)
    df["price_clean"] = df["price"].apply(clean_price)
    return df