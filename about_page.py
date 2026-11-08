import base64
from pathlib import Path
import streamlit as st

def render_about_page(asset_dir: Path):
    def image_data(filename: str) -> str:
        path = asset_dir / filename
        suffix = path.suffix.lower().replace(".", "")
        mime = "jpeg" if suffix in {"jpg", "jpeg"} else suffix
        encoded = base64.b64encode(path.read_bytes()).decode("utf-8")
        return f"data:image/{mime};base64,{encoded}"

    hero = image_data("about_campus_hero.jpg")
    header_brand = image_data("about_header_brand.png")
    footer_brand = image_data("about_footer_brand.png")

    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    :root {{
        --navy:#06234b; --deep-navy:#001f45; --blue:#0755ff;
        --red:#f51e2b; --muted:#34456c; --yellow:#ffce00;
    }}
    html, body, [class*="css"] {{font-family:'Inter',Arial,sans-serif;}}
    [data-testid="stAppViewContainer"] {{background:#fff;}}
    [data-testid="stMain"] {{padding:0!important;}}
    .block-container {{max-width:100%!important;padding:0!important;margin:0!important;}}
    #MainMenu, footer, header {{visibility:hidden;}}
    .about-utility {{
        min-height:23px;background:#a91d32;color:white;display:flex;
        justify-content:flex-end;align-items:center;padding:0 5.5%;
        font-size:9px;letter-spacing:.05px;
    }}
    .about-navbar {{
        min-height:65px;background:var(--deep-navy);color:white;display:flex;
        align-items:center;justify-content:space-between;padding:8px 6.5%;gap:24px;
    }}
    .about-brand {{width:240px;max-width:27%;height:auto;object-fit:contain;}}
    .about-navlinks {{display:flex;align-items:center;justify-content:flex-end;gap:25px;flex:1;}}
    .about-navlinks a {{color:#fff!important;text-decoration:none!important;font-size:11px;font-weight:600;white-space:nowrap;}}
    .about-navlinks a.active {{border-bottom:3px solid var(--yellow);padding:19px 0 13px;}}
    .about-search {{width:140px;background:#fff;border-radius:5px;color:#9299a8;font-size:10px;padding:7px 10px;white-space:nowrap;}}
    .about-hero {{
        height:140px;background-image:linear-gradient(90deg,rgba(0,20,32,.78),rgba(0,20,32,.08)),url('{hero}');
        background-size:cover;background-position:center 48%;display:flex;flex-direction:column;
        justify-content:center;padding:0 7%;color:#fff;
    }}
    .about-red-mark {{height:5px;width:44px;background:var(--red);border-radius:8px;margin-bottom:10px;}}
    .about-hero h1 {{font-size:36px;line-height:1.15;margin:0 0 5px;font-weight:800;color:white;}}
    .about-hero p {{font-size:15px;margin:0;color:white;}}
    .about-content {{padding:18px 6.7% 43px;background:#fff;}}
    .about-breadcrumb {{font-size:12px;color:#53617f;margin:0 0 19px;}}
    .about-section-mark {{height:5px;width:32px;background:var(--red);border-radius:8px;margin-bottom:7px;}}
    .about-content h2 {{font-size:31px;line-height:1.2;color:var(--navy);font-weight:800;margin:0 0 4px;}}
    .about-intro {{font-size:14px;line-height:1.5;color:var(--muted);margin:0 0 21px;max-width:1120px;}}
    .about-cards {{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;}}
    .about-card {{border-radius:9px;min-height:201px;padding:24px 24px 20px;display:flex;flex-direction:column;justify-content:space-between;}}
    .about-people {{background:#eaf4ff;}}
    .about-journal {{background:#eef8f1;}}
    .about-gallery {{background:#f5efff;}}
    .about-cardtop {{display:grid;grid-template-columns:64px 1fr;gap:16px;align-items:center;}}
    .about-cardicon {{width:58px;height:58px;}}
    .about-accent {{height:5px;width:53px;border-radius:6px;margin-bottom:10px;}}
    .about-people .about-accent {{background:#2e7cff;}}
    .about-journal .about-accent {{background:#27ae60;}}
    .about-gallery .about-accent {{background:#873df0;}}
    .about-card h3 {{font-size:24px;line-height:1.1;color:var(--navy);font-weight:800;margin:0;}}
    .about-card p {{font-size:11px;line-height:1.55;color:var(--muted);margin:13px 0 0;}}
    .about-cardbottom {{display:flex;justify-content:space-between;align-items:center;margin-top:16px;}}
    .about-cardbottom a {{font-size:12px;color:var(--blue)!important;text-decoration:none!important;font-weight:700;}}
    .about-arrow {{width:35px;height:35px;border-radius:50%;background:white;color:var(--blue);display:flex;align-items:center;justify-content:center;font-size:20px;box-shadow:0 2px 7px rgba(0,0,0,.08);}}
    .about-footer {{
        background:var(--deep-navy);color:white;padding:8px 7% 15px;display:grid;
        grid-template-columns:220px 1fr 1fr 1.35fr;gap:28px;align-items:center;
        min-height:88px;border-bottom:1px solid #52647e;
    }}
    .about-footer-logo {{width:205px;max-width:100%;height:auto;}}
    .about-foot-col {{border-left:1px solid #344b6b;padding-left:45px;min-height:46px;}}
    .about-foot-col strong {{display:block;font-size:10px;margin-bottom:8px;color:white;}}
    .about-foot-col span {{display:block;font-size:9px;margin:5px 0;color:white;}}
    .about-subscribe {{display:flex;gap:0;margin:4px 0 5px;}}
    .about-subscribe span {{background:white;color:#9aa2b1;padding:6px 9px;flex:1;border-radius:4px 0 0 4px;font-size:8px;}}
    .about-subscribe b {{background:var(--yellow);color:#172b4d;padding:6px 12px;border-radius:0 5px 5px 0;font-size:8px;}}
    .about-socials {{font-size:15px;letter-spacing:7px;color:white;}}
    @media(max-width:850px) {{
        .about-navbar {{padding:10px 5%;flex-wrap:wrap;}}
        .about-brand {{max-width:220px;width:45%;}}
        .about-navlinks {{gap:14px;flex-wrap:wrap;}}
        .about-content {{padding-left:5%;padding-right:5%;}}
        .about-cards {{grid-template-columns:1fr;}}
        .about-card {{min-height:175px;}}
        .about-footer {{grid-template-columns:1fr 1fr;}}
        .about-foot-col {{padding-left:15px;}}
    }}
    @media(max-width:520px) {{
        .about-utility {{font-size:7px;padding:0 3%;}}
        .about-navbar {{gap:10px;}}
        .about-navlinks {{justify-content:flex-start;gap:12px;}}
        .about-navlinks a {{font-size:10px;}}
        .about-hero {{height:150px;padding:0 6%;}}
        .about-hero h1 {{font-size:30px;}}
        .about-hero p {{font-size:12px;}}
        .about-content h2 {{font-size:25px;}}
        .about-intro {{font-size:12px;}}
        .about-card {{padding:20px;}}
        .about-card h3 {{font-size:22px;}}
        .about-footer {{grid-template-columns:1fr;gap:14px;padding:20px 7%;}}
        .about-foot-col {{border-left:0;border-top:1px solid #344b6b;padding:12px 0 0;}}
    }}
    </style>

    <div class="about-utility">University of Moratuwa&nbsp;&nbsp; | &nbsp;Students&nbsp;&nbsp; | &nbsp;Faculty &amp; Staff&nbsp;&nbsp; | &nbsp;Alumni&nbsp;&nbsp; | &nbsp;Legacy Site</div>
    <div class="about-navbar">
      <img class="about-brand" src="{header_brand}" alt="University of Moratuwa – Office of Research">
      <div class="about-navlinks">
        <a href="?page=home">Home</a>
        <a href="#">Research⌄</a>
        <a href="#">Grants⌄</a>
        <a href="#">Research Support⌄</a>
        <a class="active" href="?page=about">About Us</a>
        <div class="about-search">Search...　⌕</div>
      </div>
    </div>
    <section class="about-hero">
      <div class="about-red-mark"></div>
      <h1>About Us</h1>
      <p>The Office of Research, University of Moratuwa</p>
    </section>
    <main class="about-content">
      <div class="about-breadcrumb"><a href="?page=home">Home</a> &nbsp;›&nbsp; About Us</div>
      <div class="about-section-mark"></div>
      <h2>About the Office of Research</h2>
      <p class="about-intro">
        The Office of Research (OoR) drives and supports a vibrant research ecosystem across the University. It facilitates research
        development, funding opportunities, collaborations, and the dissemination of research outputs to create real-world impact for society.
      </p>
      <section class="about-cards">
        <article class="about-card about-people">
          <div class="about-cardtop">
            <svg class="about-cardicon" viewBox="0 0 64 64" fill="#2e7cff" aria-hidden="true">
              <circle cx="32" cy="15" r="9"/><circle cx="14" cy="23" r="7"/><circle cx="50" cy="23" r="7"/>
              <path d="M14 34c-8 0-12 5-12 13v3h20v-5c0-4 1-8 4-11-3-1-7 0-12 0zm36 0c-5 0-9 1-12 3 3 3 4 7 4 11v2h20v-3c0-8-4-13-12-13zM32 29c-11 0-17 6-17 15v7h34v-7c0-9-6-15-17-15z"/>
            </svg>
            <div><div class="about-accent"></div><h3>People</h3><p>Meet the Office of Research team, leadership and contact details.</p></div>
          </div>
          <div class="about-cardbottom"><a href="#">View People</a><span class="about-arrow">➜</span></div>
        </article>
        <article class="about-card about-journal">
          <div class="about-cardtop">
            <svg class="about-cardicon" viewBox="0 0 64 64" fill="none" stroke="#27ae60" stroke-width="4" stroke-linejoin="round" aria-hidden="true">
              <path d="M31 15C22 7 9 10 5 14v38c9-5 18-4 26 3 8-7 17-8 27-3V14c-9-5-19-7-27 1z"/><path d="M31 15v40"/>
            </svg>
            <div><div class="about-accent"></div><h3>Journal</h3><p>Explore the Office of Research journal, publications and related information.</p></div>
          </div>
          <div class="about-cardbottom"><a href="#">View Journal</a><span class="about-arrow">➜</span></div>
        </article>
        <article class="about-card about-gallery">
          <div class="about-cardtop">
            <svg class="about-cardicon" viewBox="0 0 64 64" fill="none" stroke="#873df0" stroke-width="4" stroke-linejoin="round" aria-hidden="true">
              <rect x="6" y="9" width="52" height="43" rx="4"/><circle cx="42" cy="21" r="5" fill="#873df0" stroke="none"/><path d="M10 46l15-16 11 11 7-7 11 12"/>
            </svg>
            <div><div class="about-accent"></div><h3>Gallery</h3><p>Browse highlights from research events, workshops, conferences and activities.</p></div>
          </div>
          <div class="about-cardbottom"><a href="#">View Gallery</a><span class="about-arrow">➜</span></div>
        </article>
      </section>
    </main>
    <footer class="about-footer">
      <img class="about-footer-logo" src="{footer_brand}" alt="University of Moratuwa">
      <div class="about-foot-col"><strong>More Links</strong><span>Library</span><span>Research Enterprise</span></div>
      <div class="about-foot-col"><strong>Other Links</strong><span>Vacancies</span><span>Research News</span></div>
      <div class="about-foot-col"><strong>Connect With Us</strong><div class="about-subscribe"><span>Your Email Address</span><b>SUBSCRIBE</b></div><div class="about-socials">in　f　◎　▶　𝕏</div></div>
    </footer>
    """, unsafe_allow_html=True)
    st.caption("Office of Research | University of Moratuwa")
