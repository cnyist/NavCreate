f_output = open("fold/out.txt", 'w')  # 输出文件夹
f_text = open("fold/text.txt")  # 输入文件夹
title = "CloudPlayer 的网址导航"  # 网页title
long_logo = "https://cdn.jsdelivr.net/gh/yunwanjia-cloud/nav/assets/images/white_left_icon.png"  # 长条 logo
logo = "https://cdn.jsdelivr.net/gh/yunwanjia-cloud/nav/assets/images/icon.png"  # logo
favicon = "https://cdn.jsdelivr.net/gh/yunwanjia-cloud/nav/assets/images/fa.ico"  # favicon
"""网站, 图标, 名字, 描述"""


head = """<!DOCTYPE html>
<html lang="zh">

<head>
    <script async src = "//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js" >
    </script>
    <script>
    (adsbygoogle = window.adsbygoogle || []).push({
        google_ad_client: "ca-pub-8550836177608334",
        enable_page_level_ads: true
    });
    </script>
    <script>
    var _hmt = _hmt || [];
    (function() {
      var hm = document.createElement("script");
      hm.src = "https://hm.baidu.com/hm.js?c05bb16ea908292af9f6c513087a1cc3";
      var s = document.getElementsByTagName("script")[0]; 
      s.parentNode.insertBefore(hm, s);
    })();
    </script>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="author" content="viggo" />
    <title>""" + title + """</title>
    <meta name="keywords" content="CloudPlayer">
    <meta name="description" content="nav CloudPlayer">
    <link rel="shortcut icon" href=\"""" + favicon + """">
    <link rel="stylesheet" href="http://fonts.googleapis.com/css?family=Arimo:400,700,400italic">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/yunwanjia-cloud/nav/assets/css/fonts/linecons/css/linecons.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/yunwanjia-cloud/nav/assets/css/fonts/fontawesome/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/yunwanjia-cloud/nav/assets/css/bootstrap.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/yunwanjia-cloud/nav/assets/css/xenon-core.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/yunwanjia-cloud/nav/assets/css/xenon-components.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/yunwanjia-cloud/nav/assets/css/xenon-skins.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/yunwanjia-cloud/nav/assets/css/nav.css">
    <script src="https://cdn.jsdelivr.net/gh/yunwanjia-cloud/nav/assets/js/jquery-1.11.1.min.js"></script>
    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
        <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
    <!-- / FB Open Graph -->
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://zplayer.cloud">
    <meta property="og:title" content="CloudPlayer, 云玩家, 网址导航">
    <meta property="og:description" content="CloudPlayer, 云玩家, 网址导航">
    <meta property="og:image" content="https://cdn.jsdelivr.net/gh/yunwanjia-cloud/nav/assets/images/icon.png">
    <meta property="og:site_name" content="CloudPlayer, 云玩家, 网址导航">
    <!-- / Twitter Cards -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="CloudPlayer, 云玩家, 网址导航">
    <meta name="twitter:description" content="CloudPlayer, 云玩家, 网址导航">
    <meta name="twitter:image" content="https://cdn.jsdelivr.net/gh/yunwanjia-cloud/nav/assets/images/icon.png">
</head>

<body class="page-body">
    <!-- skin-white -->
    <div class="page-container">
        <div class="sidebar-menu toggle-others fixed">
            <div class="sidebar-menu-inner">
                <header class="logo-env">
                    <!-- logo -->
                    <div class="logo">
                        <a href="index.html" class="logo-expanded">
                            <img src=\"""" + long_logo + """" width="100%" alt="" />
                        </a>
                        <a href="index.html" class="logo-collapsed">
                            <img src=\"""" + logo + """" width="40" alt="" />
                        </a>
                    </div>
                    <div class="mobile-menu-toggle visible-xs">
                        <a href="#" data-toggle="user-info-menu">
                            <i class="linecons-cog"></i>
                        </a>
                        <a href="#" data-toggle="mobile-menu">
                            <i class="fa-bars"></i>
                        </a>
                    </div>
                </header>
                <ul id="main-menu" class="main-menu">"""

