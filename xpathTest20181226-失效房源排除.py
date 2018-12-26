# coding=utf-8
from lxml import etree

def getList(a):
    # print a
    if a:
        if a[0].isdigit():
            return a[0]
        return a[0].strip().encode('utf8')
    else:
        return ""


wb_data = """


<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta http-equiv="Cache-Control" content="no-transform" />
  <meta http-equiv="Cache-Control" content="no-siteapp" />
  <meta http-equiv="Content-language" content="zh-CN" />
  <meta name="format-detection" content="telephone=no" />
  <meta name="applicable-device" content="pc">
	<meta name="description" content="贝壳上海租房网,提供永泰花苑，精装两房，近地铁 配套齐 采光好出租房源信息,此房源位于上海浦东三林的永泰花苑,2室73㎡5100元.找租房房源,就来上海贝壳租房!">
	<meta name="keywords" content="永泰花苑，精装两房，近地铁 配套齐 采光好,永泰花苑租房信息,上海浦东三林房屋出租">
	<meta http-equiv="Cache-Control" content="no-transform " />
	<title>永泰花苑，精装两房，近地铁 配套齐 采光好-永泰花苑租房信息-上海永泰花苑三林房屋出租【上海贝壳租房】</title>
	<link href="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/img/favicon.ico?_v=201812252057466d9" type="image/x-icon" rel="icon">
		<link rel="stylesheet" href="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/common/css/common.css?_v=201812252057466d9">
	  <script>
    var g_conf = {};
  </script>
    <link rel="stylesheet" href="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/page/detail/index.css?_v=201812252057466d9">
    <link href='//s1.ljcdn.com/feroot/pc/asset/lianjiaIM/css/lianjiaim.css?v=15212312340214' property='stylesheet' rel="stylesheet">
  <style>
    .browser__low {
      height: 100%;
      overflow: hidden;
    }
    .browser__low--wrapper,
    .browser__low--inner {
      display: none;
    }
    .browser__low .browser__low--wrapper {
      position: absolute;
      left: 0;
      right: 0;
      top: 0;
      bottom: 0;
      z-index: 199999;
      background: #000;
      opacity: 0.5;
      filter: alpha(opacity=50);
      display: block;
    }
    .browser__low .browser__low--inner {
      background: #fff;
      position: absolute;
      left: 50%;
      top: 50%;
      z-index: 19999999;
      width: 360px;
      height: 100px;
      margin-top: -90px;
      margin-left: -200px;
      padding: 40px 20px;
      display: block;
    }
    .browser__low .browser__low--inner p {
      font-size: 20px;
      padding-bottom: 40px;
    }
    .browser__low .browser__low--inner a {
      display: inline-block;
      color: #fff;
      background: #2ab78e;
      padding: 10px 6px;
    }
  </style>
  </head>

<body>
<div class="browser__low--wrapper"></div>
<div class="browser__low--inner">
<p>您的浏览器版本过低，请升级：</p>
<a href="https://www.baidu.com/s?wd=chrome" target="_blank">谷歌 Chrome浏览器</a>
</div>

<script>
;;(function() {
  if(!([].forEach)) {
    document.body.className += ' browser__low';
  }
})();
</script>
<div class="wrapper">
   <!--<link href="--><?//=APP_MODE === 'prod' ? '//s1.ljcdn.com/feroot/pc/asset/lianjiaIM/css/lianjiaim.css?v=15212312340214' : '//s1.pc56.lj-web-56.lianjia.com/feroot/pc/asset/lianjiaIM/css/lianjiaim.css'?><!--" property='stylesheet' rel="stylesheet">-->


<div>

  <!-- 引入公用的头、导航、搜索栏 -->
  <div class="header ">
  <ul class="header__wrapper w1150 clear typeUserInfo" id="top">
                      <li class="header__item fl "><a href="//sh.lianjia.com" target="_blank">首页</a></li>
                        <li class="header__item fl "><a href="//sh.lianjia.com/ershoufang/" target="_blank">二手房</a></li>
                        <li class="header__item fl "><a href="//sh.fang.lianjia.com/loupan/" target="_blank">新房</a></li>
                        <li class="header__item fl cur"><a href="/zufang/" target="_blank">租房</a></li>
                        <li class="header__item fl "><a href="//us.lianjia.com" target="_blank">海外</a></li>
                        <li class="header__item fl "><a href="//sh.lianjia.com/xiaoqu/" target="_blank">小区</a></li>
                        <li class="header__item fl "><a href="//sh.lianjia.com/jingjiren/" target="_blank">经纪人</a></li>
                        <li class="header__item fl "><a href="//sh.lianjia.com/wenda/" target="_blank">指南</a></li>
                        <li class="header__item fl "><a href="//sh.lianjia.com/tool.html" target="_blank">工具</a></li>
                        <li class="header__item fl "><a href="//sh.lianjia.com/yezhu/" target="_blank">发布房源</a></li>
                  <li class="header__aside fr pointer typeShowUser" data-el="login" data-event_id="10794" data-event_action="target=login">
      <span data-el="login_box">
        <span data-el="btn_login" data-id="dialog_tel" class="btn-login">登录</span>/<span class="btn-resgiter" data-el="register" data-id="dialog_reg">注册</span>
      </span>
    </li>
    <li class="top__aside fr hide" data-el="user_box">
      <a href="" data-el="userName"></a>
      <a data-el="logout_btn">退出</a>
    </li>

  </ul>

</div>
  <div class="search__area">
  <div class="beike__nav">
  <a class="beike__nav--logo" href="/zufang/"></a>
  
  <ul class="beike__nav--tab">
    <li>
      <a class="cur" href="/zufang/">首页</a>
    </li>

    <li>      
      <a class="" href="/zufang/rt200600000001/">整租</a>
    </li>

    <li><a class="" href="/zufang/rt200600000002/">合租</a></li>
            <li class="beike__nav--code">
      下载APP
      <div class="nav-list beike__nav--qrcode">
        <img src="https://ajax.api.lianjia.com/qr/getDownloadQr?location=nav&amp;ljweb_channel_key=zufang_search" alt="下载贝壳APP" class="QRcode-img">
      </div> 
    </li>
    
  </ul>
</div>  <div class="search w1150" id="search">
  <!-- <a class="search__logo" href="/"></a> -->
  <div class="search__wrap">
    <input class="search__input fl" type="text" data-el="input" placeholder="请输入区域、商圈或小区名开始找房" autocomplete="off" value="" data-value="">
    <span class="search__button fl" data-el="button"></span>
  </div>

</div>  </div>

  <!-- 房源有效时 -->
      <div class="offline w1150">
      <p class="offline__icon"></p>
      <p class="offline__title">你访问的房源已失效</p>
    </div>

    <!-- 推荐房源 -->
    <div class="content--flat w1150">
                  <div class="bottom w1150" style="">
  <div class="bottom__list">

    
        <p class="bottom__list--title">同小区在租房源</p>
    
    <div class="bottom__list--wrapper">
          <div class="bottom__list--item">
        <a href="/zufang/SH2138949138241830912.html" target="_blank" data-event_id="10805" data-event_action="house_code=SH2138949138241830912&position=1"><img alt="/zufang/SH2138949138241830912.html" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/363-274.png?_v=201812252057466d9" data-el="lazy-img" class="lazyload" data-src="https://image1.ljcdn.com/rent-house-1/44c50faf4e0fbc3e9eaf5bec679d0f7a-1543817578327/0c75ea387dea90409ef66b0e54a72bf8.jpg.250x182.jpg"></a>
        <p class="bottom__list--item__des">
          <span>
            <a href="/zufang/pudong" target="_blank">浦东</a> 
            - 
            <a href="/zufang/sanlin" target="_blank">三林</a>  
            永泰花苑          </span>
          <span class="bottom__list--item--hl fr">2530元/月</span> 
        </p>
        <p class="bottom__list--item__btm">
          4室0厅1卫 43㎡
        </p>
      </div>
          <div class="bottom__list--item">
        <a href="/zufang/SH2148033059671244800.html" target="_blank" data-event_id="10805" data-event_action="house_code=SH2148033059671244800&position=2"><img alt="/zufang/SH2148033059671244800.html" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/363-274.png?_v=201812252057466d9" data-el="lazy-img" class="lazyload" data-src="https://image1.ljcdn.com/rent-house-1/af59c1c0fd06e4806a15961e8d4ec6ff-1544900467960/896ca3a428d95e11cf3acb13142519e6.jpg.250x182.jpg"></a>
        <p class="bottom__list--item__des">
          <span>
            <a href="/zufang/pudong" target="_blank">浦东</a> 
            - 
            <a href="/zufang/sanlin" target="_blank">三林</a>  
            永泰花苑          </span>
          <span class="bottom__list--item--hl fr">1548元/月</span> 
        </p>
        <p class="bottom__list--item__btm">
          3室1厅1卫 15㎡
        </p>
      </div>
          <div class="bottom__list--item">
        <a href="/zufang/SH2138262429854081024.html" target="_blank" data-event_id="10805" data-event_action="house_code=SH2138262429854081024&position=3"><img alt="/zufang/SH2138262429854081024.html" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/363-274.png?_v=201812252057466d9" data-el="lazy-img" class="lazyload" data-src="https://image1.ljcdn.com/rent-user-avatar/cba6ab20-1c45-4876-bc52-a1f43aaf6595.250x182.jpg"></a>
        <p class="bottom__list--item__des">
          <span>
            <a href="/zufang/pudong" target="_blank">浦东</a> 
            - 
            <a href="/zufang/sanlin" target="_blank">三林</a>  
            永泰花苑          </span>
          <span class="bottom__list--item--hl fr">5100元/月</span> 
        </p>
        <p class="bottom__list--item__btm">
          2室2厅1卫 75㎡
        </p>
      </div>
        </div>
  </div>
</div>
      
            <div class="bottom w1150" style="margin-top: -62px">
  <div class="bottom__list">

    
        <p class="bottom__list--title"><a href="/zufang/sanlin" target="_blank" title="三林在租房源">三林在租房源</a></p>
    
    <div class="bottom__list--wrapper">
          <div class="bottom__list--item">
        <a href="/zufang/SH2151852508648316928.html" target="_blank" data-event_id="10806" data-event_action="house_code=SH2151852508648316928&position=1"><img alt="/zufang/SH2151852508648316928.html" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/363-274.png?_v=201812252057466d9" data-el="lazy-img" class="lazyload" data-src="https://image1.ljcdn.com/rent-user-avatar/1e5b8b10-3540-456b-b645-d3201c64fd62.250x182.jpg"></a>
        <p class="bottom__list--item__des">
          <span>
            <a href="/zufang/pudong" target="_blank">浦东</a> 
            - 
            <a href="/zufang/sanlin" target="_blank">三林</a>  
            日月豪庭(公寓)          </span>
          <span class="bottom__list--item--hl fr">2600元/月</span> 
        </p>
        <p class="bottom__list--item__btm">
          4室1厅2卫 20㎡
        </p>
      </div>
          <div class="bottom__list--item">
        <a href="/zufang/SH2142663995185184768.html" target="_blank" data-event_id="10806" data-event_action="house_code=SH2142663995185184768&position=2"><img alt="/zufang/SH2142663995185184768.html" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/363-274.png?_v=201812252057466d9" data-el="lazy-img" class="lazyload" data-src="https://image1.ljcdn.com/rent-user-avatar/d31f7b1d-e96d-404b-a299-1428fa5b6b20.250x182.jpg"></a>
        <p class="bottom__list--item__des">
          <span>
            <a href="/zufang/pudong" target="_blank">浦东</a> 
            - 
            <a href="/zufang/sanlin" target="_blank">三林</a>  
            香樟苑(浦东)          </span>
          <span class="bottom__list--item--hl fr">1600元/月</span> 
        </p>
        <p class="bottom__list--item__btm">
          4室1厅1卫 12㎡
        </p>
      </div>
          <div class="bottom__list--item">
        <a href="/zufang/SH2146352577984331776.html" target="_blank" data-event_id="10806" data-event_action="house_code=SH2146352577984331776&position=3"><img alt="/zufang/SH2146352577984331776.html" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/363-274.png?_v=201812252057466d9" data-el="lazy-img" class="lazyload" data-src="https://image1.ljcdn.com/rent-user-avatar/06cbda4a-7c27-498b-8c0a-a901f8e40054.250x182.jpg"></a>
        <p class="bottom__list--item__des">
          <span>
            <a href="/zufang/pudong" target="_blank">浦东</a> 
            - 
            <a href="/zufang/sanlin" target="_blank">三林</a>  
            上南翡翠苑          </span>
          <span class="bottom__list--item--hl fr">2500元/月</span> 
        </p>
        <p class="bottom__list--item__btm">
          3室1厅1卫 15㎡
        </p>
      </div>
        </div>
  </div>
</div>
          </div>
  
  <!-- 底部面包屑链接 -->
  <div class="bread__nav w1150" style="">
  <p class="bread__nav__wrapper oneline">
                  <a href="/zufang/">上海租房网</a>&nbsp;&gt;&nbsp;
                        <a href="/zufang/pudong/">浦东租房</a>&nbsp;&gt;&nbsp;
                        <a href="/zufang/sanlin/">三林租房</a>&nbsp;&gt;&nbsp;
                      <h1>
        <a href="/zufang/c5011000010470/">永泰花苑租房</a>
      </h1>
            </p>
</div>
</div>

<input type="hidden" data-el="showBooth" value="1">
<!--登录-->
<div class="loninContaner">
    <!--mask-->
    <div class="overlay_bg" style="display: none;"></div>
    <!--账号密码登录-->
    <div id="dialog" class="panel_login animated">
        <div class="panel_info"><i class="close_login">×</i>
            <div class="panel_tab">
                <div class="title">
                    <div class="fl">账号密码登录</div>
                </div>
                <div class="clear"></div>
                <div id="con_login_user">
                    <form action="" method="post">
                        <ul>
                            <li class="item border-t userName">
                                <input type="text" class="the_input topSpecial users" placeholder="请输入手机号" maxlength="11">
                            </li>
                            <li class="item border-b pwd">
                                <input type="password" class="the_input password" maxlength="20" placeholder="请输入登录密码"><em class="password-view"></em>
                            </li>
                            <li class="item checkVerimg" style="display:none;">
                                <input type="text" class="the_input ver-img" maxlength="6" placeholder="请输入验证码">
                                <img class="verImg">
                            </li>
                            <li class="item drag" style="display:none;">
                                <div id="drag"></div>
                            </li>
                            <li class="show-error">
                                <dd>用户名或密码错误</dd>
                            </li>
                            <li class="li_01">
                                <label class="checkbox-btn"><span class="active"><input type="checkbox" name="remember" value="1" class="mind-login" checked=""></span>7天内免登录</label><a href="javascript:;" rel="nofollow" class="toforget">忘记密码</a>
                            </li>
                            <li class="li_btn"><a class="login-user-btn">登录</a>
                            </li>
                            <li class="footer-link"><a href="javascript:;" rel="nofollow" class="totellogin">手机快捷登录</a>
                            </li>
                        </ul>
                    </form>
                </div>
                <div id="con_login_agent" class="undis">
                    <form action="" method="post">
                        <ul>
                            <li class="item">
                                <dd></dd>
                                <input type="text" class="the_input users" placeholder="输入经纪人ID号码">
                            </li>
                            <li class="item">
                                <input type="password" class="the_input password" placeholder="登录密码">
                            </li>
                            <li class="li_01">
                                <label class="checkbox-btn"><span class="active"><input type="checkbox" name="remember" value="1" class="mind-login" checked=""></span>7天内免登录</label><a href="https://passport.lianjDia.com/register/resources/lianjia/forget.html?service=http://bj.lianjia.com/" rel="nofollow">忘记密码</a>
                            </li>
                            <li>
                                <input class="login-agent-btn" value="立即登录">
                            </li>
                        </ul>
                    </form>
                </div>
            </div>
        </div>
        <div class="registered"></div>
    </div>
    <!--手机快捷登录-->
    <div id="dialog_tel" class="panel_login animated btn-login bounceIn actLoginBtn" style="display: none;">
        <div class="panel_info"><i class="close_login">×</i>
            <div class="panel_tab">
                <div class="title">
                    <div class="fl">手机快捷登录</div>
                    <div class="register_text_tel">别担心，无账号自动注册不会导致手机号被泄露</div>
                </div>
                <div class="clear"></div>
                <div id="con_login_user_tel">
                    <form action="" method="post">
                        <ul>
                            <li class="item border-t userName">
                                <input type="text" class="the_input topSpecial users_tel" maxlength="11" placeholder="请输入手机号">
                            </li>
                            <!-- <li class="item pwd"><input type="password" class="the_input password_tel"  placeholder="请输入短信验证码"/></li> -->
                            <li class="item checkVerimg" style="">
                                <input type="text" class="the_input ver-img" maxlength="6" placeholder="请输入验证码">
                                <img class="verImg" src="https://upassport.lianjia.com/freshCaptch?t=1517466208641">
                            </li>
                            <li class="item border-b Verify">
                                <input type="text" class="the_input verifycode" maxlength="6" placeholder="请输入短信验证码"><a class="send_verify_code" id="send_verify_code_tel" href="javascript:;" rel="nofollow"><em>获取验证码</em></a>
                            </li>
                            <li class="send_verify_code_s" id="send_verify_code_tel_s" href="javascript:;" rel="nofollow"><em>没有收到验证码？</em><a class="voice_a">发送语音验证码</a>
                            </li>
                            <li class="show-error">
                                <dd>用户名或密码错误</dd>
                            </li>
                            <li class="li_01">
                                <label class="checkbox-btn"><span class="active"><input type="checkbox" name="remember" value="1" class="mind-login" checked=""></span>7天内免登录</label>
                            </li>
                            <li class="li_btn"><a class="login-user-tel-btn">登录</a>
                            </li>
                            <li class="footer-link"><a href="javascript:;" rel="nofollow" class="tologin">账号密码登录</a>
                            </li>
                        </ul>
                    </form>
                </div>
            </div>
        </div>
        <div class="registered"></div>
    </div>
    <!--手机号码注册-->
    <div id="dialog_reg" class="panel_login animated">
        <div class="panel_info"><i class="close_login">×</i>
            <div class="panel_tab">
                <div class="title">
                    <div class="fl">手机号码注册</div>
                    <label class="fr register_text">已有账号？<a href="javascript:;" rel="nofollow" class="tologin">去登录</a>
                    </label>
                </div>
                <div class="clear"></div>
                <div id="con_login_user_reg">
                    <form action="" method="post">
                        <ul>
                            <li class="item border-t userName">
                                <input type="text" class="the_input topSpecial users_reg" maxlength="11" placeholder="请输入手机号">
                            </li>
                            <li class="item checkVerimg" style="">
                                <input type="text" class="the_input ver-img" maxlength="6" placeholder="请输入验证码">
                                <img class="verImg">
                            </li>
                            <li class="item border-c Verify">
                                <input type="text" class="the_input verifycode" maxlength="6" placeholder="请输入短信验证码"><a class="send_verify_code" id="send_verify_code_reg" href="javascript:;" rel="nofollow"><em>获取验证码</em></a>
                            </li>
                            <li class="item border-b pwd">
                                <input type="password" class="the_input password_reg" maxlength="20" placeholder="请输入密码（最少8位，数字+字母）"><em class="password-view"></em>
                            </li>
                            <li class="send_verify_code_s" id="send_verify_code_reg_s" href="javascript:;" rel="nofollow"><em>没有收到验证码？</em><a class="voice_a">发送语音验证码</a>
                            </li>
                            <li class="show-error">
                                <dd>用户名或密码错误</dd>
                            </li>
                            <li class="li_01">
                                <label class="checkbox-btn"><span class="active"><input type="checkbox" name="read" value="1" class="read-protocol" checked=""></span>我已阅读并同意</label>
                                <a class="toprotocol" href="//www.ke.com/zhuanti/protocol" target="_blank">《贝壳用户使用协议》</a>
                                及
                                <a class="toprotocol" href="//www.ke.com/zhuanti/serviceProtocol" target="_blank">《贝壳用户服务协议》</a>
                            </li>
                            <li class="li_btn"><a class="register-user-btn">注册</a>
                            </li>
                        </ul>
                    </form>
                </div>
            </div>
        </div>
        <div class="registered"></div>
    </div>
    <!--找回密码-->
    <div id="dialog_forget" class="panel_login animated">
        <div class="panel_info"><i class="close_login">×</i>
            <div class="panel_tab">
                <div class="title">
                    <div class="fl">找回密码</div>
                </div>
                <div class="clear"></div>
                <div id="con_forget_user_tel" class="con_forget_user_tel">
                    <form action="" method="post">
                        <ul>
                            <li class="item border-t userName">
                                <input type="text" class="the_input topSpecial user_forget_phone" placeholder="请输入手机号" maxlength="11">
                            </li>
                            <li class="item checkVerimg" style="">
                                <input type="text" class="the_input ver-img" maxlength="6" placeholder="请输入验证码">
                                <img class="verImg">
                            </li>
                            <li class="item border-b Verify">
                                <input type="text" class="the_input verifycode" maxlength="6" placeholder="请输入短信验证码"><a class="send_verify_code" id="send_verify_code_forget" href="javascript:;" rel="nofollow"><em>获取验证码</em></a>
                            </li>
                            <li class="item border-t pwd" style="margin-top:-1px;">
                                <input type="password" class="the_input password_reg" maxlength="20" placeholder="请输入密码（最少8位，数字+字母）"><em class="password-view"></em>
                            </li>
                            <li class="send_verify_code_s" id="send_verify_code_forget_s"><em>没有收到验证码？</em><a class="voice_a">发送语音验证码</a>
                            </li>
                            <li class="show-error">
                                <dd>用户名或密码错误</dd>
                            </li>
                            <li class="li_btn"><a class="user-forget">修改密码</a>
                            </li>
                        </ul>
                    </form>
                </div>
                <div id="con_forget_user_pw" class="con_forget_user_pw">
                    <form action="" method="post">
                        <ul>
                            <li class="item border-t pwd">
                                <input type="password" class="the_input password_reg" maxlength="20" placeholder="请输入密码（最少8位，数字+字母）"><em class="password-view"></em>
                            </li>
                            <li class="show-error">
                                <dd>用户名或密码错误</dd>
                            </li>
                            <li class="li_btn"><a class="modify-user-pswd">修改密码</a>
                            </li>
                        </ul>
                    </form>
                </div>
            </div>
        </div>
        <div class="registered"></div>
    </div>
</div>
<script>
  g_conf.coord = {
    longitude: '121.523601',
    latitude: '31.143103'
  };
  g_conf.subway = [{"distance":1059,"lines":["11\u53f7\u7ebf(\u8fea\u58eb\u5c3c-\u82b1\u6865)"],"name":"\u4e09\u6797","point_lat":31.149017,"point_lng":121.517781}];
  g_conf.name = '永泰花苑';
  g_conf.houseCode = 'SH2152020270188339200';
  g_conf.offline = '1';

  g_conf.pageId = 'rentalDetail';
  var __requireList = ['page/detail/index'];
</script>
</div>

<div class="fix-right-v3" id="back-top" log-mod="sidebar">
  <table>
    <tbody>
      <tr>
        <td>
          <ul>
            <li class="myfav sidebar-item">
              <a title="我关注的房源" data-url="//user.lianjia.com/site/favorHouse/" data-bl="myfav">我关注的房源</a>
              <span class="popup"><i></i>我关注的房源</span>
            </li>
            <li class="sell sidebar-item">
              <a title="在线卖房" href="//sh.lianjia.com/yezhu/" target="_blank" data-bl="sell">在线卖房</a>
              <span class="popup"><i></i>在线卖房</span>
            </li>
            <li class="baodan sidebar-item">
              <a href="//sh.lianjia.com/anxinchengnuo" title="安心保单" target="_blank" data-bl="baodan">安心保单</a>
              <span class="popup">
                <i></i>安心保单
              </span>
            </li>
            <li class="download sidebar-item">
              <a href="//www.lianjia.com/client/" title="" target="_blank" data-bl="client">下载掌上链家</a>
              <span class="popup popup-qr">
                <i></i><img src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/img/wxapp.jpg?_v=201812252057466d9" alt="下载掌上链家" width="94">
                <em class="qr-title">链家微信小程序</em>
              </span>
            </li>
            <li class="phone sidebar-item">
              <a title="官方客服">官方客服</a>
              <span class="popup"><i></i>官方客服</span>
            </li>

                        <li class="feedback sidebar-item">
              <a href="https://helper.lianjia.com/it/index2#/feedbackForC?channel=lj-pc&city=310000" title="反馈/投诉" data-bl="feedback"></a>
              <span class="popup"><i></i>反馈/投诉</span>
            </li>
          </ul>
        </td>
      </tr>
    </tbody>
  </table>
  <ul>
    <li class="gotop sidebar-item" id="gotop" style="display: none;"><a title="返回顶部">返回顶部</a><span class="popup"><i></i>返回顶部</span></li>
  </ul>
</div>
<div class="footer">
  <div class="footer__wrapper w1150">

    <div class="footer__top">
      <ul class="footer__light">
                <li><a href="/zufang/wzdt/">网站地图</a></li>
              </ul>
      <a class="footer__aside" href="tel:10109666">客服电话<span>10109666</span></a>
    </div>

    <div class="footer__middle">
      <ul data-el="parentList">
                  <li><a class="cur" data-index="0">租房城市</a></li>
                  <li><a class="" data-index="1">热门商圈</a></li>
                  <li><a class="" data-index="2">推荐小区</a></li>
                  <li><a class="" data-index="3">城市新房</a></li>
                  <li><a class="" data-index="4">城市二手房</a></li>
                  <li><a class="" data-index="5">友情链接</a></li>
              </ul>
              <ul data-el="childrenList"  style="display:block">
                      <li><a href="https://xm.lianjia.com/zufang/">厦门租房</a></li>
                      <li><a href="https://su.lianjia.com/zufang/">苏州租房</a></li>
                      <li><a href="https://sy.lianjia.com/zufang/">沈阳租房</a></li>
                      <li><a href="https://gy.lianjia.com/zufang/">贵阳租房</a></li>
                      <li><a href="https://fs.lianjia.com/zufang/">佛山租房</a></li>
                      <li><a href="https://dl.lianjia.com/zufang/">大连租房</a></li>
                      <li><a href="https://zs.lianjia.com/zufang/">中山租房</a></li>
                      <li><a href="https://jian.lianjia.com/zufang/">吉安租房</a></li>
                      <li><a href="https://gz.lianjia.com/zufang/">广州租房</a></li>
                      <li><a href="https://kf.lianjia.com/zufang/">开封租房</a></li>
                      <li><a href="https://sjz.lianjia.com/zufang/">石家庄租房</a></li>
                      <li><a href="https://bj.lianjia.com/zufang/">北京租房</a></li>
                      <li><a href="https://cc.lianjia.com/zufang/">长春租房</a></li>
                      <li><a href="https://changzhou.lianjia.com/zufang/">常州租房</a></li>
                      <li><a href="https://nb.lianjia.com/zufang/">宁波租房</a></li>
                      <li><a href="https://hz.lianjia.com/zufang/">杭州租房</a></li>
                      <li><a href="https://jx.lianjia.com/zufang/">嘉兴租房</a></li>
                      <li><a href="https://wh.lianjia.com/zufang/">武汉租房</a></li>
                      <li><a href="https://cd.lianjia.com/zufang/">成都租房</a></li>
                      <li><a href="https://xa.lianjia.com/zufang/">西安租房</a></li>
                      <li><a href="https://ganzhou.lianjia.com/zufang/">赣州租房</a></li>
                      <li><a href="https://jiujiang.lianjia.com/zufang/">九江租房</a></li>
                      <li><a href="https://zj.lianjia.com/zufang/">镇江租房</a></li>
                      <li><a href="https://qd.lianjia.com/zufang/">青岛租房</a></li>
                      <li><a href="https://hk.lianjia.com/zufang/">海口租房</a></li>
                      <li><a href="https://zz.lianjia.com/zufang/">郑州租房</a></li>
                      <li><a href="https://ts.lianjia.com/zufang/">唐山租房</a></li>
                      <li><a href="https://hf.lianjia.com/zufang/">合肥租房</a></li>
                      <li><a href="https://san.lianjia.com/zufang/">三亚租房</a></li>
                      <li><a href="https://zjk.lianjia.com/zufang/">张家口租房</a></li>
                  </ul>
               <ul data-el="childrenList"  >
                      <li><a href="https://sh.lianjia.com/zufang/huamu/">花木租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/xizangbeilu/">西藏北路租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/xinxilan/">新西兰租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/huaxin/">华新租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/nanxiang/">南翔租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/jiangqiao/">江桥租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/lujiazui/">陆家嘴租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/jiadingxincheng/">嘉定新城租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/luodian/">罗店租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/wujing/">吴泾租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/penglaigongyuan/">蓬莱公园租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/jianguoxilu/">建国西路租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/zhujiajiao/">朱家角租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/shihudang/">石湖荡租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/jinze/">金泽租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/caojing/">漕泾租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/shenminbieshu/">莘闵别墅租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/xinbang/">新浜租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/laoximen/">老西门租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/dongjiadu/">董家渡租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/liantang1/">练塘租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/jianada/">加拿大租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/hongqiao1/">虹桥租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/songjiangdaxuecheng/">松江大学城租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/gaojing/">高境租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/anshan/">鞍山租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/chunshen/">春申租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/jiadinglaocheng/">嘉定老城租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/changzheng/">长征租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/changshoulu/">长寿路租房</a></li>
                  </ul>
               <ul data-el="childrenList"  >
                      <li><a href="https://sh.lianjia.com/zufang/c5011000000037/">茸联苑</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000000008/">正阳世纪星城(绅鸿苑)</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000002453/">祥德路137弄</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000002464/">虎丘路15号</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000000819/">复兴东路256-268号</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000000023/">渔港路213弄</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000002459/">四川北路2081号</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000000003/">绿地芳满庭</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000000042/">政肃路45弄</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000001646/">城中路41弄</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000000021/">林锦庭园(东区)</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000002452/">宝龙大厦</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000002441/">临平北路50号(商铺)</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000001654/">松汇中路39弄</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5020026496599109/">吴中东路492-4号</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000000009/">江桥万达广场</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000000010/">保德路1213弄</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000002460/">横浜路325号</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000000840/">龙吴路398弄</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5020026497648786/">微宁路361号</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5020026564759254/">小木桥路456号</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000000016/">奉贤农产品交易市场</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000001642/">绿苑一邨</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000000009/">江桥万达广场</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000000013/">梦丹苑</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000000039/">凤城一村</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000000042/">政肃路45弄</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000000035/">思凡花苑二街坊</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000002445/">永泰西郊苑</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000000040/">立新村</a></li>
                  </ul>
               <ul data-el="childrenList"  >
                      <li><a href="https://nj.fang.lianjia.com/">南京楼盘</a></li>
                      <li><a href="https://hk.fang.lianjia.com/">海口楼盘</a></li>
                      <li><a href="https://xa.fang.lianjia.com/">西安楼盘</a></li>
                      <li><a href="https://zj.fang.lianjia.com/">镇江楼盘</a></li>
                      <li><a href="https://cd.fang.lianjia.com/">成都楼盘</a></li>
                      <li><a href="https://xm.fang.lianjia.com/">厦门楼盘</a></li>
                      <li><a href="https://wuhu.fang.lianjia.com/">芜湖楼盘</a></li>
                      <li><a href="https://jx.fang.lianjia.com/">嘉兴楼盘</a></li>
                      <li><a href="https://jiujiang.fang.lianjia.com/">九江楼盘</a></li>
                      <li><a href="https://lf.fang.lianjia.com/">廊坊楼盘</a></li>
                      <li><a href="https://jl.fang.lianjia.com/">吉林楼盘</a></li>
                      <li><a href="https://zjk.fang.lianjia.com/">张家口楼盘</a></li>
                      <li><a href="https://ganzhou.fang.lianjia.com/">赣州楼盘</a></li>
                      <li><a href="https://xan.fang.lianjia.com/">雄安新区楼盘</a></li>
                      <li><a href="https://gz.fang.lianjia.com/">广州楼盘</a></li>
                      <li><a href="https://bj.fang.lianjia.com/">北京楼盘</a></li>
                      <li><a href="https://zz.fang.lianjia.com/">郑州楼盘</a></li>
                      <li><a href="https://wh.fang.lianjia.com/">武汉楼盘</a></li>
                      <li><a href="https://san.fang.lianjia.com/">三亚楼盘</a></li>
                      <li><a href="https://fs.fang.lianjia.com/">佛山楼盘</a></li>
                      <li><a href="https://qd.fang.lianjia.com/">青岛楼盘</a></li>
                      <li><a href="https://cq.fang.lianjia.com/">重庆楼盘</a></li>
                      <li><a href="https://sy.fang.lianjia.com/">沈阳楼盘</a></li>
                      <li><a href="https://jn.fang.lianjia.com/">济南楼盘</a></li>
                      <li><a href="https://hui.fang.lianjia.com/">惠州楼盘</a></li>
                      <li><a href="https://sjz.fang.lianjia.com/">石家庄楼盘</a></li>
                      <li><a href="https://km.fang.lianjia.com/">昆明楼盘</a></li>
                      <li><a href="https://liangshan.fang.lianjia.com/">凉山楼盘</a></li>
                      <li><a href="https://zh.fang.lianjia.com/">珠海楼盘</a></li>
                      <li><a href="https://sh.fang.lianjia.com/">上海楼盘</a></li>
                  </ul>
               <ul data-el="childrenList"  >
                      <li><a href="https://hz.ke.com/ershoufang/">杭州二手房</a></li>
                      <li><a href="https://zz.ke.com/ershoufang/">郑州二手房</a></li>
                      <li><a href="https://wh.ke.com/ershoufang/">武汉二手房</a></li>
                      <li><a href="https://fs.ke.com/ershoufang/">佛山二手房</a></li>
                      <li><a href="https://dg.ke.com/ershoufang/">东莞二手房</a></li>
                      <li><a href="https://zh.ke.com/ershoufang/">珠海二手房</a></li>
                      <li><a href="https://su.ke.com/ershoufang/">苏州二手房</a></li>
                      <li><a href="https://cq.ke.com/ershoufang/">重庆二手房</a></li>
                      <li><a href="https://taizhou.ke.com/ershoufang/">台州二手房</a></li>
                      <li><a href="https://sy.ke.com/ershoufang/">沈阳二手房</a></li>
                      <li><a href="https://nj.ke.com/ershoufang/">南京二手房</a></li>
                      <li><a href="https://zjk.ke.com/ershoufang/">张家口二手房</a></li>
                      <li><a href="https://kf.ke.com/ershoufang/">开封二手房</a></li>
                      <li><a href="https://san.ke.com/ershoufang/">三亚二手房</a></li>
                      <li><a href="https://gz.ke.com/ershoufang/">广州二手房</a></li>
                      <li><a href="https://sjz.ke.com/ershoufang/">石家庄二手房</a></li>
                      <li><a href="https://dl.ke.com/ershoufang/">大连二手房</a></li>
                      <li><a href="https://nn.ke.com/ershoufang/">南宁二手房</a></li>
                      <li><a href="https://ganzhou.ke.com/ershoufang/">赣州二手房</a></li>
                      <li><a href="https://xan.ke.com/ershoufang/">雄安新区二手房</a></li>
                      <li><a href="https://zj.ke.com/ershoufang/">镇江二手房</a></li>
                      <li><a href="https://nb.ke.com/ershoufang/">宁波二手房</a></li>
                      <li><a href="https://jian.ke.com/ershoufang/">吉安二手房</a></li>
                      <li><a href="https://hui.ke.com/ershoufang/">惠州二手房</a></li>
                      <li><a href="https://baoding.ke.com/ershoufang/">保定二手房</a></li>
                      <li><a href="https://liangshan.ke.com/ershoufang/">凉山二手房</a></li>
                      <li><a href="https://qd.ke.com/ershoufang/">青岛二手房</a></li>
                      <li><a href="https://wx.ke.com/ershoufang/">无锡二手房</a></li>
                      <li><a href="https://changzhou.ke.com/ershoufang/">常州二手房</a></li>
                      <li><a href="https://bj.ke.com/ershoufang/">北京二手房</a></li>
                  </ul>
               <ul data-el="childrenList"  >
                  </ul>
           </div>

    <div class="footer__bottom">
      <p>链家网（北京）科技有限公司 | 网络经营许可证 京ICP备16057509号-2 | &copy; Copyright&copy;2010-2018 链家网Lianjia.com版权所有</p>
      <a target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010802024019" style="display:inline-block;text-decoration:none;height:20px;line-height:20px;"><img style="margin-right: 5px;" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/img/beian.png?_v=201812252057466d9">京公网安备 11010802024019号</a>
    </div>

  </div>
</div>

<script type="text/javascript">
  var footerList = JSON.parse(JSON.stringify([{"abbr":"zfcs","expire":"2018-12-29 23:00:02","city_id":"310000","children":[{"url":"https:\/\/xm.lianjia.com\/zufang\/","title":"\u53a6\u95e8\u79df\u623f"},{"url":"https:\/\/su.lianjia.com\/zufang\/","title":"\u82cf\u5dde\u79df\u623f"},{"url":"https:\/\/sy.lianjia.com\/zufang\/","title":"\u6c88\u9633\u79df\u623f"},{"url":"https:\/\/gy.lianjia.com\/zufang\/","title":"\u8d35\u9633\u79df\u623f"},{"url":"https:\/\/fs.lianjia.com\/zufang\/","title":"\u4f5b\u5c71\u79df\u623f"},{"url":"https:\/\/dl.lianjia.com\/zufang\/","title":"\u5927\u8fde\u79df\u623f"},{"url":"https:\/\/zs.lianjia.com\/zufang\/","title":"\u4e2d\u5c71\u79df\u623f"},{"url":"https:\/\/jian.lianjia.com\/zufang\/","title":"\u5409\u5b89\u79df\u623f"},{"url":"https:\/\/gz.lianjia.com\/zufang\/","title":"\u5e7f\u5dde\u79df\u623f"},{"url":"https:\/\/kf.lianjia.com\/zufang\/","title":"\u5f00\u5c01\u79df\u623f"},{"url":"https:\/\/sjz.lianjia.com\/zufang\/","title":"\u77f3\u5bb6\u5e84\u79df\u623f"},{"url":"https:\/\/bj.lianjia.com\/zufang\/","title":"\u5317\u4eac\u79df\u623f"},{"url":"https:\/\/cc.lianjia.com\/zufang\/","title":"\u957f\u6625\u79df\u623f"},{"url":"https:\/\/changzhou.lianjia.com\/zufang\/","title":"\u5e38\u5dde\u79df\u623f"},{"url":"https:\/\/nb.lianjia.com\/zufang\/","title":"\u5b81\u6ce2\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/","title":"\u676d\u5dde\u79df\u623f"},{"url":"https:\/\/jx.lianjia.com\/zufang\/","title":"\u5609\u5174\u79df\u623f"},{"url":"https:\/\/wh.lianjia.com\/zufang\/","title":"\u6b66\u6c49\u79df\u623f"},{"url":"https:\/\/cd.lianjia.com\/zufang\/","title":"\u6210\u90fd\u79df\u623f"},{"url":"https:\/\/xa.lianjia.com\/zufang\/","title":"\u897f\u5b89\u79df\u623f"},{"url":"https:\/\/ganzhou.lianjia.com\/zufang\/","title":"\u8d63\u5dde\u79df\u623f"},{"url":"https:\/\/jiujiang.lianjia.com\/zufang\/","title":"\u4e5d\u6c5f\u79df\u623f"},{"url":"https:\/\/zj.lianjia.com\/zufang\/","title":"\u9547\u6c5f\u79df\u623f"},{"url":"https:\/\/qd.lianjia.com\/zufang\/","title":"\u9752\u5c9b\u79df\u623f"},{"url":"https:\/\/hk.lianjia.com\/zufang\/","title":"\u6d77\u53e3\u79df\u623f"},{"url":"https:\/\/zz.lianjia.com\/zufang\/","title":"\u90d1\u5dde\u79df\u623f"},{"url":"https:\/\/ts.lianjia.com\/zufang\/","title":"\u5510\u5c71\u79df\u623f"},{"url":"https:\/\/hf.lianjia.com\/zufang\/","title":"\u5408\u80a5\u79df\u623f"},{"url":"https:\/\/san.lianjia.com\/zufang\/","title":"\u4e09\u4e9a\u79df\u623f"},{"url":"https:\/\/zjk.lianjia.com\/zufang\/","title":"\u5f20\u5bb6\u53e3\u79df\u623f"}],"title":"\u79df\u623f\u57ce\u5e02","class":""},{"abbr":"rmsq","expire":"2018-12-29 23:00:02","city_id":"310000","children":[{"url":"https:\/\/sh.lianjia.com\/zufang\/huamu\/","title":"\u82b1\u6728\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/xizangbeilu\/","title":"\u897f\u85cf\u5317\u8def\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/xinxilan\/","title":"\u65b0\u897f\u5170\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/huaxin\/","title":"\u534e\u65b0\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/nanxiang\/","title":"\u5357\u7fd4\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/jiangqiao\/","title":"\u6c5f\u6865\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/lujiazui\/","title":"\u9646\u5bb6\u5634\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/jiadingxincheng\/","title":"\u5609\u5b9a\u65b0\u57ce\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/luodian\/","title":"\u7f57\u5e97\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/wujing\/","title":"\u5434\u6cfe\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/penglaigongyuan\/","title":"\u84ec\u83b1\u516c\u56ed\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/jianguoxilu\/","title":"\u5efa\u56fd\u897f\u8def\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/zhujiajiao\/","title":"\u6731\u5bb6\u89d2\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/shihudang\/","title":"\u77f3\u6e56\u8361\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/jinze\/","title":"\u91d1\u6cfd\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/caojing\/","title":"\u6f15\u6cfe\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/shenminbieshu\/","title":"\u8398\u95f5\u522b\u5885\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/xinbang\/","title":"\u65b0\u6d5c\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/laoximen\/","title":"\u8001\u897f\u95e8\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/dongjiadu\/","title":"\u8463\u5bb6\u6e21\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/liantang1\/","title":"\u7ec3\u5858\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/jianada\/","title":"\u52a0\u62ff\u5927\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/hongqiao1\/","title":"\u8679\u6865\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/songjiangdaxuecheng\/","title":"\u677e\u6c5f\u5927\u5b66\u57ce\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/gaojing\/","title":"\u9ad8\u5883\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/anshan\/","title":"\u978d\u5c71\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/chunshen\/","title":"\u6625\u7533\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/jiadinglaocheng\/","title":"\u5609\u5b9a\u8001\u57ce\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/changzheng\/","title":"\u957f\u5f81\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/changshoulu\/","title":"\u957f\u5bff\u8def\u79df\u623f"}],"title":"\u70ed\u95e8\u5546\u5708","class":""},{"abbr":"tjxq","expire":"2018-12-29 23:00:02","city_id":"310000","children":[{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000000037\/","title":"\u8338\u8054\u82d1"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000000008\/","title":"\u6b63\u9633\u4e16\u7eaa\u661f\u57ce(\u7ec5\u9e3f\u82d1)"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000002453\/","title":"\u7965\u5fb7\u8def137\u5f04"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000002464\/","title":"\u864e\u4e18\u8def15\u53f7"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000000819\/","title":"\u590d\u5174\u4e1c\u8def256-268\u53f7"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000000023\/","title":"\u6e14\u6e2f\u8def213\u5f04"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000002459\/","title":"\u56db\u5ddd\u5317\u8def2081\u53f7"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000000003\/","title":"\u7eff\u5730\u82b3\u6ee1\u5ead"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000000042\/","title":"\u653f\u8083\u8def45\u5f04"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000001646\/","title":"\u57ce\u4e2d\u8def41\u5f04"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000000021\/","title":"\u6797\u9526\u5ead\u56ed(\u4e1c\u533a)"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000002452\/","title":"\u5b9d\u9f99\u5927\u53a6"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000002441\/","title":"\u4e34\u5e73\u5317\u8def50\u53f7(\u5546\u94fa)"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000001654\/","title":"\u677e\u6c47\u4e2d\u8def39\u5f04"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5020026496599109\/","title":"\u5434\u4e2d\u4e1c\u8def492-4\u53f7"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000000009\/","title":"\u6c5f\u6865\u4e07\u8fbe\u5e7f\u573a"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000000010\/","title":"\u4fdd\u5fb7\u8def1213\u5f04"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000002460\/","title":"\u6a2a\u6d5c\u8def325\u53f7"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000000840\/","title":"\u9f99\u5434\u8def398\u5f04"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5020026497648786\/","title":"\u5fae\u5b81\u8def361\u53f7"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5020026564759254\/","title":"\u5c0f\u6728\u6865\u8def456\u53f7"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000000016\/","title":"\u5949\u8d24\u519c\u4ea7\u54c1\u4ea4\u6613\u5e02\u573a"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000001642\/","title":"\u7eff\u82d1\u4e00\u90a8"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000000009\/","title":"\u6c5f\u6865\u4e07\u8fbe\u5e7f\u573a"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000000013\/","title":"\u68a6\u4e39\u82d1"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000000039\/","title":"\u51e4\u57ce\u4e00\u6751"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000000042\/","title":"\u653f\u8083\u8def45\u5f04"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000000035\/","title":"\u601d\u51e1\u82b1\u82d1\u4e8c\u8857\u574a"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000002445\/","title":"\u6c38\u6cf0\u897f\u90ca\u82d1"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000000040\/","title":"\u7acb\u65b0\u6751"}],"title":"\u63a8\u8350\u5c0f\u533a","class":""},{"abbr":"csxf","expire":"2018-12-29 23:00:02","city_id":"310000","children":[{"url":"https:\/\/nj.fang.lianjia.com\/","title":"\u5357\u4eac\u697c\u76d8"},{"url":"https:\/\/hk.fang.lianjia.com\/","title":"\u6d77\u53e3\u697c\u76d8"},{"url":"https:\/\/xa.fang.lianjia.com\/","title":"\u897f\u5b89\u697c\u76d8"},{"url":"https:\/\/zj.fang.lianjia.com\/","title":"\u9547\u6c5f\u697c\u76d8"},{"url":"https:\/\/cd.fang.lianjia.com\/","title":"\u6210\u90fd\u697c\u76d8"},{"url":"https:\/\/xm.fang.lianjia.com\/","title":"\u53a6\u95e8\u697c\u76d8"},{"url":"https:\/\/wuhu.fang.lianjia.com\/","title":"\u829c\u6e56\u697c\u76d8"},{"url":"https:\/\/jx.fang.lianjia.com\/","title":"\u5609\u5174\u697c\u76d8"},{"url":"https:\/\/jiujiang.fang.lianjia.com\/","title":"\u4e5d\u6c5f\u697c\u76d8"},{"url":"https:\/\/lf.fang.lianjia.com\/","title":"\u5eca\u574a\u697c\u76d8"},{"url":"https:\/\/jl.fang.lianjia.com\/","title":"\u5409\u6797\u697c\u76d8"},{"url":"https:\/\/zjk.fang.lianjia.com\/","title":"\u5f20\u5bb6\u53e3\u697c\u76d8"},{"url":"https:\/\/ganzhou.fang.lianjia.com\/","title":"\u8d63\u5dde\u697c\u76d8"},{"url":"https:\/\/xan.fang.lianjia.com\/","title":"\u96c4\u5b89\u65b0\u533a\u697c\u76d8"},{"url":"https:\/\/gz.fang.lianjia.com\/","title":"\u5e7f\u5dde\u697c\u76d8"},{"url":"https:\/\/bj.fang.lianjia.com\/","title":"\u5317\u4eac\u697c\u76d8"},{"url":"https:\/\/zz.fang.lianjia.com\/","title":"\u90d1\u5dde\u697c\u76d8"},{"url":"https:\/\/wh.fang.lianjia.com\/","title":"\u6b66\u6c49\u697c\u76d8"},{"url":"https:\/\/san.fang.lianjia.com\/","title":"\u4e09\u4e9a\u697c\u76d8"},{"url":"https:\/\/fs.fang.lianjia.com\/","title":"\u4f5b\u5c71\u697c\u76d8"},{"url":"https:\/\/qd.fang.lianjia.com\/","title":"\u9752\u5c9b\u697c\u76d8"},{"url":"https:\/\/cq.fang.lianjia.com\/","title":"\u91cd\u5e86\u697c\u76d8"},{"url":"https:\/\/sy.fang.lianjia.com\/","title":"\u6c88\u9633\u697c\u76d8"},{"url":"https:\/\/jn.fang.lianjia.com\/","title":"\u6d4e\u5357\u697c\u76d8"},{"url":"https:\/\/hui.fang.lianjia.com\/","title":"\u60e0\u5dde\u697c\u76d8"},{"url":"https:\/\/sjz.fang.lianjia.com\/","title":"\u77f3\u5bb6\u5e84\u697c\u76d8"},{"url":"https:\/\/km.fang.lianjia.com\/","title":"\u6606\u660e\u697c\u76d8"},{"url":"https:\/\/liangshan.fang.lianjia.com\/","title":"\u51c9\u5c71\u697c\u76d8"},{"url":"https:\/\/zh.fang.lianjia.com\/","title":"\u73e0\u6d77\u697c\u76d8"},{"url":"https:\/\/sh.fang.lianjia.com\/","title":"\u4e0a\u6d77\u697c\u76d8"}],"title":"\u57ce\u5e02\u65b0\u623f","class":""},{"abbr":"csesf","expire":"2018-12-29 23:00:02","city_id":"310000","children":[{"url":"https:\/\/hz.ke.com\/ershoufang\/","title":"\u676d\u5dde\u4e8c\u624b\u623f"},{"url":"https:\/\/zz.ke.com\/ershoufang\/","title":"\u90d1\u5dde\u4e8c\u624b\u623f"},{"url":"https:\/\/wh.ke.com\/ershoufang\/","title":"\u6b66\u6c49\u4e8c\u624b\u623f"},{"url":"https:\/\/fs.ke.com\/ershoufang\/","title":"\u4f5b\u5c71\u4e8c\u624b\u623f"},{"url":"https:\/\/dg.ke.com\/ershoufang\/","title":"\u4e1c\u839e\u4e8c\u624b\u623f"},{"url":"https:\/\/zh.ke.com\/ershoufang\/","title":"\u73e0\u6d77\u4e8c\u624b\u623f"},{"url":"https:\/\/su.ke.com\/ershoufang\/","title":"\u82cf\u5dde\u4e8c\u624b\u623f"},{"url":"https:\/\/cq.ke.com\/ershoufang\/","title":"\u91cd\u5e86\u4e8c\u624b\u623f"},{"url":"https:\/\/taizhou.ke.com\/ershoufang\/","title":"\u53f0\u5dde\u4e8c\u624b\u623f"},{"url":"https:\/\/sy.ke.com\/ershoufang\/","title":"\u6c88\u9633\u4e8c\u624b\u623f"},{"url":"https:\/\/nj.ke.com\/ershoufang\/","title":"\u5357\u4eac\u4e8c\u624b\u623f"},{"url":"https:\/\/zjk.ke.com\/ershoufang\/","title":"\u5f20\u5bb6\u53e3\u4e8c\u624b\u623f"},{"url":"https:\/\/kf.ke.com\/ershoufang\/","title":"\u5f00\u5c01\u4e8c\u624b\u623f"},{"url":"https:\/\/san.ke.com\/ershoufang\/","title":"\u4e09\u4e9a\u4e8c\u624b\u623f"},{"url":"https:\/\/gz.ke.com\/ershoufang\/","title":"\u5e7f\u5dde\u4e8c\u624b\u623f"},{"url":"https:\/\/sjz.ke.com\/ershoufang\/","title":"\u77f3\u5bb6\u5e84\u4e8c\u624b\u623f"},{"url":"https:\/\/dl.ke.com\/ershoufang\/","title":"\u5927\u8fde\u4e8c\u624b\u623f"},{"url":"https:\/\/nn.ke.com\/ershoufang\/","title":"\u5357\u5b81\u4e8c\u624b\u623f"},{"url":"https:\/\/ganzhou.ke.com\/ershoufang\/","title":"\u8d63\u5dde\u4e8c\u624b\u623f"},{"url":"https:\/\/xan.ke.com\/ershoufang\/","title":"\u96c4\u5b89\u65b0\u533a\u4e8c\u624b\u623f"},{"url":"https:\/\/zj.ke.com\/ershoufang\/","title":"\u9547\u6c5f\u4e8c\u624b\u623f"},{"url":"https:\/\/nb.ke.com\/ershoufang\/","title":"\u5b81\u6ce2\u4e8c\u624b\u623f"},{"url":"https:\/\/jian.ke.com\/ershoufang\/","title":"\u5409\u5b89\u4e8c\u624b\u623f"},{"url":"https:\/\/hui.ke.com\/ershoufang\/","title":"\u60e0\u5dde\u4e8c\u624b\u623f"},{"url":"https:\/\/baoding.ke.com\/ershoufang\/","title":"\u4fdd\u5b9a\u4e8c\u624b\u623f"},{"url":"https:\/\/liangshan.ke.com\/ershoufang\/","title":"\u51c9\u5c71\u4e8c\u624b\u623f"},{"url":"https:\/\/qd.ke.com\/ershoufang\/","title":"\u9752\u5c9b\u4e8c\u624b\u623f"},{"url":"https:\/\/wx.ke.com\/ershoufang\/","title":"\u65e0\u9521\u4e8c\u624b\u623f"},{"url":"https:\/\/changzhou.ke.com\/ershoufang\/","title":"\u5e38\u5dde\u4e8c\u624b\u623f"},{"url":"https:\/\/bj.ke.com\/ershoufang\/","title":"\u5317\u4eac\u4e8c\u624b\u623f"}],"title":"\u57ce\u5e02\u4e8c\u624b\u623f","class":""},{"abbr":"yqlj","title":"\u53cb\u60c5\u94fe\u63a5","city_id":"310000","expire":"2018-12-26","children":[]}]))

</script></body>


<!-- 自动推送代码 -->
<script>
  (function(){
  var canonicalURL, curProtocol;
  //Get the <link> tag
  var x=document.getElementsByTagName("link");
  //Find the last canonical URL
  if(x.length > 0){
  for (i=0;i<x.length;i++){
  if(x[i].rel.toLowerCase() == 'canonical' && x[i].href){
  canonicalURL=x[i].href;
  }
  }
  }
  //Get protocol
  if (!canonicalURL){
  curProtocol = window.location.protocol.split(':')[0];
  }
  else{
  curProtocol = canonicalURL.split(':')[0];
  }
  //Get current URL if the canonical URL does not exist
  if (!canonicalURL) canonicalURL = window.location.href;
  //Assign script content. Replace current URL with the canonical URL
  !function(){var e=/([http|https]:\/\/[a-zA-Z0-9\_\.]+\.baidu\.com)/gi,r=canonicalURL,t=document.referrer;if(!e.test(r)){var n=(String(curProtocol).toLowerCase() === 'https')?"https://sp0.baidu.com/9_Q4simg2RQJ8t7jm9iCKT-xh_/s.gif":"//api.share.baidu.com/s.gif";t?(n+="?r="+encodeURIComponent(document.referrer),r&&(n+="&l="+r)):r&&(n+="?l="+r);var i=new Image;i.src=n}}(window);})();
</script>

<script type="text/javascript" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/common/js/common.js?_v=201812252057466d9"></script>

<script type="text/javascript">
  //引入脚本后
  var imConf = {
          "ajaxroot": "\/\/ajax.api.ke.com\/",
          "imAppid": "ZULIN_WEB_20181122",
          "imAppkey": "0a4e8669fc2a50cbbeeb969726a7ab46"
      };
</script>
<script>
var __basePath = 'https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src?_v=201812252057466d9'.split("?");
require.config({
  baseUrl: __basePath[0],
  paths: {
  },
  urlArgs:  __basePath[1]
});
var config = {"fe_root":"https:\/\/s1.ljcdn.com\/matrix_lianjia_pc\/dist\/pc","version":"201812252057466d9","js_ns":"m_pages_zufangDetail","cur_city_id":"310000","cur_city_name":"\u4e0a\u6d77","cur_city_short":"sh"};
</script>
<script>
;;(function() {
  for(var i = 0, len = __requireList.length; i < len; i++) {
    require([__requireList[i]], function(engine) {
      engine.init();
    });
  }
})();
</script>
<!--动态脚本内容-->
<div style="display: none">
  <script src="https://s19.cnzz.com/z_stat.php?id=1273627291&web_id=1273627291" language="JavaScript"></script>
</div>
<script>
  window.ljConf = {
    city_abbr: 'sh',
    city_id: '310000',
    city_name: '上海',
  }
window.__UDL_CONFIG = window.__UDL_CONFIG || {};
window.__UDL_CONFIG.pid = window.__UDL_CONFIG.pid || (document.domain.search('ke.com')>-1 ? 'bigc_pc_rent':'matrixpc');
window.__UDL_CONFIG.env = ('prod' === 'prod' ? (document.domain.search('ke.com')>-1 ? 'dac' : 'lianjia') : 'test');
window.__UDL_CONFIG[document.domain.search('ke.com') > -1?'uicode':'ljweb_channel_key'] = g_conf.pageId || '';
with(document)0[(getElementsByTagName('head')[0]||body).appendChild(createElement('script')).src='//s1.ljcdn.com/matrix_pc/dist/pc/third/dig.js?'+__basePath[1]]
</script>

</html>
"""
response = etree.HTML(wb_data)
for quote in response.xpath('//div[@class="content__list--item"]'):
    print getList(quote.xpath('.//div/p[@class="content__list--item--title twoline"]/a/text()'))
    print getList(quote.xpath('.//div/p[@class="content__list--item--title twoline"]/a/@href'))

    print getList(quote.xpath('.//div/p[@class="content__list--item--des"]/a[position()=1]/@href'))
    print getList(quote.xpath('.//div/p[@class="content__list--item--des"]/a[position()=1]/text()'))
    print getList(quote.xpath('.//div/p[@class="content__list--item--des"]/a[position()=2]/@href'))
    print getList(quote.xpath('.//div/p[@class="content__list--item--des"]/a[position()=2]/text()'))

    print "***************************************************"



# print "/zufang/SH2136750194585780224.html"[8:-5]


