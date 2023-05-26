import nav

def content(title="",author="",description="",css="style.css",
           favicon="favicon.png",
           header="",nav=nav.content(),main="",
           footer=""):
  return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <meta name="author" content="{author}">
    <link rel="shortcut icon" href="{favicon}">
    <xlink rel="stylesheet" href="normalize.css">
    <link rel="stylesheet" href="{css}">
    <!--[if lt IE 9]>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv.js"></script>
    <![endif]-->
  </head>
  <body>
    <header>{header}</header>
    <nav>{nav}</nav>
    <main>{main}</main>
    <footer>{footer}</footer>
  </body>
</html>"""
