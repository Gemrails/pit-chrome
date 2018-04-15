#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<!-- saved from url=(0103)https://jobs.echinacities.com/jobs/rescont/0/3176030/1?D=aXNyZWFk&lang=cn&r=MTY5NjQ0&A=MzE3NjAzMA%3D%3D -->
<html>
 <head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /> 
  <title></title> 
  <meta property="og:image" content="https://static.echinacities.com/static/echina/img/echinajobs800.jpg" /> 
  <meta property="og:title" content="eChinacities.com" /> 
  <meta property="og:description" content="eChinacities.com" /> 
  <meta name="description" content="" /> 
  <meta name="keywords" content="" /> 
  <meta http-equiv="X-UA-Compatible" content="IE=edge" /> 
  <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" /> 
  <meta name="360-site-verification" content="ab44807066f43d9e2e734d4bb1322e1f" /> 
  <meta name="baidu-site-verification" content="LFI1W9vkEK" /> 
  <meta name="msvalidate.01" content="5D7F9ABC8ECBBEE3F157B47ABD8D656F" /> 
  <meta name="baidu_ssp_verify" content="c12378ce577e001bf860a59323279dc6" /> 
  <meta name="google-site-verification" content="d9e10EqzNoMv2syhhBR0LtG8izdXTrep1iTMjTk8bvk" /> 
  <meta name="sogou_site_verification" content="L1kK9Aa0oS" /> 
  <meta name="sogou_site_verification" content="L1kK9Aa0oS" /> 
  <link rel="dns-prefetch" href="https://www.echinacities.com/" /> 
  <link rel="dns-prefetch" href="https://jobs.echinacities.com/" /> 
  <link rel="dns-prefetch" href="https://answers.echinacities.com/" /> 
  <link rel="dns-prefetch" href="https://classifieds.echinacities.com/" /> 
  <link rel="dns-prefetch" href="https://news.echinacities.com/" /> 
  <link rel="dns-prefetch" href="https://profile.echinacities.com/" /> 
  <link rel="dns-prefetch" href="https://company.echinacities.com/" /> 
  <link rel="dns-prefetch" href="https://space.echinacities.com/" /> 
  <link rel="dns-prefetch" href="https://dating.echinacities.com/" /> 
  <link rel="dns-prefetch" href="https://static.echinacities.com/" /> 
  <link rel="shortcut icon" href="https://static.echinacities.com/favicon.ico" /> 
  <script type="text/javascript" async="" src="./1_files/ga.js"></script>
  <script src="./1_files/hm.js"></script>
  <script src="./1_files/jquery-3.2.1.min.js"></script> 
  <script src="./1_files/jquery.tap.js"></script> 
  <script src="./1_files/bootstrap.min.js"></script> 
  <script src="./1_files/vue.min.js"></script> 
  <script src="./1_files/global.js"></script> 
  <link href="./1_files/bootstrap.min.css" rel="stylesheet" /> 
  <link href="./1_files/font-awesome.min.css" rel="stylesheet" /> 
  <link charset="utf-8" href="./1_files/common.css" rel="stylesheet" /> 
  <!--[if lt IE 9]>
	      <script src="https://cdn.bootcss.com/html5shiv/3.7.3/html5shiv.min.js"></script>
	      <script src="https://cdn.bootcss.com/respond.js/1.4.2/respond.min.js"></script>
	    <![endif]--> 
 </head> 
 <body> 
  <div class="test-box-model" style="display: none;"> 
   <input class="hidden-md" value="md" /> 
   <input class="hidden-sm" value="sm" /> 
   <input class="hidden-xs" value="xs" /> 
   <input class="hidden-lg" value="lg" /> 
  </div> 
  <!-- 立即更新 --> 
  <!--[if lt IE 9]>
        <div class="browers_update">
          <div class="container">
            <span>您的浏览器版本过低，可能导致网站不能正常访问！推荐安装 Chrome 浏览器</span>
            <a href="//www.echinacities.com/static/ChromeStandalone_60.0.3112.90_Setup.exe" target="_blank" class="btn-browers">立即更新</a>
          </div>
        </div> 
        <![endif]--> 
  <input type="hidden" class="hide_employer_login" value="0" /> 
  <input type="hidden" class="header_level" value="4" /> 
  <!-- jobs头部 --> 
  <header id="header" class="eccheader">
   <div class="header_wap_wrap header_wap_wrap_pad hidden-lg hidden-md">
    <nav class="navbar navbar-default header_wap header_wap_pad shadow">
     <div class="container-fluid">
      <div class="navbar-header-pad">
       <button type="button" data-toggle="collapse" data-target="#ecc-navbar-collapse" aria-expanded="false" class="navbar-toggle navbar-toggle-pad navbar-toggle-left collapsed emp-show-left-toogle"><span class="sr-only">Toggle navigation</span> <span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span></button> 
       <a href="https://jobs.echinacities.com/" class="logo-top"><img src="./1_files/ecc_echinajobs.png" alt="eChinajobs" /></a> 
       <div class="admin">
        <!----> 
        <!----> 
        <!----> 
        <div class="dropdown">
         <a href="https://profile.echinacities.com/user/emp/card/?lang=cn" class="dropdown-toggle"><span class="username username_jobs">Alex.Shang</span></a>
        </div>
       </div>
      </div> 
      <div class="clearfix"></div> 
      <div id="ecc-navbar-collapse" class="collapse collapse-pad navbar-collapse fade" style="height: 937px;">
       <div class="nav_wrap nav_wrap_pad shadow" style="overflow: scroll; height: 637px;">
        <ul class="nav navbar-nav-jobs" style="overflow-y: scroll; min-height: 500px;">
         <li><a href="https://www.echinacities.com/">eChinacities Home</a></li> 
         <li role="separator" class="divider"></li> 
         <li data-index="201"><a href="https://jobs.echinacities.com/jobs/add?lang=cn">发布职位 
           <!----></a></li>
         <li data-index="202"><a href="https://profile.echinacities.com/user/emp/managejobs/1?sc=5&amp;lang=cn">在线职位 
           <!----></a></li>
         <li data-index="203"><a href="https://profile.echinacities.com/user/emp/apply?ty=1&amp;sc=6&amp;lang=cn">收到的简历 
           <!----></a></li>
         <li data-index="204"><a href="https://jobs.echinacities.com/job/jobs/promotion?lang=cn">购买广告服务 
           <!----></a></li>
         <li data-index="206"><a href="https://profile.echinacities.com/user/emp/company_ad?lang=cn&amp;sc=7&amp;ps=2#;main:1">站内信 
           <!----></a></li>
         <li data-index="207"><a href="https://jobs.echinacities.com/main/contact/contact_us/enterprise_service/Company?lang=cn">问题反馈 
           <!----></a></li> 
         <li class="divider" role="separator"></li> 
         <li><a href="https://www.echinacities.com/login?type=4&amp;url=https%3A%2F%2Fjobs.echinacities.com%2Fjobs%2Frescont%2F0%2F3176030%2F1%3FD%3DaXNyZWFk%26lang%3Dcn%26r%3DMTY5NjQ0%26A%3DMzE3NjAzMA%253D%253D">For Personal</a></li> 
         <!----> 
         <li class="show_download_app"><a href="https://jobs.echinacities.com/jobs/rescont/0/3176030/1?D=aXNyZWFk&amp;lang=cn&amp;r=MTY5NjQ0&amp;A=MzE3NjAzMA%3D%3D#ecc_app" data-toggle="modal" data-target="#ecc_app" class="hidden-xs"><span class="glyphicon glyphicon-phone"></span> eChinaJOBs APP</a><a href="javascript:;" class="visible-xs"><span class="glyphicon glyphicon-phone"></span> eChinaJOBs APP</a></li> 
         <li role="separator" class="divider"></li> 
         <!----> 
         <!----> 
         <!----> 
         <li class="logout"><a href="https://company.echinacities.com/logout?url=https%3A%2F%2Fjobs.echinacities.com%2Fjobs%2Frescont%2F0%2F3176030%2F1%3FD%3DaXNyZWFk%26lang%3Dcn%26r%3DMTY5NjQ0%26A%3DMzE3NjAzMA%253D%253D" class="btn btn-ecc">Sign out</a></li>
        </ul>
       </div>
      </div>
     </div>
    </nav>
   </div> 
   <div class="header_pc_wrap hidden-xs hidden-sm">
    <div class="header_pc shadow">
     <div class="topbar">
      <div class="container">
       <div class="row">
        <div class="navbar-collapse">
         <ul class="nav navbar-nav col-sm-5">
          <li><a id="baidu_shijian_user_go_home" href="https://www.echinacities.com/">eChinacities Home</a></li> 
          <li id="baidu_shijian_user_get_client" class="show_download_app"><a href="javascript:;"><span class="glyphicon glyphicon-phone"></span> eChinaJOBs APP</a></li>
         </ul> 
         <div class="col-sm-3"></div> 
         <ul class="nav navbar-nav navbar-right personalnewbox col-sm-4">
          <li class="show-toggle-box personalnew">
           <ul>
            <li><a id="baidu_tongji_user_login_top" href="https://www.echinacities.com/login?type=4&amp;url=https%3A%2F%2Fjobs.echinacities.com%2Fjobs%2Frescont%2F0%2F3176030%2F1%3FD%3DaXNyZWFk%26lang%3Dcn%26r%3DMTY5NjQ0%26A%3DMzE3NjAzMA%253D%253D">Login</a></li> 
            <li><a id="baidu_tongji_user_register_top" href="https://www.echinacities.com/register?type=4&amp;url=https%3A%2F%2Fjobs.echinacities.com%2Fjobs%2Frescont%2F0%2F3176030%2F1%3FD%3DaXNyZWFk%26lang%3Dcn%26r%3DMTY5NjQ0%26A%3DMzE3NjAzMA%253D%253D">Register</a></li>
           </ul></li> 
          <!----> 
          <li><a class="sep_line"> | </a></li> 
          <!----> 
          <li class="show-toggle-box"><a _href="//profile.echinacities.com/user/emp/card/?lang=cn" class="adminpc personal" style="cursor: pointer;"><span class="personalname">Alex.Shang</span><span class="caret"></span></a> 
           <div class="account toggle-hide" style="display: none;">
            <div class="arrowrap arrowrapicon">
             <span class="arrow-up"></span>
             <span class="arrow-up-in"></span>
            </div> 
            <ul class="account_ul tk_shadow">
             <li><a href="https://profile.echinacities.com/user/emp/card?lang=cn#;main:1">会员中心 
               <!----></a></li>
             <li><a href="https://jobs.echinacities.com/jobs/add?lang=cn">发布职位 
               <!----></a></li>
             <li><a href="https://jobs.echinacities.com/job/jobs/promotion?lang=cn">广告服务 
               <!----></a></li>
             <li><a href="https://company.echinacities.com/logout?url=https%3A%2F%2Fjobs.echinacities.com%2Fjobs%2Frescont%2F0%2F3176030%2F1%3FD%3DaXNyZWFk%26lang%3Dcn%26r%3DMTY5NjQ0%26A%3DMzE3NjAzMA%253D%253D">退出 
               <!----></a></li>
            </ul>
           </div></li>
         </ul>
        </div>
       </div>
      </div>
     </div> 
     <nav class="eccnav">
      <div class="container">
       <div class="row">
        <div class="col-sm-12">
         <a href="https://jobs.echinacities.com/" class="logo logojobs"><img src="./1_files/ecc_echinajobs.png" alt="eChinajobs" /></a> 
         <div class="headerAll">
          <div class="jobs_topfont large-text">
           The Leading Job Site for Foreigners in China
          </div> 
          <ul class="follow_us follow_us_top" style="display: block;">
           <li><b>Follow us: </b></li> 
           <li><a href="https://www.facebook.com/echinajobs/" class="facebook"><i aria-hidden="true" class="fa fa-facebook-square"></i></a></li> 
           <li><a href="https://www.linkedin.com/company/221145" class="linkedin"><i aria-hidden="true" class="fa fa-linkedin-square"></i></a></li> 
           <li><a href="https://twitter.com/eChinacities" class="tumblr"><i aria-hidden="true" class="fa fa-tumblr-square"></i></a></li>
          </ul>
         </div> 
         <div class="headerEmp" style="display: none;">
          <div class="jobs_topfont large-text">
           VIP Membership
          </div>
         </div>
        </div>
       </div>
      </div>
     </nav>
    </div>
   </div>
  </header> 
  <!-- /jobs头部 --> 
  <!-- /jobs头部 --> 
  <div class="container"> 
   <ul class="nav2 nav2jobs shadow hidden-xs hidden-sm"> 
    <li class="active"><a href="https://jobs.echinacities.com/">All Jobs</a></li> 
    <li><a href="https://jobs.echinacities.com/Beijing-jobs">Beijing Jobs</a></li> 
    <li><a href="https://jobs.echinacities.com/Shanghai-jobs">Shanghai Jobs</a></li> 
    <li><a href="https://jobs.echinacities.com/Guangzhou-jobs">Guangzhou Jobs</a></li> 
    <li><a href="https://jobs.echinacities.com/Shenzhen-jobs">Shenzhen Jobs</a></li> 
    <li><a href="https://jobs.echinacities.com/Hangzhou-jobs">Hangzhou Jobs</a></li> 
    <li><a href="https://jobs.echinacities.com/Suzhou-jobs">Suzhou Jobs</a></li> 
    <li><a href="https://jobs.echinacities.com/Qingdao-jobs">Qingdao Jobs</a></li> 
    <li><a href="https://jobs.echinacities.com/Nanjing-jobs">Nanjing Jobs</a></li> 
    <li class="nav_more_city"><a href="javascript:;">More City Jobs</a></li> 
   </ul> 
  </div> 
  <link rel="stylesheet" href="./1_files/city.css" /> 
  <script type="text/javascript" src="./1_files/city.js"></script> 
  <!-- 导航栏 --> 
  <div class="container menu-box" style="padding: 0;"> 
   <div class="col-md-12"> 
    <div class="main-header"> 
     <ol class="breadcrumb">
      <li><a href="https://jobs.echinacities.com/">Jobs</a></li>
      <li class="active">Resume</li>
     </ol> 
     <div class="languagePub">
      <a href="https://jobs.echinacities.com/jobs/rescont/0/3176030/1?D=aXNyZWFk&amp;lang=en&amp;r=MTY5NjQ0&amp;A=MzE3NjAzMA%3D%3D&amp;ref=https%253A%252F%252Fprofile.echinacities.com%252Fuser%252Femp%252Fapply%253Fty%253D1%2526lang%253Dcn%2526sc%253D6" class=""><b> English </b></a> / 
      <a href="https://jobs.echinacities.com/jobs/rescont/0/3176030/1?D=aXNyZWFk&amp;lang=cn&amp;r=MTY5NjQ0&amp;A=MzE3NjAzMA%3D%3D&amp;ref=https%253A%252F%252Fprofile.echinacities.com%252Fuser%252Femp%252Fapply%253Fty%253D1%2526lang%253Dcn%2526sc%253D6" class="color-red"><b> 中文 </b></a>
     </div> 
    </div> 
   </div> 
  </div> 
  <input type="hidden" class="menu_select_index" value="0" /> 
  <script type="text/javascript" src="./1_files/common.js"></script> 
  <link rel="stylesheet" href="./1_files/login_register.css" /> 
  <link rel="stylesheet" href="./1_files/resume_print.css" media="print" /> 
  <!-- enterprise center内容 --> 
  <main class="ecc-main employer_bodylink"> 
   <div class="container"> 
    <div class="ortip hidden-xs hidden-sm" style=""> 
     <div> 
      <b class="color-red">提示: </b>近期有少数中介利用伪造的个人简历对雇主进行欺诈。这种行为不仅非法而且是犯罪的。 本网站将对少数中介利用伪造简历投放简历库或申请职位的行为提起起诉。 我们将对
      <a href="https://jobs.echinacities.com/job/resume/reportpage?resume_id=169644&amp;lang=cn">举报非法中介</a>并使得我们起诉非法中介的雇主予以高达1000元现金或会员套餐的
      <div class="tooltipwrap"> 
       <a href="javascript:;" class="" data-toggle="tooltip" data-placement="bottom" title="" target="_blank" data-original-title="1000元人民币现金或等值会员套餐">奖励</a> 
      </div>。 
     </div> 
    </div> 
    <div class="eccwrap shadow"> 
     <div class="eccbox eccboxnob previewResume">
      <div class="row"> 
       <div class="col-md-offset-1 col-md-10"> 
        <div class="create_tit"> 
         <div class="col-sm-8 col-xs-10">
          <div class="row tit_left"> 
          </div>
         </div> 
         <div class="col-sm-4 col-xs-2">
          <div class="row tit_right"> 
           <a href="https://jobs.echinacities.com/job/resume/export_resume_pdf/169644" class="btn-sm btn-ecc hidden-sm hidden-xs">导出PDF</a> 
           <a href="javascript:;" class="btn-sm btn-ecc hidden-sm hidden-xs doPrint">打印</a> 
           <a href="javascript:;" class="btn-sm btn-ecc btnresumeback goback"><span class="glyphicon glyphicon-menu-left"></span>返回</a> 
          </div>
         </div> 
        </div> 
        <div class="print_Area"> 
         <div class="resume_logo"> 
          <img class="hidden-xs" src="./1_files/echinajob_logo.png" alt="eChinajobs" /> 
          <span class="date">更新时间: 2018-01-31</span> 
         </div> 
         <div class="resume_logoprint visible-print-block"> 
          <img src="./1_files/echinajob_logo.png" alt="eChinajobs" /> 
          <span class="date">更新时间: 2018-01-31</span> 
         </div> 
         <!-- profile_infoprint visible-print-block --> 
         <!-- profile_info hidden-xs --> 
         <table class="profile_info hidden-xs">
          <tbody> 
           <tr> 
            <td rowspan="2" class="profile_infoimg"><img src="./1_files/14496757615326.jpg" alt="" /></td> 
            <td colspan="2" class="profile_infoname"> 
             <!--企业用户未下载name--> <strong>Hasan Tezer </strong> 
             <!--/企业用户未下载name--> <span>Male | 33 years old (1984/07)</span> </td> 
           </tr> 
           <tr> 
            <td>
             <ul> 
              <li><b>国籍: </b> United Kingdom </li> 
              <li><b>当前所在地: </b> [United Kingdom]</li> 
              <li><b>工作年限: </b> 6 years</li> 
             </ul></td> 
            <!--企业用户未下载 info--> 
            <td>
             <ul> 
              <li><b>电话: </b> [+44]07562295959 </li> 
              <li><b>邮件地址: </b>hasantezer@gmail.com</li> 
             </ul> </td> 
            <!--/企业用户未下载 info--> 
           </tr> 
           <!--/企业用户已下载 info--> 
          </tbody> 
         </table> 
         <!-- resume info wap --> 
         <div class="profile_infowap visible-xs"> 
          <div class="profile_infowapleft">
           <img src="./1_files/14496757615326.jpg" alt="" />
          </div> 
          <div class="profile_infowapright"> 
           <ul> 
            <li><strong>Hasan Tezer</strong></li> 
            <li>Male</li> 
            <li>33 years old (1984/07)</li> 
            <li>hasantezer@gmail.com</li> 
           </ul> 
          </div> 
          <ul class="profile_infowapbottom"> 
           <li><b>国籍: </b> United Kingdom </li> 
           <li><b>当前所在地: </b> [United Kingdom]</li> 
           <li><b>工作年限: </b> 6 years</li> 
           <li><b>电话: </b> <a href="tel:44 07562295959" class="color-blue">[+44]07562295959</a> </li> 
          </ul> 
         </div> 
         <div class="preview_box"> 
          <div class="preview_box_tit">
           <strong>期望工作</strong>
          </div> 
          <ul class="preview_box_info"> 
           <li><b>期望工作</b></li> 
           <li>International school<br /> High school<br /> EAP/ IELTS teaching<br /> Management<br /> Editing<br /> Student advising </li> 
           <li><b> 期望工作地: </b>Beijing Shanghai Shenzhen</li> 
           <li><b> 期望行业类型: </b>English Teaching</li> 
           <li><b>期望薪资: </b>15000 - 50000 CNY/月</li> 
           <li><b>工作类型: </b>Full-time</li> 
           <li><b>到岗时间: </b>Available to begin working ASAP. </li> 
          </ul> 
         </div> 
         <div class="preview_box"> 
          <div class="preview_box_tit">
           <strong>职业经历</strong>
          </div> 
          <ul class="preview_box_info"> 
           <li><b>起止日期:</b> 2017/08 - 2017/09</li> 
           <li><b>公司名称: </b>British University</li> 
           <li><b>工作经验:</b></li> 
           <li>I taught Academic English at a British University for 5 weeks on a Pre-sessional program to students mainly from China.This also involved providing students with tutorials and advising them on their studies and University life in the UK.</li> 
          </ul> 
          <ul class="preview_box_info border_dash"> 
           <li><b>起止日期:</b> 2016/08 - 2017/08</li> 
           <li><b>公司名称: </b>Language School (Japan)</li> 
           <li><b>工作经验:</b></li> 
           <li>I worked as an IELTS instructor in Shibuya, where I taught high school students, university students and adults. I also assisted students with their applications for Universities in the UK. This role involved participating at University fairs where students can meet representatives from British universities. During the fairs, I presented seminars on IELTS and provided one to one consultation with potential students about what courses they could sign up for at the school. When the English Language centre manager was absent, I took on managerial duties at the office. This would involve timetabling and resolving issues with students and staff. I was responsible for teaching all four skills and helping students achieve a score that would allow them to study at British universities. I was also responsible for editing University applications and writing blogs about British culture for the school’s website. I planned a curriculum and taught classes at Ochanomizu University and Kyorin University in Tokyo. Throughout the year I also presented and planned seminars on British culture, University application forms and personal statements for job applications. Additionally, I wrote blog articles on British culture and University life for the website as well.</li> 
          </ul> 
          <ul class="preview_box_info border_dash"> 
           <li><b>起止日期:</b> 2016/04 - 2016/07</li> 
           <li><b>公司名称: </b>Japanese College</li> 
           <li><b>工作经验:</b></li> 
           <li>I taught medical students at a Medical College in Japan on a Temporary basis. This involved teaching large classes medical English in combination with general English lessons and TOEIC classes.</li> 
          </ul> 
          <ul class="preview_box_info border_dash"> 
           <li><b>起止日期:</b> 2015/03 - 2016/02</li> 
           <li><b>公司名称: </b>Language School (Hiroshima)</li> 
           <li><b>工作经验:</b></li> 
           <li>I taught young learners including kindergarten and adults in Japan. I was responsible for creating fun learner centered activities. The emphasis of the lessons was to improve students’ confidence in speaking English and to improve the students’ phonetic ability in English. I also assisted in preparing high school students for the Eiken University entrance examination.</li> 
          </ul> 
          <ul class="preview_box_info border_dash"> 
           <li><b>起止日期:</b> 2012/09 - 2013/07</li> 
           <li><b>公司名称: </b>Freelance UK</li> 
           <li><b>工作经验:</b></li> 
           <li>I taught different nationalities at a variety of schools in London and to private students. I taught Elementary and Pre-Intermediate level adult students using materials such as New English File. I was responsible for creating tests for the students and giving them regular homework. I also taught ESOL to young learners covering comprehension, grammar and writing.</li> 
          </ul> 
          <ul class="preview_box_info border_dash"> 
           <li><b>起止日期:</b> 2009/08 - 2012/09</li> 
           <li><b>公司名称: </b>Gyeonggi Province of Education Program in Korea</li> 
           <li><b>工作经验:</b></li> 
           <li>I taught English, assisted students with University applications and edited textbooks used in the Gyeonggi province in Korea.</li> 
          </ul> 
          <ul class="preview_box_info border_dash"> 
           <li><b>起止日期:</b> 2009/03 - 2009/07</li> 
           <li><b>公司名称: </b>Language School UK</li> 
           <li><b>工作经验:</b></li> 
           <li>I taught different nationalities at a variety of schools in London and to private students. I taught Elementary and Pre-Intermediate level adult students using materials such as New English File. I was responsible for creating tests for the students and giving them regular homework. I also taught ESOL to young learners covering comprehension, grammar and writing.</li> 
          </ul> 
          <ul class="preview_box_info border_dash"> 
           <li><b>起止日期:</b> 2007/12 - 2008/12</li> 
           <li><b>公司名称: </b>Language School Korea</li> 
           <li><b>工作经验:</b></li> 
           <li>I taught students of all ages at a private language school in South Korea. I created my own materials and was responsible for teaching reading, writing and speaking.</li> 
          </ul> 
         </div> 
         <div class="preview_box"> 
          <div class="preview_box_tit">
           <strong>教育</strong>
          </div> 
          <ul class="preview_box_info"> 
           <li><b>教育时间: </b>2013/09 - 2014/11</li> 
           <li><b>学校: </b>British University</li> 
           <li><b>主修专业: </b>Education</li> 
           <li><b>学历: </b>Master's Degree</li> 
           <li><b>资格证书: </b></li> 
           <li>Second language acquisition, educational technology, observed teaching practice (I observed classes at International House in Covent Garden and taught two observed lessons at University), Sociocultural studies in ELT and a research project (project looked at English education in East Asia)</li> 
          </ul> 
         </div> 
         <div class="preview_box"> 
          <div class="preview_box_tit">
           <strong>语言</strong>
          </div> 
          <ul class="preview_box_info"> 
           <li><b>母语:</b>English</li> 
           <li><b>中文水平:</b>Basic</li> 
           <li><b>英文水平:</b>Native</li> 
           <li> <b>Other:</b>Turkish&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>Level:</b>Advanced </li> 
           <li> <b>Japanese Level:</b>Basic </li> 
           <li> <b>Korean Level:</b>Basic </li> 
          </ul> 
         </div> 
         <div class="preview_box"> 
          <div class="preview_box_tit">
           <strong>技能</strong>
          </div> 
          <ul class="preview_box_info"> 
           <li><b>技能</b></li> 
           <li>UCAS advising - advising students on UK universities <br /><br /> Higher education fairs <br /><br /> Editing <br /><br /> IELTS<br /><br /> EAP<br /><br /> University teaching <br /><br /> High school teaching<br /> Management</li> 
           <br /> 
           <li><b>其他信息</b></li> 
           <li>I attended a course with UCAS advising international students on applying to Universities in the UK</li> 
          </ul> 
         </div> 
        </div>
        <!-- print_Area --> 
        <div class="create_tit create_titb"> 
         <div class="col-sm-8 col-xs-10">
          <div class="row tit_left"> 
          </div>
         </div> 
         <div class="col-sm-4 col-xs-2">
          <div class="row tit_right"> 
           <a href="https://jobs.echinacities.com/job/resume/export_resume_pdf/169644" class="btn-sm btn-ecc hidden-sm hidden-xs">导出PDF</a> 
           <a href="javascript:;" class="btn-sm btn-ecc hidden-sm hidden-xs doPrint">打印</a> 
           <a href="javascript:;" class="btn-sm btn-ecc btnresumeback goback"><span class="glyphicon glyphicon-menu-left"></span>返回</a> 
          </div>
         </div> 
        </div> 
       </div>
      </div>
      <!-- col-md-offset-2 col-md-8 --> 
     </div>
     <!-- eccbox shadow --> 
    </div> 
   </div>
   <!-- container --> 
  </main>
  <!-- ecc-main --> 
  <!-- /enterprise center内容 --> 
  <script src="./1_files/reusme2employer.js"></script> 
  <script>
        	$('.goback').bind('tap',function(){
        		// history.back();
        		location.href='https://profile.echinacities.com/user/emp/apply?ty=1&lang=cn&sc=6';
        		return false;
        	});
        	$('.doPrint').bind('tap',function(){
        		print();
        		return false;
        	});
        	$('.collection').bind('tap',function(){
        		getcollect(169644,1);
        		return false;
        	})
        	$('.download').bind('tap',function(){
        		getdown(169644,2890487,0,1);
        		return false;
        	});
        	


		$('.aaasuo').bind('tap',function(){
			$.post('/job/resume/changPhoneStatus/0',function(r){
				location.reload();
			});
			return false;
		})
	
        </script> 
  <!--/*service_guide*/--> 
  <div class="customer_service hidden-xs hidden-sm"> 
   <div class="service_login"> 
    <ul> 
     <li><a href="https://jobs.echinacities.com/main/contact/contact_us/enterprise_service/Company?lang=cn">客户服务</a></li> 
     <li><a href="https://jobs.echinacities.com/main/contact/contact_us/advertising_sales/Company?lang=cn">广告销售</a></li> 
     <li><a href="https://jobs.echinacities.com/main/contact/contact_us/complaints_proposals/Company?lang=cn">投诉建议</a></li> 
     <li><a href="https://jobs.echinacities.com//main/contact/common_problems/Company?lang=cn">常见问题</a></li> 
     <div class="service_kefu"> 
      <div class="service_kefubox"> 
       <img class="kefu_icon" src="./1_files/kefu_icon.png" /> 
       <div>
        在线客服
        <br />8:00-17:00
       </div> 
      </div> 
      <div class="service_kefuhover" style="display: none;"> 
       <img class="kefu_qrcode" src="https://jobs.echinacities.com/jobs/rescont/0/3176030/1?D=aXNyZWFk&amp;lang=cn&amp;r=MTY5NjQ0&amp;A=MzE3NjAzMA%3D%3D" /> 
       <ul> 
        <li><b>扫码关注雇主微信公众号</b></li> 
        <li>您可以：</li> 
        <li>在线咨询问题</li> 
        <li>随时管理在线职位</li> 
        <li>更有礼包赠送</li> 
       </ul> 
      </div> 
     </div> 
     <script>
  $(document).on('mouseover','.service_kefubox',function(){
    if($('.kefu_qrcode').attr('src')==''){
      $('.kefu_qrcode').attr('src','/weixin/swxcode');
    }
    $('.service_kefuhover').show();
  })
  $(document).on('mouseout','.service_kefubox',function(){
    $('.service_kefuhover').hide();
  })
