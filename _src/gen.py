# -*- coding: utf-8 -*-
"""Generate the hub site from data.py. Run: python3 gen.py <outdir>"""
import json, os, sys, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import SITE, CATEGORIES, FOOT_KO, FOOT_EN, GH

CSS = """/* Cardiology tools hub — shared stylesheet.
   Every page on this site is generated from one data file and shares this
   sheet, so the pages cannot drift apart. */
:root{
  --bg:#ffffff; --bg-alt:#faf8f7; --ink:#16181d; --ink-2:#4a4f5a; --ink-3:#7c828f;
  --line:#e6e2e0; --line-2:#d6d0cd;
  --accent:#7d2231; --accent-2:#9a2b3d; --accent-wash:#f7eff0;
  --serif:'Iowan Old Style','Source Serif 4',Charter,Georgia,'Times New Roman',serif;
  --sans:'Pretendard','Apple SD Gothic Neo','Segoe UI','Malgun Gothic',-apple-system,system-ui,sans-serif;
}
@media (prefers-color-scheme: dark){
  :root{
    --bg:#14161a; --bg-alt:#181b20; --ink:#e9eaee; --ink-2:#b0b5bf; --ink-3:#858b97;
    --line:#292d35; --line-2:#3a3f49;
    --accent:#e08a99; --accent-2:#f0a3b0; --accent-wash:#241a1d;
  }
}
*{box-sizing:border-box;}
html{-webkit-text-size-adjust:100%;}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--sans);
  line-height:1.65;-webkit-font-smoothing:antialiased;}
.wrap{position:relative;max-width:1080px;margin:0 auto;padding:52px 24px 72px;}

.langSwitch{position:absolute;top:48px;right:24px;display:flex;gap:6px;z-index:30;}
.langSwitch button{font:inherit;font-size:12px;font-weight:600;line-height:1;padding:7px 13px;
  border-radius:999px;border:1px solid var(--line-2);background:transparent;color:var(--ink-2);
  opacity:.7;cursor:pointer;transition:all .15s ease;}
.langSwitch button:hover{opacity:1;}
.langSwitch button[aria-pressed="true"]{opacity:1;color:var(--accent);
  border-color:var(--accent);background:var(--accent-wash);}

.crumb{font-size:12.5px;color:var(--ink-3);margin:0 0 18px;}
.crumb a{color:var(--ink-2);text-decoration:none;border-bottom:1px solid var(--line-2);}
.crumb a:hover{color:var(--accent);border-color:var(--accent);}

header.masthead{border-bottom:2px solid var(--accent);padding-bottom:24px;margin-bottom:26px;}
.eyebrow{font-size:11.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent);
  font-weight:700;margin:0 0 12px;}
h1{font-family:var(--serif);font-size:clamp(27px,4.2vw,40px);line-height:1.15;font-weight:600;
  letter-spacing:-.015em;margin:0 0 12px;max-width:22ch;}
.lede{color:var(--ink-2);font-size:15.5px;margin:0;max-width:62ch;}
.byline{margin:18px 0 0;font-size:13px;color:var(--ink-3);}
.byline a{color:var(--ink-2);}

.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:1px;
  background:var(--line);border:1px solid var(--line);margin-top:26px;}
.card{background:var(--bg);padding:20px 20px 18px;display:flex;flex-direction:column;
  transition:background .15s ease;}
.card:hover{background:var(--bg-alt);}
.card h2,.card h3{font-size:15.5px;font-weight:650;margin:0 0 3px;letter-spacing:-.005em;
  font-family:var(--sans);}
.card .slug{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
  font-size:11.5px;color:var(--ink-3);margin:0 0 9px;}
.card p.desc{font-size:13.5px;color:var(--ink-2);margin:0 0 14px;flex:1;}
.card code{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:.92em;
  background:var(--bg-alt);padding:1px 4px;border-radius:3px;}
.links{display:flex;gap:8px;flex-wrap:wrap;align-items:center;}
.links a{font-size:12.5px;font-weight:600;text-decoration:none;padding:5px 11px;border-radius:6px;
  border:1px solid var(--line-2);color:var(--ink-2);transition:all .13s ease;}
.links a:hover{border-color:var(--accent);color:var(--accent);}
.links a.primary{background:var(--accent);border-color:var(--accent);color:#fff;}
.links a.primary:hover{background:var(--accent-2);border-color:var(--accent-2);color:#fff;}
@media (prefers-color-scheme: dark){
  .links a.primary,.links a.primary:hover{color:#1a1113;}
}
.tag{display:inline-block;font-size:10.5px;font-weight:700;letter-spacing:.05em;
  text-transform:uppercase;padding:2px 7px;border-radius:4px;margin-left:7px;vertical-align:2px;
  background:var(--accent-wash);color:var(--accent);border:1px solid var(--line-2);}

/* root index: category cards */
.catgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:1px;
  background:var(--line);border:1px solid var(--line);margin-top:30px;}
a.cat{background:var(--bg);padding:26px 24px;text-decoration:none;color:inherit;display:block;
  transition:background .15s ease;}
a.cat:hover{background:var(--bg-alt);}
a.cat h2{font-family:var(--serif);font-size:21px;font-weight:600;margin:0 0 8px;
  letter-spacing:-.01em;color:var(--ink);}
a.cat p{font-size:13.5px;color:var(--ink-2);margin:0 0 14px;}
a.cat .meta{font-size:12px;color:var(--accent);font-weight:700;letter-spacing:.04em;}

footer{margin-top:56px;padding-top:22px;border-top:1px solid var(--line);
  color:var(--ink-3);font-size:12.5px;line-height:1.75;}
footer p{margin:0 0 8px;max-width:74ch;}
footer a{color:var(--ink-2);}
@media(max-width:620px){
  .wrap{padding:36px 18px 56px;}
  .langSwitch{position:static;justify-content:flex-end;margin:0 0 16px;}
  .grid,.catgrid{grid-template-columns:1fr;}
}
"""

