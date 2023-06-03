import _nav

def content(title="",author="",description="",css="style.css",
           favicon="favicon.ico",
           header="",nav=_nav.content(),main="",
           footer=""):
  return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <meta name="author" content="{author}">
    <link rel="icon" type="image/x-icon" href="{favicon}">
    <link rel="stylesheet" href="normalize.css">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <link href='https://fonts.googleapis.com/css?family=EB Garamond' rel='stylesheet'>
    <link href='https://fonts.googleapis.com/css?family=Dejavu Sans' rel='stylesheet'>
    <xlink href='https://fonts.googleapis.com/css?family=Lato' rel='stylesheet'>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="{css}">
    <!--[if lt IE 9]>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv.js"></script>
    <![endif]-->
  </head>
  <body>
   <div id=wrap>
    <header>{header}</header>
    <main>{main}</main>
    <footer>{footer}</footer>
   </div>
  </body>
</html>"""
