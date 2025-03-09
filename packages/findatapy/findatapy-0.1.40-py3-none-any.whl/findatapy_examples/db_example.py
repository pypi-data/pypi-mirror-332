
from findatapy.util import DataConstants

databento_api_key = DataConstants().databento_api_key
import databento as db

client = db.Historical(databento_api_key)

# RYZ4 and RPZ4 (EURJPY and EURGBP futures respectively)

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    symbols=["RYZ4", "RPZ4"],
    schema="ohlcv-1d",
    start="2024-10-01T00:00:00",
    end="2024-11-08T00:10:00",
    # limit=1,
)
df = data.to_df()
df = df.set_index('symbol', append=True).unstack(level='symbol')
fields = df.columns.levels[0]
tickers = df.columns.levels[1]

new_cols = []

for fi in fields:
    for ti in tickers:
        new_cols.append(ti + "." + fi)

df.columns = new_cols
df.index.name = "Date"

print(df)


print(df.iloc[0].to_json(indent=4))