JS = """/* Shared i18n runtime — same pattern as echo-sim, htn-risk and score2-ap.
   Korean is the document default and is read straight out of the markup, so a
   page can never carry a Korean string that has no English counterpart without
   it being obvious. Each page defines I18N_EN before loading this file. */
var I18N = { ko: {}, en: (typeof I18N_EN === 'object' && I18N_EN) ? I18N_EN : {} };

(function(){
  var n = document.querySelectorAll('[data-i18n]'), i, j;
  for(i = 0; i < n.length; i++) I18N.ko[n[i].getAttribute('data-i18n')] = n[i].innerHTML;
  I18N.ko.doc_title = document.title;
  var a = document.querySelectorAll('[data-i18n-attr]');
  for(i = 0; i < a.length; i++){
    var spec = a[i].getAttribute('data-i18n-attr').split('|');
    for(j = 0; j < spec.length; j++){
      var p = spec[j].split(':');
      if(p.length === 2) I18N.ko[p[1]] = a[i].getAttribute(p[0]);
    }
  }
})();

var LANG = (function(){
  try{ var s = localStorage.getItem('tipcode-lang');
       if(s === 'ko' || s === 'en') return s; }catch(e){}
  return (navigator.language || '').toLowerCase().indexOf('ko') === 0 ? 'ko' : 'en';
})();

function t(k){
  var d = I18N[LANG];
  if(d && d[k] !== undefined) return d[k];
  return (I18N.ko[k] !== undefined) ? I18N.ko[k] : k;
}
function applyStaticI18n(){
  document.documentElement.setAttribute('lang', LANG);
  document.title = t('doc_title');
  var n = document.querySelectorAll('[data-i18n]'), i, j;
  for(i = 0; i < n.length; i++) n[i].innerHTML = t(n[i].getAttribute('data-i18n'));
  var a = document.querySelectorAll('[data-i18n-attr]');
  for(i = 0; i < a.length; i++){
    var spec = a[i].getAttribute('data-i18n-attr').split('|');
    for(j = 0; j < spec.length; j++){
      var p = spec[j].split(':');
      if(p.length === 2) a[i].setAttribute(p[0], t(p[1]));
    }
  }
  var kb = document.getElementById('lang-ko'), eb = document.getElementById('lang-en');
  if(kb) kb.setAttribute('aria-pressed', LANG === 'ko');
  if(eb) eb.setAttribute('aria-pressed', LANG === 'en');
}
function setLang(l){
  if(l !== 'ko' && l !== 'en') return;
  LANG = l;
  try{ localStorage.setItem('tipcode-lang', l); }catch(e){}
  applyStaticI18n();
}
applyStaticI18n();
"""

TOGGLE = """  <div class="langSwitch" role="group" aria-label="Language / 언어">
    <button type="button" id="lang-ko" onclick="setLang('ko')" aria-pressed="true">한국어</button>
    <button type="button" id="lang-en" onclick="setLang('en')" aria-pressed="false">EN</button>
  </div>
"""


def page(prefix, title_ko, desc_ko, en, body, extra_head=""):
    return """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#7d2231">
<title>%(title)s</title>
<meta name="description" data-i18n-attr="content:meta_desc" content="%(desc)s">
<link rel="stylesheet" href="%(prefix)sassets/site.css">
%(extra)s</head>
<body>
<div class="wrap">
%(toggle)s%(body)s
</div>
<script>
var I18N_EN = %(en)s;
</script>
<script src="%(prefix)sassets/i18n.js"></script>
</body>
</html>
""" % {"title": title_ko, "desc": desc_ko, "prefix": prefix, "extra": extra_head,
       "toggle": TOGGLE, "body": body,
       "en": json.dumps(en, ensure_ascii=False, indent=2)}


def footer(en):
    en["f_1"], en["f_2"] = FOOT_EN[0], FOOT_EN[1]
    en["byline"] = SITE["byline_en"]
    return ("""  <footer>
    <p data-i18n="f_1">%s</p>
    <p data-i18n="f_2">%s</p>
    <p data-i18n="byline">%s</p>
  </footer>""" % (FOOT_KO[0], FOOT_KO[1], SITE["byline_ko"]))


