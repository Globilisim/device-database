import pandas as pd
import json
import requests

# Google'ın resmi listesi
url = "https://storage.googleapis.com/play_public/supported_devices.csv"

# Listeyi indirip okuyalım
df = pd.read_csv(url, encoding='utf-16')

# Türkiye'de popüler olan markalar
popular_brands = ['Samsung', 'Oppo', 'Vivo', 'Realme', 'Infinix', 'Tecno', 'Casper', 'General Mobile', 'Reeder', 'Xiaomi', 'POCO', 'Redmi']

# Filtreleme yapalım
filtered_df = df[df['Retail Branding'].isin(popular_brands)]

devices = []
for _, row in filtered_df.iterrows():
    devices.append({
        "brand": str(row['Retail Branding']),
        "codename": str(row['Device']),
        "model": str(row['Model']),
        "marketName": str(row['Marketing Name'])
    })

data = {
    "lastUpdated": pd.Timestamp.now().strftime("%Y-%m-%d"),
    "devices": devices
}

# JSON olarak kaydedelim
with open('universal-devices.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("İşlem başarıyla tamamlandı, JSON güncellendi.")
