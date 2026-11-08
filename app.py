import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="UOM Research & Innovation",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Support both layouts:
# 1) images uploaded beside app.py (your current GitHub layout)
# 2) images stored inside an assets/ folder
ROOT = Path(__file__).parent
ASSET = ROOT / "assets" if (ROOT / "assets").is_dir() else ROOT

def img(name):
    path = ASSET / name
    if not path.is_file():
        raise FileNotFoundError(
            f"Missing image: {path}. Keep the image beside app.py "
            "or place it inside an assets/ folder."
        )
    return str(path)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.stApp { background: #fff; color: #092b55; }
.block-container { padding-top: 0 !important; padding-bottom: 0.5rem !important; max-width: 1500px; }
header[data-testid="stHeader"] { display:none; }
div[data-testid="stToolbar"] { display:none; }
.top-strip { background:#8e203b; color:#fff; text-align:right; padding:4px 7%; font-size:10px; font-weight:600; }
.navbar { background:#052750; color:white; display:flex; align-items:center; justify-content:space-between; padding:12px 7%; gap:20px; }
.brand { color:white; font-size:20px; font-weight:800; line-height:1.05; letter-spacing:.2px; }
.brand small { display:block; font-size:10px; font-weight:500; letter-spacing:1px; }
.navlinks { display:flex; align-items:center; gap:25px; color:white; font-size:11px; font-weight:700; }
.hero img { width:100%; height:205px; object-fit:cover; display:block; }
.section { padding:18px 7% 10px; }
h2 { color:#082c58; font-size:25px !important; font-weight:800 !important; margin:0 0 7px 0 !important; line-height:1.1; }
.redline { width:30px; height:4px; background:#d51f45; margin-bottom:7px; border-radius:3px; }
p { color:#596575; font-size:12px; line-height:1.45; }
a { color:#0875ee !important; text-decoration:none !important; font-weight:600; }
button[kind="secondary"] { border-color:#d6e0ed !important; color:#0a315e !important; }
.feature-card, .news-card { border:1px solid #e6ebf1; border-radius:6px; overflow:hidden; background:#fff; box-shadow:0 2px 5px #102b4a10; height:100%; }
.feature-card img { width:100%; height:70px; object-fit:cover; display:block; }
.feature-body { padding:8px 10px 9px; }
.feature-body strong { display:block; color:#092d5c; font-size:12px; margin-bottom:4px; }
.feature-body p { margin:0; font-size:11px; line-height:1.35; min-height:44px; }
.feature-link { text-align:right; margin-top:4px; font-size:11px; }
.news-band { background:#edf6ff; padding:18px 7% 15px; margin-top:8px; }
.news-card { display:flex; gap:10px; padding:7px; min-height:110px; }
.news-card img { width:105px; min-width:105px; height:96px; object-fit:cover; border-radius:3px; }
.news-body { min-width:0; }
.news-date { color:#687487; font-size:9px; margin-bottom:4px; }
.news-body strong { display:block; color:#092d5c; font-size:11px; line-height:1.3; }
.news-body p { font-size:10px; line-height:1.3; margin:5px 0; }
.footer { background:#052750; color:white; padding:22px 7%; margin-top:0; }
.footer h4 { color:white; font-size:12px; margin:0 0 8px; }
.footer p, .footer a { color:white !important; font-size:11px; line-height:1.8; }
.footer-brand { font-size:19px; font-weight:800; line-height:1.1; }
.footer-brand small { display:block; font-size:9px; font-weight:500; }
.stTextInput input { border-radius:3px; }
@media (max-width: 800px) {
 .navlinks { display:none; }
 .navbar { padding:12px 5%; }
 .section, .news-band { padding-left:5%; padding-right:5%; }
 .hero img { height:150px; }
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="top-strip">Students&nbsp;&nbsp; | &nbsp;Faculty &amp; Staff&nbsp;&nbsp; | &nbsp;Alumni&nbsp;&nbsp; | &nbsp;Legacy Site</div>
<div class="navbar">
  <div class="brand">🎓 &nbsp; UNIVERSITY OF<br><span style="font-size:22px">MORATUWA</span></div>
  <div class="navlinks"><span>ACADEMIC</span><span>RESEARCH</span><span>PEOPLE</span><span>ABOUT</span><span>CONTACTS</span></div>
</div>
""", unsafe_allow_html=True)

# Search is functional and can be connected to the site's search endpoint later.
search_col, _ = st.columns([1, 5])
with search_col:
    st.text_input("Search", placeholder="Search the research website...", label_visibility="collapsed")

st.markdown(f'<div class="hero"><img src="data:image/jpeg;base64,{__import__("base64").b64encode(open(img("hero_banner.jpg"),"rb").read()).decode()}"></div>', unsafe_allow_html=True)

st.markdown('<div class="section">', unsafe_allow_html=True)
left, right = st.columns([0.88, 1.12], gap="large")
with left:
    st.markdown('<div class="redline"></div><h2>Welcome to University of<br>Moratuwa Research</h2>', unsafe_allow_html=True)
    st.markdown("""
    <p>At the University of Moratuwa, we are committed to advancing research excellence by fostering a supportive and dynamic research environment. Through effective administration and strategic initiatives, we strive to position the University as a globally recognized center for innovation and discovery.</p>
    <p>We actively promote research development, facilitate access to national and international funding opportunities, and ensure transparent communication of research policies and processes to strengthen our research community.</p>
    """, unsafe_allow_html=True)
    if st.button("Learn more  →", key="learn_more"):
        st.info("Connect this button to the About Us page or research portal URL.")
with right:
    st.image(img("campus_building.jpg"), use_container_width=True)

features = [
    ("feature_researcher.jpg", "Find a Researcher", "Explore the diverse expertise within the University of Moratuwa's research community."),
    ("feature_units.jpg", "Research units and groups", "Delve into the specialized research units and collaborative groups that form the backbone of our research excellence."),
    ("feature_support.jpg", "Research support", "Discover the support and resources available to help you at every stage of your research journey."),
    ("feature_multi.jpg", "Multidisciplinary research", "Fostering collaboration across disciplines to address complex global and local challenges."),
    ("feature_awards.jpg", "Research awards", "Discover the recognition and achievements of our vibrant research community."),
]
feature_cols = st.columns(5, gap="small")
for col, (picture, title, desc) in zip(feature_cols, features):
    with col:
        st.markdown(f"""
        <div class="feature-card">
          <img src="data:image/jpeg;base64,{__import__("base64").b64encode(open(img(picture),"rb").read()).decode()}">
          <div class="feature-body"><strong>{title}</strong><p>{desc}</p><div class="feature-link"><a href="#">Explore →</a></div></div>
        </div>
        """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="news-band"><div class="redline"></div><h2>Recent Research News</h2>', unsafe_allow_html=True)
news = [
    ("news_sustainability.jpg", "12 Sep 2025", "UoM Researchers Develop Sustainable Construction Material Using Local Resources", "A multidisciplinary team at the University of Moratuwa has developed an innovative construction material."),
    ("news_transport.jpg", "05 Sep 2025", "New Study Proposes Greener Urban Transport Solutions for Sri Lanka", "Researchers from UoM highlight strategies for low-carbon urban mobility in a recent publication."),
    ("news_ai.jpg", "28 Aug 2025", "UoM Team Advances AI Applications in Disaster Risk Management", "A research team at the University of Moratuwa has developed a novel AI-based model."),
]
news_cols = st.columns(3, gap="small")
for col, (picture, date, title, desc) in zip(news_cols, news):
    with col:
        st.markdown(f"""
        <div class="news-card">
          <img src="data:image/jpeg;base64,{__import__("base64").b64encode(open(img(picture),"rb").read()).decode()}">
          <div class="news-body"><div class="news-date">{date}</div><strong>{title}</strong><p>{desc}</p><a href="#">Read more →</a></div>
        </div>
        """, unsafe_allow_html=True)
st.markdown('<div style="text-align:right;padding:10px 0 0"><a href="#">View all news →</a></div></div>', unsafe_allow_html=True)

st.markdown("""
<div class="footer">
  <div style="display:grid;grid-template-columns:1.25fr 1fr 1fr 1.2fr;gap:25px">
    <div><div class="footer-brand">🎓 UNIVERSITY OF<br><span style="font-size:22px">MORATUWA</span><small>Wisdom&nbsp; • &nbsp;Innovation&nbsp; • &nbsp;Impact</small></div></div>
    <div><h4>More Links</h4><a href="#">Library</a><br><a href="#">Research Enterprise</a></div>
    <div><h4>Other Links</h4><a href="#">Vacancies</a><br><a href="#">Research News</a></div>
    <div><h4>Connect With Us</h4></div>
  </div>
</div>
""", unsafe_allow_html=True)
email_col, subscribe_col = st.columns([3, 1])
with email_col:
    email = st.text_input("Email address", placeholder="Your Email Address", label_visibility="collapsed")
with subscribe_col:
    if st.button("SUBSCRIBE", use_container_width=True):
        if "@" in email and "." in email:
            st.success("Thank you for subscribing!")
        else:
            st.error("Please enter a valid email address.")

st.caption("University of Moratuwa Research & Innovation | Homepage concept built with Streamlit")