</script> 
    </ul> 
   </div> 
  </div> 
  <!--//*customer service*/-->
  <input type="hidden" class="resume_id" value="169644" /> 
  <!-- resumelocked --> 
  <div class="modal fade" id="resumelocked" tabindex="-1" role="dialog"> 
   <div class="modal-dialog" role="document"> 
    <div class="modal-content"> 
     <div class="modal-header"> 
      <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button> 
      <h4 class="modal-title">Hi there!</h4> 
     </div> 
     <div class="modal-body"> 
      <p class="ortip ortipsm">The phone number you had previously submitted on your CV was reported by other recruiters as unreachable and confirmed by our administrator and because of this your CV has been locked. Users of locked CVs are unable to apply for jobs on eChinacities.com or update it. Please input a valid cell phone in the box below and finish verification of your phone number to unlock your CV immediately.</p> 
      <form class="form-horizontal form-horizontallock"> 
       <div class="form-group"> 
        <div class="col-sm-offset-2 col-sm-4">
         <input type="text" class="form-control tel" maxlength="11" placeholder="Enter a valid cell phone number" />
        </div> 
        <div class="col-sm-4">
         <a href="javascript:;" class="btn btn-ecc-empty btn-block get_code">Obtain verification code</a>
        </div> 
       </div> 
       <div class="form-group"> 
        <div class="col-sm-offset-2 col-sm-8">
         <input type="text" maxlength="6" class="form-control code" placeholder="Input verification code" />
        </div> 
        <div class="col-sm-offset-2 col-sm-10">
         <div class="small-text">
          In 
          <span class="timer">60</span> seconds you may click again “Obtain a verification code” button.
         </div>
        </div> 
       </div> 
       <div class="form-group"> 
        <div class="col-sm-offset-2 col-sm-10"> 
         <button type="button" class="btn btn-ecc confirm">Submit</button> 
        </div> 
       </div> 
      </form> 
      <p>Please submit the following request to eChinacities if you have difficult to unlock the CV by yourself. Our customer service team will respond to your request within 48 hours. <a href="javascript:;" class="color-blue show_hide">Click to submit from</a></p> 
      <form class="form-horizontal form-horizontallock show_hide_box" style="display: none;"> 
       <div class="form-group"> 
        <label class="col-sm-3 control-label">Phone number: </label> 
        <div class="col-sm-8"> 
         <input type="text" class="form-control tel_admin_email_phone" placeholder="Enter a valid cell phone number" /> 
         <!--               <div class="color-red">Please enter a valid cell phone number.</div>
 --> 
        </div> 
       </div> 
       <div class="form-group"> 
        <label class="col-sm-3 control-label">Reason: </label> 
        <div class="col-sm-8"> 
         <input type="text" class="form-control tel_admin_email_reason" placeholder="Reason" /> 
         <!--               <div class="color-red">Please enter reasons of not being able to unlock CV.</div>
 --> 
        </div> 
       </div> 
       <div class="form-group"> 
        <div class="col-sm-offset-3 col-sm-8"> 
         <button type="button" class="btn btn-ecc tel_admin_email">Submit</button> 
        </div> 
       </div> 
      </form> 
     </div> 
    </div>
    <!-- /.appmodal-content --> 
   </div>
   <!-- /.appmodal-dialog --> 
  </div>
  <!-- /.appmodal --> 
  <script>
	
	var delay_timer=null;
	var report_get_code=false;
	$('.get_code').bind('tap',function(){
		if(report_get_code) return;

		var tel=$('#resumelocked .tel').val();
		if(tel==''){
			$.alert('Enter a valid cell phone number',function(){},'状态','关闭');
			return false;
		}else{
			report_get_code=true;
			$.ajax({
			   type: "POST",
		   url: "/resume/send_sms_code",
			   data: "tel="+tel,
			   dataType: "json",
			   success: function(msg){
				 if(msg.err == 'success'){
				 	delay(60);
				 }else{
				 	$.alert('Send error',function(){},'状态','关闭');
				 }
			   }
			});
		}
	})
	function delay(time){
		delay_timer=setInterval(function(){
			time--;
			if(time==0){
			   	report_get_code=false;
				$('#resumelocked .timer').text(60);
				$('.get_code').text('Obtain verification code');
			}else{
				$('.get_code').text('Success');
				$('#resumelocked .timer').text(time);
			}
			
		},1000);
	}


	$('#resumelocked .confirm').bind('tap',function(){
		var tel = $('#resumelocked .tel').val();
		var code = $('#resumelocked .code').val();
		if(tel == ''){
			$.alert('Enter a valid cell phone number',function(){},'状态','关闭');
			return false;
		}
		if(code == ''){
			$.alert('Input verification code',function(){},'状态','关闭');
			return false;
		}
		$.ajax({
		   type: "POST",
		   url: "/resume/public_resume_rep_tel",
		   data: "tel="+tel+"&code="+code,
		   dataType: "json",
		   success: function(msg){
			 if(msg.err == 1){
			 	$.alert('Success',function(){location.reload();},'状态','关闭');
			 }else{
			 	$.alert('Error',function(){},'状态','关闭');
			 }
		   }
		});
	})
	$('.show_hide').bind('tap',function(){
		if($('.show_hide_box').css('display')=='none'){
			$('.show_hide_box').show();
			$('.show_hide').text('Close');
		}else{
			$('.show_hide_box').hide();
			$('.show_hide').text('Click to submit from');
		}
		return false;
	})
	// $('.tel_admin_email_phone').bind('keyup',tel_admin_email_phone);
	$('.tel_admin_email').bind('click',function(){
		data={
			phone:$('.tel_admin_email_phone').val(),
			reson:$('.tel_admin_email_reason').val(),
		}
		if($.trim(data.phone) == ''){
			$.alert('Please enter a valid cell phone number.',function(){},'状态','关闭');
			return false;
		}
		if($.trim(data.reson) == ''){
			$.alert('Please enter reasons of not being able to unlock CV.',function(){},'状态','关闭');
			return false;
		}
		$('.tel_admin_email').prop('disabled',1);
		var but = $(this);
		but.attr('disabled',1);
		$.getJSON('/utils/mail2admin/1',data,function(r){
			if(r.code == 1){
				$.alert('Sent successfully!',function(){location.reload();},'状态','关闭');
			}
		});
	})
	// 
