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
	<meta name="description" content="贝壳上海租房网,提供真实的上海浦东租房信息、出租房源信息、租房价格,包括上海浦东整租、合租、公寓出租等信息,以及上海浦东房屋出租个人信息、经纪人信息、品牌公寓信息等.找租房房源,就来上海贝壳租房!">
	<meta name="keywords" content="上海浦东租房信息,上海浦东出租房网,上海浦东房屋出租价格">
	<meta http-equiv="Cache-Control" content="no-transform " />
	<title>上海浦东租房信息_上海浦东出租房源|房屋出租价格【上海贝壳租房】</title>
	<link href="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/img/favicon.ico?_v=201812111636405e7" type="image/x-icon" rel="icon">
		<link rel="stylesheet" href="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/common/css/common.css?_v=201812111636405e7">
	  <script>
    var g_conf = {};
  </script>
    <link rel="stylesheet" href="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/page/list/index.css?_v=201812111636405e7">
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
   
<div>
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
  <div class="bread__nav w1150" style="margin-bottom: 0px;">
  <p class="bread__nav__wrapper oneline">
                  <a href="http://sh.lianjia.com/">链家网上海站</a>&nbsp;&gt;&nbsp;
                        <a href="http://sh.lianjia.com/zufang/">上海租房</a>&nbsp;&gt;&nbsp;
                      <h1>
        <a href="http://sh.lianjia.com/zufang/pudong/">浦东租房</a>
      </h1>
            </p>
