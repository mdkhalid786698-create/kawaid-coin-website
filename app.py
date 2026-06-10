import streamlit as st

st.set_page_config(
    page_title="Kawaid Coin",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Kawaid Coin (KWD)")
st.subheader("Built on BNB Smart Chain")

st.markdown("---")

col1, col2 = st.columns([1,2])

with col1:
    st.image("logo.png", width=250)

with col2:
    st.markdown("""
    ## About KWD

    Kawaid Coin (KWD) is a community-driven cryptocurrency built on BNB Smart Chain.

    Focused on:
    - Community Growth
    - Security
    - Future Utility
    - Ecosystem Expansion
    """)

st.markdown("---")

st.header("📢 Official Links")

st.markdown("""
- X: https://x.com/KawaidCoin
- Telegram Community: https://t.me/KawaidCoin
- Telegram News: https://t.me/KawaidCoinNews
""")

st.markdown("---")

st.header("📜 Contract Address")

st.header("📊 Token Info")

col1, col2, col3 = st.columns(3)

col1.metric("Token Symbol", "KWD")
col2.metric("Network", "BNB Chain")
col3.metric("Total Supply", "1,000,000")

st.code("0xD9D8d0f75ECf289e331DEa2C466cEf1227a11670")

st.link_button("🚀 Buy KWD", "https://pancakeswap.finance/")

st.metric("🔥 Current Price", "Coming Soon")
st.metric("👥 Holders Goal", "Community Building Phase")

st.markdown("---")

st.header("🛣️ Roadmap")

st.markdown("""
### Phase 1
✅ Token Launch  
✅ Social Media Setup  
✅ Community Launch  

### Phase 2
🔄 Website Development  
🔄 Whitepaper  
🔄 PancakeSwap Listing  

### Phase 3
🚀 Marketing Expansion  
🚀 Partnerships  
🚀 Utility Development  
""")

st.header("📄 Whitepaper")

st.info("""
Kawaid Coin (KWD) aims to build a strong crypto ecosystem focused on:
- Community Growth
- Secure Transactions
- Utility Development
- Future Expansion
""")

st.markdown("---")

st.success("Kawaid Coin (KWD) • Community • Growth • Future Utility 🚀")