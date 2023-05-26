import _template

def forhead(back="white",front="black"):
    return f"""<td width="33%" style="background-color: {back}; color: {front};text-align: center; font-weight: bold;">"""

def main(): return f"""


<h1>Tim Menzies:
se 4 ai, 4 good!</h1>
<img style="background-color: white;" align=right width=300 src="assets/img/head.png">
<em><p> It's an AI world.  
But is that software being  used, as it should? Is it optimized? Unbiased? Explainable? 

<p>Maybe  someone should look into that...</p></em>

<p style="background-color: yellow;">I seek <b>talented</b> graduate students to find and fix (as much as we can) the
<b>short-comings in real-world AI/ML</b>. 
<a href="students.html">Is that you?</a></p>
<hr>
<p>
Tim Menzies (<b>IEEE Fellow</b>, Ph.D., UNSW, 1995) is a <b>full Professor</b> in CS at North Carolina State
where he explores how SE can improve optimization, ethics, and explainable AI.
He is the director of the RAISE lab (real world AI for SE) and the author of over <b>280 publications</b>
 (refereed) with 20,000+ citations and an h-index of 69.  
He has graduated <b>18 Ph.D. students</b>, and has been a 
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
       <lI>Optimize AL/ML systems. 
       <li>Dramatically reduce ML's cost.
       <li>Make AI explainable.
       <li>Measure and mitigate ML discrimination.
       </ul>
 </td><td valign=top>
       <a href="industry.html">Ask me how</a>
 to innovate on time, on budget. 
 I've done this with many companies. For example:
 <ul>
              <li>
                <a href="https://pdfs.semanticscholar.org/ae7d/96ee5c7838343a7cf176d008cf3eaaeba1ef.pdf">Microsoft</a>;
                <li> <a href="https://www.sbir.gov/sbirsearch/detail/4945">Grammatech</a>;
                  <li><a href="http://www.slideshare.net/timmenzies/172529main-ken-andtimsoftwareassuranceresearchatwestvirginia?qid=4ddfaa48-dea3-4397-800b-74170c2722da&amp;v=&amp;b=&amp;from_search=4">NASA</a>;
                    <li><a href="https://goo.gl/XtT1OI"> CSIRO</a>
                    <li>LexisNexis: e.g. <a href= "http://www.slideshare.net/slideshow/embed_code/key/f8etbZ448ukfOs">1</a>,<a 
                                       href="pdf/Best_Practice_SE_text_mining.pdf">2</a>,<a 
                                       href="pdf/LNPoster2018GREEN.pdf">3</a>,<a 
                                       href="https://arxiv.org/pdf/1905.07019.pdf">4</a>.<a 
                                       href="https://arxiv.org/pdf/1905.06390.pdf">5</a>;<br>
                                     <li>         IBM: e.g. <a href= "https://github.com/timm/16/blob/master/matt.pdf">1</a>,<a 
                                                         href= "https://arxiv.org/pdf/1711.03933.pdf">2</a>,<a 
                                                         href="https://arxiv.org/pdf/1710.09055.pdf">3</a>,<a 
                                                         href="https://arxiv.org/pdf/1710.08736.pdf">4</a>;
            </ul>

</td><td valign=top>
<ul>
<li>Grants: 13.3 million (total) 
<li>Students: 18 Ph.D. (past) + 6 (current). 
<li>H-index: 69 (May'23)
<li>Papers: 108 journal + 137 conference + 86 other
<li>EIC, ASE journal; 
<li>Current/past AE for TSE, TOSEM, EMSE, CACM, IST, ASEj
<li>Co-general chair: ICMSE'16; RAISE'19, PROMISE'05..'12
<li>co-PC chair: ASE'12, NEIR'15, SSBSE'17, PROMISE'20
<li>PC member: ICSE'23, SANER'23, ICSE'22, IJCAI'22, AAAI'22, ICML'22, MSR'22, ESEM'22, IJCAI'21. AAAI'21, ICSE'21, MSR'21, ASE'20, ICSE'20, ESEM'20, FSE'19, ASE'19, MSR'19, SSBSE, PROMISE,...
<li>
IEEE Technical Council on SE. 2022, 2021
<li>
NASA software research chair: 2002-2004
<li>
NSF panelist: 13 times (2003-2020)
</ul>
</td></tr></table>
"""


print(_template.content(main=main()))