</div>  <div class="filter">
    <div class="filter__wrapper w1150" id="filter">
      <ul class="filter__item--noaside">
        <li class="filter__item--level1 down strong" data-tab="1" data-el="area" data-antitarget="station"><a href="/zufang/" onclick="return false;">按区域</a></li>
              <li class="filter__item--level1 " data-tab="1" data-el="station" data-antitarget="area"><a href="/zufang/" onclick="return false;">按地铁线</a></li>
            </ul>

      <ul data-target="area" class="">
              <li data-id="0" data-type="district" class="filter__item--level2 filter__item--aside ">
          <a href="/zufang/"  rel="nofollow">不限</a>
        </li>
              <li data-id="310106" data-type="district" class="filter__item--level2  ">
          <a href="/zufang/jingan/"  >静安</a>
        </li>
              <li data-id="310104" data-type="district" class="filter__item--level2  ">
          <a href="/zufang/xuhui/"  >徐汇</a>
        </li>
              <li data-id="310101" data-type="district" class="filter__item--level2  ">
          <a href="/zufang/huangpu/"  >黄浦</a>
        </li>
              <li data-id="310105" data-type="district" class="filter__item--level2  ">
          <a href="/zufang/changning/"  >长宁</a>
        </li>
              <li data-id="310107" data-type="district" class="filter__item--level2  ">
          <a href="/zufang/putuo/"  >普陀</a>
        </li>
              <li data-id="310115" data-type="district" class="filter__item--level2  strong">
          <a href="/zufang/pudong/"  >浦东</a>
        </li>
              <li data-id="310113" data-type="district" class="filter__item--level2  ">
          <a href="/zufang/baoshan/"  >宝山</a>
        </li>
              <li data-id="310108" data-type="district" class="filter__item--level2  ">
          <a href="/zufang/zhabei/"  >闸北</a>
        </li>
              <li data-id="310109" data-type="district" class="filter__item--level2  ">
          <a href="/zufang/hongkou/"  >虹口</a>
        </li>
              <li data-id="310110" data-type="district" class="filter__item--level2  ">
          <a href="/zufang/yangpu/"  >杨浦</a>
        </li>
              <li data-id="310112" data-type="district" class="filter__item--level2  ">
          <a href="/zufang/minhang/"  >闵行</a>
        </li>
              <li data-id="310116" data-type="district" class="filter__item--level2  ">
          <a href="/zufang/jinshan/"  >金山</a>
        </li>
              <li data-id="310114" data-type="district" class="filter__item--level2  ">
          <a href="/zufang/jiading/"  >嘉定</a>
        </li>
              <li data-id="310230" data-type="district" class="filter__item--level2  ">
          <a href="/zufang/chongming/"  >崇明</a>
        </li>
              <li data-id="310120" data-type="district" class="filter__item--level2  ">
          <a href="/zufang/fengxian/"  >奉贤</a>
        </li>
              <li data-id="310117" data-type="district" class="filter__item--level2  ">
          <a href="/zufang/songjiang/"  >松江</a>
        </li>
              <li data-id="310118" data-type="district" class="filter__item--level2  ">
          <a href="/zufang/qingpu/"  >青浦</a>
        </li>
            </ul>

      <ul class="hide" data-target="station">
              <li data-id="0" data-type="line" class="filter__item--level2 filter__item--aside strong">
          <a href="/ditiezufang/" rel="nofollow">不限</a>
        </li>
              <li data-id="143685036" data-type="line" class="filter__item--level2  ">
          <a href="/ditiezufang/li143685036/" >1号线</a>
        </li>
              <li data-id="143685058" data-type="line" class="filter__item--level2  ">
          <a href="/ditiezufang/li143685058/" >2号线</a>
        </li>
              <li data-id="143684974" data-type="line" class="filter__item--level2  ">
          <a href="/ditiezufang/li143684974/" >3号线</a>
        </li>
              <li data-id="143685059" data-type="line" class="filter__item--level2  ">
          <a href="/ditiezufang/li143685059/" >4号线</a>
        </li>
              <li data-id="143685060" data-type="line" class="filter__item--level2  ">
          <a href="/ditiezufang/li143685060/" >5号线</a>
        </li>
              <li data-id="143685061" data-type="line" class="filter__item--level2  ">
          <a href="/ditiezufang/li143685061/" >6号线</a>
        </li>
              <li data-id="110460726" data-type="line" class="filter__item--level2  ">
          <a href="/ditiezufang/li110460726/" >7号线</a>
        </li>
              <li data-id="143685063" data-type="line" class="filter__item--level2  ">
          <a href="/ditiezufang/li143685063/" >8号线</a>
        </li>
              <li data-id="143685064" data-type="line" class="filter__item--level2  ">
          <a href="/ditiezufang/li143685064/" >9号线</a>
        </li>
              <li data-id="143685065" data-type="line" class="filter__item--level2  ">
          <a href="/ditiezufang/li143685065/" >10号线(新江湾城-虹桥火车站)</a>
        </li>
              <li data-id="5020034682070158" data-type="line" class="filter__item--level2  ">
          <a href="/ditiezufang/li5020034682070158/" >10号线(新江湾城-航中路)</a>
        </li>
              <li data-id="143685066" data-type="line" class="filter__item--level2  ">
          <a href="/ditiezufang/li143685066/" >11号线(迪士尼-花桥)</a>
        </li>
              <li data-id="5020034644313403" data-type="line" class="filter__item--level2  ">
          <a href="/ditiezufang/li5020034644313403/" >11号线(迪士尼-嘉定北)	</a>
        </li>
              <li data-id="110460731" data-type="line" class="filter__item--level2  ">
          <a href="/ditiezufang/li110460731/" >12号线</a>
        </li>
              <li data-id="110460732" data-type="line" class="filter__item--level2  ">
          <a href="/ditiezufang/li110460732/" >13号线</a>
        </li>
              <li data-id="110460733" data-type="line" class="filter__item--level2  ">
          <a href="/ditiezufang/li110460733/" >16号线</a>
        </li>
              <li data-id="99620692" data-type="line" class="filter__item--level2  ">
          <a href="/ditiezufang/li99620692/" >17号线</a>
        </li>
              <li data-id="5020034301305472" data-type="line" class="filter__item--level2  ">
          <a href="/ditiezufang/li5020034301305472/" >轨道交通浦江线</a>
        </li>
            </ul>

              <ul data-target="area">
                                                <li data-id="0" data-type="bizcircle" class="filter__item--level3 filter__item--aside strong">
                <a href="/zufang/pudong/">不限</a>
              </li>
                                  <li class="filter__item--title">b</li>                          <li data-id="611900123" data-type="bizcircle" class="filter__item--level3  ">
                <a href="/zufang/beicai/">北蔡</a>
              </li>
                          <li data-id="613000290" data-type="bizcircle" class="filter__item--level3  ">
                <a href="/zufang/biyun/">碧云</a>
              </li>
                                  <li class="filter__item--title">c</li>                          <li data-id="613000291" data-type="bizcircle" class="filter__item--level3  ">
                <a href="/zufang/caolu/">曹路</a>
              </li>
                          <li data-id="613000292" data-type="bizcircle" class="filter__item--level3  ">
                <a href="/zufang/chuansha/">川沙</a>
              </li>
                                  <li class="filter__item--title">d</li>                          <li data-id="613000293" data-type="bizcircle" class="filter__item--level3  ">
                <a href="/zufang/datuanzhen/">大团镇</a>
              </li>
                                  <li class="filter__item--title">g</li>                          <li data-id="613000297" data-type="bizcircle" class="filter__item--level3  ">
                <a href="/zufang/geqing/">合庆</a>
              </li>
                          <li data-id="613000295" data-type="bizcircle" class="filter__item--level3  ">
                <a href="/zufang/gaohang/">高行</a>
              </li>
                          <li data-id="613000294" data-type="bizcircle" class="filter__item--level3  ">
                <a href="/zufang/gaodong/">高东</a>
              </li>
                                  <li class="filter__item--title">h</li>                          <li data-id="611900130" data-type="bizcircle" class="filter__item--level3  ">
                <a href="/zufang/huamu/">花木</a>
              </li>
                          <li data-id="613000296" data-type="bizcircle" class="filter__item--level3  ">
                <a href="/zufang/hangtou/">航头</a>
              </li>
                          <li data-id="613000298" data-type="bizcircle" class="filter__item--level3  ">
                <a href="/zufang/huinan/">惠南</a>
              </li>
                                  <li class="filter__item--title">j</li>                          <li data-id="611900131" data-type="bizcircle" class="filter__item--level3  ">
                <a href="/zufang/jinqiao/">金桥</a>
              </li>
                          <li data-id="613000299" data-type="bizcircle" class="filter__item--level3  ">
                <a href="/zufang/jinyang/">金杨</a>
              </li>
                                  <li class="filter__item--title">k</li>                          <li data-id="613000300" data-type="bizcircle" class="filter__item--level3  ">
                <a href="/zufang/kangqiao/">康桥</a>
              </li>
                                  <li class="filter__item--title">l</li>                          <li data-id="611900136" data-type="bizcircle" class="filter__item--level3  ">
                <a href="/zufang/lujiazui/">陆家嘴</a>
              </li>
                          <li data-id="613000301" data-type="bizcircle" class="filter__item--level3  ">
                <a href="/zufang/laogangzhen/">老港镇</a>
              </li>
                          <li data-id="613000303" data-type="bizcircle" class="filter__item--level3  ">
                <a href="/zufang/lingangxincheng/">临港新城</a>
              </li>
                          <li data-id="613000302" data-type="bizcircle" class="filter__item--level3  ">
                <a href="/zufang/lianyang/">联洋</a>
              </li>
                                  <li class="filter__item--title">n</li>                          <li data-id="613000305" data-type="bizcircle" class="filter__item--level3  ">
                <a href="/zufang/nichengzhen/">泥城镇</a>
              </li>
                          <li data-id="613000304" data-type="bizcircle" class="filter__item--level3  ">
                <a href="/zufang/nanmatou/">南码头</a>
              </li>
                                  <li class="filter__item--title">s</li>                          <li data-id="611900138" data-type="bizcircle" class="filter__item--level3  ">
                <a href="/zufang/sanlin/">三林</a>
              </li>
                          <li data-id="611900139" data-type="bizcircle" class="filter__item--level3  ">
                <a href="/zufang/shibo/">世博</a>
              </li>
                          <li data-id="613000307" data-type="bizcircle" class="filter__item--level3  ">
                <a href="/zufang/shuyuanzhen/">书院镇</a>
              </li>
                                  <li class="filter__item--title">t</li>                          <li data-id="611900141" data-type="bizcircle" class="filter__item--level3  ">
                <a href="/zufang/tangqiao/">塘桥</a>
              </li>
                          <li data-id="613000308" data-type="bizcircle" class="filter__item--level3  ">
                <a href="/zufang/tangzhen/">唐镇</a>
              </li>
                                  <li class="filter__item--title">w</li>                          <li data-id="611900143" data-type="bizcircle" class="filter__item--level3  ">
                <a href="/zufang/waigaoqiao/">外高桥</a>
              </li>
                          <li data-id="613000309" data-type="bizcircle" class="filter__item--level3  ">
                <a href="/zufang/wanxiangzhen/">万祥镇</a>
              </li>
                          <li data-id="613000310" data-type="bizcircle" class="filter__item--level3  ">
                <a href="/zufang/weifang/">潍坊</a>
              </li>
                                  <li class="filter__item--title">x</li>                          <li data-id="613000312" data-type="bizcircle" class="filter__item--level3  ">
                <a href="/zufang/xuanqiao/">宣桥</a>
              </li>
                          <li data-id="613000311" data-type="bizcircle" class="filter__item--level3  ">
                <a href="/zufang/xinchang/">新场</a>
              </li>
                                  <li class="filter__item--title">y</li>                          <li data-id="611101108" data-type="bizcircle" class="filter__item--level3  ">
                <a href="/zufang/yuqiao1/">御桥</a>
              </li>
                          <li data-id="613000313" data-type="bizcircle" class="filter__item--level3  ">
                <a href="/zufang/yangdong/">杨东</a>
              </li>
                          <li data-id="613000315" data-type="bizcircle" class="filter__item--level3  ">
                <a href="/zufang/yuanshen/">源深</a>
              </li>
                          <li data-id="613000314" data-type="bizcircle" class="filter__item--level3  ">
                <a href="/zufang/yangjing/">洋泾</a>
              </li>
                                  <li class="filter__item--title">z</li>                          <li data-id="611900148" data-type="bizcircle" class="filter__item--level3  ">
                <a href="/zufang/zhangjiang/">张江</a>
              </li>
                          <li data-id="613000317" data-type="bizcircle" class="filter__item--level3  ">
                <a href="/zufang/zhuqiao/">祝桥</a>
              </li>
                          <li data-id="613000316" data-type="bizcircle" class="filter__item--level3  ">
                <a href="/zufang/zhoupu/">周浦</a>
              </li>
                              </ul>
      
              <ul data-target="station">
                  </ul>
      
              <ul class="filter__ul" data-el="rentType">
            <li class="filter__item--level4 filter__item--aside"><a href="javascript:;">方式</a></li>
                      <li data-id="0" class="filter__item--level4 strong">
              <a href="/zufang/pudong/" rel="nofollow" >不限</a>
            </li>
                      <li data-id="200600000001" class="filter__item--level4 ">
              <a href="/zufang/pudong/rt200600000001/"  >整租</a>
            </li>
                      <li data-id="200600000002" class="filter__item--level4 ">
              <a href="/zufang/pudong/rt200600000002/"  >合租</a>
            </li>
                  </ul>
      
      
              <ul class="filter__ul" data-el="filterPrice">
            <li class="filter__item--level5 filter__item--aside"><a href="javascript:;">租金</a></li>
                      <li class="filter__item--level5 check ">
              <a href="/zufang/pudong/rp1/">≤1000元</a>
            </li>
                      <li class="filter__item--level5 check ">
              <a href="/zufang/pudong/rp2/">1000-1500元</a>
            </li>
                      <li class="filter__item--level5 check ">
              <a href="/zufang/pudong/rp3/">1500-2000元</a>
            </li>
                      <li class="filter__item--level5 check ">
              <a href="/zufang/pudong/rp4/">2000-3000元</a>
            </li>
                      <li class="filter__item--level5 check ">
              <a href="/zufang/pudong/rp5/">3000-5000元</a>
            </li>
                      <li class="filter__item--level5 check ">
              <a href="/zufang/pudong/rp6/">5000-8000元</a>
            </li>
                      <li class="filter__item--level5 check ">
              <a href="/zufang/pudong/rp7/">≥8000元</a>
            </li>
                      <li class="filter__item--input" data-url="/zufang/pudong/brp{min}erp{max}/"><input type="text" data-el="input_start" value="">-<input data-el="input_end" type="text" value="">元<span class="filter__button" data-el="button"></span></li>
        </ul>
      
              <ul class="filter__ul">
            <li class="filter__item--level5 filter__item--aside"><a href="javascript:;">户型</a></li>
                      <li class="filter__item--level5 check ">
              <a href="/zufang/pudong/l0/">一居</a>
            </li>
                      <li class="filter__item--level5 check ">
              <a href="/zufang/pudong/l1/">两居</a>
            </li>
                      <li class="filter__item--level5 check ">
              <a href="/zufang/pudong/l2/">三居</a>
            </li>
                      <li class="filter__item--level5 check ">
              <a href="/zufang/pudong/l3/">四居+</a>
            </li>
                  </ul>
      
      
              <ul class="filter__ul ">
            <li class="filter__item--level5 filter__item--aside"><a href="javascript:;">朝向</a></li>
                      <li class="filter__item--level5 check ">
              <a rel="nofollow" href="/zufang/pudong/f100500000001/">东</a>
            </li>
                      <li class="filter__item--level5 check ">
              <a rel="nofollow" href="/zufang/pudong/f100500000005/">西</a>
            </li>
                      <li class="filter__item--level5 check ">
              <a rel="nofollow" href="/zufang/pudong/f100500000003/">南</a>
            </li>
                      <li class="filter__item--level5 check ">
              <a rel="nofollow" href="/zufang/pudong/f100500000007/">北</a>
            </li>
                      <li class="filter__item--level5 check ">
              <a rel="nofollow" href="/zufang/pudong/f100500000009/">南北</a>
            </li>
                  </ul>
      
              <ul class="filter__ul hide">
            <li class="filter__item--level5 filter__item--aside"><a href="javascript:;">品牌</a></li>
                      <li class="filter__item--level5 check ">
              <a href="/zufang/pudong/ab200301001000/">链家</a>
            </li>
                      <li class="filter__item--level5 check ">
              <a href="/zufang/pudong/ab200302002000/">自如</a>
            </li>
                          </ul>
      
              <ul class="filter__ul hide">
            <li class="filter__item--level5 filter__item--aside"><a href="javascript:;">特色</a></li>
                      <li class="filter__item--level5 check ">
              <a rel="nofollow" href="/zufang/pudong/su1/">近地铁</a>
            </li>
                      <li class="filter__item--level5 check ">
              <a rel="nofollow" href="/zufang/pudong/bc1/">拎包入住</a>
            </li>
                      <li class="filter__item--level5 check ">
              <a rel="nofollow" href="/zufang/pudong/de1/">精装修</a>
            </li>
                      <li class="filter__item--level5 check ">
              <a rel="nofollow" href="/zufang/pudong/rpw1/">押一付一</a>
            </li>
                      <li class="filter__item--level5 check ">
              <a rel="nofollow" href="/zufang/pudong/in1/">新上</a>
            </li>
                      <li class="filter__item--level5 check ">
              <a rel="nofollow" href="/zufang/pudong/ht1/">认证公寓</a>
            </li>
                      <li class="filter__item--level5 check ">
              <a rel="nofollow" href="/zufang/pudong/hk1/">随时看房</a>
            </li>
                      <li class="filter__item--level5 check ">
              <a rel="nofollow" href="/zufang/pudong/cl10011/">0元住</a>
            </li>
                  </ul>
      
              <ul class="filter__ul hide">
            <li class="filter__item--level5 filter__item--aside"><a href="javascript:;">楼层</a></li>
                      <li class="filter__item--level5 check ">
              <a rel="nofollow" href="/zufang/pudong/lc200500000003/">低楼层</a>
            </li>
                      <li class="filter__item--level5 check ">
              <a rel="nofollow" href="/zufang/pudong/lc200500000002/">中楼层</a>
            </li>
                      <li class="filter__item--level5 check ">
              <a rel="nofollow" href="/zufang/pudong/lc200500000001/">高楼层</a>
            </li>
                  </ul>
      
              <ul class="filter__ul hide">
            <li class="filter__item--level5 filter__item--aside"><a href="javascript:;">电梯</a></li>
                      <li class="filter__item--level5 check ">
              <a rel="nofollow" href="/zufang/pudong/ie0/">无电梯</a>
            </li>
                      <li class="filter__item--level5 check ">
              <a rel="nofollow" href="/zufang/pudong/ie1/">有电梯</a>
            </li>
                  </ul>
          </div>
    <div class="filter__item--more" data-el="filterMore">收起<i class="more-icon"></i></div>
  </div>

  <div class="content w1150" id="content">
    <div class="content__article">
      <p class="content__title">
        已为您找到 <span class="content__title--hl">6892</span> 套 上海租房

        <span class="content__title--aside"><a href="/zufang/" id="clearUrl">清空条件</a></span>
      </p>

      <ul class="content__filter" id="contentList">
                        <li data-event_id="10800" data-event_action="search_condition=/zufang/pudong/" class='content__filter--selected'>
            <a href="/zufang/pudong/" data-event_id="10797" data-event_action="target=综合排序">综合排序</a>
          </li>
                                <li data-event_id="10800" data-event_action="search_condition=/zufang/pudong/rco11/" >
            <a href="/zufang/pudong/rco11/" data-event_id="10797" data-event_action="target=最新上架">最新上架</a>
          </li>
                                                                                                          <li data-event_id="10800" data-event_action="search_condition=/zufang/pudong/rco21/" class=' '>

                          <a href="/zufang/pudong/rco21/" data-event_id="10797" data-event_action="target=价格">价格</a>
                      </li>
                                                                                                          <li data-event_id="10800" data-event_action="search_condition=/zufang/pudong/rco31/" class=' '>

                          <a href="/zufang/pudong/rco31/" data-event_id="10797" data-event_action="target=面积">面积</a>
                      </li>
                    </ul>
            <div class="content__list">
                        <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SH2135972204813492224.html"><img alt="金光小区 2室1厅 5200元" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=201812111636405e7" data-src="https://image1.ljcdn.com/310000-inspection/f7b00d74-aaca-4881-8de7-66a06023d681.jpg_600x450.jpg.250x182.jpg" class="lazyload"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SH2135972204813492224.html">
                    金光小区 2室1厅 5200元                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/pudong">浦东</a>-<a href="/zufang/sanlin" target="_blank">三林</a>
                  <i>/</i>
                  62㎡
                  <i>/</i>南                  <i>/</i>
                    2室1厅1卫                  <span class="hide">
                    <i>/</i>
                    低楼层                                            （6层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">12天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em>5200</em> 元/月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SH2136024121254092800.html"><img alt="陆家嘴板块，精装设计一室一厅，可拎包入住诚意租。" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=201812111636405e7" data-src="https://image1.ljcdn.com/310000-inspection/ca0b0417-403d-4d60-b921-a0a3be686997.jpg.250x182.jpg" class="lazyload"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SH2136024121254092800.html">
                    陆家嘴板块，精装设计一室一厅，可拎包入住诚意租。                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/pudong">浦东</a>-<a href="/zufang/lujiazui" target="_blank">陆家嘴</a>
                  <i>/</i>
                  40㎡
                  <i>/</i>南                  <i>/</i>
                    1室1厅1卫                  <span class="hide">
                    <i>/</i>
                    高楼层                                            （6层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">12天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em>5200</em> 元/月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SH2136650136586297344.html"><img alt="新川苑 大三房精装修 有停车位 拎包入住 价格可谈" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=201812111636405e7" data-src="https://image1.ljcdn.com/310000-inspection/1d97cd35-f94a-44ea-896e-c4e88560a738.jpg.250x182.jpg" class="lazyload"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SH2136650136586297344.html">
                    新川苑 大三房精装修 有停车位 拎包入住 价格可谈                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/pudong">浦东</a>-<a href="/zufang/chuansha" target="_blank">川沙</a>
                  <i>/</i>
                  130㎡
                  <i>/</i>南 北                  <i>/</i>
                    3室2厅2卫                  <span class="hide">
                    <i>/</i>
                    中楼层                                            （6层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">11天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em>5000</em> 元/月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SH2136750194585780224.html"><img alt="金橘新苑，中装二房，一改二，钥匙在手，说看就看" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=201812111636405e7" data-src="https://image1.ljcdn.com/310000-inspection/eff9d135-4b90-4a82-812d-a86805427501.jpg.250x182.jpg" class="lazyload"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SH2136750194585780224.html">
                    金橘新苑，中装二房，一改二，钥匙在手，说看就看                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/pudong">浦东</a>-<a href="/zufang/sanlin" target="_blank">三林</a>
                  <i>/</i>
                  61㎡
                  <i>/</i>南                  <i>/</i>
                    2室1厅1卫                  <span class="hide">
                    <i>/</i>
                    低楼层                                            （18层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">11天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em>4700</em> 元/月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SH2136949915656929280.html"><img alt="近地铁，南北两房+小区中间位置+中间楼层+看房方便" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=201812111636405e7" data-src="https://image1.ljcdn.com/310000-inspection/0f5b3d1c-291f-44c1-acb9-8c1faba21ed5.jpg.250x182.jpg" class="lazyload"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SH2136949915656929280.html">
                    近地铁，南北两房+小区中间位置+中间楼层+看房方便                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/pudong">浦东</a>-<a href="/zufang/yangjing" target="_blank">洋泾</a>
                  <i>/</i>
                  50㎡
                  <i>/</i>南                  <i>/</i>
                    2室1厅1卫                  <span class="hide">
                    <i>/</i>
                    中楼层                                            （6层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">10天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em>4500</em> 元/月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SH2137388927936634880.html"><img alt="金色碧云 2室2厅 9900元" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=201812111636405e7" data-src="https://image1.ljcdn.com/310000-inspection/f47131fc-6379-4b67-8b4b-2ab3472ad765.jpg.250x182.jpg" class="lazyload"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SH2137388927936634880.html">
                    金色碧云 2室2厅 9900元                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/pudong">浦东</a>-<a href="/zufang/biyun" target="_blank">碧云</a>
                  <i>/</i>
                  97㎡
                  <i>/</i>南                  <i>/</i>
                    2室2厅1卫                  <span class="hide">
                    <i>/</i>
                    低楼层                                            （14层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">10天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em>9900</em> 元/月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SH2137535819886632960.html"><img alt="陆家嘴八佰伴旁边，一室户出租，价格优惠，看房方便。" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=201812111636405e7" data-src="https://image1.ljcdn.com/310000-inspection/dc0f4d7f-7900-46d6-a6ee-798c4e85b06d.jpg.250x182.jpg" class="lazyload"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SH2137535819886632960.html">
                    陆家嘴八佰伴旁边，一室户出租，价格优惠，看房方便。                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/pudong">浦东</a>-<a href="/zufang/lujiazui" target="_blank">陆家嘴</a>
                  <i>/</i>
                  29㎡
                  <i>/</i>南                  <i>/</i>
                    1室0厅1卫                  <span class="hide">
                    <i>/</i>
                    中楼层                                            （5层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">10天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em>3500</em> 元/月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SH2137553685725847552.html"><img alt="暖色系一房 温馨舒适 全装全配 拎包入住 随时看房" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=201812111636405e7" data-src="https://image1.ljcdn.com/310000-inspection/7b457708-3515-4aaf-87fb-d8a64e19c224.jpg.250x182.jpg" class="lazyload"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SH2137553685725847552.html">
                    暖色系一房 温馨舒适 全装全配 拎包入住 随时看房                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/pudong">浦东</a>-<a href="/zufang/lianyang" target="_blank">联洋</a>
                  <i>/</i>
                  76㎡
                  <i>/</i>南                  <i>/</i>
                    1室2厅1卫                  <span class="hide">
                    <i>/</i>
                    中楼层                                            （23层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">10天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em>9000</em> 元/月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SH2137616532824932352.html"><img alt="六号线金桥站，金桥国际，久金广场，精装修。" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=201812111636405e7" data-src="https://image1.ljcdn.com/310000-inspection/a88bd920-267b-4a1d-b3f8-7a1d0737cb68.jpg.250x182.jpg" class="lazyload"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SH2137616532824932352.html">
                    六号线金桥站，金桥国际，久金广场，精装修。                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/pudong">浦东</a>-<a href="/zufang/jinyang" target="_blank">金杨</a>
                  <i>/</i>
                  39㎡
                  <i>/</i>南                  <i>/</i>
                    1室1厅1卫                  <span class="hide">
                    <i>/</i>
                    高楼层                                            （6层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">9天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em>3800</em> 元/月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SH2137662471233093632.html"><img alt="近8号线杨思站，一室一厅精装修，家具家电全配户型好" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=201812111636405e7" data-src="https://image1.ljcdn.com/310000-inspection/de6b7dde-e5db-4791-aefb-ff31d8176036.jpg.250x182.jpg" class="lazyload"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SH2137662471233093632.html">
                    近8号线杨思站，一室一厅精装修，家具家电全配户型好                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/pudong">浦东</a>-<a href="/zufang/sanlin" target="_blank">三林</a>
                  <i>/</i>
                  40㎡
                  <i>/</i>南                  <i>/</i>
                    1室1厅1卫                  <span class="hide">
                    <i>/</i>
                    高楼层                                            （6层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">9天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em>4200</em> 元/月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SH2137695162426728448.html"><img alt="婚房装修，品牌家具，塘桥四号线地铁口精装两房，" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=201812111636405e7" data-src="https://image1.ljcdn.com/310000-inspection/7ae23b12-af4b-4076-b2e9-cfa4011e062e.jpg.250x182.jpg" class="lazyload"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SH2137695162426728448.html">
                    婚房装修，品牌家具，塘桥四号线地铁口精装两房，                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/pudong">浦东</a>-<a href="/zufang/tangqiao" target="_blank">塘桥</a>
                  <i>/</i>
                  53㎡
                  <i>/</i>南 北                  <i>/</i>
                    2室1厅1卫                  <span class="hide">
                    <i>/</i>
                    高楼层                                            （6层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">9天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em>6200</em> 元/月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SH2137712823575519232.html"><img alt="世纪大道地铁 竹园新村精装两房 拎包入住 干净整洁" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=201812111636405e7" data-src="https://image1.ljcdn.com/310000-inspection/test-44ff0f96-773c-4666-900d-df561756f8e2.png.250x182.jpg" class="lazyload"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SH2137712823575519232.html">
                    世纪大道地铁 竹园新村精装两房 拎包入住 干净整洁                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/pudong">浦东</a>-<a href="/zufang/yuanshen" target="_blank">源深</a>
                  <i>/</i>
                  53㎡
                  <i>/</i>南                  <i>/</i>
                    2室1厅1卫                  <span class="hide">
                    <i>/</i>
                    高楼层                                            （6层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">9天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em>4800</em> 元/月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SH2138206428446867456.html"><img alt="中等装修，自住风格，采光好，距离地铁500米" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=201812111636405e7" data-src="https://image1.ljcdn.com/310000-inspection/26c2db7a-91da-431b-bbad-98d41be33713.jpg.250x182.jpg" class="lazyload"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SH2138206428446867456.html">
                    中等装修，自住风格，采光好，距离地铁500米                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/pudong">浦东</a>-<a href="/zufang/jinqiao" target="_blank">金桥</a>
                  <i>/</i>
                  40㎡
                  <i>/</i>南                  <i>/</i>
                    1室1厅1卫                  <span class="hide">
                    <i>/</i>
                    中楼层                                            （6层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">9天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em>3500</em> 元/月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SH2138301666267496448.html"><img alt="近云台地铁口精装装修两房，适合居家白领上班居住" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=201812111636405e7" data-src="https://image1.ljcdn.com/310000-inspection/4291062e-bf1c-4b05-8596-9197f3fb25e0.jpg.250x182.jpg" class="lazyload"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SH2138301666267496448.html">
                    近云台地铁口精装装修两房，适合居家白领上班居住                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/pudong">浦东</a>-<a href="/zufang/shibo" target="_blank">世博</a>
                  <i>/</i>
                  68㎡
                  <i>/</i>南                  <i>/</i>
                    2室1厅1卫                  <span class="hide">
                    <i>/</i>
                    中楼层                                            （12层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">9天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em>6000</em> 元/月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SH2138331911796834304.html"><img alt="近69双线，业主诚意出租，价格可谈，拎包入住." src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=201812111636405e7" data-src="https://image1.ljcdn.com/310000-inspection/190d626a-4b5f-452b-a9fe-e7de0d9fb495.jpg.250x182.jpg" class="lazyload"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SH2138331911796834304.html">
                    近69双线，业主诚意出租，价格可谈，拎包入住.                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/pudong">浦东</a>-<a href="/zufang/jinyang" target="_blank">金杨</a>
                  <i>/</i>
                  41㎡
                  <i>/</i>南                  <i>/</i>
                    1室1厅1卫                  <span class="hide">
                    <i>/</i>
                    低楼层                                            （4层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">9天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em>3500</em> 元/月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SH2138367772047187968.html"><img alt="8号线杨思站 精装两房 一站换乘6、11号线 诚意出租" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=201812111636405e7" data-src="https://image1.ljcdn.com/310000-inspection/a597ae88-7ed2-4b23-a213-b877bcf99355.jpg.250x182.jpg" class="lazyload"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SH2138367772047187968.html">
                    8号线杨思站 精装两房 一站换乘6、11号线 诚意出租                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/pudong">浦东</a>-<a href="/zufang/sanlin" target="_blank">三林</a>
                  <i>/</i>
                  54㎡
                  <i>/</i>南                  <i>/</i>
                    2室1厅1卫                  <span class="hide">
                    <i>/</i>
                    高楼层                                            （6层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">8天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em>4500</em> 元/月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SH2138376815688032256.html"><img alt="新出精装修87平大两房 楼层佳 看房方便 近地铁" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=201812111636405e7" data-src="https://image1.ljcdn.com/310000-inspection/49d61568-8933-40ad-8514-7d7780d4aa7b.jpg.250x182.jpg" class="lazyload"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SH2138376815688032256.html">
                    新出精装修87平大两房 楼层佳 看房方便 近地铁                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/pudong">浦东</a>-<a href="/zufang/tangqiao" target="_blank">塘桥</a>
                  <i>/</i>
                  87㎡
                  <i>/</i>南                  <i>/</i>
                    2室2厅1卫                  <span class="hide">
                    <i>/</i>
                    低楼层                                            （6层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">8天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em>7300</em> 元/月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SH2138396254324137984.html"><img alt="品臻国际公寓 精装一室 看房有钥匙" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=201812111636405e7" data-src="https://image1.ljcdn.com/310000-inspection/5a55a7cb-90a9-49fb-a082-9e79ddccbba1.jpg.250x182.jpg" class="lazyload"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SH2138396254324137984.html">
                    品臻国际公寓 精装一室 看房有钥匙                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/pudong">浦东</a>-<a href="/zufang/waigaoqiao" target="_blank">外高桥</a>
                  <i>/</i>
                  55㎡
                  <i>/</i>南                  <i>/</i>
                    1室1厅1卫                  <span class="hide">
                    <i>/</i>
                    中楼层                                            （19层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">8天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em>3600</em> 元/月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SH2138441523220447232.html"><img alt="浦江海景 2室2厅 16000元" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=201812111636405e7" data-src="https://image1.ljcdn.com/310000-inspection/2988d372-d432-434e-ade4-685dd42f8fd4.jpg.250x182.jpg" class="lazyload"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SH2138441523220447232.html">
                    浦江海景 2室2厅 16000元                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/pudong">浦东</a>-<a href="/zufang/tangqiao" target="_blank">塘桥</a>
                  <i>/</i>
                  122㎡
                  <i>/</i>南                  <i>/</i>
                    2室2厅2卫                  <span class="hide">
                    <i>/</i>
                    低楼层                                            （20层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">8天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em>16000</em> 元/月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SH2138442110876532736.html"><img alt="中冶尚城  中层精装两房  南北通透" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=201812111636405e7" data-src="https://image1.ljcdn.com/310000-inspection/bf81f8a8-9dc7-45e1-9e4f-a0b322014648.jpg.250x182.jpg" class="lazyload"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SH2138442110876532736.html">
                    中冶尚城  中层精装两房  南北通透                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/pudong">浦东</a>-<a href="/zufang/jinqiao" target="_blank">金桥</a>
                  <i>/</i>
                  88㎡
                  <i>/</i>南                  <i>/</i>
                    2室2厅1卫                  <span class="hide">
                    <i>/</i>
                    中楼层                                            （14层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">8天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em>5800</em> 元/月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SH2138854732167380992.html"><img alt="6号线精装全配两房，户型正气，家电全配，看房方便" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=201812111636405e7" data-src="https://image1.ljcdn.com/310000-inspection/a25f0031-07a3-4c4f-9d62-e2e50048b2e6.jpg.250x182.jpg" class="lazyload"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SH2138854732167380992.html">
                    6号线精装全配两房，户型正气，家电全配，看房方便                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/pudong">浦东</a>-<a href="/zufang/jinqiao" target="_blank">金桥</a>
                  <i>/</i>
                  65㎡
                  <i>/</i>南                  <i>/</i>
                    2室1厅1卫                  <span class="hide">
                    <i>/</i>
                    中楼层                                            （6层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">8天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em>4600</em> 元/月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SH2139067936852418560.html"><img alt="精装两室 近2号线川沙站 近公园 采光通风优良随时看房" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=201812111636405e7" data-src="https://image1.ljcdn.com/310000-inspection/prod-b535e313-63a0-41b3-b1f4-f4e00bf775b8.png.250x182.jpg" class="lazyload"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SH2139067936852418560.html">
                    精装两室 近2号线川沙站 近公园 采光通风优良随时看房                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/pudong">浦东</a>-<a href="/zufang/chuansha" target="_blank">川沙</a>
                  <i>/</i>
                  65㎡
                  <i>/</i>南                  <i>/</i>
                    2室1厅1卫                  <span class="hide">
                    <i>/</i>
                    高楼层                                            （5层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">7天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em>3500</em> 元/月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SH2139087104310263808.html"><img alt="浦建小区 1室1厅 4500元" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=201812111636405e7" data-src="https://image1.ljcdn.com/310000-inspection/feaec37a-ef3b-409d-a063-3233ffb9716c.jpg.250x182.jpg" class="lazyload"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SH2139087104310263808.html">
                    浦建小区 1室1厅 4500元                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/pudong">浦东</a>-<a href="/zufang/tangqiao" target="_blank">塘桥</a>
                  <i>/</i>
                  34㎡
                  <i>/</i>南                  <i>/</i>
                    1室1厅1卫                  <span class="hide">
                    <i>/</i>
                    中楼层                                            （6层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">7天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em>4500</em> 元/月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SH2139111097834143744.html"><img alt="金桥酒店公寓  二期带煤气户型 有钥匙，随时看房" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=201812111636405e7" data-src="https://image1.ljcdn.com/310000-inspection/test-c1b8c3f1-99f7-4eb1-9023-774872c2af76.png.250x182.jpg" class="lazyload"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SH2139111097834143744.html">
                    金桥酒店公寓  二期带煤气户型 有钥匙，随时看房                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/pudong">浦东</a>-<a href="/zufang/biyun" target="_blank">碧云</a>
                  <i>/</i>
                  65㎡
                  <i>/</i>南                  <i>/</i>
                    1室1厅1卫                  <span class="hide">
                    <i>/</i>
                    高楼层                                            （19层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">7天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em>6500</em> 元/月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SH2139895651540926464.html"><img alt="近地铁，精装修，拎包入住，配套齐全" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=201812111636405e7" data-src="https://image1.ljcdn.com/310000-inspection/e657f2b4-3682-4fde-a904-d6600125eb17.jpg.250x182.jpg" class="lazyload"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SH2139895651540926464.html">
                    近地铁，精装修，拎包入住，配套齐全                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/pudong">浦东</a>-<a href="/zufang/weifang" target="_blank">潍坊</a>
                  <i>/</i>
                  31㎡
                  <i>/</i>南                  <i>/</i>
                    1室1厅1卫                  <span class="hide">
                    <i>/</i>
                    低楼层                                            （6层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">6天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_new">新上</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em>4100</em> 元/月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SH2140243125745229824.html"><img alt="电梯精装大一房+拎包入住+居住感舒适+看房来电" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=201812111636405e7" data-src="https://image1.ljcdn.com/310000-inspection/7eba0d66-6bbf-4a43-a675-b6e409fc79e4.jpg.250x182.jpg" class="lazyload"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SH2140243125745229824.html">
                    电梯精装大一房+拎包入住+居住感舒适+看房来电                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/pudong">浦东</a>-<a href="/zufang/tangqiao" target="_blank">塘桥</a>
                  <i>/</i>
                  77㎡
                  <i>/</i>东南                  <i>/</i>
                    1室1厅1卫                  <span class="hide">
                    <i>/</i>
                    低楼层                                            （28层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">6天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_new">新上</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em>6500</em> 元/月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SH2140269465009389568.html"><img alt="仁恒滨江正气三房 精装修全配  有钥匙随时看房" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=201812111636405e7" data-src="https://image1.ljcdn.com/310000-inspection/881e1ff0-a1f7-4ad5-a0c0-17869cfda728.jpg.250x182.jpg" class="lazyload"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SH2140269465009389568.html">
                    仁恒滨江正气三房 精装修全配  有钥匙随时看房                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/pudong">浦东</a>-<a href="/zufang/lujiazui" target="_blank">陆家嘴</a>
                  <i>/</i>
                  130㎡
                  <i>/</i>南                  <i>/</i>
                    3室2厅2卫                  <span class="hide">
                    <i>/</i>
                    中楼层                                            （26层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">6天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_new">新上</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em>23000</em> 元/月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SH2140450309213003776.html"><img alt="阳光花城 3室1厅 8500元" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=201812111636405e7" data-src="https://image1.ljcdn.com/310000-inspection/89a123f8-9417-4e2b-ba06-1ac52950c3b7.jpg.250x182.jpg" class="lazyload"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SH2140450309213003776.html">
                    阳光花城 3室1厅 8500元                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/pudong">浦东</a>-<a href="/zufang/zhangjiang" target="_blank">张江</a>
                  <i>/</i>
                  113㎡
                  <i>/</i>南                  <i>/</i>
                    3室1厅1卫                  <span class="hide">
                    <i>/</i>
                    中楼层                                            （18层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">6天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_new">新上</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em>8500</em> 元/月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SH2140528289469972480.html"><img alt="二线江景，小区人车分流，精装修，交通便利！！！" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=201812111636405e7" data-src="https://image1.ljcdn.com/310000-inspection/prod-037be717-d62b-4264-a7c2-c701060cd3cd.jpg.250x182.jpg" class="lazyload"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SH2140528289469972480.html">
                    二线江景，小区人车分流，精装修，交通便利！！！                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/pudong">浦东</a>-<a href="/zufang/yuanshen" target="_blank">源深</a>
                  <i>/</i>
                  155㎡
                  <i>/</i>南 北                  <i>/</i>
                    3室2厅2卫                  <span class="hide">
                    <i>/</i>
                    中楼层                                            （29层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">5天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_new">新上</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em>14499</em> 元/月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SH2140570546847621120.html"><img alt="洪山花苑 5室2厅 12000元" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=201812111636405e7" data-src="https://image1.ljcdn.com/shfdfs-image/20170904/ff3969d4-2068-4a15-8653-a867e7a34bda.jpg.250x182.jpg" class="lazyload"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SH2140570546847621120.html">
                    洪山花苑 5室2厅 12000元                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/pudong">浦东</a>-<a href="/zufang/shibo" target="_blank">世博</a>
                  <i>/</i>
                  131㎡
                  <i>/</i>南                  <i>/</i>
                    5室2厅2卫                  <span class="hide">
                    <i>/</i>
                    高楼层                                            （6层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">5天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_new">新上</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em>12000</em> 元/月</span>
              </div>
          </div>
                    </div>
      <div class="content__pg" data-el="page_navigation" data-url="/zufang/pudong/pg{page}/" data-totalPage=100 data-curPage=1>
      </div>
          </div>
        <div class="content__aside">
      <div class="download">
  <div class="title">下载链家APP</div>
  <div class="qr-code"><img width="94" height="94" src="https://ajax.api.lianjia.com/qr/getDownloadQr?location=right&amp;ljweb_channel_key=zufang_search" alt="下载贝壳APP">
    <div class="text">
      <p>扫描上方二维码</p>
      <p>随时查看新房源</p>
      <p class="get-more">
        <a href="//www.lianjia.com/client/">了解更多
          <img width="9" height="9" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEUAAACcn6Gfn5+an5+bnqCbnqGfn5+cn6EV6DbuAAAAB3RSTlMA0BAw8LAgvf5k9AAAAEdJREFUKM9jIBOkBqMJhBcqoAmUC6EKmJSjKWEWR1eiiK6ECZsSA3QlzuhKSihRghDA0EJ/BWIoCgzh4YMIZALRYBrMQAkAAF5bGMBkrwzqAAAAAElFTkSuQmCC">
        </a>
      </p>
    </div>
  </div>
