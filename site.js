addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll("h2,h3").forEach(function (h) {
    if (!h.id) {
      var s = h.textContent.trim().toLowerCase().replace(/[^a-z0-9]+/g, "-");
      if (s.charAt(0) === "-") s = s.slice(1);
      if (s.charAt(s.length - 1) === "-") s = s.slice(0, -1);
      h.id = s;
    }
  });
  var k = [38, 38, 40, 40, 37, 39, 37, 39, 66, 65], i = 0;
  addEventListener("keydown", function (e) {
    i = (e.keyCode === k[i]) ? i + 1 : 0;
    if (i === k.length) { document.body.classList.toggle("konami"); i = 0; }
  });
});