</script>
  <script>
		$('.tooltipwrap').hover(function(){},function(){$(this).find('.fade').remove();})

	$('.get_lock').bind('tap',function(){
		$('#resumelocked').modal('show');
		return false;
	});
</script> 
  <script>
function tmp_scroll() {
	var tmp=$('.profile_info').offset().top+$('.profile_info').height();
	if($(window).scrollTop() > tmp){
		$('.down_savefix:last').show();
	}else{
		$('.down_savefix:last').hide();
	}
}
tmp_scroll();
	$(window).scroll(tmp_scroll);
</script> 
  <!-- top --> 
  <div class="back_to_top large-text" onclick="$(window).scrollTop(0);" style="bottom: 100px;"> 
   <span class="glyphicon glyphicon-arrow-up" aria-hidden="true"></span> 
  </div> 
  <!-- /top --> 
  <script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?96e775c5e2e9c52158bba90e8ceecf7c";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();
</script> 
  <script type="text/javascript">
        var _gaq = _gaq || [];
          
          
          _gaq.push(['_setAccount', 'UA-5050936-9']);
          _gaq.push(['_setDomainName', 'echinacities.com']);
          _gaq.push(['_trackPageview']);

          (function() {
            var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
            ga.src = ('https:' == document.location.protocol ? 'https://ssl' : '//www') + '.google-analytics.com/ga.js';
            var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
          })();
        </script> 
  <!-- <img src="//jobs.echinacities.com/weixin/swxcode" alt="">
 --> 
  <script type="text/javascript" src="./1_files/tongji.js"></script> 
  <st-div id="__selection-translator__"> 
   <st-div class="__st-box__" style="display: none; position: fixed; z-index: 99999; left: 0px; top: 0px; transform: translateX(876px) translateY(226px);"> 
    <st-header> 
     <st-span class="st-icon-pin" title="固定"></st-span> 
     <st-span class="st-icon-down-open" title="展开"></st-span> 
     <st-span class="st-icon-cog" title="设置"></st-span> 
    </st-header> 
    <st-div class="__query-form__" style="display: none;"> 
     <st-div> 
      <textarea placeholder="输入要翻译的句子或单词"></textarea> 
     </st-div> 
     <st-div> 
      <select> <option value="">自动判断</option> <option value="zh">中文</option><option value="zh-CN">中文(简体)</option><option value="zh-HK">中文(香港)</option><option value="zh-TW">中文(繁体)</option><option value="en">英语</option><option value="ja">日语</option><option value="ko">朝鲜语</option><option value="de">德语</option><option value="fr">法语</option><option value="ru">俄语</option><option value="th">泰语</option><option value="af">南非语</option><option value="ar">阿拉伯语</option><option value="az">阿塞拜疆语</option><option value="be">比利时语</option><option value="bg">保加利亚语</option><option value="ca">加泰隆语</option><option value="cs">捷克语</option><option value="cy">威尔士语</option><option value="da">丹麦语</option><option value="dv">第维埃语</option><option value="el">希腊语</option><option value="eo">世界语</option><option value="es">西班牙语</option><option value="et">爱沙尼亚语</option><option value="eu">巴士克语</option><option value="fa">法斯语</option><option value="fi">芬兰语</option><option value="fo">法罗语</option><option value="gl">加里西亚语</option><option value="gu">古吉拉特语</option><option value="he">希伯来语</option><option value="hi">印地语</option><option value="hr">克罗地亚语</option><option value="hu">匈牙利语</option><option value="hy">亚美尼亚语</option><option value="id">印度尼西亚语</option><option value="is">冰岛语</option><option value="it">意大利语</option><option value="ka">格鲁吉亚语</option><option value="kk">哈萨克语</option><option value="kn">卡纳拉语</option><option value="kok">孔卡尼语</option><option value="ky">吉尔吉斯语</option><option value="lt">立陶宛语</option><option value="lv">拉脱维亚语</option><option value="mi">毛利语</option><option value="mk">马其顿语</option><option value="mn">蒙古语</option><option value="mr">马拉地语</option><option value="ms">马来语</option><option value="mt">马耳他语</option><option value="nb">挪威语(伯克梅尔)</option><option value="nl">荷兰语</option><option value="ns">北梭托语</option><option value="pa">旁遮普语</option><option value="pl">波兰语</option><option value="pt">葡萄牙语</option><option value="qu">克丘亚语</option><option value="ro">罗马尼亚语</option><option value="sa">梵文</option><option value="se">北萨摩斯语</option><option value="sk">斯洛伐克语</option><option value="sl">斯洛文尼亚语</option><option value="sq">阿尔巴尼亚语</option><option value="sv">瑞典语</option><option value="sw">斯瓦希里语</option><option value="syr">叙利亚语</option><option value="ta">泰米尔语</option><option value="te">泰卢固语</option><option value="tl">塔加路语</option><option value="tn">茨瓦纳语</option><option value="tr">土耳其语</option><option value="ts">宗加语</option><option value="tt">鞑靼语</option><option value="uk">乌克兰语</option><option value="ur">乌都语</option><option value="uz">乌兹别克语</option><option value="vi">越南语</option><option value="xh">班图语</option><option value="zu">祖鲁语</option> </select> 
      <st-div class="__exchange__"> 
       <st-span class="st-icon-exchange"></st-span> 
      </st-div> 
      <select> <option value="">自动选择</option> <option value="zh">中文</option><option value="zh-CN">中文(简体)</option><option value="zh-HK">中文(香港)</option><option value="zh-TW">中文(繁体)</option><option value="en">英语</option><option value="ja">日语</option><option value="ko">朝鲜语</option><option value="de">德语</option><option value="fr">法语</option><option value="ru">俄语</option><option value="th">泰语</option><option value="af">南非语</option><option value="ar">阿拉伯语</option><option value="az">阿塞拜疆语</option><option value="be">比利时语</option><option value="bg">保加利亚语</option><option value="ca">加泰隆语</option><option value="cs">捷克语</option><option value="cy">威尔士语</option><option value="da">丹麦语</option><option value="dv">第维埃语</option><option value="el">希腊语</option><option value="eo">世界语</option><option value="es">西班牙语</option><option value="et">爱沙尼亚语</option><option value="eu">巴士克语</option><option value="fa">法斯语</option><option value="fi">芬兰语</option><option value="fo">法罗语</option><option value="gl">加里西亚语</option><option value="gu">古吉拉特语</option><option value="he">希伯来语</option><option value="hi">印地语</option><option value="hr">克罗地亚语</option><option value="hu">匈牙利语</option><option value="hy">亚美尼亚语</option><option value="id">印度尼西亚语</option><option value="is">冰岛语</option><option value="it">意大利语</option><option value="ka">格鲁吉亚语</option><option value="kk">哈萨克语</option><option value="kn">卡纳拉语</option><option value="kok">孔卡尼语</option><option value="ky">吉尔吉斯语</option><option value="lt">立陶宛语</option><option value="lv">拉脱维亚语</option><option value="mi">毛利语</option><option value="mk">马其顿语</option><option value="mn">蒙古语</option><option value="mr">马拉地语</option><option value="ms">马来语</option><option value="mt">马耳他语</option><option value="nb">挪威语(伯克梅尔)</option><option value="nl">荷兰语</option><option value="ns">北梭托语</option><option value="pa">旁遮普语</option><option value="pl">波兰语</option><option value="pt">葡萄牙语</option><option value="qu">克丘亚语</option><option value="ro">罗马尼亚语</option><option value="sa">梵文</option><option value="se">北萨摩斯语</option><option value="sk">斯洛伐克语</option><option value="sl">斯洛文尼亚语</option><option value="sq">阿尔巴尼亚语</option><option value="sv">瑞典语</option><option value="sw">斯瓦希里语</option><option value="syr">叙利亚语</option><option value="ta">泰米尔语</option><option value="te">泰卢固语</option><option value="tl">塔加路语</option><option value="tn">茨瓦纳语</option><option value="tr">土耳其语</option><option value="ts">宗加语</option><option value="tt">鞑靼语</option><option value="uk">乌克兰语</option><option value="ur">乌都语</option><option value="uz">乌兹别克语</option><option value="vi">越南语</option><option value="xh">班图语</option><option value="zu">祖鲁语</option> </select> 
     </st-div> 
     <st-div> 
      <select> <option value="YouDao">有道翻译</option> <option value="BaiDu">百度翻译</option> <option value="Google">谷歌翻译</option> <option value="GoogleCN">谷歌翻译（国内）</option> </select> 
      <st-div class="__action-list__"> 
       <st-div class="__button__ __btn-translate__">
        翻译 
        <st-span class="st-icon-down-dir"></st-span> 
       </st-div> 
       <st-div class="__expand__"> 
        <st-div class="__button__">
         朗读
        </st-div> 
        <st-div class="__button__">
         复制
        </st-div> 
       </st-div> 
      </st-div> 
     </st-div> 
    </st-div> 
    <st-div class="__translate-result__" style="display: none;">
     正在查询，请稍候……
    </st-div> 
    <st-div class="__translate-result__"> 
     <st-div style="display: none;"> 
      <st-span></st-span> 
      <st-span class="__retry__">
       重试
      </st-span> 
     </st-div> 
     <st-div> 
      <st-div class="__phonetic__"> 
       <st-span style="display: none;"></st-span> 
       <st-span class="__copy-and-read__"> 
        <st-span>
         朗读
        </st-span> 
        <st-span style="display: none;">
         复制
        </st-span> 
       </st-span> 
      </st-div> 
      <st-div style="display: none;"> 
       <st-ul> 
       </st-ul> 
       <st-div class="__copy-and-read__"> 
        <st-span class="__copy-and-read__">
         复制
        </st-span> 
       </st-div> 
      </st-div> 
      <st-div style="display: none;"> 
       <st-div class="__copy-and-read__"> 
        <st-span class="__copy-and-read__">
         朗读
        </st-span> 
        <st-span class="__copy-and-read__">
         复制
        </st-span> 
       </st-div> 
      </st-div> 
     </st-div> 
    </st-div> 
    <st-footer> 
     <st-span style="">
      via 
      <a target="_blank" href="https://jobs.echinacities.com/jobs/rescont/0/3176030/1?D=aXNyZWFk&amp;lang=cn&amp;r=MTY5NjQ0&amp;A=MzE3NjAzMA%3D%3D">谷歌翻译</a>
     </st-span> 
    </st-footer> 
   </st-div> 
   <st-div class="__st-btn__" style="display: none; position: fixed; z-index: 99999; left: 0px; top: 0px; transform: translateX(876px) translateY(226px);">
    译
   </st-div> 
  </st-div>
 </body>
</html>
"""

soup = BeautifulSoup(html_doc)

import time
#print soup.title
#print soup.title.name
#print soup.title.string
#print soup.p
#print soup.a
#print soup.find_all('a')
#print soup.find(id='link3')
full_text = soup.get_text()
mm = full_text.encode("UTF-8").split("导出PDF")[1]
"\n".join(mm.split("\n\n\n\n"))