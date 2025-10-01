import pandas as pd
import matplotlib.pyplot as plt

data_dict = {
    "Imię": ["Anna", "Piotr", "Kasia"],
    "Wiek": [25, 30, 22],
    "Miasto": ["Warszawa", "Kraków", "Gdańsk"]
}

df_dict = pd.DataFrame(data_dict)
df_dict

df_csv = pd.read_csv("data.csv")
df_csv

data_list = [
    ["Anna", 25, "Warszawa"],
    ["Piotr", 30, "Kraków"],
    ["Kasia", 22, "Gdańsk"]
]

df_list = pd.DataFrame(data_list, columns=["Imię", "Wiek", "Miasto"])
print(df_list)

df_transposed = df_list.T
print(df_transposed.head(10))

print("Pierwsze 10 wierszy:")
print(df_csv.head(10))

print("\nOstatnie 10 wierszy:")
print(df_csv.tail(10))

print("\nInformacje o ramce danych:")
print(df_csv.info())

print("\nLiczba wierszy i kolumn:")
print(df_csv.shape)

print("\nStatystyki kolumn liczbowych:")
print(df_csv.describe())

print("\nStatystyki kolumn kategorycznych:")
print(df_csv.describe(include=['object']))

print("\nUsunięcie brakujących wartości:")
df_no_na = df_csv.dropna()
print(df_no_na)

print("\nWybór pojedynczej kolumny po nazwie:")
print(df_csv["location_name"])

print("\nWybór wielu kolumn po nazwach:")
print(df_csv[["sex_id", "measure_name"]])

print("\nWybór pojedynczego wiersza po indeksie (iloc):")
print(df_csv.iloc[0])

print("\nWybór wielu wierszy po indeksach (iloc):")
print(df_csv.iloc[0:2])

print("\nWybór konkretnego wiersza i kolumny (iloc):")
print(df_csv.iloc[0, 1])

print("\nWybór konkretnego wiersza i kolumny (loc) po nazwach:")
print(df_csv.loc[0, "location_name"])

print("\nWiersze, gdzie sex_id = 1:")
print(df_csv[df_csv["sex_id"] == 1])


print("\nWiersze, gdzie location_name zawiera 'China' i sex_name == 'Male':")
print(df_csv[df_csv["location_name"].str.contains("China") & (df_csv["sex_name"] == "Male")])

print("\nWiersze, gdzie location_name zawiera 'China':")
print(df_csv[df_csv["location_name"].str.contains("China")])

print("\nWiersze, gdzie location_name nie zawiera 'China':")
print(df_csv[~df_csv["location_name"].str.contains("China")])

df_csv["sex_id_plus_1"] = df_csv["sex_id"] + 1
print(df_csv.head())

df_csv = df_csv.drop(columns=["sex_id_plus_1"])
print(df_csv.head())

df_csv = df_csv.rename(columns={"sex_name": "Płeć"})
print(df_csv.columns.tolist())

df_csv.to_csv("data_updated.csv", index=False)
print("Ramka danych zapisana jako data_updated.csv")

print("\nŚrednia, maksimum i minimum kolumny sex_id:")
print("Średnia:", df_csv["sex_id"].mean())
print("Maksimum:", df_csv["sex_id"].max())
print("Minimum:", df_csv["sex_id"].min())

print("\nLiczba wierszy w df_csv:")
print(len(df_csv))

print("\nWartości unikatowe w kolumnie location_name:")
print(df_csv["location_name"].unique())

print("\nLiczba wierszy, gdzie Płeć == 'Male':")
print((df_csv["Płeć"] == "Male").sum())

print("\nSortowanie rosnąco według sex_id:")
print(df_csv.sort_values(by="sex_id", ascending=True))

print("\nSortowanie malejąco według sex_id:")
print(df_csv.sort_values(by="sex_id", ascending=False))

print("\n10 największych wartości sex_id:")
print(df_csv.nlargest(10, "sex_id"))

print("\n10 najmniejszych wartości sex_id:")
print(df_csv.nsmallest(10, "sex_id"))

print("\n10 największych wartości sex_id dla location_name zawierającego 'China':")
print(df_csv[df_csv["location_name"].str.contains("China")].nlargest(10, "sex_id"))

print("\nŚrednie wartości kolumn liczbowych grupowane według location_name:")
numeric_cols = df_csv.select_dtypes(include='number').columns
grouped_mean = df_csv.groupby("location_name")[numeric_cols].mean()
print(grouped_mean)

print("\nGrupowanie z różnymi agregacjami:")
agg_dict = {
    "sex_id": ["mean", "median", "count"],
    "Płeć": ["count"]
}
grouped_custom = df_csv.groupby("location_name").agg(agg_dict)
print(grouped_custom)

print("\nNazwy kolumn indeksu złożonego:")
print(grouped_custom.columns)

print("\nSortowanie według kolumny ('sex_id', 'mean'):")
sorted_grouped = grouped_custom.sort_values(by=("sex_id", "mean"), ascending=False)
print(sorted_grouped)

print("\nTabela przestawna (pivot table):")
pivot_df = df_csv.pivot_table(
    index="location_name",
    columns="Płeć",
    values="sex_id",
    aggfunc="mean"
)
print(pivot_df)

print("\nIndeksy tabeli przestawnej:")
print(pivot_df.index)

print("\nKolumny tabeli przestawnej:")
print(pivot_df.columns)

print("\nTabela przestawna z indeksami złożonymi:")
pivot_df_multi = df_csv.pivot_table(
    index=["location_name", "Płeć"],
    values="sex_id",
    aggfunc="mean"
)
print(pivot_df_multi)
print("\nIndeksy złożone:")
print(pivot_df_multi.index)

pivot_df_multi.plot(kind="bar", figsize=(12,6))
plt.title("Średnie wartości sex_id dla każdej lokalizacji i płci")
plt.ylabel("Średnie sex_id")
plt.xlabel("location_name i Płeć")
plt.xticks(rotation=45)
plt.show()

print("\nHistogram kolumny sex_id:")
df_csv["sex_id"].hist(bins=5, figsize=(8,5))
plt.title("Histogram kolumny sex_id")
plt.xlabel("sex_id")
plt.ylabel("Liczba wierszy")
plt.show()

df2 = pd.DataFrame({
    "location_id": [1, 4, 6],
    "new_column": ["A", "B", "C"]
})

merged_df = pd.merge(df_csv, df2, on="location_id", how="left")
print("\nPołączenie metodą merge:")
print(merged_df.head())

concat_df = pd.concat([df_csv, df_csv], ignore_index=True)
print("\nPołączenie metodą concat:")
print(concat_df.head())

df_csv["sex_id_times_2"] = df_csv["sex_id"] * 2
df_csv["sex_id_plus_10"] = df_csv["sex_id"] + 10

print("\nNowe kolumny dodane przez operacje matematyczne:")
print(df_csv[["sex_id", "sex_id_times_2", "sex_id_plus_10"]].head())

df_csv["sex_id_squared"] = df_csv["sex_id"].apply(lambda x: x**2)
df_csv["sex_id_category"] = df_csv["sex_id"].apply(lambda x: "Low" if x < 2 else "High")

print("\nNowe kolumny dodane przy użyciu funkcji lambda:")
print(df_csv[["sex_id", "sex_id_squared", "sex_id_category"]].head())

print("\nPrzetwarzanie dużego pliku w kawałkach (chunksize):")
chunk_size = 5 
for chunk in pd.read_csv("data.csv", chunksize=chunk_size):
    print("\nNowy chunk:")
    print(chunk)
