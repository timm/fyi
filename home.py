import _template

def forhead(back="white",front="black"):
    return f"""<td width="33%" style="background-color: {back}; color: {front};text-align: center; font-weight: bold;">"""

def main(): return f"""

<img style="background-color: white;" align=left width=300 src="assets/img/head.png">
<h1>se 4 ml 4 good</h1>

<em><p> It's an ML world.  
But is that software being  used, as it should? Is it optimized? Unbiased? Explainable? 

<p>Maybe  someone should look into that ...</p></em>

<p style="background-color: yellow;">I seek <b>talented</b> graduate students to find and fix (as much as we can) the
<b>short-comings in real-world ML</b>. 
<a href="students.html">Is that you?</a></p>
<p>Tim Menzies (<b>IEEE Fellow</b>, Ph.D., UNSW, 1995) is a <b>full Professor</b> in CS at North Carolina State
where he explores how SE can improve optimization, ethics, and explainable AI.
He is the director of the RAISE lab (real world AI for SE) and the author of over <b>280 publications</b>
 (refereed) with 20,000+ citations and an h-index of 69.  
He has graduated <b>20 Ph.D. students</b>, and has been a 
lead researcher on projects for NSF, NIJ, DoD, NASA, USDA (total funding of 
<b>$13+ million</b>) as well as joint research work with private companies. Prof. Menzies is the 
<b>editor-in-chief</b> of the Automated Software Engineering journal and 
<b>associate editor of TSE</b>  (IEEE Transactions on Software Engineering) and other leading SE journals. 
For more, see his web site https://timm.fyi. </p>

<table cellpadding="3px" ><tr>
{forhead("yellow")}        For students</td>
{forhead("green","white")} For indusry</td>
{forhead("orange")}        For researchers</td>
</tr>
<tr><td valign=top> 
       <a href="students.html">Ask me how to ...</a>
      <ul>
      <li>Accelerate your SE career:<br>in research and/or industry. 
       <lI>Optimize ML systems. 
       <li>Dramatically reduce ML's cost.
       <li>Make AI explainable.
       <li>Measure and mitigate ML discrimination.
       </ul>
 </td><td valign=top>
 Want to innovate on time, on budget?
       <a href="industry.html">Ask me how.</a>

</td><td valign=top>
<b>About me:</br>
</td></tr></table>
"""


print(_template.content(main=main()))