</div>    </div> 
      </div>

  
  
</div>

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
<div class="hide">
  <a href="/zufang/pudong/"></a>
  <a href="/zufang/pudong/pg2/"></a>
  <a href="/zufang/pudong/pg3/"></a>
  <a href="/zufang/pudong/pg4/"></a>
  <a href="/zufang/pudong/pg5/"></a>
  <a href="/zufang/pudong/pg6/"></a>
  <a href="/zufang/pudong/pg7/"></a>
  <a href="/zufang/pudong/pg8/"></a>
  <a href="/zufang/pudong/pg9/"></a>
  <a href="/zufang/pudong/pg10/"></a>
</div>

<script>
  g_conf.pageId = 'rentalList';
  var __requireList = ['page/list/index'];
  document.getElementById('clearUrl').href = '/zufang/pudong/brp{min}erp{max}/'.split('zufang/')[0] + 'zufang/';
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
                <i></i><img src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/img/wxapp.jpg?_v=201812111636405e7" alt="下载掌上链家" width="94">
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
                  <li><a class="" data-index="4">友情链接</a></li>
              </ul>
              <ul data-el="childrenList"  style="display:block">
                      <li><a href="https://sy.lianjia.com/zufang/">沈阳租房</a></li>
                      <li><a href="https://cd.lianjia.com/zufang/">成都租房</a></li>
                      <li><a href="https://sx.lianjia.com/zufang/">绍兴租房</a></li>
                      <li><a href="https://cq.lianjia.com/zufang/">重庆租房</a></li>
                      <li><a href="https://nj.lianjia.com/zufang/">南京租房</a></li>
                      <li><a href="https://zh.lianjia.com/zufang/">珠海租房</a></li>
                      <li><a href="https://taizhou.lianjia.com/zufang/">台州租房</a></li>
                      <li><a href="https://nb.lianjia.com/zufang/">宁波租房</a></li>
                      <li><a href="https://hk.lianjia.com/zufang/">海口租房</a></li>
                      <li><a href="https://jx.lianjia.com/zufang/">嘉兴租房</a></li>
                      <li><a href="https://ty.lianjia.com/zufang/">太原租房</a></li>
                      <li><a href="https://xan.lianjia.com/zufang/">雄安新区租房</a></li>
                      <li><a href="https://zz.lianjia.com/zufang/">郑州租房</a></li>
                      <li><a href="https://cc.lianjia.com/zufang/">长春租房</a></li>
                      <li><a href="https://qd.lianjia.com/zufang/">青岛租房</a></li>
                      <li><a href="https://sjz.lianjia.com/zufang/">石家庄租房</a></li>
                      <li><a href="https://liangshan.lianjia.com/zufang/">凉山租房</a></li>
                      <li><a href="https://kf.lianjia.com/zufang/">开封租房</a></li>
                      <li><a href="https://km.lianjia.com/zufang/">昆明租房</a></li>
                      <li><a href="https://xm.lianjia.com/zufang/">厦门租房</a></li>
                      <li><a href="https://hui.lianjia.com/zufang/">惠州租房</a></li>
                      <li><a href="https://jn.lianjia.com/zufang/">济南租房</a></li>
                      <li><a href="https://bj.lianjia.com/zufang/">北京租房</a></li>
                      <li><a href="https://wh.lianjia.com/zufang/">武汉租房</a></li>
                      <li><a href="https://ganzhou.lianjia.com/zufang/">赣州租房</a></li>
                      <li><a href="https://cs.lianjia.com/zufang/">长沙租房</a></li>
                      <li><a href="https://wx.lianjia.com/zufang/">无锡租房</a></li>
                      <li><a href="https://fs.lianjia.com/zufang/">佛山租房</a></li>
                      <li><a href="https://gz.lianjia.com/zufang/">广州租房</a></li>
                      <li><a href="https://changzhou.lianjia.com/zufang/">常州租房</a></li>
                  </ul>
               <ul data-el="childrenList"  >
                      <li><a href="https://sh.lianjia.com/zufang/xintiandi/">新天地租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/xuanqiao/">宣桥租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/caojiadu/">曹家渡租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/malu/">马陆租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/chongmingxincheng/">崇明新城租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/chongmingqita/">崇明其它租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/nanjingxilu/">南京西路租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/mangu/">曼谷租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/riben/">日本租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/maqiao/">马桥租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/gaojing/">高境租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/tangzhen/">唐镇租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/chenjiazhen/">陈家镇租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/xuxing/">徐行租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/gaohang/">高行租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/kunshan1/">昆山租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/jinganxincheng/">静安新城租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/jiuting/">九亭租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/lianyang/">联洋租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/hongqiao1/">虹桥租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/yangdong/">杨东租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/renminguangchang/">人民广场租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/zhuanghang/">庄行租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/jinhui/">金汇租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/xianghuaqiao/">香花桥租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/xietulu/">斜土路租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/haiwan/">海湾租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/jiadingxincheng/">嘉定新城租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/xinjiangwancheng/">新江湾城租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/zhenguang/">真光租房</a></li>
                  </ul>
               <ul data-el="childrenList"  >
                      <li><a href="https://sh.lianjia.com/zufang/c5011000017738/">仓库静安区</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000017869/">天吉小区</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000016294/">中房华东大厦</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000018276/">福海公寓</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000015351/">凯旋公寓</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000014545/">马桥公寓</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000016434/">大木桥路456号</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000018549/">桂景苑</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000017646/">云台大厦</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000017628/">元和投资大厦</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000016231/">华升公寓</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000016666/">鼎邦丽池(公寓)</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000017636/">亭园大厦</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000017630/">宝莲城</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000016667/">建德坊</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000014173/">蓝村小区</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000015023/">银城大厦</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000016607/">欣怡小区</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000014700/">俞二小区</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000017366/">赵家宅小区</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000016177/">贵人大厦</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000018263/">联洋花园(一期)</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000014187/">上虹新村</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011102207375/">长青企业广场</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000020399/">平顺路721弄</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000014515/">华庭雅居</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000016575/">中二小区</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000017863/">涵养村</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000013726/">浦坊大楼</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000018703/">淮海西路346弄</a></li>
                  </ul>
               <ul data-el="childrenList"  >
                      <li><a href="https://xm.fang.lianjia.com/">厦门楼盘</a></li>
                      <li><a href="https://san.fang.lianjia.com/">三亚楼盘</a></li>
                      <li><a href="https://wuhu.fang.lianjia.com/">芜湖楼盘</a></li>
                      <li><a href="https://ganzhou.fang.lianjia.com/">赣州楼盘</a></li>
                      <li><a href="https://zh.fang.lianjia.com/">珠海楼盘</a></li>
                      <li><a href="https://sz.fang.lianjia.com/">深圳楼盘</a></li>
                      <li><a href="https://cq.fang.lianjia.com/">重庆楼盘</a></li>
                      <li><a href="https://ty.fang.lianjia.com/">太原楼盘</a></li>
                      <li><a href="https://qd.fang.lianjia.com/">青岛楼盘</a></li>
                      <li><a href="https://lf.fang.lianjia.com/">廊坊楼盘</a></li>
                      <li><a href="https://liangshan.fang.lianjia.com/">凉山楼盘</a></li>
                      <li><a href="https://taizhou.fang.lianjia.com/">台州楼盘</a></li>
                      <li><a href="https://zz.fang.lianjia.com/">郑州楼盘</a></li>
                      <li><a href="https://cd.fang.lianjia.com/">成都楼盘</a></li>
                      <li><a href="https://zs.fang.lianjia.com/">中山楼盘</a></li>
                      <li><a href="https://zj.fang.lianjia.com/">镇江楼盘</a></li>
                      <li><a href="https://jian.fang.lianjia.com/">吉安楼盘</a></li>
                      <li><a href="https://cc.fang.lianjia.com/">长春楼盘</a></li>
                      <li><a href="https://bj.fang.lianjia.com/">北京楼盘</a></li>
                      <li><a href="https://sjz.fang.lianjia.com/">石家庄楼盘</a></li>
                      <li><a href="https://wx.fang.lianjia.com/">无锡楼盘</a></li>
                      <li><a href="https://xan.fang.lianjia.com/">雄安新区楼盘</a></li>
                      <li><a href="https://cs.fang.lianjia.com/">长沙楼盘</a></li>
                      <li><a href="https://yt.fang.lianjia.com/">烟台楼盘</a></li>
                      <li><a href="https://dg.fang.lianjia.com/">东莞楼盘</a></li>
                      <li><a href="https://gy.fang.lianjia.com/">贵阳楼盘</a></li>
                      <li><a href="https://hui.fang.lianjia.com/">惠州楼盘</a></li>
                      <li><a href="https://kf.fang.lianjia.com/">开封楼盘</a></li>
                      <li><a href="https://sy.fang.lianjia.com/">沈阳楼盘</a></li>
                      <li><a href="https://sh.fang.lianjia.com/">上海楼盘</a></li>
                  </ul>
               <ul data-el="childrenList"  >
                  </ul>
           </div>

    <div class="footer__bottom">
      <p>链家网（北京）科技有限公司 | 网络经营许可证 京ICP备16057509号-2 | &copy; Copyright&copy;2010-2018 链家网Lianjia.com版权所有</p>
      <a target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010802024019" style="display:inline-block;text-decoration:none;height:20px;line-height:20px;"><img style="margin-right: 5px;" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/img/beian.png?_v=201812111636405e7">京公网安备 11010802024019号</a>
    </div>

  </div>