middle = """                    <li>
                        <a href="about.html">
                            <i class="linecons-heart"></i>
                            <span class="tooltip-blue">关于本站</span>
                            <span class="label label-Primary pull-right hidden-collapsed">♥︎</span>
                        </a>
                    </li>
                </ul>
            </div>
        </div>
        <div class="main-content">
            <nav class="navbar user-info-navbar" role="navigation">
                <!-- User Info, Notifications and Menu Bar -->
                <!-- Left links for user info navbar -->
                <ul class="user-info-menu left-links list-inline list-unstyled">
                    <li class="hidden-sm hidden-xs">
                        <a href="#" data-toggle="sidebar">
                            <i class="fa-bars"></i>
                        </a>
                    </li>
                </ul>
            </nav>
            <!--  -->"""

tail = """            </div>
            <br />
        </div>
    </div>
    <!-- 锚点平滑移动 -->
    <script type="text/javascript">
    $(document).ready(function() {
         //img lazy loaded
         const observer = lozad();
         observer.observe();

        $('.user-info-menu .hidden-sm').click(function(){
            if($('.sidebar-menu').hasClass('collapsed')) {
                $('.has-sub.expanded > ul').attr("style","")
            } else {
                $('.has-sub.expanded > ul').show()
            }
        })
        $("#main-menu li ul li").click(function() {
            $(this).siblings('li').removeClass('active'); // 删除其他兄弟元素的样式
            $(this).addClass('active'); // 添加当前元素的样式
        });
        $("a.smooth").click(function(ev) {
            ev.preventDefault();

            public_vars.$mainMenu.add(public_vars.$sidebarProfile).toggleClass('mobile-is-visible');
            ps_destroy();
            $("html, body").animate({
                scrollTop: $($(this).attr("href")).offset().top - 30
            }, {
                duration: 500,
                easing: "swing"
            });
        });
        return false;
    });

    var href = "";
    var pos = 0;
    $("a.smooth").click(function(e) {
        $("#main-menu li").each(function() {
            $(this).removeClass("active");
        });
        $(this).parent("li").addClass("active");
        e.preventDefault();
        href = $(this).attr("href");
        pos = $(href).position().top - 30;
    });
    </script>
    <!-- Bottom Scripts -->
    <script src="https://cdn.jsdelivr.net/gh/yunwanjia-cloud/nav/assets/js/bootstrap.min.js"></script>
    <script src="https://cdn.jsdelivr.net/gh/yunwanjia-cloud/nav/assets/js/TweenMax.min.js"></script>
    <script src="https://cdn.jsdelivr.net/gh/yunwanjia-cloud/nav/assets/js/resizeable.js"></script>
    <script src="https://cdn.jsdelivr.net/gh/yunwanjia-cloud/nav/assets/js/joinable.js"></script>
    <script src="https://cdn.jsdelivr.net/gh/yunwanjia-cloud/nav/assets/js/xenon-api.js"></script>
    <script src="https://cdn.jsdelivr.net/gh/yunwanjia-cloud/nav/assets/js/xenon-toggles.js"></script>
    <!-- JavaScripts initializations and stuff -->
    <script src="https://cdn.jsdelivr.net/gh/yunwanjia-cloud/nav/assets/js/xenon-custom.js"></script>
    <script src="https://cdn.jsdelivr.net/gh/yunwanjia-cloud/nav/assets/js/lozad.js"></script>
</body>

</html>"""

li_head = "<li>"
li_tail = "</li>"
a_tail = "</a>"
ul_head = "<ul>"
ul_tail = "</ul>"
def a_head(name):
    return '<a href="#' + name + '" class="smooth">'
def span_all(name):
    return '<span class="title">' + name + '</span>'
def get_title_text(title):
    for i in range(len(title)):
        if title[i] != ' ':
            continue
        if title[-1] == '\n':
            return title[i + 1:-1]
        else:
            return title[i + 1:]
def get_title_level(line):
    temp = '#'
    sum = 0
    for i in line:
        if i == temp:
            sum += 1
        else:
            return sum
def create_list(title):
    tag = 0
    text_list = []
    text_list.insert(tag, a_head(title))
    tag += 1
    text_list.insert(tag, a_tail)
    text_list.insert(tag, span_all(title))
    return text_list


