#!/usr/bin/env python3
"""rawify.py — regenerate raw/ versions of blog posts.

Takes each root-level post <slug>.html (fancy version), extracts the
content between its first <hr> (end of nav) and last <hr> (start of
foot), rewrites relative links to ../ (except links to sibling posts,
which stay inside raw/), and wraps it in the raw/ chrome.

Usage: python3 etc/rawify.py [slug ...]     (default: all SLUGS)
Run from the repo root. Idempotent — safe to re-run any time.
Add new posts to SLUGS below.
"""
import re, sys, pathlib

SLUGS = ("tournament unstable snap2 drr luk ezr2 ezr "
         "symbolic_ai higher_way compact_ai").split()

HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{desc}">
<title>{title}</title>
<link rel="icon" type="image/png" href="../favicon.png">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Ubuntu+Mono:ital,wght@0,400;0,700;1,400&display=swap">
<style>
html {{ background: white; }}
body {{ max-width: 600px; margin: 10px auto; padding: 10px; font-size: 13px; line-height: 1.4; color: black; font-family: "Ubuntu Mono", "Courier New", monospace; }}
h1,h2,h3 {{ margin: 0.9em 0 0.3em; }}
center h2 {{ margin: 0.3em 0; }}
h2   {{ font-size: 22px; }}
center.top {{ background: #cc0000; color: white; padding: 3px 10px; margin-bottom: 5px; }}
center.top a {{ color: white; }}
a    {{ color: #cc0000; text-decoration: none; }}
a:hover {{ text-decoration: underline; }}
p.card {{ padding: 0.5em 0.8em; background: whitesmoke; }}
pre  {{ background: whitesmoke; padding: 0.6em 0.8em; overflow-x: auto; }}
img  {{ max-width: 100%; }}
hr   {{ display: none; }}
.f   {{ font-size: small; }}
center {{ text-align: left; }}
.hd  {{ display: flex; justify-content: space-between; gap: 10px; }}
.rhs {{ display: flex; flex-direction: column; justify-content: space-between; text-align: right; }}
.hd p {{ text-align: right; }}
a.cta {{ background: #cc0000; color: white; padding: 3px 10px; display: inline-block; margin-top: 2px; }}
@media (max-width: 480px) {{
  .hd {{ flex-direction: column; }}
  .hd p, .rhs {{ text-align: left; }}
}}
</style>
</head>
<body>

<center class="f top"><span style="float: right;"><a href="index.html">home</a></span>Tim Menzies &middot; prof &middot; <a href="https://www.csc.ncsu.edu/">cs</a> &middot; <a href="https://www.ncsu.edu/">NC State</a></center>

<center>
<div class="hd">
<p><img src="timm.png" width="240" alt="Tim Menzies"></p>
<div class="rhs">
<p class="f"><a href="research.html">research</a> |
<a href="teach.html">teach</a> |
<b><a href="blog.html">blog</a></b> |
<a href="news.html">news</a><br>
papers: <a href="https://arxiv.org/search/?searchtype=all&amp;query=tim+menzies">arxiv</a> |
<a href="https://scholar.google.com/citations?user=7htTUTgmLtUC">Scholar</a> |
<a href="research.html">by topic</a></p>
<h2>{h1}</h2>
<p class="f"><a href="mailto:timm@ieee.org">timm@ieee.org</a><br>
+1-304-376-2859<br>
<a class="cta" href="https://calendar.app.google/D1Pm35W7kd66pDUw5">make appointment</a><br>
<a class="cta" href="https://forms.gle/yQuFkgrP3Kkq68Dk6">join reading group</a></p>
</div>
</div>
<hr>
</center>

'''

FOOT = '''

<center class="f" style="text-align: center;">
<img src="badges/construction.gif" width="88" height="31" alt="under construction">
<img src="badges/best_ns.gif" width="88" height="31" alt="best viewed with netscape navigator 3">
<img src="badges/geocities-official.gif" width="88" height="31" alt="geocities official">
<br>
visitors: <span style="background: black; color: #33ff33; padding: 1px 5px; letter-spacing: 2px;">000042</span><br>
<a href="https://wholeearth.info/">&ldquo;We can&rsquo;t put it together. It is together.&rdquo;</a>
</center>

</body>
</html>
'''

def fix_url(m):
    attr, url = m.group(1), m.group(2)
    if re.match(r'(https?:|mailto:|tel:|#|\.\./)', url):
        return m.group(0)
    stem = url.split('#')[0]
    if stem.endswith('.html') and stem[:-5] in SLUGS:  # sibling post -> raw twin
        return f'{attr}="{url}"'
    return f'{attr}="../{url}"'

def rawify(slug):
    src = pathlib.Path(f'{slug}.html').read_text()
    title = re.search(r'<title>(.*?)</title>', src, re.S).group(1).strip()
    d = re.search(r'<meta name="description" content="(.*?)">', src, re.S)
    desc = re.sub(r'\s+', ' ', d.group(1)) if d else title
    parts = src.split('<hr>')
    content = '<hr>'.join(parts[1:-1]).strip()  # first <hr> .. last <hr>
    content = re.sub(r'(href|src)="([^"]*)"', fix_url, content)
    content = re.sub(r'<i class="fa-[^"]*"></i>(&nbsp;)?\s*', '', content)
    h1 = re.search(r'<h1[^>]*>(.*?)</h1>\n?', content, re.S)
    content = content.replace(h1.group(0), '', 1) if h1 else content
    h1 = re.sub(r'\s+', ' ', h1.group(1)).strip() if h1 else title
    content = re.sub(  # byline: name/email/site now live in the chrome
      r'<p>Tim Menzies <a[^>]*>timm@ieee\.org</a>\s*·\s*<a[^>]*\n?[^>]*>timm\.fyi</a>\s*·\s*',
      '<p class="f">', content, count=1)
    summary = f'<p class="card"><b>Summary</b><br>\n{desc}</p>\n\n'
    out = HEAD.format(title=title, desc=desc, h1=h1) + summary + content + FOOT.format(slug=slug)
    pathlib.Path(f'raw/{slug}.html').write_text(out)
    print(f'raw/{slug}.html')

if __name__ == '__main__':
    for slug in (sys.argv[1:] or SLUGS):
        rawify(slug)