</div>

<script type="text/javascript">
  var footerList = JSON.parse(JSON.stringify([{"abbr":"zfcs","expire":"2018-12-15 23:00:01","city_id":"310000","children":[{"url":"https:\/\/sy.lianjia.com\/zufang\/","title":"\u6c88\u9633\u79df\u623f"},{"url":"https:\/\/cd.lianjia.com\/zufang\/","title":"\u6210\u90fd\u79df\u623f"},{"url":"https:\/\/sx.lianjia.com\/zufang\/","title":"\u7ecd\u5174\u79df\u623f"},{"url":"https:\/\/cq.lianjia.com\/zufang\/","title":"\u91cd\u5e86\u79df\u623f"},{"url":"https:\/\/nj.lianjia.com\/zufang\/","title":"\u5357\u4eac\u79df\u623f"},{"url":"https:\/\/zh.lianjia.com\/zufang\/","title":"\u73e0\u6d77\u79df\u623f"},{"url":"https:\/\/taizhou.lianjia.com\/zufang\/","title":"\u53f0\u5dde\u79df\u623f"},{"url":"https:\/\/nb.lianjia.com\/zufang\/","title":"\u5b81\u6ce2\u79df\u623f"},{"url":"https:\/\/hk.lianjia.com\/zufang\/","title":"\u6d77\u53e3\u79df\u623f"},{"url":"https:\/\/jx.lianjia.com\/zufang\/","title":"\u5609\u5174\u79df\u623f"},{"url":"https:\/\/ty.lianjia.com\/zufang\/","title":"\u592a\u539f\u79df\u623f"},{"url":"https:\/\/xan.lianjia.com\/zufang\/","title":"\u96c4\u5b89\u65b0\u533a\u79df\u623f"},{"url":"https:\/\/zz.lianjia.com\/zufang\/","title":"\u90d1\u5dde\u79df\u623f"},{"url":"https:\/\/cc.lianjia.com\/zufang\/","title":"\u957f\u6625\u79df\u623f"},{"url":"https:\/\/qd.lianjia.com\/zufang\/","title":"\u9752\u5c9b\u79df\u623f"},{"url":"https:\/\/sjz.lianjia.com\/zufang\/","title":"\u77f3\u5bb6\u5e84\u79df\u623f"},{"url":"https:\/\/liangshan.lianjia.com\/zufang\/","title":"\u51c9\u5c71\u79df\u623f"},{"url":"https:\/\/kf.lianjia.com\/zufang\/","title":"\u5f00\u5c01\u79df\u623f"},{"url":"https:\/\/km.lianjia.com\/zufang\/","title":"\u6606\u660e\u79df\u623f"},{"url":"https:\/\/xm.lianjia.com\/zufang\/","title":"\u53a6\u95e8\u79df\u623f"},{"url":"https:\/\/hui.lianjia.com\/zufang\/","title":"\u60e0\u5dde\u79df\u623f"},{"url":"https:\/\/jn.lianjia.com\/zufang\/","title":"\u6d4e\u5357\u79df\u623f"},{"url":"https:\/\/bj.lianjia.com\/zufang\/","title":"\u5317\u4eac\u79df\u623f"},{"url":"https:\/\/wh.lianjia.com\/zufang\/","title":"\u6b66\u6c49\u79df\u623f"},{"url":"https:\/\/ganzhou.lianjia.com\/zufang\/","title":"\u8d63\u5dde\u79df\u623f"},{"url":"https:\/\/cs.lianjia.com\/zufang\/","title":"\u957f\u6c99\u79df\u623f"},{"url":"https:\/\/wx.lianjia.com\/zufang\/","title":"\u65e0\u9521\u79df\u623f"},{"url":"https:\/\/fs.lianjia.com\/zufang\/","title":"\u4f5b\u5c71\u79df\u623f"},{"url":"https:\/\/gz.lianjia.com\/zufang\/","title":"\u5e7f\u5dde\u79df\u623f"},{"url":"https:\/\/changzhou.lianjia.com\/zufang\/","title":"\u5e38\u5dde\u79df\u623f"}],"title":"\u79df\u623f\u57ce\u5e02","class":""},{"abbr":"rmsq","expire":"2018-12-15 23:00:01","city_id":"310000","children":[{"url":"https:\/\/sh.lianjia.com\/zufang\/xintiandi\/","title":"\u65b0\u5929\u5730\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/xuanqiao\/","title":"\u5ba3\u6865\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/caojiadu\/","title":"\u66f9\u5bb6\u6e21\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/malu\/","title":"\u9a6c\u9646\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/chongmingxincheng\/","title":"\u5d07\u660e\u65b0\u57ce\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/chongmingqita\/","title":"\u5d07\u660e\u5176\u5b83\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/nanjingxilu\/","title":"\u5357\u4eac\u897f\u8def\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/mangu\/","title":"\u66fc\u8c37\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/riben\/","title":"\u65e5\u672c\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/maqiao\/","title":"\u9a6c\u6865\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/gaojing\/","title":"\u9ad8\u5883\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/tangzhen\/","title":"\u5510\u9547\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/chenjiazhen\/","title":"\u9648\u5bb6\u9547\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/xuxing\/","title":"\u5f90\u884c\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/gaohang\/","title":"\u9ad8\u884c\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/kunshan1\/","title":"\u6606\u5c71\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/jinganxincheng\/","title":"\u9759\u5b89\u65b0\u57ce\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/jiuting\/","title":"\u4e5d\u4ead\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/lianyang\/","title":"\u8054\u6d0b\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/hongqiao1\/","title":"\u8679\u6865\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/yangdong\/","title":"\u6768\u4e1c\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/renminguangchang\/","title":"\u4eba\u6c11\u5e7f\u573a\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/zhuanghang\/","title":"\u5e84\u884c\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/jinhui\/","title":"\u91d1\u6c47\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/xianghuaqiao\/","title":"\u9999\u82b1\u6865\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/xietulu\/","title":"\u659c\u571f\u8def\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/haiwan\/","title":"\u6d77\u6e7e\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/jiadingxincheng\/","title":"\u5609\u5b9a\u65b0\u57ce\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/xinjiangwancheng\/","title":"\u65b0\u6c5f\u6e7e\u57ce\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/zhenguang\/","title":"\u771f\u5149\u79df\u623f"}],"title":"\u70ed\u95e8\u5546\u5708","class":""},{"abbr":"tjxq","expire":"2018-12-15 23:00:01","city_id":"310000","children":[{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000017738\/","title":"\u4ed3\u5e93\u9759\u5b89\u533a"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000017869\/","title":"\u5929\u5409\u5c0f\u533a"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000016294\/","title":"\u4e2d\u623f\u534e\u4e1c\u5927\u53a6"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000018276\/","title":"\u798f\u6d77\u516c\u5bd3"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000015351\/","title":"\u51ef\u65cb\u516c\u5bd3"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000014545\/","title":"\u9a6c\u6865\u516c\u5bd3"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000016434\/","title":"\u5927\u6728\u6865\u8def456\u53f7"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000018549\/","title":"\u6842\u666f\u82d1"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000017646\/","title":"\u4e91\u53f0\u5927\u53a6"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000017628\/","title":"\u5143\u548c\u6295\u8d44\u5927\u53a6"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000016231\/","title":"\u534e\u5347\u516c\u5bd3"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000016666\/","title":"\u9f0e\u90a6\u4e3d\u6c60(\u516c\u5bd3)"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000017636\/","title":"\u4ead\u56ed\u5927\u53a6"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000017630\/","title":"\u5b9d\u83b2\u57ce"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000016667\/","title":"\u5efa\u5fb7\u574a"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000014173\/","title":"\u84dd\u6751\u5c0f\u533a"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000015023\/","title":"\u94f6\u57ce\u5927\u53a6"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000016607\/","title":"\u6b23\u6021\u5c0f\u533a"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000014700\/","title":"\u4fde\u4e8c\u5c0f\u533a"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000017366\/","title":"\u8d75\u5bb6\u5b85\u5c0f\u533a"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000016177\/","title":"\u8d35\u4eba\u5927\u53a6"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000018263\/","title":"\u8054\u6d0b\u82b1\u56ed(\u4e00\u671f)"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000014187\/","title":"\u4e0a\u8679\u65b0\u6751"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011102207375\/","title":"\u957f\u9752\u4f01\u4e1a\u5e7f\u573a"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000020399\/","title":"\u5e73\u987a\u8def721\u5f04"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000014515\/","title":"\u534e\u5ead\u96c5\u5c45"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000016575\/","title":"\u4e2d\u4e8c\u5c0f\u533a"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000017863\/","title":"\u6db5\u517b\u6751"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000013726\/","title":"\u6d66\u574a\u5927\u697c"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000018703\/","title":"\u6dee\u6d77\u897f\u8def346\u5f04"}],"title":"\u63a8\u8350\u5c0f\u533a","class":""},{"abbr":"csxf","expire":"2018-12-15 23:00:01","city_id":"310000","children":[{"url":"https:\/\/xm.fang.lianjia.com\/","title":"\u53a6\u95e8\u697c\u76d8"},{"url":"https:\/\/san.fang.lianjia.com\/","title":"\u4e09\u4e9a\u697c\u76d8"},{"url":"https:\/\/wuhu.fang.lianjia.com\/","title":"\u829c\u6e56\u697c\u76d8"},{"url":"https:\/\/ganzhou.fang.lianjia.com\/","title":"\u8d63\u5dde\u697c\u76d8"},{"url":"https:\/\/zh.fang.lianjia.com\/","title":"\u73e0\u6d77\u697c\u76d8"},{"url":"https:\/\/sz.fang.lianjia.com\/","title":"\u6df1\u5733\u697c\u76d8"},{"url":"https:\/\/cq.fang.lianjia.com\/","title":"\u91cd\u5e86\u697c\u76d8"},{"url":"https:\/\/ty.fang.lianjia.com\/","title":"\u592a\u539f\u697c\u76d8"},{"url":"https:\/\/qd.fang.lianjia.com\/","title":"\u9752\u5c9b\u697c\u76d8"},{"url":"https:\/\/lf.fang.lianjia.com\/","title":"\u5eca\u574a\u697c\u76d8"},{"url":"https:\/\/liangshan.fang.lianjia.com\/","title":"\u51c9\u5c71\u697c\u76d8"},{"url":"https:\/\/taizhou.fang.lianjia.com\/","title":"\u53f0\u5dde\u697c\u76d8"},{"url":"https:\/\/zz.fang.lianjia.com\/","title":"\u90d1\u5dde\u697c\u76d8"},{"url":"https:\/\/cd.fang.lianjia.com\/","title":"\u6210\u90fd\u697c\u76d8"},{"url":"https:\/\/zs.fang.lianjia.com\/","title":"\u4e2d\u5c71\u697c\u76d8"},{"url":"https:\/\/zj.fang.lianjia.com\/","title":"\u9547\u6c5f\u697c\u76d8"},{"url":"https:\/\/jian.fang.lianjia.com\/","title":"\u5409\u5b89\u697c\u76d8"},{"url":"https:\/\/cc.fang.lianjia.com\/","title":"\u957f\u6625\u697c\u76d8"},{"url":"https:\/\/bj.fang.lianjia.com\/","title":"\u5317\u4eac\u697c\u76d8"},{"url":"https:\/\/sjz.fang.lianjia.com\/","title":"\u77f3\u5bb6\u5e84\u697c\u76d8"},{"url":"https:\/\/wx.fang.lianjia.com\/","title":"\u65e0\u9521\u697c\u76d8"},{"url":"https:\/\/xan.fang.lianjia.com\/","title":"\u96c4\u5b89\u65b0\u533a\u697c\u76d8"},{"url":"https:\/\/cs.fang.lianjia.com\/","title":"\u957f\u6c99\u697c\u76d8"},{"url":"https:\/\/yt.fang.lianjia.com\/","title":"\u70df\u53f0\u697c\u76d8"},{"url":"https:\/\/dg.fang.lianjia.com\/","title":"\u4e1c\u839e\u697c\u76d8"},{"url":"https:\/\/gy.fang.lianjia.com\/","title":"\u8d35\u9633\u697c\u76d8"},{"url":"https:\/\/hui.fang.lianjia.com\/","title":"\u60e0\u5dde\u697c\u76d8"},{"url":"https:\/\/kf.fang.lianjia.com\/","title":"\u5f00\u5c01\u697c\u76d8"},{"url":"https:\/\/sy.fang.lianjia.com\/","title":"\u6c88\u9633\u697c\u76d8"},{"url":"https:\/\/sh.fang.lianjia.com\/","title":"\u4e0a\u6d77\u697c\u76d8"}],"title":"\u57ce\u5e02\u65b0\u623f","class":""},{"abbr":"yqlj","title":"\u53cb\u60c5\u94fe\u63a5","city_id":"310000","expire":"2018-12-11","children":[]}]))

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

<script type="text/javascript" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/common/js/common.js?_v=201812111636405e7"></script>

<script type="text/javascript">
  //引入脚本后
  var imConf = {
          "ajaxroot": "\/\/ajax.api.ke.com\/",
          "imAppid": "ZULIN_WEB_20181122",
          "imAppkey": "0a4e8669fc2a50cbbeeb969726a7ab46"
      };
</script>
<script>
var __basePath = 'https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src?_v=201812111636405e7'.split("?");
require.config({
  baseUrl: __basePath[0],
  paths: {
  },
  urlArgs:  __basePath[1]
});
var config = {"fe_root":"https:\/\/s1.ljcdn.com\/matrix_lianjia_pc\/dist\/pc","version":"201812111636405e7","js_ns":"m_pages_zufangSearch","cur_city_id":"310000","cur_city_name":"\u4e0a\u6d77","cur_city_short":"sh"};
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



print "/zufang/SH2136750194585780224.html"[8:-5]


