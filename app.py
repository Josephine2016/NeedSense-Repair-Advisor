import streamlit as st

st.set_page_config(
    page_title="NeedSense Repair Advisor",
    page_icon="🔧",
    layout="wide",
)

PRODUCTS = [
    {
        "name": "QUICK 861DW Rework Station",
        "category": "Repair Equipment",
        "use": "Hot-air rework and component removal",
        "price": 450000,
        "skill": "Advanced",
    },
    {
        "name": "QUICK 857DW+ Rework Station",
        "category": "Repair Equipment",
        "use": "Hot-air rework and soldering tasks",
        "price": 250000,
        "skill": "Intermediate",
    },
    {
        "name": "Digital Microscope",
        "category": "Testing Equipment",
        "use": "Magnified inspection of small components",
        "price": 180000,
        "skill": "Beginner",
    },
    {
        "name": "Digital Multimeter",
        "category": "Testing Equipment",
        "use": "Electrical measurements and fault diagnosis",
        "price": 35000,
        "skill": "Beginner",
    },
    {
        "name": "Precision Diagonal Pliers",
        "category": "Tools",
        "use": "Precision cutting and wire trimming",
        "price": 12000,
        "skill": "Beginner",
    },
    {
        "name": "Soldering Flux",
        "category": "Consumables",
        "use": "Supporting soldering and rework",
        "price": 5000,
        "skill": "Beginner",
    },
       {
        "name": "Helping-Hand Magnifier",
        "category": "Testing Equipment",
        "use": "Magnified inspection of small components",
        "price": 15000,
        "skill": "Beginner",
    },
    {
        "name": "Magnifying Lamp",
        "category": "Testing Equipment",
        "use": "Hands-free magnified inspection of circuit boards",
        "price": 35000,
        "skill": "Beginner",
    },
    {
        "name": "Entry-Level Inspection Microscope",
        "category": "Testing Equipment",
        "use": "Magnified inspection of small electronic components",
        "price": 80000,
        "skill": "Beginner",
    },
    {
        "name": "DC Power Supply",
        "category": "Testing Equipment",
        "use": "Powering devices and diagnosing motherboard faults",
        "price": 45000,
        "skill": "Intermediate"
    },
       {
        "name": "ZXW Motherboard Viewer",
        "category": "Testing Equipment",
        "use": "View motherboard circuit diagrams and component connections",
        "price": 50000,
        "skill": "Intermediate"
    },
    {
        "name": "Oscilloscope",
        "category": "Testing Equipment",
        "use": "Analyze electronic signals during motherboard diagnosis",
        "price": 95000,
        "skill": "Advanced"
    },
    {
        "name": "DC Ammeter",
        "category": "Testing Equipment",
        "use": "Measure current consumption during electrical diagnosis",
        "price": 25000,
        "skill": "Intermediate"
    },



]


def recommend_products(task, budget):
    task = task.lower()
    matches = []       
    keywords = {
    "hot air": ["hot-air rework"],
    "solder": ["soldering", "hot-air rework"],
    "microscope": ["magnified inspection"],
    "inspection": ["magnified inspection"],
    "electrical": ["electrical measurements"],
    "diagnosis": ["fault diagnosis", "electrical"],
    "cutting": ["precision cutting"],
    "flux": ["soldering"],
    "voltage": ["electrical measurements"],
    "current": [
        "current consumption",
        "powering devices",
        "electrical measurements",
    ],
    "motherboard": [
        "motherboard faults",
        "motherboard circuit diagrams",
        "motherboard diagnosis",
        "electrical measurements",
    ],
    "circuit diagram": ["motherboard circuit diagrams"],
    "oscilloscope": ["electronic signals"],
    "power supply": ["powering devices"],
    "multimeter": ["electrical measurements"],
    "short circuit": [
        "electrical measurements",
        "motherboard faults",
    ],
}



    requested_uses = []

    for keyword, uses in keywords.items():
        if keyword in task:
            requested_uses.extend(uses)

    for product in PRODUCTS:
        matched = (
            any(use in product["use"].lower() for use in requested_uses)
            if requested_uses
            else True
        )

        if matched and product["price"] <= budget:
            matches.append(product)

    return matches


st.title("🔧 NeedSense Repair Advisor")
st.subheader("Find suitable tools for your repair task")

st.write(
    "Describe the repair you need to perform. "
    "The advisor will search a sample product catalogue and suggest options."
)

with st.form("repair_request"):
    task = st.text_area(
        "What repair task do you need tools for?",
        placeholder="Example: I need to diagnose electrical faults on a phone.",
    )

    budget = st.number_input(
        "Your maximum budget (₦)",
        min_value=0,
        value=100000,
        step=5000,
    )

    submitted = st.form_submit_button("Find Suitable Tools")

if submitted:
    if not task.strip():
        st.warning("Please describe the repair task first.")
    else:
        results = recommend_products(task, budget)

        if results:
            st.success(f"Found {len(results)} catalogue match(es).")

            for product in results:
                with st.container(border=True):
                    st.subheader(product["name"])
                    st.write(f"**Category:** {product['category']}")
                    st.write(f"**Purpose:** {product['use']}")
                    st.write(f"**Listed demo price:** ₦{product['price']:,}")
                    st.write(f"**Suggested experience level:** {product['skill']}")

            st.caption(
                "Demo only: product prices are illustrative, not verified live prices. "
                "Compatibility and stock availability have not been verified."
            )
        else:
            st.warning(
                "No matching products were found within your budget. "
                "Try increasing your budget or describing the task differently."
            )

st.divider()
st.caption("NeedSense Repair Advisor | Early MVP demonstration")