def tool_card(tl):
    tag = ""
    if tl.get("tag"):
        tag = '<span class="tag">%s</span>' % tl["tag"]
    elif tl.get("tag_ko"):
        tag = '<span class="tag">%s</span>' % tl["tag_ko"]
    key = tl.get("key") or tl["repo"].replace("-", "_").replace(".", "_")
    links = []
    if tl.get("live"):
        links.append('<a class="primary" href="%s" data-i18n="open">열기</a>' % tl["live"])
    links.append('<a href="%s%s">GitHub</a>' % (GH, tl["repo"]))
    return ("""      <div class="card">
        <h3 data-i18n="%s_h">%s%s</h3>
        <p class="slug">%s</p>
        <p class="desc" data-i18n="%s_d">%s</p>
        <div class="links">%s</div>
      </div>""" % (key, tl["ko"], tag, tl["repo"], key, tl["dko"], "".join(links)))


def build(out):
    os.makedirs(os.path.join(out, "assets"), exist_ok=True)
    open(os.path.join(out, "assets", "site.css"), "w", encoding="utf-8").write(CSS)
    open(os.path.join(out, "assets", "i18n.js"), "w", encoding="utf-8").write(JS)

    # ---- root ----
    en = {"doc_title": "Cardiology tools — Kang-Un Choi",
          "meta_desc": "Clinical calculators, teaching simulators, imaging workflow tools and research harnesses in cardiology",
          "eyebrow": "Cardiology · Clinical Tools &amp; Research Harnesses",
          "title": SITE["title_en"], "lede": SITE["lede_en"]}
    cats = []
    for c in CATEGORIES:
        en["c_%s" % c["dir"]] = c["en"]
        en["c_%s_n" % c["dir"]] = c["note_en"]
        en["c_%s_m" % c["dir"]] = "%d tools →" % len(c["tools"])
        cats.append("""    <a class="cat" href="%s/">
      <h2 data-i18n="c_%s">%s</h2>
      <p data-i18n="c_%s_n">%s</p>
      <span class="meta" data-i18n="c_%s_m">도구 %d개 →</span>
    </a>""" % (c["dir"], c["dir"], c["ko"], c["dir"], c["note_ko"],
                c["dir"], len(c["tools"])))
    body = """  <header class="masthead">
    <p class="eyebrow" data-i18n="eyebrow">Cardiology · Clinical Tools &amp; Research Harnesses</p>
    <h1 data-i18n="title">%s</h1>
    <p class="lede" data-i18n="lede">%s</p>
  </header>

  <div class="catgrid">
%s
  </div>

%s""" % (SITE["title_ko"], SITE["lede_ko"], "\n".join(cats), footer(en))
    open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(
        page("", "심장내과 임상 도구 모음", "심장내과 임상 계산기 · 교육 시뮬레이터 · 진료 워크플로 도구 · 연구 하네스 모음", en, body))

    # ---- one page per category ----
    for c in CATEGORIES:
        en = {"doc_title": "%s — Cardiology tools" % c["en"].replace("&amp;", "&"),
              "meta_desc": c["note_en"], "title": c["en"], "lede": c["note_en"],
              "crumb": 'Cardiology tools', "open": "Open",
              "eyebrow": "Cardiology · Clinical Tools &amp; Research Harnesses"}
        for tl in c["tools"]:
            key = tl.get("key") or tl["repo"].replace("-", "_").replace(".", "_")
            tag = ""
            if tl.get("tag"):
                tag = '<span class="tag">%s</span>' % tl["tag"]
            elif tl.get("tag_en"):
                tag = '<span class="tag">%s</span>' % tl["tag_en"]
            en["%s_h" % key] = tl["en"] + tag
            en["%s_d" % key] = tl["den"]
        cards = "\n".join(tool_card(tl) for tl in c["tools"])
        body = """  <p class="crumb">← <a href="../" data-i18n="crumb">심장내과 임상 도구 모음</a></p>
  <header class="masthead">
    <p class="eyebrow" data-i18n="eyebrow">Cardiology · Clinical Tools &amp; Research Harnesses</p>
    <h1 data-i18n="title">%s</h1>
    <p class="lede" data-i18n="lede">%s</p>
  </header>

  <div class="grid">
%s
  </div>

%s""" % (c["ko"], c["note_ko"], cards, footer(en))
        d = os.path.join(out, c["dir"])
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(
            page("../", "%s — 심장내과 임상 도구" % c["ko"].replace("&amp;", "&"),
                 c["note_ko"], en, body))
    return out


if __name__ == "__main__":
    o = build(sys.argv[1] if len(sys.argv) > 1 else "./out")
    for root, _, fs in os.walk(o):
        for f in sorted(fs):
            p = os.path.join(root, f)
            print("%8d  %s" % (os.path.getsize(p), os.path.relpath(p, o)))
