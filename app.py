import streamlit as st
import pandas as pd

# Sample data (you can expand with your full mine list)
mines = [
    ("Wani", "Durgapur Rayyatwari OC", 1729000),
    ("Wani", "Bellora-Naigaon OC (Expansion)", 2460000),
    ("Wani", "Ukni OC (Expansion)", 3810000),
    ("Wani", "Penganga OC", 1857000),
    ("Nagpur", "Saoner OC", 1200000),
    ("Wani North","Amalgamation Yekona I & II OC",1030000),
    ("Wani North","Dahegaon Makardhokra 2&4 OC",3500000),
    ("Wani North","Kosar Gokul OC",1680000),
    ("Wani North","Yekona II UG->OC",1156000),
    ("Wani North","Niljai Deep OC",1670000),
    ("Wani North","Naglon OC",1289000),
    ("Wani North","Naigaon Develi OC",1228000),
   ("Ballarpur","Ballarpur Opencast Mine",625000),
   ("Ballarpur","Gouri Deep OC",378000),
    ("Ballarpur","GouriPauni OC (Amalgamation)",2574000),
    ("Ballarpur","Pauni-II Expansion OC",3250000),
    ("Ballarpur","Dhuptala OC",1681000),
    ("Ballarpur","Sasti OC",1889000),
    ("Ballarpur","Ballarpur Colliery 3&4 Pits (UG)",71000),
    ("Nagpur","Adasa UG to OC",715460),
   ("Nagpur","Amalgamated InderKamptee Deep OC",3090000),
   ("Nagpur","Bhanegaon OC",1149700),
   ("Nagpur","Gondegaon Extension OC",3500000),
   ("Nagpur","Patansaongi UG (Expansion)",38640),
  ("Nagpur","Saoner UG (Expansion)",504960),
    ("Nagpur","Silewara UG (Expansion)",69080),
   ("Nagpur","Singhori OC (Expansion)",1199000),
  ("Umrer","Makardhokra-I OC",4200000),
   ("Umrer","Dinesh OC (MKD-III)",4432500),
  ("Umrer","Umrer OC",3110000),
    ("Umrer","Gokul OC",1807000),
   ("Chandrapur","Durgapur OC",2500000),
   ("Chandrapur","Durgapur Rayatwari Colliery (UG)",100000),
   ("Chandrapur","Chanda Rayatwari Colliery",60,000),
    ("Kanhan","Ambara OC",1,000,000),
    ("Kanhan","Ghorawari OC",1,500,000),
    ("Kanhan","Mohan (Maori) UG",38330),
    ("Kanhan","Nandan UG",405,000),
    ("Kanhan","Sharda UG",34555),
    ("Kanhan","Tandsi UG",35505),
   ("Pench","Barkuhi OC",750,000),
   ("Pench","Chhinda OC Mine",130,000),
  ("Pench","Dhankasa UG Mine",1,000,000-1,200,000),
   ("Pench","Jamuniya UG Mine",828,000),
      ]


# Convert to DataFrame
df = pd.DataFrame(mines, columns=["Region", "Mine Name", "Yearly Output (tonnes)"])
df["Daily Output (tonnes)"] = (df["Yearly Output (tonnes)"] / 365).round(2)

# Streamlit UI
st.title("⛏️ WCL Coal Output Dashboard")

# Search options
search_by = st.selectbox("🔍 Search by:", ["Mine Name", "Region", "Yearly Output"])

query = st.text_input("Enter value to search:")

if st.button("Search"):
    if search_by == "Mine Name":
        result = df[df["Mine Name"].str.contains(query, case=False, na=False)]
    elif search_by == "Region":
        result = df[df["Region"].str.contains(query, case=False, na=False)]
    else:
        try:
            value = int(query)
            result = df[df["Yearly Output (tonnes)"] == value]
        except:
            st.error("Please enter a valid number for Yearly Output")
            result = pd.DataFrame()

    if not result.empty:
        st.success("✅ Results Found:")
        st.dataframe(result)
    else:
        st.warning("⚠️ No match found!")

# Show full data
if st.checkbox("Show All Mines"):
    st.dataframe(df)

# Region totals
st.subheader("📊 Region-wise Total Output")
region_totals = df.groupby("Region")[["Yearly Output (tonnes)", "Daily Output (tonnes)"]].sum()
st.dataframe(region_totals)

# Grand total
st.subheader("🏆 Grand Total")
st.write(f"Total Yearly Output: {df['Yearly Output (tonnes)'].sum():,} tonnes")
st.write(f"Total Daily Output: {df['Daily Output (tonnes)'].sum():,.2f} tonnes")
