import streamlit as st
import json

# Load data
@st.cache_data
def load_data():
    with open("refined_drug_data.json", "r", encoding="utf-8") as f:
        return json.load(f)

data = load_data()

st.set_page_config(page_title="Drug Info Search", layout="wide")
st.title("💊 Drug Information Search App")

search_term = st.text_input("Search by Drug Name or Condition").lower()

if search_term:
    results = [
        drug for drug in data
        if search_term in drug.get("DrugName", "").lower()
        or any(search_term in tag for tag in drug.get("SearchTags", []))
    ]
else:
    results = data

if not results:
    st.warning("No matching drugs found.")
else:
    st.success(f"Showing {len(results)} result(s).")

    for drug in results:
        with st.expander(f"🔹 {drug.get('DrugName', 'Unknown Drug')}"):
            st.write("**Class**:", drug.get("Class", "N/A"))
            st.write("**Indications**:", ", ".join(drug.get("Indications", [])))
            st.write("**MOA**:", drug.get("MOA", "N/A"))
            st.write("**Side Effects**:", ", ".join(drug.get("SideEffects", [])))
            st.write("**Contraindications**:", ", ".join(drug.get("Contraindications", [])))
            st.write("**Dosage Form**:", drug.get("DosageForm", "N/A"))
            st.write("**Strength**:", drug.get("Strength", "N/A"))
            st.write("**Adult Dosing**:", drug.get("Dosing", "N/A"))
            st.write("**Max Dose**:", drug.get("MaxDose", "N/A"))
            st.write("**Brand Names**:", ", ".join(drug.get("Brands", [])))
            st.write("**Special Counselling Points**:", ", ".join(drug.get("Counselling", [])))
            st.write("**Monitoring**:", drug.get("Monitoring", "N/A"))
            st.write("**Storage**:", drug.get("Storage", "N/A"))
