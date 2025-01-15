
import _template

def forhead(back="white",front="black"):
    return f"""<td swidth="33%" style="background-color: {back}; color: {front};text-align: center; font-weight: bold;">"""

def main(): return """
<script>
function openCity(cityName) {
  var i;
  var x = document.getElementsByClassName("city");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";  
  }
  document.getElementById(cityName).style.display = "block";  
}
</script>
""" + f"""


<p style="text-align:left; margin-bottom: 5px; padding-bottom: 0px;">

<a href="https://scholar.google.com/citations?user=7htTUTgmLtUC&hl=en&authuser=1">papers
<i class="ai ai-google-scholar ai-lg"></i></a>
 &nbsp;|&nbsp;  <a href="https://arxiv.org/search/?searchtype=all&query=tim+menzies&size=200&order=-announced_date_first">pre-prints
<i class="ai ai-arxiv ai-lg"></i></a>
 &nbsp;|&nbsp; 
<a href="https://dblp.org/pid/m/TimMenzies.html">dblp <i class="ai ai-dblp ai-lg"></i></a>
<span style="float:right; margin-bottom: 0px; padding-bottom:0px;">

<i class="fa-solid fa-envelope fa-xl"></i> <a href="mailto:timm@ieee.org">timm@ieee.org</a>  
 &nbsp;|&nbsp; <i class="fa-solid fa-phone fa-xl"> </i> +1-304-376-2859
 &nbsp;|&nbsp; <i class="fa-solid fa-map fa-xl"> </i> rm 3304, EB2 (<a href="https://www.csc.ncsu.edu/department/map/CSCMapDirections.pdf">map</a>)

                    </span>
                    </p>
<img style="xpadding-bottom:8px; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.3), 0 6px 20px 0 rgba(0, 0, 0, 0.3);" width="100%" src="assets/img/timm2.png">
<center>
<p>&nbsp;</p>
<font color=#CC0000><p> So I seek <b>talented</b> grad students &amp;
<b>industrial partners</b> to find + fix the
<b>problems in real-world AI/ML</b>. <br><b>Is that you?</b>  Maybe "yes" if  <b>you want to be a leader in AI</b> (and not just another follower). </p></font>
 <a href="https://www.youtube.com/playlist?list=PLOgGLL2KRJ7x1qbFQjzDn1tCjCHAw6pGo">videos
<i class="fab fa-youtube fa-lg"></i></a> 
|
 &nbsp; 
<a href="https://www.goodreads.com/review/list/1469588-tim-menzies?ref=nav_mybooks"><i class="fab fa-goodreads fa-lg"></i></a>
 &nbsp; 
<a href="https://www.facebook.com/tim.menzies"><i class="fab fa-facebook fa-lg"></i></a>
 &nbsp; 
<a href="https://twitter.com/timmenzies?lang=en"><i class="fab fa-twitter fa-lg"></i></a>
 &nbsp; 
<a href="https://www.linkedin.com/in/tim-menzies-444183"><i class="fab fa-linkedin fa-lg"></i></a>
</center>
<hr>
<table xcellpadding=10px ><tr>
<td width=50% valign=top>

<b>News:</b>
<ul>
 <li id="">  <b>Jan'25</b>: Elected ACM Fellow
 <li id="">  <b>Jan'25</b>: New grant, $310K Better fuzzing, with L3harris
 <li id="">  <b>Dec'24</b>: Podcast, <a href="https://newbooksnetwork.com/diversify-your-publishing-portfolio-an-interview-with-tim-menzies">Diversify Publishing</a>
 <li id="">  <b>Nov'24</b> Paper, IEEE Software <a href="https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10705752">AI Over-Hype</a>
 <li id="">  <b>Nov'24</b> Paper, IEEE ACCESS <a href="https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10438420">Data Synthesis</a>
 <li id="">  <b>Nov'24</b>: Xueqi  Yang completes her Ph.D.
 <li id="">  <b>Oct'24</b> Tutorial, ASE'24 <a href="http://tiny.cc/ models24">Understandable Models</a>
 <li id="">  <b>Oct'24</b> Paper, EMSE <a href="https://arxiv.org/pdf/2211.05920"> "Co-training" for SSL</a>
 <li id="">  <b>Sept '24</b> Tutorial, Models'24 <a href="http://tiny.cc/ models24">Understandable Models</a>
 <li id="">  <b>Sept'24</b>: Elected ASE Fellow
 <li id="">  <b>Sept'24</b>: Rahul Yedida completes his Ph.D.
 <li id="">  <b>July'24</b> Paper, TSE <a href="https://arxiv.org/pdf/2107.08310">How to Achieve Equalized Odds</a>
 <li id="">  <b>June'24</b>: Kewen Peng completes his Ph.D.
 <li id="">  <b>June'24</b>: Xiao Ling completes his Ph.D.
         <!-- li> <button class="w3-bar-w3-round item w3-button" style="background-color:#CC0000;"
    border:0px solid #CC0000;  " onclick="openCity('News')"><font color="white"><b><u>More news</u></b></font></button --->
  </ul>
          </td>
          <td>&nbsp;</td>
<td width=43% valign=top>
Tim Menzies (<b>ACM Fellow</b>, <b>IEEE Fellow</b>, <b>ASE Fellow</b>, Ph.D., UNSW, 1995) is a <b>full Professor</b> in Computer Science at North Carolina State
where he explores how 
to make best dcisions using the least amount of data.
He is the director of the Irrational Research lab (mad scientists r'us) and the author of over
<b>300 publications</b>
 (refereed) with 24,000 citations and an h-index of 74.  
He has graduated <b>22 Ph.D. students</b>, and has been a 
lead researcher on projects for NSF, NIJ, DoD, NASA, USDA (total funding of 
<b>$13+ million</b>) as well as joint research work with private companies.
Prof. Menzies is the 
<b>editor-in-chief</b> of the Automated Software Engineering journal and 
<b>associate editor of TSE</b>  (IEEE Transactions on Software Engineering) and other leading SE journals. 
For more, see his web site https://timm.fyi. 
</td>
          </tr></table>
<hr>
<p>
Currently:
<lul>
<li><b>Editor-in-chief:</b> Automated Software Engienering journal
<li><b>Editorial Board:</b> Communications of the ACM (opinions)
<li><b>Associate Editor:</b> IEEE Trans SE, IEEE Software (SE+ethics) 
<li><b>Track co-chair:</b> ESEM'25 (doctoral symposium)
<li><b>Program committees:</b> ICSE'26, ICSE'25, FSE'25, SANER'25, ESEM'25, CAIN'25, AAAI(ethics)'25
</p>
<!----

<hr>

<div class="w3-bar w3-black" xstyle="padding:20px;"> 
<center>
  <button class="w3-bar-item w3-button" style="border:1px solid #CCC; border-radius: 8px; solid #CCC; background-color:yellow; xpadding-top:12px;" onclick="openCity('For Students')"><h4>For Students</h4></button>
  &nbsp;&nbsp;<b> </b>&nbsp;&nbsp;
  <button class="w3-bar-item w3-button" style="xpadding-top:12px; border:1px solid #CCC;  border-radius: 8px; background-color:lightblue; " onclick="openCity('For Industry')"><h4>For Industry</h4></button>
  &nbsp;&nbsp;<b> </b>&nbsp;&nbsp;
  <button class="w3-bar-item w3-button" style="xpadding-top:12px; border:1px solid #CCC;  border-radius: 8px; background-color:orange;" onclick="openCity('For Researchers')"><h4>For Researchers</h4></button>
</center>
</div>

<div id="News" class="w3-container city" style="display:none">
<hr>
          <h5>News Archive</h5>
 <p> <b>Papers:</b> <ul>
            <li id="">    <b>Feb'23</b>: To appear, Expert Systems with Applications: <a href="https://arxiv.org/pdf/2109.14569.pdf">Redesigning Cloud Applications</a>
              <li id="dim"> <b>Jan'23</b>: Accepted to TOSEM:  <a href="https://arxiv.org/pdf/2105.11082.pdf">Assessing Early Bird Heuristic</a>
            <li id="dim"> <b>Jan'23</b>: Accepted to TOSEM: <a href="https://arxiv.org/pdf/2110.13029.pdf">Fair Enough: Searching for Sufficient Measures of Fairness</a>
  <Li id="dim"> <b>Feb'23</b>: For ICSE'23 journal first. Reports on <a href="https://arxiv.org/pdf/2208.01595.pdf">vulnerabilities</a>; <a href="https://arxiv.org/pdf/2110.01109.pdf">Fair-Mask</a>; <a href="https://arxiv.org/pdf/2201.10592.pdf">labeling cost</a>
            <li id="dim"> <b>Feb'23</b>: To appear, IEEE Software: <a href="https://arxiv.org/pdf/2301.10407.pdf">Avoiding Malicious Explanations</a>
            <li id="">    <b>Jan'23</b>: To appear, IEEE Software: <a href="pdf/ethicalMindset.pdf">Engineering Ethical Mindset</a>
		        <li id="">    <b>Jan'23</b>: Accepted to EMSE: <a href="https://arxiv.org/pdf/2106.02716.pdf">Enhancing the Interpretability of Model-based Optimizations</a>
            <li id="">    <b>Dec'22</b>: Accepted to IEEE TSE: <a href="pdf/tseStaticCode22.pdf">How to Find Actionable Static Analysis Warnings</a></li>
            <li id="dim"> <b>Dec'22</b>: 2022 papers = <a href="https://dblp.org/pid/m/TimMenzies.html">TSE*8 + EMSE*6 + TOSEM*2 + MSR*3 + other*3</a> </li>
            <li id="">    <b>Oct'22</b>: new TSE journal paper:  <a href="https://arxiv.org/pdf/2110.01109.pdf">FairMask</a>:v.fast multi-attribute fairness</li>
            <li id="dim"> <b>June'22</b>: journal paper: EMSE, Predicting next year's project health, <a href="https://link.springer.com/article/10.1007/s10664-022-10171-0">for 1200 projects</a>.</li>
            <li>...
         </ul>
         <b> Talks:</b>
            <ul> 
            <li id=""> <b>Dec'22</b>: invited as a "Future of SE" speaker, for ICSE'23</li>
            <li id="dim"> <b>Dec'22</b>: invited talk, RIT</b>: Refactoring AI for SE</a></li>
            <li id=""> <b>Nov'22</b>: briefing, MSR'23</b>: <a href="http://tiny.cc/22review">Reviewer 2: Go F’yourself (not) </a></li>
            <li id=""> <b>Nov'22</b>: keynote, SSBSE'21</b>: <a href="http://tiny.cc/22search">Future of (S)SBSE</a> </li>
              <li id="dim"> <b>Nov'22</b>: keynote, ISSRE</b>: <a href="http://tiny.cc/22issre">How to refactor AI (for SE)</a> </li>
              <li id=""> <b>Oct'22</b>: keynote, ISSRE</b>: <a href="http://tiny.cc/advice22">Advice to new faculty</a> 
              <li id="dim"> <b>Oct'22</b>: keynote, ASE 2022</b>: Advice to Ph.D. students [<a href="https://docs.google.com/presentation/d/e/2PACX-1vSP6M_fILGT_It9R9A8w0B-8F3b0Tjo76Mlg04dEGP3SD6gfM5uWqZzQ7VrJ89zd6YQHX6KzW9WQdQC/pub?start=false&loop=false&delayms=3000">slides</a>]</li> 
              <li id=""> <b>May'22</b>: 12 ICSE talks done, just 7 left to go. Oy vey.</li>
              <li id="dim"> <b>Mar 1,'22</b>: invited as keynote speaker for ISSRE'22.</li>
              <li>...
            </ul>
            <b>Grants:</b>
            <ul>
            <li id="">    <b>Mar'23</b>: New gift from DivePlane: studies on surrogate data ($50K)
              <li id=""> <b>Oct'22 </b>: new Grant, Learning Analytical Sciences: $170K. SSL for DL</li>
              <li id="dim"> <b>Oct'22 </b>: ICSE accepts our workshop proposal for FAIRWARE'23</li>
              <li id=""> <b>Sept'22</b>: gift from Meta: $50K. Much appreciated.</li>
              <li id="dim"> <b>Oct'22 </b>: new Grant, Learning Analytical Sciences: $170K. SSL for DL</li>
              <li>...
            </ul> <b>Service:</b><ul>
		        <li id="dim"> <b>Mar'23</b>: ICSE'23 accepts our <a href="https://conf.researchr.org/track/icse-2023/rose-festival">ROSE'23 proposal</a> (open science in SE).
            <Li id="">    <b>Mar'23</b>: Invited to PC of ICSE'24 NIER track
            <Li id="dim"> <b>Feb'23</b>: Invited to the review board for 2024 IEEE Fellow applications.
            <Li id="">    <b>Feb'23</b>: Invited to ESEM'23 program committee.
		        <li id="dim"> <b>Dec'22</b>: Journal of Systems and Softwares accept special issue proposal for FAIRWARE'23 papers</i>
            <li id=""> <b>Dec'22</b>: invited to IJCAI'23 program committee;</li>
              <li id="dim"> <b>Nov'22</b>: invited, PC member, EASE'23</li>
              <li id=""> <b>Oct'22</b>: invited, PC member, CAIN'23</li>
              <li id="dim"> <b>May 9,'22</b>: Fairware'22 (equitable SE technology) a <a href="https://fairwares.github.io">great success</a>.</li> 
              <li id=""> <b>Feb 1,'22</b>: invited, PC member, ICSE'23.</li>
              <li id="dim"> <b>Mar 20,'22</b>: invited to be Associate Editor, IEEE TSE.</li>
              <li>...
            </ul>
            <b>Other:</b>
            <ul>
            <li id="dim"> <b>Jan'23</b>: Video for CACM article <a href="https://vimeo.com/783003055">Reuse is Rampant</a>
		        <li id=""> <b>Dec'22</b>: my latest grad, the talented <a href="https://raw.githubusercontent.com/timm/timm.github.io/master/img/xia.png">Dr Tianpei (Patrick) Xia</a> (with proud parents)</li>
            <li id="dim"> <b>Dec'22</b>: departmental newsletter on my SE subject: <a href="https://www.csc.ncsu.edu/news/2498">Making the Pitch!</a></li>
            <li id=""> <b>Dec'22</b>: 2022 funding = $220K (new) + $2.5M (on-going);</li>
            <li id="dim"> <b>Dec'22</b>: 2022 Ph.D.s = 1 (new) + 5 (completed) + 5 (on-going);</li>
            <li id=""> <b>May 6,'22</b>: just graduated 5 Ph.D. students (a new departmental record).</li>
            <li id="dim"> <b>May'22</b>: my Ph.d. students start summer work at Amazon, Indeed, Facebook.</li>
            <li>...
            </ul></p>

</div>

<div id="For Students" class="w3-container city" style="display:block">
<hr>
  </a><h3>For Students</h3>
  <table>
<tr>

<td valign=top width=30%>
<p>
             <b>My graduated Ph.D. students:</b><br>
                <a href="http://documentslide.com/documents/zhihao-scott-chen.html"><img alt="Scott Chen" width="35" height="35" align=middle src="https://raw.githubusercontent.com/timm/timm.github.io/master/img/who/scottchen.png"></a>
                <a href="http://www.messiah.edu/info/21665/our_faculty/2753/department_faculty/4"><img alt="David Owen" width="35" height="35" align=middle src="https://raw.githubusercontent.com/timm/timm.github.io/master/img/who/davidowen.png"></a>
                <a href="http://nandeshwar.info/"><img alt="Ashutosh Nandeshwar" width="35" height="35" align=middle src="https://raw.githubusercontent.com/timm/timm.github.io/master/img/who/ashutosh.png"></a>
                <a href="http://www.kocaguneli.com/"><img alt="Ekrem Kocaguneli" width="35" height="35" align=middle src="https://raw.githubusercontent.com/timm/timm.github.io/master/img/who/ekrem.png"></a>
                <a href="http://www.birzeit.edu/en/faculty-staff/abdel-salam-sayyad"><img alt="Abdel Salem Sayyad" width="35" height="35" align=middle src="https://raw.githubusercontent.com/timm/timm.github.io/master/img/who/abdel.png"></a>
                <a href="http://www.fayolapeters.com/about/"><img alt="Fayola Peters" width="35" height="35" align=middle src="https://raw.githubusercontent.com/timm/timm.github.io/master/img/who/fayola.png"></a>
                <a href="https://www.linkedin.com/in/joseph-krall-53125470/"><img alt="Joe Krall" width="35" height="35" align=middle src="https://raw.githubusercontent.com/timm/timm.github.io/master/img/who/joekrall.png"></a>
                <a href="http://greggay.com/"><img alt="Greg Gay" width="35" height="35" align=middle src="https://raw.githubusercontent.com/timm/timm.github.io/master/img/who/greg.png"></a>
                <a href="http://ai4se.net/people/2014/09/30/Wei-Fu/"><img alt="Wei Fu" width="35" height="35" align=middle src="https://raw.githubusercontent.com/timm/timm.github.io/master/img/wei.jpg"></a>
                <a href="http://ai4se.net/people/2014/10/15/Vivek-Nair/"><img alt="Vivek Nair" width="35" height="35" align=middle src="https://raw.githubusercontent.com/timm/timm.github.io/master/img/vivek.jpg"></a>
                <a href="http://ai4se.net/people/2015/09/01/Amritanshu-Agrawal/"><img alt="Amritanshu Agrawal" width="35" height="35" align=middle src="https://raw.githubusercontent.com/timm/timm.github.io/master/img/amrit.jpg"></a>
                <a href="http://ai4se.net/people/2015/08/15/Jianfeng-Chen/"><img alt="Jianfeng Chen" width="35" height="35" align=middle src="https://raw.githubusercontent.com/timm/timm.github.io/master/img/chen.jpg"></a>
                <a href="http://ai4se.net/people/2014/10/04/Rahul-Krishna/"><img alt="Rahul Krishna" width="35" height="35" align=middle src="https://raw.githubusercontent.com/timm/timm.github.io/master/img/rahlk.jpg"></a>
                <a href="http://ai4se.net/people/2015/08/30/Zhe-Yu/"><img alt="Zhe Yu" width="35" height="35" align=middle src="https://raw.githubusercontent.com/timm/timm.github.io/master/img/Zhe.jpg"></a>
                <a href="http://ai4se.net/people/2017/09/02/Huy-Tu/"><img alt="Joymallya Chakraborty" width="35" height="35" align=middle src="https://raw.githubusercontent.com/timm/timm.github.io/master/img/img-joy.png"></a>
                <a href="https://rshu.github.io"><img alt="Rui Shu" width="35" height="35" align=middle src="https://raw.githubusercontent.com/timm/timm.github.io/master/img/img-riu.png"></a>
                <a href="http://ai4se.net/people/2017/09/02/Huy-Tu/"><img alt="Shrikanth Chandrasekaran" width="35" height="35" align=middle src="https://raw.githubusercontent.com/timm/timm.github.io/master/img/img-shrikamtj.png"></a>
                <a href="http://ai4se.net/people/2017/09/01/Tianpei-Xia/"><img alt="Tianpei Xia" width="35" height="35" align=middle src="assets/img/who/Patrick.png"></a>
                <a href="http://ai4se.net/people/2017/09/02/Huy-Tu/"><img alt="Huy Tu" width="35" height="35" align=middle src="assets/img/who/huy.jpeg"></a>
</p>
<p>
      <b> My current Ph.D. students:</b></br>
                <a href="http://ai4se.net/people/2017/09/02/Huy-Tu/"><img alt="Xueqi(Sherry) Yang" width="35" height="35" align=middle src="https://raw.githubusercontent.com/timm/timm.github.io/master/img/img-cherry.png"></a>
<a href="https://www.linkedin.com/in/xiao-ling-339a15189/"><img align=middle alt="Xiao Ling" src="assets/img/head.png" width=35 height=35></a>
                <a href="http://ai4se.net/people/kewenPeng"><img alt="Kewen Peng" width="35" height="35" align=middle src="assets/img/who/KewenPeng.jpeg"></a>
                <a href="https://www.suvodeepmajumder.us"><img alt="Suvodeep Najumder" width="35" height="35" align=middle src="https://raw.githubusercontent.com/timm/timm.github.io/master/img/duvodeep.png"></a>
                <a href="https://avatars0.githubusercontent.com/u/30708955?s=460&amp;v=4"><img alt="Andre Motta" width="35" height="35" align=middle src="https://avatars0.githubusercontent.com/u/30708955?s=460&amp;v=4"></a>
                <a href="https://yrahul3910.github.io/whyrahul/"><img alt="Andre Motta" width="35" height="35" align=middle src="https://raw.githubusercontent.com/timm/timm.github.io/master/img//rahulYedida.png"></a>
            </p>

</td>
<td width=30px></td>
<td valign=top >
 <p><a href="#students">Ask me how to </a> </b>
      accelerate your SE career (in research and/or industry). For example, by exploring:
      <ul>
       <lI>Optimizing AL/ML systems. 
       <li>Dramatically reducing ML's cost.
       <li>Making AI explainable.
       <li>Measuring and mitigating ML discrimination.
       </ul>

       See also my work on  learning significant patterns from software project data:
       <ul><li>Defect prediction
             <li>Effort estimation
             <li>Configuration (including cloud config)
             <li>Static code analysis false alarms
             <li>Technical debt
              <li>Reduce cost of testing
       </ul>
</td>

</tr>
</table>
<hr>
<b>Thinking about graduate studies at NC State?</b>
            <ul>
              <li> <a href="https://www.youtube.com/watch?v=LRoI-Rw4GBY">Why NC State?</a> </li>
              <li> <a href="http://ai4se.net">My lab</a> </li>
              <li> <a href="https://docs.google.com/spreadsheets/d/1oWGEfEdt4aXZ_chBLTzw2RkKhGTKIKReetkcb8Zo2F4/edit"> My students</a> </li>
              <li> <a href="http://tiny.cc/tim17phd">How 2 b a grad student?</a> </li>
<li> <a href="http://www.ncsu.edu/grad/programs/how-to-apply/index.php">Apply here</a>.
To help you out, I list below some answers to frequently asked questions.
If the following does not answers your questions then please feel free to email me and I will do my best to reply to your queries.</p>
            </ul>

<p><img src="https://collegeinformations.com/wp-content/uploads/2012/06/Graduate-Studies.jpg" align=right width=200></p>


<p><b>Applying:</b> American universities accept new graduate students for start-of-study in mid-August and mid-January.
The application process for those dates starts months in advance. You should be planning your application at least one year before your desired start date.
I have no authority to accept students but, once they are accepted, I can supervise graduate students. So please review our admissions procedures at our departmental Web site.
That said, during the admissions review process, all faculty are sent a sheet listing the candidate students and I am allowed to "nudge" a handful of names. So if you elect to enroll here then please ping me so I can watch for your application in the system.</p>

<p><b> Tips for writing to Professors:</b>
When writing to a CS prof in the USA, here is a big tip on how to attract their attention.
<b>Do not send a form letter</b>-- we get enough of those.
To prove that you are not sending a form letter, best to make some reference to their current research, perhaps even to one of their recent papers (and how your prior work or interests match up).
Demonstrate that you have done a little homework before sending and email about the department. E.g.</p>

<ul>
    <li>Read over the department's recruitment policies and say things like "I am targeting an application for your next round of applications for (say) January 2016 which I will submit to <insert correct email name or web page reference here>".</li>
</ul>

<p><b>Working with me</b>:
As to me supervising you, I do not take on students until they have completed one of my grad subjects. This lets us check each other out before we commit too much to each other.
As to funding, I do not guarantee that my supervised students get funding from me. Funding comes and goes depending on the whims of the funding agencies and my policy is to fund my long-term Ph.D. students before anyone else.</p>

<ul>
    <li>That said, for your information, over the last decade, 75% of my students were fully funded.</li>
</ul>
<hr>
<a a name=fall2023><h4>Fall 2023 Indepdent Study Topics</h4></a>
<p> For fall 2023, I will be running teams of ugrad, masters, PhDs working on the following topics.
<p> Please note that:
<ul>
<li>
Indepdent study is an <em>unpaid</em> position where you work for the ideas (and for the grade), not cash.
<li> Depedending on your dedication and success on these topics, this work would be suitable for publciation and  a top-tiered refereed event.
<li> Also, for Ph.D. Students I go on to say
<Ul>
<li> This work would be suitable for a Ph.D. topic.
<li> In 2024, this work might be able to fund a few of you as a GRA (depending on the random number generator called "funding bodies").
</ul>
</ul>
<table width="100%"  border-spacing="20px">
    <tr><td width="300">
    Team1:<br><h4>The best data is fake data?</h4></td><td width="300x">Team2:<br><h4>Is (Human <u>and</u> AI) better than (Human <u>or</u> AI)?</h4></td></tr>
<tr><td align=center>

<img src="assets/img/synth.png" height=300 xalign=center></td>

</td>
<td width="40%">

<img src="assets/img/help.png" width=250 xalign=center></td>


</td></tr>
<tr><td valign=top>
Why wait for data? Why not synthesis it? 
Many fields have been fumblding and bumbling around with synthetic data generation, for decades.
But a new generation of synthesis algirithms suggest that all that prior work could be blown away by much better and much faster algoriths
(e.g. GAN is really slow and new methods are far faster).
By exploring those new algorithms we could:
<ul>
<li> making the data needed to stress test a system;
<li> changing existing biases in data, thereby (e.g.) removing data discrimination;
<li> create all the data needed to  satisfy the needs of  data hungry machine learning algorithms.
<li> impute missing information in existing data;
<li> enable data sharing, without incurring the wrath of legislative bodies (in this way, organizations can share insights, thereby assisting in scientific reasoning).
<li> When most people work with the synthetic , not the real data, then this increases data security;
<li> Synthetic data can exploit current trends in data, thereby supporting forecasting.
</ul>
<p>
Interested? Then please read 
<a href="https://dl.acm.org/doi/pdf/10.1145/3085504.3091117">more</a> and
<a href="https://arxiv.org/pdf/2203.11410.pdf">some more</a>.
<p>
<td valign=top>
To forge an effective partnership, humans and artificial intelligence (AI) need to understand each
another’s strengths and limitations. For example, AI tools  work better when
taking advice from one person but have issues dealing with advice from large teams. Therefore, we
propose a system to extend current AI tools  with particle-swarm optimization and generative transformer models
to handle teams; specifically:
<ul>
<li> debates and disagreements between team members;
<li> team members
with an established track record of offering good/bad advice; and <li> team members that (consciously or
unconsciously) offer advice that leads to discriminatory models.<br>
</ul>
<p>Interested? Then please read 
<a href="assets/pdf/NSF22_advice.pdf">more</a> and
<a href="https://react-lm.github.io/">some more</a>. 
</td></tr></table>

---->



</ul>

</div>

<div id="For Industry" class="w3-container city" style="display:none">
<hr>
  <h3>For Industry</h3>
 <b>Ask me how</b>
 to innovate on time, on budget. 
 I've done this with many companies. For example:
 <ul>
              <li>
                <a href="https://thomas-zimmermann.com/publications/files/kocaganeli-icse-2013.pdf">Microsoft</a>;
                <li> <a href="https://www.sbir.gov/sbirsearch/detail/4945">Grammatech</a>;
                  <li><a href="http://www.slideshare.net/timmenzies/172529main-ken-andtimsoftwareassuranceresearchatwestvirginia?qid=4ddfaa48-dea3-4397-800b-74170c2722da&amp;v=&amp;b=&amp;from_search=4">NASA</a>;
                    <li><a href="https://www.researchgate.net/profile/Tim-Menzies/publication/2278548_An_Expert_System_for_Raising_Pigs/links/09e4150c30f02cc14d000000/An-Expert-System-for-Raising-Pigs.pdf">CSIRO</a>
                    <li>LexisNexis: e.g. <a href= "http://www.slideshare.net/slideshow/embed_code/key/f8etbZ448ukfOs">1</a>,<a 
                                       href="https://timm.github.io/pdf/Best_Practice_SE_text_mining.pdf">2</a>,<a 
                                       href="phttps://timm.github.io/pdf/LNPoster2018GREEN.pdf">3</a>,<a 
                                       href="https://arxiv.org/pdf/1905.07019.pdf">4</a>.<a 
                                       href="https://arxiv.org/pdf/1905.06390.pdf">5</a>;<br>
                                     <li>         IBM: e.g. <a href= "https://github.com/timm/16/blob/master/matt.pdf">1</a>,<a 
                                                         href= "https://arxiv.org/pdf/1711.03933.pdf">2</a>,<a 
                                                         href="https://arxiv.org/pdf/1710.09055.pdf">3</a>,<a 
                                                         href="https://arxiv.org/pdf/1710.08736.pdf">4</a>;
            </ul>

</div>

<div id="For Researchers" class="w3-container city" style="display:none">
<hr>
  <h3>For Researchers</h3>
<img align=right width=300 src="assets/img/method.png">
<P>Here is what I believe:
<ul>
<li>AI software is still software so faults in SE means faults in AI.
<li>SE teams often race to deliver AI-based solutions without first
checking for bias, optimality, explainability, acceptability to stakeholders etc.
<li>The good news is decades of work in SE
(e.g. in configuration management and multi-stakeholder reasoning and other work)
means that we can address those problems.
<li>
The bad news is that those methods are rarely applied in SE (since they can be cumbersome), 
so how can we expect them to be used in AI?
<li>Recent results from SE analytics offers  orders of magnitude improvements in those methods. So
now is the time to
find and fix  those faults (in SE methods), thereby enabling dramatic improvements in AI.
</ul>
<p>Will these fixed methods resolve all the problems we see with
poor configuration and optimization, bias and discrimination? Of course not. But do they offer
a dramatic improvement for at least part of the problem? Definitely!
 <dl>
              <dt>My awards</dt><dd> <ul><li>IEEE Fellow, 2018
                <li>Author of one of SE's 20-most cited papers <a href="https://scholar.google.com/citations?view_op=view_citation&hl=en&user=7htTUTgmLtUC&citation_for_view=7htTUTgmLtUC:u5HHmVD_uO8C">(cites/year)</a>;<br>
                  <li>Distinguished paper award, FSE'21
                    <li>Distinguished paper award, ICSE'19
                      <li>Most influential paper award, ICSME'19
                        <li>2017 Inaugural  MSR Foundational Contribution Award
                          <li>Locally, Google Scholar ranks me as the
<a 
href="https://scholar.google.com/citations?hl=en&authuser=1&view_op=search_authors&mauthors=North+Carolina+State+University++computer+science&btnG=">
  second-most</a> cited author in CS at NCSU.
<li>Internationally, Google Scholar ranks me:<ul>
                  <li>
first for <a 
href="https://scholar.google.com/citations?view_op=search_authors&hl=en&authuser=1&mauthors=label:search_based_software_engineering">search-based SE</a> 
and <a
href="https://scholar.google.com/citations?view_op=search_authors&hl=en&authuser=1&mauthors=label:defect_prediction">defect prediction</a>;
<li>
second for <a
href="https://scholar.google.com/citations?view_op=search_authors&hl=en&authuser=1&mauthors=label:software_cost_estimation">effort estimation</a>;
<li>
  and 
third for <a
href="https://scholar.google.com/citations?view_op=search_authors&hl=en&authuser=1&mauthors=label:expert_systems">expert systems</a> and
<a 
  href="https://scholar.google.com/citations?view_op=search_authors&hl=en&authuser=1&mauthors=label:software_analytics">software analytics</a>.</ul></ul>

<dt>My publications</dt><dd id="dim"> H-index: 67 (Oct'22).</dd>
              <dt>My grad&nbsp;students</dt><dd> Ph.D.: 6 current. 18 past.<br>Masters (by research): 32 </dd>
              <dt>My papers</dt><dd id=dim>108 journal + 137 conference + 86 other </dd>
              <dt>My funding</dt><dd> Total= <a href= "https://docs.google.com/spreadsheets/d/1Y5YrD3WkZlee7LLXLN5m9vvMPL2qBU-vruHpRr77dqg/edit"> $13.3 million</a> (total). From many sources, e.g.:
                &nbsp;&nbsp;<img height="50" src=
                                    "assets/img/grammatech-squarelogo.png" align=middle>
                <img height="50" style="padding-bottom: 10px;"  align=middle src="assets/img/ibm.png">&nbsp;<img 
                                                                             height="50" src="assets/img/ln.png" align=massets/iddle>  <img 
                                                                                         width="50" src="assets/img/nara.png" align=middle>
                                                                             <img height=
                                                                             "50" src=
                                                                                     "https://pbs.twimg.com/profile_images/67630775/button_meatball_normal.png" align=middle>
                                                                             &nbsp;&nbsp;&nbsp;<img height="50" src=
                                                                                                                   "https://icons.iconarchive.com/icons/danleech/simple/256/facebook-icon.png" align=middle> </dd>
              </dd><dt>My journal works</dt><dd id=dim>
                editor-in-chief: Automated Software Engineering journal<br>
                assoc. ed.: TSE, CACM, IEEE Software<br>
                editorial board: JSS. SQJ<br>
                advisory board: EMSE<br>
                prior: assoc. ed. IST, TOSEM, ASEJ, Big Data Research, IET Software
              </dd><dt>My conference work</dt><dd>
                co-general chair: ICMSE'16; RAISE'19, PROMISE'05..'12<br>
                co-PC chair: ASE'12, NEIR'15, SSBSE'17, PROMISE'20<br>
                artifacts co-chair:ASE'21, ICSE'20, ASE'20, FSE'18, FSE'16<br>
                program committees: ICSE'23, SANER'23, ICSE'22, IJCAI'22, AAAI'22, ICML'22, MSR'22, ESEM'22, 
                IJCAI'21. AAAI'21,  ICSE'21, MSR'21, 
                ASE'20, ICSE'20, ESEM'20, FSE'19, ASE'19, MSR'19, SSBSE, PROMISE,...
              </dd>
              <dt>My professional work</dt><dd id="dim">
                Roving member, IEEE Technical Council on SE. 2022, 2021</dd>
              <dt>My government work </dt><dd>
                NASA software research chair: 2002-2004<br>
                NSF panelist: 13 times (2003-2020)</dd>
            </dl>


</div>

<center>
<!--
script type="text/javascript" src="//rf.revolvermaps.com/0/0/6.js?i=55izg6asozu&amp;m=7&amp;c=e63100&amp;cr1=ffffff&amp;f=arial&amp;l=0&amp;bv=90&amp;lx=-420&amp;ly=420&amp;hi=20&amp;he=7&amp;hc=a8ddff&amp;rs=80" 
async="async"></script --->
</center>
 """


print(_template.content(title="Tim Menzies", main=main()))
