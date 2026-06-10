import streamlit as st

st.set_page_config(
    page_title="Kawaid Coin",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<div style='text-align:center; padding:10px;'>
<a href='#about-kwd'>About</a> |
<a href='#official-links'>Links</a> |
<a href='#token-information'>Tokenomics</a> |
<a href='#roadmap'>Roadmap</a> |
<a href='#whitepaper'>Whitepaper</a>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<h1 style='text-align: center;'>🚀 Kawaid Coin (KWD)</h1>
<h3 style='text-align: center;'>Built on BNB Smart Chain</h3>
""", unsafe_allow_html=True)

st.markdown("---")

col1, col2 = st.columns([1,2])

with col1:
    st.image("logo.png", width=300)

with col2:
    st.subheader("About KWD")

    st.write("""
Kawaid Coin (KWD) is a community-driven cryptocurrency built on BNB Smart Chain.

Focused on:

• Community Growth  
• Security  
• Future Utility  
• Ecosystem Expansion
""")

st.markdown("---")

st.markdown("<h1 id='official-links'>📢 Official Links</h1>", unsafe_allow_html=True)

st.markdown("""
- X: https://x.com/KawaidCoin
- Telegram Community: https://t.me/KawaidCoin
- Telegram News: https://t.me/KawaidCoinNews
""")

st.markdown("---")

st.subheader("📊 Token Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Token Symbol", "KWD")

with col2:
    st.metric("Network", "BNB Smart Chain")

with col3:
    st.metric("Total Supply", "1,000,000")

st.subheader("📜 Contract Address")

st.code("0xD9D8d0f75ECf289e331DEa2C466cEf1227a11670")

st.markdown("---")

st.header("🛣️ Roadmap")

st.subheader("Phase 1")
st.write("""
✅ Token Launch  
✅ Social Media Setup  
✅ Community Launch  
""")

st.subheader("Phase 2")
st.write("""
🔹 Website Development  
🔹 Whitepaper Release  
🔹 PancakeSwap Listing  
""")

st.subheader("Phase 3")
st.write("""
🚀 Marketing Expansion  
🚀 Partnerships  
🚀 Utility Development  
""")

st.header("📄 Whitepaper")

st.write("""
Kawaid Coin (KWD) aims to build a strong crypto ecosystem focused on:
- Community Growth
- Security
- Utility Development
- Future Expansion
""")

st.markdown("---")

st.caption("© 2026 Kawaid Coin (KWD) | Built on BNB Smart Chain")

