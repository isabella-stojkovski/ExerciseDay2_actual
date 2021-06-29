## 2a

FNAME = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user"
df = pd.read_csv(FNAME, sep="|")
df.set_index("user_id")

## 2b

df.tail(10)
df.head(25)

## 2c

df.info()

## 2d

df_occupation = df.value_counts("occupation")
df_occupation = pd.DataFrame([df.value_counts("occupation")], columns = ["occupation", "Count"])
df_occupation.columns = ["occupation", "Count"]
print(df_occupation)

## 2e

len(df_occupation)

df_occupation.sort_values(by="occupation")
df_occupation.rename(columns={"Occ":"occupation"})
print(df_occupation)


df_occupation[:1]
df_occupation.info()



