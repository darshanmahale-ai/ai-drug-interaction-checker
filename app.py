import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Drug Interaction Checker", layout="wide")
st.title("💊⚠️ AI Drug Interaction Alert System")
st.markdown("Enter 2 drugs - AI checks for dangerous interactions")

# Small but real interaction database (you can expand)
INTERACTIONS = {
    ("warfarin", "aspirin"): {"severity": "HIGH", "effect": "Increased bleeding risk", "action": "Avoid combination, monitor INR"},
    ("warfarin", "ibuprofen"): {"severity": "HIGH", "effect": "GI bleeding + anticoagulation", "action": "Use paracetamol instead"},
    ("metformin", "alcohol"): {"severity": "MODERATE", "effect": "Risk of lactic acidosis", "action": "Limit alcohol"},
    ("lisinopril", "ibuprofen"): {"severity": "MODERATE", "effect": "Kidney injury + reduces BP effect", "action": "Monitor BP & kidney function"},
    ("simvastatin", "grapefruit"): {"severity": "HIGH", "effect": "Increased statin toxicity, muscle damage", "action": "Avoid grapefruit juice"},
    ("paracetamol", "alcohol"): {"severity": "MODERATE", "effect": "Liver toxicity risk", "action": "Limit to <2g/day"},
    ("amoxicillin", "warfarin"): {"severity": "MODERATE", "effect": "Enhanced anticoagulation", "action": "Monitor INR closely"},
}

st.subheader("Check Interaction")

col1, col2 = st.columns(2)
with col1:
    drug1 = st.text_input("Drug 1", "Warfarin").lower().strip()
with col2:
    drug2 = st.text_input("Drug 2", "Aspirin").lower().strip()

if st.button("Check Interaction 🔍", use_container_width=True):
    key = (drug1, drug2) if (drug1, drug2) in INTERACTIONS else (drug2, drug1) if (drug2, drug1) in INTERACTIONS else None

    if key:
        data = INTERACTIONS[key]
        if data['severity'] == "HIGH":
            st.error(f"### 🚨 HIGH RISK INTERACTION FOUND")
        else:
            st.warning(f"### ⚠️ MODERATE RISK")

        st.markdown(f"**Effect:** {data['effect']}")
        st.markdown(f"**Recommended Action:** {data['action']}")
        st.markdown(f"**Severity:** {data['severity']}")
    else:
        st.success(f"### ✅ No major interaction found in database for {drug1.title()} + {drug2.title()}")
        st.info("Note: This demo uses curated database. Production version uses DrugBank + BioBERT NER.")

st.divider()
st.subheader("Full Interaction Database")
df = pd.DataFrame([{"Drug A": k[0].title(), "Drug B": k[1].title(), **v} for k,v in INTERACTIONS.items()])
st.dataframe(df, use_container_width=True)

st.markdown("---")
st.markdown("**Future:** Integrate BioBERT to auto-extract interactions from FDA labels + DrugBank API (500k+ interactions).")