div_row_head = '<div class="row">'
div_tail = '</div>'
div_col = """<div class="col-sm-3">"""
div_x_com = '<div class="xe-comment">'
div_xe = '<div class="xe-comment-entry">'

block_list = []
tag_block = 0

def div_onclick_head(url):
    return """<div class="xe-widget xe-conversations box2 label-info" onclick="window.open('""" + url + """', '_blank')" data-toggle="tooltip" data-placement="bottom" title="" data-original-title=\"""" + url + """">"""
def a_img_all(src):
    return """<a class="xe-user-img"><img data-src=\"""" + src + """" class="lozad img-circle" width="40"></a>"""
def a_href_all(name):
    return """<a href="#" class="xe-user-name overflowClip_1"><strong>""" + name + """</strong></a>"""
def p_over_all(desc):
    return """<p class="overflowClip_2">""" + desc + "</p>"
def h_n_all(n, title):
    n = str(n)
    return '<h' + n + """ class="text-gray"><i class="linecons-tag" style="margin-right: 7px;" id=\"""" + title + """"></i>""" + title + '</h1>'

def c_4_block(line):
    block_list = []
    tag_block = 0
    if line[-1] == '\n':
        line = line[:-1]
    line_list = line.split(',')
    block_list.insert(tag_block, div_col)
    tag_block += 1
    block_list.insert(tag_block, div_tail)
    block_list.insert(tag_block, div_onclick_head(line_list[0]))
    tag_block += 1
    block_list.insert(tag_block, div_tail)
    block_list.insert(tag_block, div_xe)
    tag_block += 1
    block_list.insert(tag_block, div_tail)
    block_list.insert(tag_block, a_img_all(line_list[1]))
    tag_block += 1
    block_list.insert(tag_block, div_x_com)
    tag_block += 1
    block_list.insert(tag_block, div_tail)
    block_list.insert(tag_block, a_href_all(line_list[2]))
    tag_block += 1
    block_list.insert(tag_block, p_over_all(line_list[3]))
    return block_list

def new_block(now_title, now_level, f_text):
    block_list = []
    tag_block = 0
    while True:
        block_list.insert(tag_block, div_row_head)
        tag_block += 1
        block_list.insert(tag_block, div_tail)
        for i in range(4):
            fine_num = f_text.tell()
            line = f_text.readline()
            if line == '':
                break
            if get_title_level(line) != 0:
                f_text.seek(fine_num)
                break
            block_list[tag_block:tag_block] = c_4_block(line)
            tag_block += 11
        if line == '':
            break
        if get_title_level(line) != 0:
            break
        tag_block += 1
    return block_list

block_list = []
def create_block(now_level, now_title):
    text_list = []
    tag = 0
    while(True):
        now_line = f_text.readline()
        now_level = get_title_level(now_line)
        now_title = get_title_text(now_line)
        global block_list
        block_list.append(h_n_all(now_level, now_title))

        fine_num = f_text.tell()
        next_line = f_text.readline()
        next_title = get_title_text(next_line)
        next_level = get_title_level(next_line)
        if next_level == 0:
            f_text.seek(fine_num)
            block_list += new_block(now_title, now_level, f_text)
            fine_num = f_text.tell()
            next_line = f_text.readline()
            next_title = get_title_text(next_line)
            next_level = get_title_level(next_line)
        f_text.seek(fine_num)

        text_list.insert(tag, li_head)
        tag += 1
        text_list.insert(tag, li_tail)
        temp = create_list(now_title)
        text_list[tag:tag] = temp
        tag += len(temp)

        if next_line == '':
            return text_list, -1, block_list

        if(now_level < next_level):
            text_list.insert(tag, ul_head)
            tag += 1
            text_list.insert(tag, ul_tail)
            temp, re_next_level, an_temp = create_block(next_level, next_title)
            text_list[tag:tag] = temp
            tag += len(temp)
            tag += 2
            if re_next_level < now_level:
                return text_list, re_next_level, block_list
            elif re_next_level == -1:
                return text_list, -1, block_list
        if(now_level == next_level):
            tag += 1
            continue
        if(now_level > next_level):
            return text_list, next_level, block_list
my = create_block(0, 1)
f_output.write(head + ("".join(my[0])) + middle + ("".join(my[2])) + tail)