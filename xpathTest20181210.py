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


<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><meta http-equiv="X-UA-Compatible" content="IE=edge" /><meta http-equiv="Cache-Control" content="no-transform" /><meta http-equiv="Cache-Control" content="no-siteapp" /><meta http-equiv="Content-language" content="zh-CN" /><meta name="format-detection" content="telephone=no" /><meta name="applicable-device" content="pc"><link rel="alternate" media="only screen and (max-width: 640px)" href="https://m.lianjia.com/sh/zufang/pudong/" >
<meta name="mobile-agent" content="format=html5;url=https://m.lianjia.com/sh/zufang/pudong/"><script>
ljConf = {
    city_id: '310000',
    city_abbr: 'sh',
    city_name: '上海',
    channel: 'zufang',
    page: 'zufang_search',
    pageConfig: {"ajaxroot":"\/\/ajax.api.lianjia.com\/","imAppid":"LIANJIA_WEB_20160624","imAppkey":"6dfdcee27d78b1107fceeca55d80b7bd"},
    feroot: '//s1.ljcdn.com/feroot/',
    ucid:'',
    cdn:'0',
};
</script>

<!-- 2017.11.8 市场需求加上新的统计 -->
<!-- 2017.7.18 开放全国 -->
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?9152f8221cb6243a53c83b956842be8a";
  var s = document.getElementsByTagName("script")[0];
  s.parentNode.insertBefore(hm, s);
})();
</script>
<script src="https://s1.ljcdn.com/feroot/pc/asset/common/tingyun-rum.js?_v=20181206222953"></script><title>浦东租房_上海浦东房屋出租(上海链家网)</title>
<meta name="description" content="链家浦东租房网,现有真实房屋租赁6909套.为需要房屋租出租赁的用户提供区域租房和地铁租房,方便您更快捷的了解找到合适的居住房屋.在浦东租房就到上海链家网. " />
<meta name="keywords" content="浦东租房网,浦东租房,浦东个人房源出租,浦东房屋出租,浦东房屋租赁 " />
<link href="/favicon.ico" type="image/x-icon" rel=icon><link href="/favicon.ico" type="image/x-icon" rel="shortcut icon"><link rel="stylesheet" href="https://s1.ljcdn.com/feroot/pc/asset/common.css?_v=20181206222953">
<link rel="stylesheet" href="https://s1.ljcdn.com/feroot/pc/asset/list.css?_v=20181206222953">
<!--[if lt IE 9]><script type="text/javascript" src="https://s1.ljcdn.com/feroot/dep/common-require/html5.js?_v=20181206222953"></script><![endif]-->
<script>
function RESIZEIMG(b,k,l,m){var c=b.parentNode;var d=parseInt(c.offsetWidth)||k;var e=parseInt(c.offsetHeight)||l;var f=d/e;var g=b.naturalWidth||b.width;var h=b.naturalHeight||b.height;var i=g/h;var j="width";if(f<i){j="height";try{b.style["left"]="-"+parseInt(Math.abs((d-(g*e/h))/2))+"px"}catch(e){}}else if(m){try{b.style["top"]="-"+parseInt(Math.abs((e-(h*d/g))/2))+"px"}catch(e){}};b.style[j]="100%";};
</script>
<script>
var _czc = _czc || [];
_czc.push(["_setAccount", "1254525948"]);
</script>

<script type="text/javascript">
var _smq = _smq || [];
_smq.push(['_setAccount', '41331c2', new Date()]);
_smq.push(['_setDomainName', 'lianjia.com']);
_smq.push(['pageview']);
(function() {
var sm = document.createElement('script'); sm.type = 'text/javascript'; sm.async = true;
sm.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'cdnmaster.com/sitemaster/collect.js';
var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(sm, s);
})();
</script>
</head><body><script>
__STAT_LJ_CONF = {
    params: {
        ljweb_group: ['SEARCH','BIGDATA_PC'],
        ljweb_id: '',
        ljweb_mod: '',
        ljweb_bl: '',
        ljweb_el: '',
        ljweb_sl: '',
        ljweb_index: '',
        ljweb_value: '',
        ljweb_url: '',
        ljweb_ljref: (document.cookie.match(/(?:^| )ljref=([^;]*)(?:;|$)/) || ['',''])[1],
        ljweb_sample: (document.cookie.match(/(?:^| )sample_traffic_test=([^;]*)(?:;|$)/) || ['',''])[1],
        ljweb_ref: document.referrer,
        ljweb_cid: '310000',
        ljweb_channel: 'zufang',
        ljweb_page: 'zufang_search',
        ljweb_source: '',
        ljweb_stat_id: ''
    }
};



var UT = {
    send: function() {

    }
};
var LjUserTrack = {
    log: [],
    initInterval: false,
    intervalLog: function() {
        setTimeout(function() {
            if(window.$ULOG && $ULOG.send) {
                for(var i = 0, l = LjUserTrack.log.length; i < l; i++) {
                    LjUserTrack.__send(LjUserTrack.log[i]);
                }

                for(var m = 0, n = LjUserTrack.logIds.length; m < n; m++) {
                    LjUserTrack.__sendId(LjUserTrack.logIds[m]);
                }
                for(var j = 0, k = LjUserTrack.logDatas.length; j < k; j++) {
                    LjUserTrack.__sendData(LjUserTrack.logDatas[j].id, LjUserTrack.logDatas[j].data);
                }
            } else {
                LjUserTrack.intervalLog();
            }
        }, 16.7);
    },
    _start_time: +new Date,
    logDatas: [],
    __sendData: function(id, data) {
        if(id && (typeof(data) == 'object')){
          data.pid = (window.__UDL_CONFIG && window.__UDL_CONFIG.pid && window.__UDL_CONFIG.pid)||"lianjiaweb";
          data.key = window.location.href;
          window.$ULOG && $ULOG.send(id, data);
        }
    },
    sendData: function(id, data) {
        if(window.$ULOG && $ULOG.send) {
            LjUserTrack.__sendData(id, data);
        } else {
            LjUserTrack.logDatas.push({id: id, data: data});

            LjUserTrack.initInterval || (LjUserTrack.initInterval = true, LjUserTrack.intervalLog());

        }
    },
    __send: function(data) {
        var evt_id = data.evt_id || '10043';
        if('evt_id' in data) {
            delete data.evt_id;
        }

        window.$ULOG && $ULOG.send(evt_id, {
            "pid": (window.__UDL_CONFIG && window.__UDL_CONFIG.pid && window.__UDL_CONFIG.pid)||"lianjiaweb",
            "key": window.location.href,
            "action": data
        });
    },
    logIds: [],
    __sendId: function(id) {
        id && window.$ULOG && window.$ULOG && $ULOG.send(id, {
            "pid": (window.__UDL_CONFIG && window.__UDL_CONFIG.pid && window.__UDL_CONFIG.pid)||"lianjiaweb",
            "key": window.location.href
        });
    },
    sendId: function(id) {
        if(window.$ULOG && $ULOG.send) {
            LjUserTrack.__sendId(id);
        } else {
            LjUserTrack.logIds.push(id);

            LjUserTrack.initInterval || (LjUserTrack.initInterval = true, LjUserTrack.intervalLog());

        }
    },
    send: function(data, el, config) {

        var utConf = __STAT_LJ_CONF;
        var params = config || utConf.params,
            win = window,
            j;

        data.groupIndex = data.ljweb_group || 0;

        if (params) {
            for (var d in params) {
                if(params[d] !== j && data[d] === j) {
                    data[d] = params[d];
                }
            }
        }

        if(el) {
            this.checkClick(el, data);
        }

        data.ljweb_group = params['ljweb_group'][data.groupIndex || 0];

        delete data.groupIndex;

        if(data.typ) {
            data.ljweb_bl = (data.ljweb_bl || '') + '_' + data.typ;
            delete data.typ;
        }

        if(window.$ULOG && $ULOG.send) {
            LjUserTrack.__send(data);
        } else {
            LjUserTrack.log.push(data);

            LjUserTrack.initInterval || (LjUserTrack.initInterval = true, LjUserTrack.intervalLog());

        }

    },
    checkClick: function(el, data) {

        var TAG_LINK = 'A';
        var href = '';
        var elParent = null;

        href = (el.tagName.toUpperCase() === TAG_LINK ? el.getAttribute("href", 2) : '');
        if(!href && (elParent = el.parentNode) && elParent.nodeType === 1) {
            href = (elParent.tagName.toUpperCase() === TAG_LINK ? elParent.getAttribute("href", 2) : '');
        }

        if(href) {
            data.ljweb_url = href;
        } else {
            data.ljweb_url = data.ljweb_url
                  || el.getAttribute("data-log_url")
                  || (elParent=el.parentNode||el).getAttribute("data-log_url")
                  || (
                        (elParent=elParent.parentNode||elParent)
                     && (elParent.nodeType === 1)
                     && elParent.getAttribute("data-log_url")
                     )
                  || "";
        }

        this.attr(el, data);

    },
    path: function() {

    },
    attr: function(el, data) {
        var modId     = el.getAttribute("log-mod");
        var blAttr    = el.getAttribute("data-bl");
        var elAttr    = el.getAttribute("data-el");
        var slAttr    = el.getAttribute("data-sl");
        var InAttr    = el.getAttribute("data-log_index");
        var valAttr   = el.getAttribute("data-log_value");
        var idAttr    = el.getAttribute("data-log_id");
        var groupAttr = el.getAttribute("data-log_group");
        var sourceAttr = el.getAttribute("data-log_source");
        var statIdAttr = el.getAttribute("data-log_statId");
        var evtId     = el.getAttribute("data-log_evtid");

        data.ljweb_bl    = data.ljweb_bl || blAttr || '';
        data.ljweb_el    = data.ljweb_el || elAttr || '';
        data.ljweb_sl    = data.ljweb_sl || slAttr || '';
        data.ljweb_index = data.ljweb_index || InAttr || '';
        data.ljweb_value = data.ljweb_value || valAttr || '';
        data.ljweb_id    = data.ljweb_id || idAttr || '';
        data.ljweb_source    = data.ljweb_source || sourceAttr || '';
        data.ljweb_stat_id    = data.ljweb_stat_id || statIdAttr || 0;
        data.groupIndex  = data.groupIndex || groupAttr || 0;
        data.evt_id      = data.evt_id || evtId || '';

        if (!modId) {
            if (el.parentNode && el.parentNode.nodeType === 1 && el.parentNode.tagName.toUpperCase() !== 'BODY') {
                this.attr(el.parentNode, data);
            }
        } else {
            data.ljweb_mod = modId;
        }
    }
};

;;(function() {
    var isW3c = !!document.addEventListener;

    LjUserTrack.send({
        ljweb_mod: 'pv',
        ljweb_group: 1
    });

    /*window[isW3c ? 'addEventListener' : 'attachEvent'](
        (isW3c ? '': 'on') + 'beforeunload',
        function(e) {
            var _end_time = +new Date;
            UT.send({type: 'show', subtype: 'stay', time: (_end_time-UT._start_time)/1000});
        },
        false);*/
})();





</script>


<header class="lianjia-header "><div class="nav-wrap"><div class="wrapper "><div class="fl"><a class="logo" href="//www.lianjia.com/"  title="链家房产网"><!-- <img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/logo.png?_v=20181206222953"> --></a></div><div class="fr nav  "><div class="fl"><ul>
		                          <li>
                <a  class="" href="https://sh.lianjia.com/ershoufang/" >二手房</a>
            </li>
          	    		                          <li>
                <a  class="" href="https://sh.fang.lianjia.com/" >新房</a>
            </li>
          	    		                          <li>
                <a  class="on" href="https://sh.lianjia.com/zufang/" >租房</a>
            </li>
          	    		                          <li>
                <a  class="" href="https://us.lianjia.com" >海外</a>
            </li>
          	    		                          <li>
                <a  class="" href="https://shang.lianjia.com/sh" >商业办公</a>
            </li>
          	    		                          <li>
                <a  class="" href="https://sh.lianjia.com/xiaoqu/" >小区</a>
            </li>
          	    		                          <li>
                <a  class="" href="https://sh.lianjia.com/jingjiren/" >经纪人</a>
            </li>
          	    		    	        <li class="hover">
	            <a  class="" href="https://sh.lianjia.com/wenda/" >
	            指南
	            </a>
	            <div class="nav-list">
	                <dd>
	                    <i></i>
	                                                                                <dl>
                                    <a href="https://sh.lianjia.com/wenda/" >问答</a>
                                </dl>
                                                                                                                <dl>
                                    <a href="https://news.lianjia.com/sh/baike/" >百科</a>
                                </dl>
                                                    	                </dd>
	            </div>
	        </li>
	    		                          <li>
                <a  class="" href="https://sh.lianjia.com/tool.html" target="_blank">工具</a>
            </li>
          	    		                          <li>
                <a  class="" href="https://sh.lianjia.com/yezhu/" target="_blank">发布房源</a>
            </li>
          	    	</ul></div><div class="fr login"><div class="ti-hover"><div class="login-panel typeUserInfo"><script type="text/template" class="template">
      <%if(data && data.username){%>
        <%if(data.isAgent){%>
         <a href="<%=$.env.fixedUrl('//agent.lianjia.com/')%>"><span><%=data.username%></span></a>
        <%}else{%>
          <a href="<%=$.env.fixedUrl('//user.lianjia.com/')%>" rel="nofollow"><span><%=data.username%></span></a>
         <%}%>
         <span id="indexTipContainer"></span>
         <%if(data.isAgent){%>
           <span class="welcome"><a class="reg" href="<%=data.logoutUrl%>" rel="nofollow">退出</a></span>
         <%}else{%>
           <span class="welcome"><a class="reg" href="<%=data.logoutUrl%>" rel="nofollow">退出</a></span>
          <%}%>
      <%}else{%>
        <span class="welcome"><a class="btn-register" href="<%=data.registerUrl%>" rel="nofollow"><span class="log">注册</span></a>|<a class="btn-login bounceIn actLoginBtn" href="<%=data.loginUrl%>"><span class="reg">登录</span></a></span>
      <%}%>
    </script><div class="typeShowUser"><span class="welcome"><a class="btn-register" href="https://passport.lianjia.com/register/resources/lianjia/register.html?service=https%3A%2F%2Fwww.lianjia.com%2Fuser%2Fchecklogin%3Fredirect%3Dhttps%253A%252F%252Fsh.lianjia.com%252Fzufang%252Fpudong%252F"  rel="nofollow" ><span class="log">注册</span></a>|<a href="https://upassport.lianjia.com/login?service=https%3A%2F%2Fwww.lianjia.com%2Fuser%2Fchecklogin%3Fredirect%3Dhttps%253A%252F%252Fsh.lianjia.com%252Fzufang%252Fpudong%252F" class="btn-login bounceIn actLoginBtn" rel="nofollow"><span class="reg">登录</span></a></span></div></div><div class="user-news" id="userNews"><script type="text/template" id="News">
        <ul>
          <li class="s-li"><span class="userNewsTriangle"></span></li>
        <%for(var i in group_by_type){%>
          <%if(group_by_type[i].unread !== 0 && pushMsgMap.hasOwnProperty(i)){%>
            <li>
              <a href="<%=pushMsgMap[i].url%>">
                <%=$.replaceTpl(pushMsgMap[i].text, {unread:group_by_type[i].unread})%>
              </a>
            </li>
          <%}%>
        <%}%>
        </ul>
      </script></div></div>
</div></div></div></div></header>
<!-- NAV头部搜索模块 -->
<div class="searchs"><div class="wrapper"><div class="fl" log-mod="search"><div class="search-txt"><form class="clear" id="searchForm" action="/zufang/rs" data-action="/zufang/rs" method="post"><div class="search-tab"><i class="icon" data-bl="switch"></i><div data-bl="switch" class="check"  formact="/zufang/rs" actdata="zufang">租房</div><ul class="tabs" data-bl="switch"><li><label actData="channel=zufang" formact="/zufang/rs" tra="" tips="请输入区域、板块或小区名开始找房">租房</label></li><li><label formact="/ershoufang/rs" actData="channel=ershoufang" tra="_blank" tips="请输入区域、板块或小区名开始找房">二手房</label></li><li><label formact="/xiaoqu/rs" actData="channel=xiaoqu" tra="_blank" tips="请输入小区名开始查找小区">小区</label></li><li><label formact="/chengjiao/rs" actData="channel=chengjiao" tra="_blank" tips="">成交</label></li><li><label formact="/loupan/rs" actData="channel=xinfang" tra="_blank" tips="请输入楼盘名称开始找房">新房</label></li><li><label formact="/jingjiren/rs" actData="channel=jingjiren" tra="_blank" tips="请输入商圈、小区或经纪人的姓名、电话...">经纪人</label></li></ul><div  class="txt-serach"><input class="left txt" name="keyword" autocomplete="off" placeholder="请输入区域、板块或小区名开始找房" id="keyword-box"><div class="hot-sug" data-bl="sug" data-el="history"><ul id="zufang"><li class="hot-name">热门搜索</li><div class="list"><li><a href="http://sh.lianjia.com/zufang/rs%E9%9D%99%E5%AE%89%E6%96%B0%E5%9F%8E/" data-log_channel="zufang" data-log_index="1" data-log_value="静安新城">静安新城</a></li><li><a href="http://sh.lianjia.com/zufang/rs%E5%A4%A7%E5%8D%8E%E9%94%A6%E7%BB%A3%E5%8D%8E%E5%9F%8E/" data-log_channel="zufang" data-log_index="2" data-log_value="大华锦绣华城">大华锦绣华城</a></li><li><a href="http://sh.lianjia.com/zufang/rs%E4%B8%AD%E8%BF%9C%E4%B8%A4%E6%B9%BE%E5%9F%8E/" data-log_channel="zufang" data-log_index="3" data-log_value="中远两湾城">中远两湾城</a></li><li><a href="http://sh.lianjia.com/zufang/rs%E7%91%9E%E8%99%B9%E6%96%B0%E5%9F%8E/" data-log_channel="zufang" data-log_index="4" data-log_value="瑞虹新城">瑞虹新城</a></li><li><a href="http://sh.lianjia.com/zufang/rs%E9%98%B3%E5%85%89%E5%A8%81%E5%B0%BC%E6%96%AF/" data-log_channel="zufang" data-log_index="5" data-log_value="阳光威尼斯">阳光威尼斯</a></li><li><a href="http://sh.lianjia.com/zufang/rs%E4%B8%8A%E6%B5%B7%E5%BA%B7%E5%9F%8E/" data-log_channel="zufang" data-log_index="6" data-log_value="上海康城">上海康城</a></li></div><li class="del">清除历史记录</li></ul><ul id="ershoufang"><li class="hot-name">热门搜索</li><div class="list"><li><a href="http://sh.lianjia.com/ershoufang/rs%E4%B8%8A%E6%B5%B7%E5%BA%B7%E5%9F%8E/" data-log_channel="ershoufang" data-log_index="1" data-log_value="上海康城">上海康城</a></li><li><a href="http://sh.lianjia.com/ershoufang/rs%E6%85%A7%E8%8A%9D%E6%B9%96%E8%8A%B1%E5%9B%AD/" data-log_channel="ershoufang" data-log_index="2" data-log_value="慧芝湖花园">慧芝湖花园</a></li><li><a href="http://sh.lianjia.com/ershoufang/rs%E5%A5%A5%E6%9E%97%E5%8C%B9%E5%85%8B%E8%8A%B1%E5%9B%AD/" data-log_channel="ershoufang" data-log_index="3" data-log_value="奥林匹克花园">奥林匹克花园</a></li><li><a href="http://sh.lianjia.com/ershoufang/rs%E4%B8%AD%E8%BF%9C%E4%B8%A4%E6%B9%BE%E5%9F%8E/" data-log_channel="ershoufang" data-log_index="4" data-log_value="中远两湾城">中远两湾城</a></li><li><a href="http://sh.lianjia.com/ershoufang/rs%E4%B8%9C%E6%96%B9%E6%9B%BC%E5%93%88%E9%A1%BF/" data-log_channel="ershoufang" data-log_index="5" data-log_value="东方曼哈顿">东方曼哈顿</a></li><li><a href="http://sh.lianjia.com/ershoufang/rs%E6%96%B0%E6%B9%96%E6%98%8E%E7%8F%A0%E5%9F%8E/" data-log_channel="ershoufang" data-log_index="6" data-log_value="新湖明珠城">新湖明珠城</a></li><li><a href="http://sh.lianjia.com/ershoufang/rs%E7%BB%8F%E7%BA%AC%E5%9F%8E%E5%B8%82%E7%BB%BF%E6%B4%B2/" data-log_channel="ershoufang" data-log_index="7" data-log_value="经纬城市绿洲">经纬城市绿洲</a></li><li><a href="http://sh.lianjia.com/ershoufang/rs%E4%BF%9D%E5%88%A9%E8%A5%BF%E5%AD%90%E6%B9%BE/" data-log_channel="ershoufang" data-log_index="8" data-log_value="保利西子湾">保利西子湾</a></li></div><li class="del">清除历史记录</li></ul><ul id="xiaoqu"><li class="hot-name">热门搜索</li><div class="list"><li><a href="http://sh.lianjia.com/xiaoqu/rs%E5%A5%A5%E6%9E%97%E5%8C%B9%E5%85%8B%E8%8A%B1%E5%9B%AD/" data-log_channel="xiaoqu" data-log_index="1" data-log_value="奥林匹克花园">奥林匹克花园</a></li><li><a href="http://sh.lianjia.com/xiaoqu/rs%E4%B8%96%E8%8C%82%E6%BB%A8%E6%B1%9F%E8%8A%B1%E5%9B%AD/" data-log_channel="xiaoqu" data-log_index="2" data-log_value="世茂滨江花园">世茂滨江花园</a></li><li><a href="http://sh.lianjia.com/xiaoqu/rs%E4%BF%9D%E5%88%A9%E8%A5%BF%E5%AD%90%E6%B9%BE/" data-log_channel="xiaoqu" data-log_index="3" data-log_value="保利西子湾">保利西子湾</a></li><li><a href="http://sh.lianjia.com/xiaoqu/rs%E6%96%B0%E9%AB%98%E8%8B%91/" data-log_channel="xiaoqu" data-log_index="4" data-log_value="新高苑">新高苑</a></li><li><a href="http://sh.lianjia.com/xiaoqu/rs%E4%B9%9D%E5%9F%8E%E6%B9%96%E6%BB%A8%E5%9B%BD%E9%99%85/" data-log_channel="xiaoqu" data-log_index="5" data-log_value="九城湖滨国际">九城湖滨国际</a></li><li><a href="http://sh.lianjia.com/xiaoqu/rs%E5%90%8C%E6%B6%A6%E8%8F%B2%E8%AF%97%E8%89%BE%E4%BC%A6/" data-log_channel="xiaoqu" data-log_index="6" data-log_value="同润菲诗艾伦">同润菲诗艾伦</a></li><li><a href="http://sh.lianjia.com/xiaoqu/rs%E4%BB%81%E6%81%92%E6%BB%A8%E6%B1%9F%E5%9B%AD/" data-log_channel="xiaoqu" data-log_index="7" data-log_value="仁恒滨江园">仁恒滨江园</a></li></div><li class="del">清除历史记录</li></ul><ul style="border:0;"></ul><ul id="loupan"><li class="hot-name">热门搜索</li><div class="list"><li><a href="http://sh.fang.lianjia.com/loupan/rs%E8%A5%BF%E7%8E%AF%E4%B8%AD%E5%BF%83%E6%98%9F%E4%BF%A1%E5%90%8D%E9%82%B8/" data-log_channel="loupan" data-log_index="1" data-log_value="西环中心星信名邸">西环中心星信名邸</a></li><li><a href="http://sh.fang.lianjia.com/loupan/rs%E8%B7%AF%E5%8A%B2%E4%BD%98%E5%B1%B1%E9%99%A2%E5%AD%90/" data-log_channel="loupan" data-log_index="2" data-log_value="路劲佘山院子">路劲佘山院子</a></li><li><a href="http://sh.fang.lianjia.com/loupan/rs%E4%B8%AD%E9%AA%8F%E5%A4%A9%E6%82%A6/" data-log_channel="loupan" data-log_index="3" data-log_value="中骏天悦">中骏天悦</a></li><li><a href="http://sh.fang.lianjia.com/loupan/rs%E7%A6%B9%E6%B4%B2%E5%BA%9C/" data-log_channel="loupan" data-log_index="4" data-log_value="禹洲府">禹洲府</a></li><li><a href="http://sh.fang.lianjia.com/loupan/rs%E8%87%BB%E6%B0%B4%E5%B2%B8/" data-log_channel="loupan" data-log_index="5" data-log_value="臻水岸">臻水岸</a></li><li><a href="http://sh.fang.lianjia.com/loupan/rs%E5%B0%9A%E6%99%AF%E4%B8%BD%E5%9B%AD/" data-log_channel="loupan" data-log_index="6" data-log_value="尚景丽园">尚景丽园</a></li></div><li class="del">清除历史记录</li></ul><ul style="border:0;"></ul></div><div id="suggest-cont" class="suggest-wrap" data-bl="sug" data-el="sug"></div></div><div class="savesearch" city-id="310000"></div></div><button  type="submit" data-bl="search" data-el="search" class="act-search btn home-ico ico-search LOGCLICKEVTID" target="_blank" daty-id="310000">搜索</button></form></div></div><div class="fr last"><div class="ditu fr"><a href="/dituzufang/" target="_blank"><i></i>地图找房</a></div></div></div></div>


<script  type="text/javascript">
;+function() {

    var oWrap_video_all = document.getElementById('wrap-video-all');
    if(!oWrap_video_all) {
        return;
    }

    oWrap_video_all.onclick = function(){
        var oVideo_box = document.getElementById('video-box');
        var oVideo_close = document.getElementById('video-close');
        oVideo_box.style.display = "block";
        oVideo_close.onclick = function(){
              oVideo_box.style.display = "none";
        }
    }
}();

</script>
<div class="savelist">
    <script type="text/template" id="savesearch">
    <%if(data && data.data){%>
        <span class="s-show"><%=data.count%>条已保存搜索<label></label></span>
        <div class="cunn">
            <ul>
                <li class="title">已保存搜索</li>
                <li class="list">
                    <% for(var i = 0; i < data.data.length;i++){ var dat = data.data;%>
                        <div class="li">
                            <a href="<%=dat[i].url%>" target="_blank">
                                <%if (dat[i].query){%>
                                    <span class="fl se"><%=dat[i].query%></span>
                                <%}%>
                                <span class="fl ti">
                                    <%for(var j = 0; j<dat[i].title.length;j++){%>
                                       <%=dat[i].title[j]%>
                                    <%}%>
                                </span>
                            </a>
                        </div>
                    <%}%>
                </li>
                 <%if (data.data.length > 3) {%>
                    <li class="more">查看全部已保存搜索</li>
                <%}%>
            </ul>
        </div>
    <%}%>
    </script>
</div>



<!-- 面包屑模块 -->
<div class="intro clear" mod-id="lj-common-bread"><div class="container"><div class="fl l-txt"><i class="icon"></i>&nbsp;<a href="/">链家网上海站</a><span class="stp">&nbsp;&gt;&nbsp;</span><a href="/zufang/">上海租房</a><span class="stp">&nbsp;&gt;&nbsp;</span><span>浦东租房</span><h1 class="index_h1">浦东租房</h1></div><div class="fr r-txt"></div></div></div><div class="wrapper">
<div class="filter-box"><div class="hd clear"><ul class="tab-lst"><li class="on"><a href="/zufang/"><span>全部租房</span></a></li><li><a href="/ditiezufang/"><span>地铁租房</span></a></li></ul><div class="info"><span class="num">真实房源，假一赔百元，不封顶！</span></div></div><div><div class="bd" id="filter-options"><dl class="dl-lst clear"><dt>区域：</dt><dd data-index="0"><div class="option-list"><a href="/zufang/">不限</a><a href="/zufang/pudong/" class="on">浦东</a><a href="/zufang/minhang/">闵行</a><a href="/zufang/baoshan/">宝山</a><a href="/zufang/xuhui/">徐汇</a><a href="/zufang/putuo/">普陀</a><a href="/zufang/yangpu/">杨浦</a><a href="/zufang/changning/">长宁</a><a href="/zufang/songjiang/">松江</a><a href="/zufang/jiading/">嘉定</a><a href="/zufang/huangpu/">黄浦</a><a href="/zufang/jingan/">静安</a><a href="/zufang/zhabei/">闸北</a><a href="/zufang/hongkou/">虹口</a><a href="/zufang/qingpu/">青浦</a><a href="/zufang/fengxian/">奉贤</a><a href="/zufang/jinshan/">金山</a><a href="/zufang/chongming/">崇明</a><a href="/zufang/shanghaizhoubian/">上海周边</a></div><div class="option-list sub-option-list"><a href="/zufang/pudong/" class="on">不限</a><span>B</span><a href="/zufang/beicai/">北蔡</a><a href="/zufang/biyun/">碧云</a><span>C</span><a href="/zufang/caolu/">曹路</a><a href="/zufang/chuansha/">川沙</a><span>D</span><a href="/zufang/datuanzhen/">大团镇</a><span>G</span><a href="/zufang/geqing/">合庆</a><a href="/zufang/gaohang/">高行</a><a href="/zufang/gaodong/">高东</a><span>H</span><a href="/zufang/huamu/">花木</a><a href="/zufang/hangtou/">航头</a><a href="/zufang/huinan/">惠南</a><span>J</span><a href="/zufang/jinqiao/">金桥</a><a href="/zufang/jinyang/">金杨</a><span>K</span><a href="/zufang/kangqiao/">康桥</a><span>L</span><a href="/zufang/lujiazui/">陆家嘴</a><a href="/zufang/laogangzhen/">老港镇</a><a href="/zufang/lingangxincheng/">临港新城</a><a href="/zufang/lianyang/">联洋</a><span>N</span><a href="/zufang/nichengzhen/">泥城镇</a><a href="/zufang/nanmatou/">南码头</a><span>S</span><a href="/zufang/sanlin/">三林</a><a href="/zufang/shibo/">世博</a><a href="/zufang/shuyuanzhen/">书院镇</a><span>T</span><a href="/zufang/tangqiao/">塘桥</a><a href="/zufang/tangzhen/">唐镇</a><span>W</span><a href="/zufang/waigaoqiao/">外高桥</a><a href="/zufang/wanxiangzhen/">万祥镇</a><a href="/zufang/weifang/">潍坊</a><span>X</span><a href="/zufang/xuanqiao/">宣桥</a><a href="/zufang/xinchang/">新场</a><span>Y</span><a href="/zufang/yuqiao1/">御桥</a><a href="/zufang/yangdong/">杨东</a><a href="/zufang/yuanshen/">源深</a><a href="/zufang/yangjing/">洋泾</a><span>Z</span><a href="/zufang/zhangjiang/">张江</a><a href="/zufang/zhuqiao/">祝桥</a><a href="/zufang/zhoupu/">周浦</a></div></dd></dl>
<dl class="dl-lst clear"><dt>租金：</dt><dd data-index="1"><div class="option-list"><a href="/zufang/pudong/" class="on"rel="nofollow">不限</a><a href="/zufang/pudong/rp1/"rel="nofollow">1000元以下</a><a href="/zufang/pudong/rp2/"rel="nofollow">1000-2000元</a><a href="/zufang/pudong/rp3/"rel="nofollow">2000-4000元</a><a href="/zufang/pudong/rp4/"rel="nofollow">4000-6000元</a><a href="/zufang/pudong/rp5/"rel="nofollow">6000-8000元</a><a href="/zufang/pudong/rp6/"rel="nofollow">8000-12000元</a><a href="/zufang/pudong/rp7/"rel="nofollow">12000元以上</a><div class="custom" data-type="price"><div class="txt-box"><input type="text" class="txt" name="min_price" data-index="1" value="" /></div>&nbsp;-&nbsp;<div class="txt-box"><input type="text" class="txt" name="max_price" data-index="1" value="" /></div>&nbsp;元<input type="button" data-type="price" class="ok" value="确定" /></div></div></dd></dl>
<dl class="dl-lst clear"><dt>面积：</dt><dd data-index="2"><div class="option-list"><a href="/zufang/pudong/" class="on"rel="nofollow">不限</a><a href="/zufang/pudong/ra1/"rel="nofollow">50平以下</a><a href="/zufang/pudong/ra2/"rel="nofollow">50-70平</a><a href="/zufang/pudong/ra3/"rel="nofollow">70-90平</a><a href="/zufang/pudong/ra4/"rel="nofollow">90-110平</a><a href="/zufang/pudong/ra5/"rel="nofollow">110-150平</a><a href="/zufang/pudong/ra6/"rel="nofollow">150平以上</a><div class="custom" data-type="area"><div class="txt-box"><input type="text" class="txt" name="min_area" data-index="2" value="" /></div>&nbsp;-&nbsp;<div class="txt-box"><input type="text" class="txt" name="max_area" data-index="2" value="" /></div>&nbsp;平<input type="button" data-type="area" class="ok" value="确定" /></div></div></dd></dl>
<dl class="dl-lst clear"><dt>房型：</dt><dd data-index="3"><div class="option-list"><a href="/zufang/pudong/" class="on"rel="nofollow">不限</a><a href="/zufang/pudong/l1/"rel="nofollow">一室</a><a href="/zufang/pudong/l2/"rel="nofollow">二室</a><a href="/zufang/pudong/l3/"rel="nofollow">三室</a><a href="/zufang/pudong/l4/"rel="nofollow">四室</a><a href="/zufang/pudong/l5/"rel="nofollow">五室</a><a href="/zufang/pudong/l6/"rel="nofollow">五室以上</a></div></dd></dl>
</div><div class="filter-bar01"><div id="sort-panel" class="sort-panel"><div class="left"><div class="fs14"><span class="left">筛选：</span></div><div class="right"><div class="d-1 dropdown"><span>朝向</span><i></i><ul class="fil-item"><a href="/zufang/pudong/f1/"><li>朝东</li></a><a href="/zufang/pudong/f2/"><li>朝南</li></a><a href="/zufang/pudong/f3/"><li>朝西</li></a><a href="/zufang/pudong/f4/"><li>朝北</li></a><a href="/zufang/pudong/f5/"><li>南北</li></a></ul></div><div class="d-2 dropdown"><span>楼层</span><i></i><ul class="fil-item"><a href="/zufang/pudong/lc1/"><li>低楼层</li></a><a href="/zufang/pudong/lc2/"><li>中楼层</li></a><a href="/zufang/pudong/lc3/"><li>高楼层</li></a></ul></div><div class="d-3 dropdown"><span>品牌</span><i></i><ul class="fil-item"><a href="/zufang/pudong/"><li>全部品牌</li></a><a href="/zufang/pudong/bd1/"><li>链家</li></a><a href="/zufang/pudong/bd2/"><li>自如</li></a></ul></div><div class="d-4 dropdown"><span>方式</span><i></i><ul class="fil-item"><a href="/zufang/pudong/"><li>全部方式</li></a><a href="/zufang/pudong/rt1/"><li>整租</li></a><a href="/zufang/pudong/rt2/"><li>合租</li></a></ul></div><div class="item-check"><ul><li><a href="/zufang/pudong/su1/"><i></i>近地铁</a></li><li><a href="/zufang/pudong/rd1/"><i></i>精装修</a></li><li><a href="/zufang/pudong/ky1/"><i></i>随时看房</a></li><li><a href="/zufang/pudong/idb1/"><i></i>独立阳台</a></li><li><a href="/zufang/pudong/pt1/"><i></i>独卫</a></li></ul></div><!-- <div class="item-check"><ul><li><a href="#;" class="check-a"><i></i>满五唯一</a></li><li><a href="#;"><i></i>房本满五年</a></li><li><a href="#;"><i></i>近地铁</a></li><li><a href="#;"><i></i>学区房</a></li><li><a href="#;"><i></i>不限购</a></li></ul></div> --></div></div></div></div><div id="filter-bar" class="filter-bar"><h3>条件：</h3><div class="filter-conditions"><span id="filter-display-bar"><script>;+function() {var filterTpl = '';filterTpl += '<a href="/zufang/"><span>浦东</span><span class="del"></span></a>';document.write(filterTpl);}();</script></span><script>;+function() {var filterTpl = '<a href="/zufang" id="filter-empty" class="del-all"><i></i>清空筛选选项</a>';document.write(filterTpl);}();</script></div><div class="clear"></div></div><div class="filter-bar01"><div class="sort-bar" id="sort-bar"><span>排序：</span><div class="sort-parent on"><a href="/zufang/pudong/"><span>默认</span></a></div><div class="sort-parent"><a href="/zufang/pudong/rco10/"><span>最新</span></a></div><div class="sort-parent"><a href="/zufang/pudong/rco20/"><span>租金低</span></a></div><div class="sort-parent"><span>面积</span><i></i><ul class="sort-children"><li><a href="/zufang/pudong/rco31/">面积从小到大</a></li><li><a href="/zufang/pudong/rco32/">面积从大到小</a></li></ul></div></div></div></div></div><div class="main-box clear"><div id="sem_card"></div><div class="con-box"><div class="list-head clear"><h2>共有<span>6909</span>套上海在租房源</h2><div class="view-type" id="viewType"><div class="modeshows modeshow"><span class="l-show view-mod" data-type="real" id="lshow"><i></i>实景图模式</span></div></div></div><div class="list-wrap"><ul id="house-lst" class="house-lst"><li data-index="0" data-log_index="0" data-id="107100866140" data-el="zufang" data-housecode="107100866140" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100866140.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953" alt="万科翡翠公园(公寓) 2室2厅 10000元" data-apart-layout="https://image1.ljcdn.com/x-se/hdic-frame/d8a835ae-bf30-42fb-92ee-4b8abeafb7da.png.280x210.jpg" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100866140.html" title="万科翡翠公园(公寓) 2室2厅 10000元">万科翡翠公园(公寓) 2室2厅 10000元</a><i class="new-label"></i></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000001156/" class="laisuzhou"><span class="region">万科翡翠公园(公寓)&nbsp;&nbsp;</span></a><span class="zone"><span>2室2厅&nbsp;&nbsp;</span></span><span class="meters">86.79平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/zhangjiang/">张江租房</a><span>/</span>高楼层(共18层)<span>/</span>板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"></div></div></div></div><div class="col-3"><div class="price"><span class="num">10000</span>元/月</div><div class="price-pre">2018.12.07 更新</div></div><div class="col-2"><div class="square"><div><span class="num">0</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="1" data-log_index="1" data-id="107100854596" data-el="zufang" data-housecode="107100854596" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100854596.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/167d93b6-7652-4fd1-a3e3-eed26eefd53d.jpg_600x450.jpg.280x210.jpg" alt="朝南一房采光好、配套齐全拎包可入住" data-apart-layout="https://image1.ljcdn.com/x-se/hdic-frame/ab213a69-fd40-4d42-bc51-a23a97ab1424.png.280x210.jpg" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100854596.html" title="朝南一房采光好、配套齐全拎包可入住">朝南一房采光好、配套齐全拎包可入住</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000012035/" class="laisuzhou"><span class="region">由由二村&nbsp;&nbsp;</span></a><span class="zone"><span>1室1厅&nbsp;&nbsp;</span></span><span class="meters">46.36平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/beicai/">北蔡租房</a><span>/</span>中楼层(共6层)<span>/</span>1997年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="fang-subway"></span><span class="fang-subway-ex"><span>近地铁</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">4100</span>元/月</div><div class="price-pre">2018.12.03 更新</div></div><div class="col-2"><div class="square"><div><span class="num">0</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="2" data-log_index="2" data-id="107100837634" data-el="zufang" data-housecode="107100837634" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100837634.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/52007935-919a-4aa5-83f5-4d30fa60c929.jpg.280x210.jpg" alt="新上房源 : 11号线御桥站，家具家电齐全，楼层位置好" data-apart-layout="https://image1.ljcdn.com/x-se/hdic-frame/6e943ef4-76df-48e5-a9c8-ba4c529f3d1e.png.280x210.jpg" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100837634.html" title="新上房源 : 11号线御桥站，家具家电齐全，楼层位置好">新上房源 : 11号线御桥站，家具家电齐全，楼层位置好</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000014070/" class="laisuzhou"><span class="region">京浦小区&nbsp;&nbsp;</span></a><span class="zone"><span>2室1厅&nbsp;&nbsp;</span></span><span class="meters">52.59平米&nbsp;&nbsp;</span><span>南 北</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/yuqiao1/">御桥租房</a><span>/</span>低楼层(共6层)<span>/</span>1995年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="fang-subway"></span><span class="fang-subway-ex"><span>近地铁</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">4400</span>元/月</div><div class="price-pre">2018.12.09 更新</div></div><div class="col-2"><div class="square"><div><span class="num">1</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="3" data-log_index="3" data-id="107100789007" data-el="zufang" data-housecode="107100789007" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100789007.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/5929c93d-4bac-4521-8324-32eca6061b7e.jpg.280x210.jpg" alt="富特五村两房全装全配 交通方便 预约可看房" data-apart-layout="https://image1.ljcdn.com/x-se/hdic-frame/a3ce6674-a158-4f88-8673-1094e6619b09.png.280x210.jpg" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100789007.html" title="富特五村两房全装全配 交通方便 预约可看房">富特五村两房全装全配 交通方便 预约可看房</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000004950/" class="laisuzhou"><span class="region">富特五村&nbsp;&nbsp;</span></a><span class="zone"><span>2室1厅&nbsp;&nbsp;</span></span><span class="meters">58.34平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/waigaoqiao/">外高桥租房</a><span>/</span>高楼层(共6层)<span>/</span>1993年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="haskey"></span><span class="haskey-ex"><span>随时看房</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">3800</span>元/月</div><div class="price-pre">2018.12.09 更新</div></div><div class="col-2"><div class="square"><div><span class="num">7</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="4" data-log_index="4" data-id="107100852016" data-el="zufang" data-housecode="107100852016" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100852016.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/26c2db7a-91da-431b-bbad-98d41be33713.jpg.280x210.jpg" alt="中等装修，自住风格，采光好，距离地铁500米" data-apart-layout="https://image1.ljcdn.com/x-se/hdic-frame/c1231b27-1f2c-4dea-843f-5b0ca78100cf.png.280x210.jpg" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100852016.html" title="中等装修，自住风格，采光好，距离地铁500米">中等装修，自住风格，采光好，距离地铁500米</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000010777/" class="laisuzhou"><span class="region">博三小区&nbsp;&nbsp;</span></a><span class="zone"><span>1室1厅&nbsp;&nbsp;</span></span><span class="meters">40.18平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/jinqiao/">金桥租房</a><span>/</span>中楼层(共6层)<span>/</span>1994年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="fang-subway"></span><span class="fang-subway-ex"><span>近地铁</span></span><span class="haskey"></span><span class="haskey-ex"><span>随时看房</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">3500</span>元/月</div><div class="price-pre">2018.12.09 更新</div></div><div class="col-2"><div class="square"><div><span class="num">10</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="5" data-log_index="5" data-id="107100844818" data-el="zufang" data-housecode="107100844818" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100844818.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100844818.html" title="华高二村 2室1厅 4500元">华高二村 2室1厅 4500元</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000012924/" class="laisuzhou"><span class="region">华高二村&nbsp;&nbsp;</span></a><span class="zone"><span>2室1厅&nbsp;&nbsp;</span></span><span class="meters">74.75平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/gaohang/">高行租房</a><span>/</span>低楼层(共6层)<span>/</span>1995年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="fang-subway"></span><span class="fang-subway-ex"><span>近地铁</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">4500</span>元/月</div><div class="price-pre">2018.12.07 更新</div></div><div class="col-2"><div class="square"><div><span class="num">0</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="6" data-log_index="6" data-id="107100866864" data-el="zufang" data-housecode="107100866864" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100866864.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/75a02096-72d9-4c7e-9906-1afd368afeb1.jpg.280x210.jpg" alt="6、13号线东明站400米内 万科物业精装全配 中层采光好" data-apart-layout="https://image1.ljcdn.com/x-se/hdic-frame/1411c7f2-8051-400a-8412-a96d2d806442.png.280x210.jpg" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100866864.html" title="6、13号线东明站400米内 万科物业精装全配 中层采光好">6、13号线东明站400米内 万科物业精装全配 中层采光好</a><i class="new-label"></i></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000014516/" class="laisuzhou"><span class="region">万科金色城品&nbsp;&nbsp;</span></a><span class="zone"><span>1室1厅&nbsp;&nbsp;</span></span><span class="meters">54.71平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/shibo/">世博租房</a><span>/</span>中楼层(共18层)<span>/</span>2007年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="fang-subway"></span><span class="fang-subway-ex"><span>近地铁</span></span><span class="decoration"></span><span class="decoration-ex"><span>精装修</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">6000</span>元/月</div><div class="price-pre">2018.12.08 更新</div></div><div class="col-2"><div class="square"><div><span class="num">0</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="7" data-log_index="7" data-id="107100855815" data-el="zufang" data-housecode="107100855815" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100855815.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/7d876b48-9617-4f3e-a109-fd42d72b910c.jpg.280x210.jpg" alt="建中路171弄 3室1厅 9000元" data-apart-layout="https://image1.ljcdn.com/x-se/hdic-frame/5de6d2fc-aaba-48a9-ad7e-00053ceb7f9b.png.280x210.jpg" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100855815.html" title="建中路171弄 3室1厅 9000元">建中路171弄 3室1厅 9000元</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000011542/" class="laisuzhou"><span class="region">建中路171弄&nbsp;&nbsp;</span></a><span class="zone"><span>3室1厅&nbsp;&nbsp;</span></span><span class="meters">86.09平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/zhangjiang/">张江租房</a><span>/</span>中楼层(共6层)<span>/</span>1993年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="haskey"></span><span class="haskey-ex"><span>随时看房</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">9000</span>元/月</div><div class="price-pre">2018.12.09 更新</div></div><div class="col-2"><div class="square"><div><span class="num">0</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="8" data-log_index="8" data-id="107100828181" data-el="zufang" data-housecode="107100828181" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100828181.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/0a018b10-1a03-4fce-a499-283398062b40.jpg.280x210.jpg" alt="上房金丰苑，电梯房，大两房，精装修" data-apart-layout="https://image1.ljcdn.com/x-se/hdic-frame/f2f9ba13-89da-4c24-9326-72920948b7c1.png.280x210.jpg" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100828181.html" title="上房金丰苑，电梯房，大两房，精装修">上房金丰苑，电梯房，大两房，精装修</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000013503/" class="laisuzhou"><span class="region">上房金丰苑&nbsp;&nbsp;</span></a><span class="zone"><span>2室2厅&nbsp;&nbsp;</span></span><span class="meters">98.73平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/jinyang/">金杨租房</a><span>/</span>中楼层(共24层)<span>/</span>2002年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"></div></div></div></div><div class="col-3"><div class="price"><span class="num">5800</span>元/月</div><div class="price-pre">2018.12.03 更新</div></div><div class="col-2"><div class="square"><div><span class="num">3</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="9" data-log_index="9" data-id="107100740862" data-el="zufang" data-housecode="107100740862" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100740862.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/test-a509b60f-13f2-49f8-8e5b-4782e1acd25b.png.280x210.jpg" alt="周 边配套：万达广场，乐购，万达电影城" data-apart-layout="https://image1.ljcdn.com/x-se/hdic-frame/test-fd0bf580-02f7-421d-b689-10b0da54473b.png.280x210.jpg" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100740862.html" title="周 边配套：万达广场，乐购，万达电影城">周 边配套：万达广场，乐购，万达电影城</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000013718/" class="laisuzhou"><span class="region">南华城&nbsp;&nbsp;</span></a><span class="zone"><span>2室2厅&nbsp;&nbsp;</span></span><span class="meters">80平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/kangqiao/">康桥租房</a><span>/</span>中楼层(共6层)<span>/</span>1994年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"></div></div></div></div><div class="col-3"><div class="price"><span class="num">3800</span>元/月</div><div class="price-pre">2018.12.07 更新</div></div><div class="col-2"><div class="square"><div><span class="num">0</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="10" data-log_index="10" data-id="107100858309" data-el="zufang" data-housecode="107100858309" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100858309.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/1f1d0ad0-dfb1-44c4-b514-a705c6280112.jpg.280x210.jpg" alt="汇锦城精装修大两房，干净漂亮 有钥匙随时好看" data-apart-layout="https://image1.ljcdn.com/x-se/hdic-frame/3447a134-bb18-409b-9da5-5727e8dd866f.png.280x210.jpg" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100858309.html" title="汇锦城精装修大两房，干净漂亮 有钥匙随时好看">汇锦城精装修大两房，干净漂亮 有钥匙随时好看</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000010599/" class="laisuzhou"><span class="region">汇锦城二期&nbsp;&nbsp;</span></a><span class="zone"><span>2室2厅&nbsp;&nbsp;</span></span><span class="meters">84.28平米&nbsp;&nbsp;</span><span>南 北</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/xinchang/">新场租房</a><span>/</span>低楼层(共18层)<span>/</span>2012年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"></div></div></div></div><div class="col-3"><div class="price"><span class="num">2600</span>元/月</div><div class="price-pre">2018.12.07 更新</div></div><div class="col-2"><div class="square"><div><span class="num">1</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="11" data-log_index="11" data-id="107100853138" data-el="zufang" data-housecode="107100853138" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100853138.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/86d02930-bcd0-4805-b740-bbeed513eeed.jpg.280x210.jpg" alt="新芳邻精装两房出租，近地铁，交通便捷，小区安静" data-apart-layout="https://image1.ljcdn.com/x-se/hdic-frame/48052d94-b980-4f78-a5b6-c5553fa53643.png.280x210.jpg" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100853138.html" title="新芳邻精装两房出租，近地铁，交通便捷，小区安静">新芳邻精装两房出租，近地铁，交通便捷，小区安静</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000012790/" class="laisuzhou"><span class="region">新芳邻&nbsp;&nbsp;</span></a><span class="zone"><span>2室1厅&nbsp;&nbsp;</span></span><span class="meters">69.69平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/caolu/">曹路租房</a><span>/</span>低楼层(共6层)<span>/</span>2002年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="fang-subway"></span><span class="fang-subway-ex"><span>近地铁</span></span><span class="decoration"></span><span class="decoration-ex"><span>精装修</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">4000</span>元/月</div><div class="price-pre">2018.12.09 更新</div></div><div class="col-2"><div class="square"><div><span class="num">1</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="12" data-log_index="12" data-id="107100858421" data-el="zufang" data-housecode="107100858421" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100858421.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/e39e9bb2-12ac-472b-9b56-362cc6529cd8.jpg.280x210.jpg" alt="银丰苑 1室1厅 3000元" data-apart-layout="https://image1.ljcdn.com/x-se/hdic-frame/d29b3034-6f86-4539-8f8a-17a5a16e149b.png.280x210.jpg" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100858421.html" title="银丰苑 1室1厅 3000元">银丰苑 1室1厅 3000元</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000011594/" class="laisuzhou"><span class="region">银丰苑&nbsp;&nbsp;</span></a><span class="zone"><span>1室1厅&nbsp;&nbsp;</span></span><span class="meters">52.79平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/caolu/">曹路租房</a><span>/</span>低楼层(共6层)<span>/</span>2007年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="fang-subway"></span><span class="fang-subway-ex"><span>近地铁</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">3000</span>元/月</div><div class="price-pre">2018.12.04 更新</div></div><div class="col-2"><div class="square"><div><span class="num">0</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="13" data-log_index="13" data-id="107100855940" data-el="zufang" data-housecode="107100855940" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100855940.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/eee98746-9413-4683-8010-5c37105795d2.jpg_600x450.jpg.280x210.jpg" alt="2号世纪公园站 全新精装三房，电器新，诚意出租" data-apart-layout="https://image1.ljcdn.com/x-se/hdic-frame/4039fef5-6eb5-4e59-aa10-ed436cce7f1e.png.280x210.jpg" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100855940.html" title="2号世纪公园站 全新精装三房，电器新，诚意出租">2号世纪公园站 全新精装三房，电器新，诚意出租</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000010070/" class="laisuzhou"><span class="region">瑞达苑&nbsp;&nbsp;</span></a><span class="zone"><span>3室2厅&nbsp;&nbsp;</span></span><span class="meters">110.3平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/huamu/">花木租房</a><span>/</span>高楼层(共6层)<span>/</span>1995年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="fang-subway"></span><span class="fang-subway-ex"><span>近地铁</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">9000</span>元/月</div><div class="price-pre">2018.12.03 更新</div></div><div class="col-2"><div class="square"><div><span class="num">0</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="14" data-log_index="14" data-id="107100855966" data-el="zufang" data-housecode="107100855966" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100855966.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/b67e9e59-7914-40b1-a6a8-2d33848b4761.jpg.280x210.jpg" alt="上钢八九村 2室1厅 5500元" data-apart-layout="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100855966.html" title="上钢八九村 2室1厅 5500元">上钢八九村 2室1厅 5500元</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000014649/" class="laisuzhou"><span class="region">上钢八九村&nbsp;&nbsp;</span></a><span class="zone"><span>2室1厅&nbsp;&nbsp;</span></span><span class="meters">50.12平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/shibo/">世博租房</a><span>/</span>高楼层(共6层)<span>/</span>1984年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="fang-subway"></span><span class="fang-subway-ex"><span>近地铁</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">5500</span>元/月</div><div class="price-pre">2018.12.09 更新</div></div><div class="col-2"><div class="square"><div><span class="num">4</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="15" data-log_index="15" data-id="107100860813" data-el="zufang" data-housecode="107100860813" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100860813.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/5cbce608-a017-45ce-bc89-27e22bfe4f95.jpg.280x210.jpg" alt="精装四房+美式风格+独立电梯+小区景观大道位置好" data-apart-layout="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100860813.html" title="精装四房+美式风格+独立电梯+小区景观大道位置好">精装四房+美式风格+独立电梯+小区景观大道位置好</a><i class="new-label"></i></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000017980/" class="laisuzhou"><span class="region">仁恒河滨城&nbsp;&nbsp;</span></a><span class="zone"><span>4室2厅&nbsp;&nbsp;</span></span><span class="meters">207.67平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/lianyang/">联洋租房</a><span>/</span>低楼层(共26层)<span>/</span>2005年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"></div></div></div></div><div class="col-3"><div class="price"><span class="num">29000</span>元/月</div><div class="price-pre">2018.12.09 更新</div></div><div class="col-2"><div class="square"><div><span class="num">0</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="16" data-log_index="16" data-id="107100856847" data-el="zufang" data-housecode="107100856847" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100856847.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/23ba983a-5d46-494a-a492-e7ee2c6366d8.jpg.280x210.jpg" alt="万邦都市花园 3室2厅 12000元" data-apart-layout="https://image1.ljcdn.com/x-se/hdic-frame/1419486f-64df-4ff3-a020-1910ba5f5813.png.280x210.jpg" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100856847.html" title="万邦都市花园 3室2厅 12000元">万邦都市花园 3室2厅 12000元</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000018309/" class="laisuzhou"><span class="region">万邦都市花园&nbsp;&nbsp;</span></a><span class="zone"><span>3室2厅&nbsp;&nbsp;</span></span><span class="meters">136.67平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/beicai/">北蔡租房</a><span>/</span>中楼层(共18层)<span>/</span>2003年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="fang-subway"></span><span class="fang-subway-ex"><span>近地铁</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">12000</span>元/月</div><div class="price-pre">2018.12.10 更新</div></div><div class="col-2"><div class="square"><div><span class="num">2</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="17" data-log_index="17" data-id="107100843315" data-el="zufang" data-housecode="107100843315" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100843315.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/db427b2e-26ac-4c72-bb48-b9a42a2ebc2b.jpg.280x210.jpg" alt="地铁电梯两房 居家装修 价格美丽....." data-apart-layout="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100843315.html" title="地铁电梯两房 居家装修 价格美丽.....">地铁电梯两房 居家装修 价格美丽.....</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000015027/" class="laisuzhou"><span class="region">茂兴大厦&nbsp;&nbsp;</span></a><span class="zone"><span>2室1厅&nbsp;&nbsp;</span></span><span class="meters">85.04平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/tangqiao/">塘桥租房</a><span>/</span>低楼层(共24层)<span>/</span>1995年建塔楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="fang-subway"></span><span class="fang-subway-ex"><span>近地铁</span></span><span class="haskey"></span><span class="haskey-ex"><span>随时看房</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">6300</span>元/月</div><div class="price-pre">2018.12.03 更新</div></div><div class="col-2"><div class="square"><div><span class="num">3</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="18" data-log_index="18" data-id="107100854437" data-el="zufang" data-housecode="107100854437" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100854437.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/cf04a1c5-f55b-408e-a966-ba928e12713f.jpg.280x210.jpg" alt="万科清林径 精装全配 3221 近地铁 采光好高层" data-apart-layout="https://image1.ljcdn.com/x-se/hdic-frame/d61afc6c-137b-449c-89ca-5003f1927151.png.280x210.jpg" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100854437.html" title="万科清林径 精装全配 3221 近地铁 采光好高层">万科清林径 精装全配 3221 近地铁 采光好高层</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000009225/" class="laisuzhou"><span class="region">万科清林径&nbsp;&nbsp;</span></a><span class="zone"><span>3室2厅&nbsp;&nbsp;</span></span><span class="meters">118.63平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/xinchang/">新场租房</a><span>/</span>中楼层(共18层)<span>/</span>2012年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="decoration"></span><span class="decoration-ex"><span>精装修</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">4500</span>元/月</div><div class="price-pre">2018.12.09 更新</div></div><div class="col-2"><div class="square"><div><span class="num">1</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="19" data-log_index="19" data-id="107100848553" data-el="zufang" data-housecode="107100848553" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100848553.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/648352b1-b44f-43aa-9a0a-5e918f8924c2.jpg.280x210.jpg" alt="东方冠郡，南北通透精装2房，家具家电齐全 拎包入住" data-apart-layout="https://image1.ljcdn.com/x-se/hdic-frame/3e5c7359-fe29-45d0-adb0-f670854a3697.png.280x210.jpg" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100848553.html" title="东方冠郡，南北通透精装2房，家具家电齐全 拎包入住">东方冠郡，南北通透精装2房，家具家电齐全 拎包入住</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000015282/" class="laisuzhou"><span class="region">东方冠郡&nbsp;&nbsp;</span></a><span class="zone"><span>2室2厅&nbsp;&nbsp;</span></span><span class="meters">99平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/xinchang/">新场租房</a><span>/</span>高楼层(共18层)<span>/</span>2013年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"></div></div></div></div><div class="col-3"><div class="price"><span class="num">2800</span>元/月</div><div class="price-pre">2018.12.02 更新</div></div><div class="col-2"><div class="square"><div><span class="num">1</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="20" data-log_index="20" data-id="107100721615" data-el="zufang" data-housecode="107100721615" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100721615.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/cb002ea5-a3b9-4a28-a1f8-f074786c3306.jpg.280x210.jpg" alt="电梯高层采光好精装修拎包入住。" data-apart-layout="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100721615.html" title="电梯高层采光好精装修拎包入住。">电梯高层采光好精装修拎包入住。</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011102205778/" class="laisuzhou"><span class="region">青客公寓幸福里&nbsp;&nbsp;</span></a><span class="zone"><span>3室2厅&nbsp;&nbsp;</span></span><span class="meters">116.85平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/geqing/">合庆租房</a><span>/</span>高楼层(共16层)<span>/</span>2013年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="haskey"></span><span class="haskey-ex"><span>随时看房</span></span><span class="decoration"></span><span class="decoration-ex"><span>精装修</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">6200</span>元/月</div><div class="price-pre">2018.12.08 更新</div></div><div class="col-2"><div class="square"><div><span class="num">0</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="21" data-log_index="21" data-id="107100847554" data-el="zufang" data-housecode="107100847554" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100847554.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/bf36f6d4-7c90-40e5-9746-8a25920d2015.jpg.280x210.jpg" alt="锦绣小区 2室1厅 6500元" data-apart-layout="https://image1.ljcdn.com/x-se/hdic-frame/d95e6857-6de0-451a-8351-d2e6d5e0826c.png.280x210.jpg" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100847554.html" title="锦绣小区 2室1厅 6500元">锦绣小区 2室1厅 6500元</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000015609/" class="laisuzhou"><span class="region">锦绣小区&nbsp;&nbsp;</span></a><span class="zone"><span>2室1厅&nbsp;&nbsp;</span></span><span class="meters">65平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/huamu/">花木租房</a><span>/</span>高楼层(共6层)<span>/</span>1996年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"></div></div></div></div><div class="col-3"><div class="price"><span class="num">6500</span>元/月</div><div class="price-pre">2018.12.08 更新</div></div><div class="col-2"><div class="square"><div><span class="num">0</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="22" data-log_index="22" data-id="107100864544" data-el="zufang" data-housecode="107100864544" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100864544.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/9e74a502-e624-4707-98bb-fd2f6d8000e9.jpg.280x210.jpg" alt="2号线地铁大一房 朝南精装黄 金2楼 随看 业主诚意出租" data-apart-layout="https://image1.ljcdn.com/310000-frame/157f02e2-c22b-4433-936b-bd20f20a0cd7.jpg.280x210.jpg" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100864544.html" title="2号线地铁大一房 朝南精装黄 金2楼 随看 业主诚意出租">2号线地铁大一房 朝南精装黄 金2楼 随看 业主诚意出租</a><i class="new-label"></i></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000015981/" class="laisuzhou"><span class="region">东昌新村&nbsp;&nbsp;</span></a><span class="zone"><span>1室1厅&nbsp;&nbsp;</span></span><span class="meters">40.48平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/lujiazui/">陆家嘴租房</a><span>/</span>低楼层(共6层)<span>/</span>1980年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="fang-subway"></span><span class="fang-subway-ex"><span>近地铁</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">4300</span>元/月</div><div class="price-pre">2018.12.10 更新</div></div><div class="col-2"><div class="square"><div><span class="num">0</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="23" data-log_index="23" data-id="107100852455" data-el="zufang" data-housecode="107100852455" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100852455.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953" alt="沈默花苑 两房出租 看房随时 诚意出租" data-apart-layout="https://image1.ljcdn.com/x-se/hdic-frame/9345e0af-9c25-4711-81b3-dfd12228a8e6.png.280x210.jpg" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100852455.html" title="沈默花苑 两房出租 看房随时 诚意出租">沈默花苑 两房出租 看房随时 诚意出租</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000014180/" class="laisuzhou"><span class="region">沈默花苑&nbsp;&nbsp;</span></a><span class="zone"><span>2室2厅&nbsp;&nbsp;</span></span><span class="meters">84.84平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/zhoupu/">周浦租房</a><span>/</span>低楼层(共6层)<span>/</span>2008年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"></div></div></div></div><div class="col-3"><div class="price"><span class="num">4100</span>元/月</div><div class="price-pre">2018.12.07 更新</div></div><div class="col-2"><div class="square"><div><span class="num">1</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="24" data-log_index="24" data-id="107001346658" data-el="zufang" data-housecode="107001346658" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107001346658.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107001346658.html" title="南园坊 2室1厅 1500元">南园坊 2室1厅 1500元</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000002725/" class="laisuzhou"><span class="region">南园坊&nbsp;&nbsp;</span></a><span class="zone"><span>2室1厅&nbsp;&nbsp;</span></span><span class="meters">97.44平米&nbsp;&nbsp;</span><span>暂无数据</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/huinan/">惠南租房</a><span>/</span>高楼层(共4层)<span>/</span>2004年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"></div></div></div></div><div class="col-3"><div class="price"><span class="num">1500</span>元/月</div><div class="price-pre">2018.12.08 更新</div></div><div class="col-2"><div class="square"><div><span class="num">0</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="25" data-log_index="25" data-id="107100866403" data-el="zufang" data-housecode="107100866403" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100866403.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/5ecdf020-6632-457f-88ae-ff0672654a05.jpg.280x210.jpg" alt="业主诚意出租+精装修2房+2.7.16号线+小区位置好" data-apart-layout="https://image1.ljcdn.com/x-se/shfdfs-image/20141211/6740e917-fb94-4edd-a90a-305eee228868.jpg.280x210.jpg" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100866403.html" title="业主诚意出租+精装修2房+2.7.16号线+小区位置好">业主诚意出租+精装修2房+2.7.16号线+小区位置好</a><i class="new-label"></i></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000003169/" class="laisuzhou"><span class="region">大唐盛世花园&nbsp;&nbsp;</span></a><span class="zone"><span>2室2厅&nbsp;&nbsp;</span></span><span class="meters">97.05平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/huamu/">花木租房</a><span>/</span>中楼层(共12层)<span>/</span>2008年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="fang-subway"></span><span class="fang-subway-ex"><span>近地铁</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">14000</span>元/月</div><div class="price-pre">2018.12.08 更新</div></div><div class="col-2"><div class="square"><div><span class="num">0</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="26" data-log_index="26" data-id="107100778822" data-el="zufang" data-housecode="107100778822" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100778822.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/817ea6cf-4ff1-49af-a2fa-b891dc453d2e.jpg.280x210.jpg" alt="全新装修，价格可谈，优质一房，近地铁" data-apart-layout="https://image1.ljcdn.com/x-se/hdic-frame/7a810240-74a3-47e7-a464-5bea02ff861e.png.280x210.jpg" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100778822.html" title="全新装修，价格可谈，优质一房，近地铁">全新装修，价格可谈，优质一房，近地铁</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000002687/" class="laisuzhou"><span class="region">微山二村&nbsp;&nbsp;</span></a><span class="zone"><span>1室1厅&nbsp;&nbsp;</span></span><span class="meters">29.4平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/tangqiao/">塘桥租房</a><span>/</span>中楼层(共6层)<span>/</span>1984年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="fang-subway"></span><span class="fang-subway-ex"><span>近地铁</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">5600</span>元/月</div><div class="price-pre">2018.12.07 更新</div></div><div class="col-2"><div class="square"><div><span class="num">0</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="27" data-log_index="27" data-id="107100865431" data-el="zufang" data-housecode="107100865431" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100865431.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/110d1abe-18b2-404b-833d-467242798046.jpg.280x210.jpg" alt="长清路595弄 1室1厅 4600元" data-apart-layout="https://image1.ljcdn.com/x-se/hdic-frame/6c032af1-4b6b-4e70-a6c2-c946ddff53f3.png.280x210.jpg" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100865431.html" title="长清路595弄 1室1厅 4600元">长清路595弄 1室1厅 4600元</a><i class="new-label"></i></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011063203093/" class="laisuzhou"><span class="region">长清路595弄&nbsp;&nbsp;</span></a><span class="zone"><span>1室1厅&nbsp;&nbsp;</span></span><span class="meters">43.25平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/sanlin/">三林租房</a><span>/</span>高楼层(共6层)<span>/</span>1994年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="fang-subway"></span><span class="fang-subway-ex"><span>近地铁</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">4600</span>元/月</div><div class="price-pre">2018.12.07 更新</div></div><div class="col-2"><div class="square"><div><span class="num">0</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="28" data-log_index="28" data-id="107100862912" data-el="zufang" data-housecode="107100862912" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100862912.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100862912.html" title="近六号线十三号线东明路站 交通便利 出行方便">近六号线十三号线东明路站 交通便利 出行方便</a><i class="new-label"></i></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000014789/" class="laisuzhou"><span class="region">云台二小区&nbsp;&nbsp;</span></a><span class="zone"><span>1室1厅&nbsp;&nbsp;</span></span><span class="meters">44.99平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/shibo/">世博租房</a><span>/</span>中楼层(共6层)<span>/</span>1995年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="fang-subway"></span><span class="fang-subway-ex"><span>近地铁</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">3400</span>元/月</div><div class="price-pre">2018.12.10 更新</div></div><div class="col-2"><div class="square"><div><span class="num">0</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="29" data-log_index="29" data-id="107100861844" data-el="zufang" data-housecode="107100861844" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100861844.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/b7ef94a5-9f4e-48f0-97e6-9540c0f891b2.jpg.280x210.jpg" alt="杨园三村两房一厅南北户型东西全配" data-apart-layout="https://image1.ljcdn.com/x-se/hdic-frame/7e480df6-bbee-4030-92fb-47ba16f8dc08.png.280x210.jpg" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100861844.html" title="杨园三村两房一厅南北户型东西全配">杨园三村两房一厅南北户型东西全配</a><i class="new-label"></i></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000013720/" class="laisuzhou"><span class="region">杨园三村&nbsp;&nbsp;</span></a><span class="zone"><span>2室1厅&nbsp;&nbsp;</span></span><span class="meters">54.63平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/gaodong/">高东租房</a><span>/</span>高楼层(共6层)<span>/</span>1993年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="haskey"></span><span class="haskey-ex"><span>随时看房</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">3100</span>元/月</div><div class="price-pre">2018.12.07 更新</div></div><div class="col-2"><div class="square"><div><span class="num">1</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li></ul><div style="display:none;"></div>
<div class="page-box house-lst-page-box" comp-module='page' page-url="/zufang/pudong/pg{page}/"page-data='{"totalPage":100,"curPage":1}'></div>


</div></div><!-- <div id="list-side" class="side-bar" style="display:none;"><div id="map-box" class="map-box"></div><div class="search-widget"><form action=""><input type="text" class="txt" placeholder="搜哪儿去哪儿！" /><input type="submit" value="" class="btn" /></form></div></div> --></div><!--  <div class="recommend" id="rec-dom" style="display:none"><div class="hd clear"><h5>热门小区推荐</h5></div><div class="recommend-lst clear"></div></div> -->
</div>

<div class="pagination_group_a">
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
 <script type="text/template" id="sem_card_tpl" semResblockId="">
 
      <div class="agentCardPush LOGVIEW" log-mod="zufang_list_semcard" data-bl="agent" data-el="<%=data.agentUcid%>" data-log_id="20001" data-log_value="<%=data.resblockId%>" data-log_source="<%=data.ljwebSource%>" data-log_statId="<%=data.ljwebStatId%>">
        <div class="agentCardAgentInfo">
          <a href="<%=data.agentUrl%>" target="_blank" class="agentCardAgentImg LOGCLICK" data-bl="agent"  data-log_value="<%=data.resblockId%>" data-log_source="<%=data.ljwebSource%>" data-log_statId="<%=data.ljwebStatId%>"><img src="<%=data.photoPath%>.75x100.jpg" alt="小区顾问"></a>
          <div class="cardAgentInfo">
            <div class="cardAgentNameContainer im-talk"><a target="_blank" href="<%=data.agentUrl%>" class="cardAgentName LOGCLICK" data-bl="agent"  data-log_value="<%=data.resblockId%>" data-log_source="<%=data.ljwebSource%>" data-log_statId="<%=data.ljwebStatId%>"><%=data.name%></a><a class="cardAgentIM LOGCLICK im-talk" data-bl="agent_im" data-ucid="<%=data.agentUcid%>"  data-source-port="PC:ershou_zufang_list_top" data-source-extends=<%=JSON.stringify(communityId)%>></a><span class="cardAgentTitle">置业顾问</span></div>
            <div class="cardAgentPhone"><%=data.fourPhoneOne%></div>
            <div class="cardAgentDesc"><%=data.desc%></div>
          </div>
        </div>
        <div class="agentCardResblockInfo">
          <div class="agentCardResblockName">
            <a class="agentCardResblockTitle LOGCLICK" data-bl="agent_resblock_name"  data-log_value="<%=data.resblockId%>" data-log_source="<%=data.ljwebSource%>" data-log_statId="<%=data.ljwebStatId%>" target="_blank" href="<%=data.resblockUrl%>"><%=data.resblockName%></a>
            <span class="agentCardResblockSubTitle"><%=data.districtName%><%=data.bizcircleName%></span>
            <a href="<%=data.resblockUrl%>" target="_blank" class="agentCardResblockLink LOGCLICK" data-bl="agent_resblock_info"  data-log_value="<%=data.resblockId%>" data-log_source="<%=data.ljwebSource%>" data-log_statId="<%=data.ljwebStatId%>">查看小区详情</a>
          </div>
          <div class="agentCardResblockDetail">
            <div class="agentCardDetailItem">
              <div class="agentCardDetailTitle">小区租金</div>
              <a href="<%=data.fangjiaUrl%>" target="_blank" class="agentCardDetailInfo LOGCLICK" data-bl="agent_resblock_avg" data-log_value="<%=data.resblockId%>" data-log_source="<%=data.ljwebSource%>" data-log_statId="<%=data.ljwebStatId%>">
              <%if (data.unitPrice != '暂无'){%>
              <%=data.unitPrice%>元/月
              <%}else{%>
                暂无
              <%}%>
              </a>
            </div>
            <div class="agentCardDetailItem">
              <div class="agentCardDetailTitle">正在出租</div>
              <div class="agentCardDetailInfo"><%=data.sellNum%>套</div>
            </div>
            <div class="agentCardDetailItem">
              <div class="agentCardDetailTitle">近90天成交</div>
              <div class="agentCardDetailInfo"><%=data['90saleCount']%>套</div>
            </div>
            <div class="agentCardDetailItem">
              <div class="agentCardDetailTitle">近30天带看</div>
              <div class="agentCardDetailInfo"><%=data.day30See%>次</div>
            </div>
          </div>
        </div>
      </div>

</script>
<div class="footer"><div class="wrapper"><div class="f-title"><div class="fl"><ul><li><a href="https://www.lianjia.com/zhuanti/home/" rel="nofollow" target="_blank">了解链家</a></li><li><a href="https://sh.lianjia.com/about/aboutlianjia/" rel="nofollow" target="_blank">关于链家</a></li><li><a href="https://sh.lianjia.com/about/contactus/" rel="nofollow" target="_blank">联系我们</a></li><li><a href="http://join.lianjia.com/" rel="nofollow" target="_blank">加入我们</a></li><li><a href="https://www.lianjia.com/privacy/" rel="nofollow" target="_blank">隐私声明</a></li><li><a href="https://sh.lianjia.com/sitemap/" target="_blank">网站地图</a></li><li><a href="https://page.lianjia.com/subject/youlian.html" rel="nofollow" target="_blank">友情链接</a></li><li><a href="https://agent.lianjia.com/" rel="nofollow" target="_blank">经纪人登录</a></li></ul></div><div class="fr">官方客服 1010 9666</div></div><div class="lianjia-link-box"><div class="fl"><div class="tab"><span  class="hover">城市二手房</span><span >房产资讯</span><span >城区二手房</span><span >城区租房</span><span >城区小区</span><span >热门小区</span><span >热门问答</span><span >热门百科</span></div><div class="link-list"><div><dd><a target="_blank" href="https://bj.lianjia.com/">北京房产网</a><a target="_blank" href="https://sh.lianjia.com/">上海房产网</a><a target="_blank" href="https://gz.lianjia.com/">广州房产网</a><a target="_blank" href="https://sz.lianjia.com/">深圳房产网</a><a target="_blank" href="https://tj.lianjia.com/">天津房产网</a><a target="_blank" href="https://cd.lianjia.com/">成都房产网</a><a target="_blank" href="https://nj.lianjia.com/">南京房产网</a><a target="_blank" href="https://hz.lianjia.com/">杭州房产网</a><a target="_blank" href="https://qd.lianjia.com/">青岛房产网</a><a target="_blank" href="https://dl.lianjia.com/">大连房产网</a><a target="_blank" href="https://su.lianjia.com/">苏州房产网</a><a target="_blank" href="https://xm.lianjia.com/">厦门房产网</a><a target="_blank" href="https://wh.lianjia.com/">武汉房产网</a><a target="_blank" href="https://cq.lianjia.com/">重庆房产网</a><a target="_blank" href="https://cs.lianjia.com/">长沙房产网</a><a target="_blank" href="https://jn.lianjia.com/">济南房产网</a><a target="_blank" href="https://fs.lianjia.com/">佛山房产网</a><a target="_blank" href="https://dg.lianjia.com/">东莞房产网</a><a target="_blank" href="https://xa.lianjia.com/">西安房产网</a><a target="_blank" href="https://sjz.lianjia.com/">石家庄房产网</a><a target="_blank" href="https://yt.lianjia.com/">烟台房产网</a><a target="_blank" href="https://wz.lianjia.com/">温州房产网</a><a target="_blank" href="https://zs.lianjia.com/">中山房产网</a><a target="_blank" href="https://zh.lianjia.com/">珠海房产网</a><a target="_blank" href="https://jx.lianjia.com/">嘉兴房产网</a><a target="_blank" href="https://hui.lianjia.com/">惠州房产网</a><a target="_blank" href="https://ty.lianjia.com/">太原房产网</a><a target="_blank" href="https://sy.lianjia.com/">沈阳房产网</a><a target="_blank" href="https://nt.lianjia.com/">南通房产网</a><a target="_blank" href="https://hk.lianjia.com/">海口房产网</a><a target="_blank" href="https://wf.lianjia.com/">潍坊房产网</a><a target="_blank" href="https://linyi.lianjia.com/">临沂房产网</a><a target="_blank" href="https://wx.lianjia.com/">无锡房产网</a><a target="_blank" href="https://san.lianjia.com/">三亚房产网</a><a target="_blank" href="https://lf.lianjia.com/">廊坊房产网</a><a target="_blank" href="https://hf.lianjia.com/">合肥房产网</a><a target="_blank" href="https://km.lianjia.com/">昆明房产网</a><a target="_blank" href="https://zz.lianjia.com/">郑州房产网</a><a target="_blank" href="https://quanzhou.lianjia.com/">泉州房产网</a><a target="_blank" href="https://zj.lianjia.com/">镇江房产网</a><a target="_blank" href="https://qy.lianjia.com/">清远房产网</a><a target="_blank" href="https://sx.lianjia.com/">绍兴房产网</a><a target="_blank" href="https://weihai.lianjia.com/">威海房产网</a><a target="_blank" href="https://zhangzhou.lianjia.com/">漳州房产网</a><a target="_blank" href="https://cc.lianjia.com/">长春房产网</a><a target="_blank" href="https://gy.lianjia.com/">贵阳房产网</a><a target="_blank" href="https://hhht.lianjia.com/">呼和浩特房产网</a><a target="_blank" href="https://changde.lianjia.com/">常德房产网</a><a target="_blank" href="https://sr.lianjia.com/">上饶房产网</a><a target="_blank" href="https://fz.lianjia.com/">福州房产网</a><a target="_blank" href="https://zhuzhou.lianjia.com/">株洲房产网</a><a target="_blank" href="https://yinchuan.lianjia.com/">银川房产网</a><a target="_blank" href="https://bh.lianjia.com/">北海房产网</a><a target="_blank" href="https://xianyang.lianjia.com/">咸阳房产网</a><a target="_blank" href="https://ha.lianjia.com/">淮安房产网</a><a target="_blank" href="https://mianyang.lianjia.com/">绵阳房产网</a><a target="_blank" href="https://dazhou.lianjia.com/">达州房产网</a><a target="_blank" href="https://xinxiang.lianjia.com/">新乡房产网</a><a target="_blank" href="https://nanchong.lianjia.com/">南充房产网</a><a target="_blank" href="https://luoyang.lianjia.com/">洛阳房产网</a><a target="_blank" href="https://zhanjiang.lianjia.com/">湛江房产网</a><a target="_blank" href="https://nc.lianjia.com/">南昌房产网</a><a target="_blank" href="https://huangshi.lianjia.com/">黄石房产网</a><a target="_blank" href="https://xy.lianjia.com/">襄阳房产网</a><a target="_blank" href="https://zb.lianjia.com/">淄博房产网</a><a target="_blank" href="https://kf.lianjia.com/">开封房产网</a><a target="_blank" href="https://yichang.lianjia.com/">宜昌房产网</a><a target="_blank" href="https://nb.lianjia.com/">宁波房产网</a><a target="_blank" href="https://xc.lianjia.com/">许昌房产网</a><a target="_blank" href="https://hrb.lianjia.com/">哈尔滨房产网</a><a target="_blank" href="https://changzhou.lianjia.com/">常州房产网</a><a target="_blank" href="https://jiangmen.lianjia.com/">江门房产网</a><a target="_blank" href="https://lz.lianjia.com/">兰州房产网</a><a target="_blank" href="https://liuzhou.lianjia.com/">柳州房产网</a><a target="_blank" href="https://mas.lianjia.com/">马鞍山房产网</a><a target="_blank" href="https://dd.lianjia.com/">丹东房产网</a><a target="_blank" href="https://gl.lianjia.com/">桂林房产网</a><a target="_blank" href="https://huzhou.lianjia.com/">湖州房产网</a><a target="_blank" href="https://yc.lianjia.com/">盐城房产网</a><a target="_blank" href="https://taizhou.lianjia.com/">台州房产网</a><a target="_blank" href="https://hanzhong.lianjia.com/">汉中房产网</a><a target="_blank" href="https://liangshan.lianjia.com/">凉山房产网</a><a target="_blank" href="https://jh.lianjia.com/">金华房产网</a><a target="_blank" href="https://nn.lianjia.com/">南宁房产网</a><a target="_blank" href="https://wuhu.lianjia.com/">芜湖房产网</a><a target="_blank" href="https://jl.lianjia.com/">吉林房产网</a><a target="_blank" href="https://aq.lianjia.com/">安庆房产网</a><a target="_blank" href="https://ganzhou.lianjia.com/">赣州房产网</a><a target="_blank" href="https://baoji.lianjia.com/">宝鸡房产网</a><a target="_blank" href="https://jian.lianjia.com/">吉安房产网</a></dd></div><div><dd><a target="_blank" href="https://news.lianjia.com/">房产资讯</a><a target="_blank" href="https://news.lianjia.com/bj/">北京房产资讯</a><a target="_blank" href="https://news.lianjia.com/bj/baike/">北京房产百科</a><a target="_blank" href="https://bj.lianjia.com/wenda/">北京房产知识</a><a target="_blank" href="https://news.lianjia.com/sh/">上海房产资讯</a><a target="_blank" href="https://news.lianjia.com/sh/baike/">上海房产百科</a><a target="_blank" href="https://sh.lianjia.com/wenda/">上海房产知识</a><a target="_blank" href="https://news.lianjia.com/gz/">广州房产资讯</a><a target="_blank" href="https://news.lianjia.com/gz/baike/">广州房产百科</a><a target="_blank" href="https://gz.lianjia.com/wenda/">广州房产知识</a><a target="_blank" href="https://news.lianjia.com/sz/">深圳房产资讯</a><a target="_blank" href="https://news.lianjia.com/sz/baike/">深圳房产百科</a><a target="_blank" href="https://sz.lianjia.com/wenda/">深圳房产知识</a><a target="_blank" href="https://news.lianjia.com/tj/">天津房产资讯</a><a target="_blank" href="https://news.lianjia.com/tj/baike/">天津房产百科</a><a target="_blank" href="https://tj.lianjia.com/wenda/">天津房产知识</a><a target="_blank" href="https://news.lianjia.com/cd/">成都房产资讯</a><a target="_blank" href="https://news.lianjia.com/cd/baike/">成都房产百科</a><a target="_blank" href="https://cd.lianjia.com/wenda/">成都房产知识</a><a target="_blank" href="https://news.lianjia.com/nj/">南京房产资讯</a><a target="_blank" href="https://news.lianjia.com/nj/baike/">南京房产百科</a><a target="_blank" href="https://nj.lianjia.com/wenda/">南京房产知识</a><a target="_blank" href="https://news.lianjia.com/hz/">杭州房产资讯</a><a target="_blank" href="https://news.lianjia.com/hz/baike/">杭州房产百科</a><a target="_blank" href="https://hz.lianjia.com/wenda/">杭州房产知识</a><a target="_blank" href="https://news.lianjia.com/qd/">青岛房产资讯</a><a target="_blank" href="https://news.lianjia.com/qd/baike/">青岛房产百科</a><a target="_blank" href="https://qd.lianjia.com/wenda/">青岛房产知识</a><a target="_blank" href="https://news.lianjia.com/dl/">大连房产资讯</a><a target="_blank" href="https://news.lianjia.com/dl/baike/">大连房产百科</a><a target="_blank" href="https://dl.lianjia.com/wenda/">大连房产知识</a><a target="_blank" href="https://news.lianjia.com/su/">苏州房产资讯</a><a target="_blank" href="https://news.lianjia.com/su/baike/">苏州房产百科</a><a target="_blank" href="https://su.lianjia.com/wenda/">苏州房产知识</a><a target="_blank" href="https://news.lianjia.com/xm/">厦门房产资讯</a><a target="_blank" href="https://news.lianjia.com/xm/baike/">厦门房产百科</a><a target="_blank" href="https://news.lianjia.com/wh/">武汉房产资讯</a><a target="_blank" href="https://news.lianjia.com/wh/baike/">武汉房产百科</a><a target="_blank" href="https://news.lianjia.com/cq/">重庆房产资讯</a><a target="_blank" href="https://news.lianjia.com/cq/baike/">重庆房产百科</a><a target="_blank" href="https://cq.lianjia.com/wenda/">重庆房产知识</a><a target="_blank" href="https://news.lianjia.com/cs/">长沙房产资讯</a><a target="_blank" href="https://news.lianjia.com/cs/baike/">长沙房产百科</a><a target="_blank" href="https://cs.lianjia.com/wenda/">长沙房产知识</a><a target="_blank" href="https://news.lianjia.com/jn/">济南房产资讯</a><a target="_blank" href="https://news.lianjia.com/jn/baike/">济南房产百科</a><a target="_blank" href="https://jn.lianjia.com/wenda/">济南房产知识</a><a target="_blank" href="https://news.lianjia.com/fs/">佛山房产资讯</a><a target="_blank" href="https://news.lianjia.com/fs/baike/">佛山房产百科</a><a target="_blank" href="https://fs.lianjia.com/wenda/">佛山房产知识</a><a target="_blank" href="https://news.lianjia.com/dg/">东莞房产资讯</a><a target="_blank" href="https://news.lianjia.com/dg/baike/">东莞房产百科</a><a target="_blank" href="https://dg.lianjia.com/wenda/">东莞房产知识</a><a target="_blank" href="https://news.lianjia.com/xa/">西安房产资讯</a><a target="_blank" href="https://news.lianjia.com/xa/baike/">西安房产百科</a><a target="_blank" href="https://xa.lianjia.com/wenda/">西安房产知识</a><a target="_blank" href="https://news.lianjia.com/sjz/">石家庄房产资讯</a><a target="_blank" href="https://news.lianjia.com/sjz/baike/">石家庄房产百科</a><a target="_blank" href="https://sjz.lianjia.com/wenda/">石家庄房产知识</a><a target="_blank" href="https://news.lianjia.com/yt/">烟台房产资讯</a><a target="_blank" href="https://news.lianjia.com/yt/baike/">烟台房产百科</a><a target="_blank" href="https://news.lianjia.com/sy/">沈阳房产资讯</a><a target="_blank" href="https://news.lianjia.com/sy/baike/">沈阳房产百科</a><a target="_blank" href="https://sy.lianjia.com/wenda/">沈阳房产知识</a><a target="_blank" href="https://news.lianjia.com/hf/">合肥房产资讯</a><a target="_blank" href="https://news.lianjia.com/hf/baike/">合肥房产百科</a><a target="_blank" href="https://hf.lianjia.com/wenda/">合肥房产知识</a><a target="_blank" href="https://news.lianjia.com/zz/">郑州房产资讯</a><a target="_blank" href="https://news.lianjia.com/zz/baike/">郑州房产百科</a></dd></div><div><dd><a target="_blank" href="https://sh.lianjia.com/ershoufang/shanghaizhoubian/">上海周边二手房</a><a target="_blank" href="https://sh.lianjia.com/ershoufang/jiading/">嘉定二手房</a><a target="_blank" href="https://sh.lianjia.com/ershoufang/fengxian/">奉贤二手房</a><a target="_blank" href="https://sh.lianjia.com/ershoufang/baoshan/">宝山二手房</a><a target="_blank" href="https://sh.lianjia.com/ershoufang/chongming/">崇明二手房</a><a target="_blank" href="https://sh.lianjia.com/ershoufang/xuhui/">徐汇二手房</a><a target="_blank" href="https://sh.lianjia.com/ershoufang/putuo/">普陀二手房</a><a target="_blank" href="https://sh.lianjia.com/ershoufang/yangpu/">杨浦二手房</a><a target="_blank" href="https://sh.lianjia.com/ershoufang/songjiang/">松江二手房</a><a target="_blank" href="https://sh.lianjia.com/ershoufang/pudong/">浦东二手房</a><a target="_blank" href="https://sh.lianjia.com/ershoufang/haiwai/">海外二手房</a><a target="_blank" href="https://sh.lianjia.com/ershoufang/hongkou/">虹口二手房</a><a target="_blank" href="https://sh.lianjia.com/ershoufang/jinshan/">金山二手房</a><a target="_blank" href="https://sh.lianjia.com/ershoufang/changning/">长宁二手房</a><a target="_blank" href="https://sh.lianjia.com/ershoufang/minhang/">闵行二手房</a><a target="_blank" href="https://sh.lianjia.com/ershoufang/zhabei/">闸北二手房</a><a target="_blank" href="https://sh.lianjia.com/ershoufang/qingpu/">青浦二手房</a><a target="_blank" href="https://sh.lianjia.com/ershoufang/jingan/">静安二手房</a><a target="_blank" href="https://sh.lianjia.com/ershoufang/huangpu/">黄浦二手房</a></dd></div><div><dd><a target="_blank" href="https://sh.lianjia.com/zufang/shanghaizhoubian/">上海周边租房</a><a target="_blank" href="https://sh.lianjia.com/zufang/jiading/">嘉定租房</a><a target="_blank" href="https://sh.lianjia.com/zufang/fengxian/">奉贤租房</a><a target="_blank" href="https://sh.lianjia.com/zufang/baoshan/">宝山租房</a><a target="_blank" href="https://sh.lianjia.com/zufang/chongming/">崇明租房</a><a target="_blank" href="https://sh.lianjia.com/zufang/xuhui/">徐汇租房</a><a target="_blank" href="https://sh.lianjia.com/zufang/putuo/">普陀租房</a><a target="_blank" href="https://sh.lianjia.com/zufang/yangpu/">杨浦租房</a><a target="_blank" href="https://sh.lianjia.com/zufang/songjiang/">松江租房</a><a target="_blank" href="https://sh.lianjia.com/zufang/pudong/">浦东租房</a><a target="_blank" href="https://sh.lianjia.com/zufang/haiwai/">海外租房</a><a target="_blank" href="https://sh.lianjia.com/zufang/hongkou/">虹口租房</a><a target="_blank" href="https://sh.lianjia.com/zufang/jinshan/">金山租房</a><a target="_blank" href="https://sh.lianjia.com/zufang/changning/">长宁租房</a><a target="_blank" href="https://sh.lianjia.com/zufang/minhang/">闵行租房</a><a target="_blank" href="https://sh.lianjia.com/zufang/zhabei/">闸北租房</a><a target="_blank" href="https://sh.lianjia.com/zufang/qingpu/">青浦租房</a><a target="_blank" href="https://sh.lianjia.com/zufang/jingan/">静安租房</a><a target="_blank" href="https://sh.lianjia.com/zufang/huangpu/">黄浦租房</a></dd></div><div><dd><a target="_blank" href="https://sh.lianjia.com/xiaoqu/shanghaizhoubian/">上海周边小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/jiading/">嘉定小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/fengxian/">奉贤小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/baoshan/">宝山小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/chongming/">崇明小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/xuhui/">徐汇小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/putuo/">普陀小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/yangpu/">杨浦小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/songjiang/">松江小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/pudong/">浦东小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/haiwai/">海外小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/hongkou/">虹口小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/jinshan/">金山小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/changning/">长宁小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/minhang/">闵行小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/zhabei/">闸北小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/qingpu/">青浦小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/jingan/">静安小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/huangpu/">黄浦小区</a></dd></div><div><dd><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000002603/">控江路1039弄</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000015724/">中天碧云</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000017775/">田林新苑</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000015110/">创智坊(公寓)</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000009836/">恒阳花苑</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000002571/">延吉东路131弄</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000010239/">锦绣满堂花园</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000015370/">东泉小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000018178/">日月星辰</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000011266/">逸仙华庭</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000015518/">菱翔苑</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000017850/">文化名园</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000015732/">君临天下(别墅)</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000011327/">梅陇六村</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000015837/">德州七村</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000001418/">长泰东郊御园(公寓)</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000008108/">曙光南桥小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000013999/">龙南五村</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000016955/">强生古北花园</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000016168/">王家堂小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000017710/">西班牙名园</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000000013/">梦丹苑</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000016932/">舒乐小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5010482933837522/">海上郡</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000017788/">南泉苑</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000016317/">甘泉一村</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000012078/">朗诗绿色街区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000004948/">瑞阳苑</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000001729/">凌兆新村(凌兆路379弄)</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000017432/">皇朝新城</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000014131/">东陆新村七街坊</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000003672/">静安新城七区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011102207585/">玉兰香苑(四期)</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000010976/">环城新村</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000017264/">海天花园(别墅)</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000016332/">沁风雅泾</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000014851/">星云苑</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000014972/">平阳绿家园</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000008851/">金硕河畔景园东区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000005191/">西郊英园</a></dd></div><div><dd><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b1001/">房价行情</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b1002/">购房建议</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b1003/">购房资质</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b1004/">买房风险</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b1005/">二手房</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b1006/">新房</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b1007/">海外买房</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b2001/">税费计算</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b2002/">认购签约</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b2003/">资金监管</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b2004/">过户流程</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b2005/">入住交接</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b3001/">房屋估价</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b3002/">卖房流程</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b3003/">出售方案</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b3004/">业主风险</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b3005/">卖旧买新</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b5001/">贷款利率</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b5002/">首付月供</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b5003/">贷款流程</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b5004/">住房公积金</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b5005/">商业贷款</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b5006/">融资借款</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b5007/">金融方案</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b6001/">房产政策</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b6002/">法律纠纷</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b6003/">保障住房</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b6004/">其他</a></dd></div><div><dd><a target="_blank" href="https://news.lianjia.com/sh/baike/0033/">房产政策</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0035/">购房建议</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0036/">购房资质</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0037/">房屋贷款</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0039/">保障住房</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0040/">产权/变更</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0041/">法律纠纷</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0042/">房屋装修</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0044/">准备买房</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0045/">看房/选房</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0046/">签约/定房</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0047/">全款/贷款</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0048/">缴税/过户</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0049/">入住/交接</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0050/">买房风险</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0051/">准备买房</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0052/">看房/选房</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0053/">认购新房</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0054/">签约/定房</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0055/">全款/贷款</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0056/">收房/验房</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0057/">装修/入住</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0058/">退房/维权</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0059/">各国概况</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0060/">计划买房</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0061/">签约定房</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0062/">银行贷款</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0063/">交易过户</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0064/">房屋代理</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0066/">准备卖房</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0067/">产权核验</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0068/">收定金/签约</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0069/">分步收款</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0070/">缴税/过户</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0071/">交房须知</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0072/">卖房风险</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0073/">准备换房</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0074/">换房方案</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0075/">卖旧/买新</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0077/">缴税/过户</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0078/">交房/收房</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0079/">换房风险</a><a target="_blank" href="https://news.lianjia.com/sh/baike/00779/">找房看房</a><a target="_blank" href="https://news.lianjia.com/sh/baike/00780/">签约付款</a><a target="_blank" href="https://news.lianjia.com/sh/baike/00781/">物业交割</a><a target="_blank" href="https://news.lianjia.com/sh/baike/00782/">租房纠纷</a><a target="_blank" href="https://news.lianjia.com/sh/baike/00783/">我是房东</a></dd></div></div></div><div class="clear"></div></div><div class="bottom"><div class="copyright fl">链家网（北京）科技有限公司 | 网络经营许可证 京ICP备16057509号-2 | © Copyright©2010-2018 链家网Lianjia.com版权所有</div><div style="width:300px;color: #888c8e;font-size: 12px;line-height: 20px;"><a target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010802024019" style="display:inline-block;text-decoration:none;height:20px;line-height:20px;"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/home/beian.png?_v=20181206222953"" style="float:left;"><p style="float:left;height:20px;line-height:20px;margin: 0px 0px 0px 5px;color: #888c8e;">京公网安备 11010802024019号</p></a></div></div></div></div>

<script src="https://s1.ljcdn.com/feroot/pc/asset/base/fe.js?_v=20181206222953"></script><script src="https://s1.ljcdn.com/feroot/pc/asset/common/common.js?_v=20181206222953"></script><div style="display:none"><script src="https://s1.ljcdn.com/feroot/dep/ljanalytics.js?_v=20181206222953"></script></div><div id="only" data-city="sh" data-page="zufang_search"></div>

<script>var path = 'https://s1.ljcdn.com/feroot/pc/asset?_v=20181206222953'.split("?");require.config({baseUrl: path[0],paths: {'echarts' : '../../dep/echarts-1.4.1/build/echarts','echarts/chart/bar' : '../../dep/echarts-1.4.1/build/echarts','echarts/chart/line' : '../../dep/echarts-1.4.1/build/echarts','echarts/chart/pie' : '../../dep/echarts-1.4.1/build/echarts','echarts3' : '../../dep/echarts3/echarts3','common': 'common','jquery-ui': '../../dep/jquery-ui/jquery-ui.min','zeroclipboard': '../../dep/zeroclipboard-2.2.0/ZeroClipboard'},urlArgs:  path[1]});var feData = {"cityName": "北京","getFavHouseUrl":       "/api/gethousefav","setFavHouseUrl":       "/api/sethousefav","getLastSearch":        "/api/getlastsearch","getCommunityHistory":  "/api/getcommunityhistory","verifyHouse":          "/api/verifyHouse","getUser":              "/api/getUser","verifyCode":           "/verifycode/getVerifyCode","complaint":            "/api/complaint","getDecoration":        "/api/getDecoration","trendData" :           "/site/getpicinfo"}</script>
<script type="text/javascript">
require(['list/main'], function (main) {
    main.init({
        feRoot: 'https://s1.ljcdn.com/feroot/?_v=20181206222953',
        cityName: '上海',
        mapak: 'C106a48023d9606dcdad761cbc070095',
        mapDomId: 'map-box',
        reqData: {
            cityId: '310000'
        },

        common: feData,
        price: '/zufang/pudong/brp{min}erp{max}/',
        area: '/zufang/pudong/rba{min}rea{max}/',

        dingdingBox: ''
    });
});
require(['common/backtopV3'], function (main) {
  main({
    ucid: '',
    uuid: 'a7ad8b25-df36-4b00-8ab6-ac1f0fe123df',
    loadingImg: 'https://s1.ljcdn.com/feroot/pc/asset/ershoufang/sellDetail/img/loading.gif?_v=20181206222953',
    qrImg: '//ajax.api.lianjia.com/qr/getDownloadQr'
  });
});
require(['zufang/main'], function (main) {
    main.init({
        feRoot: 'https://s1.ljcdn.com/feroot/?_v=20181206222953',
        cityName: '上海',
        mapak: 'C106a48023d9606dcdad761cbc070095',
        mapDomId: 'map-box',
        reqData: {
            cityId: '310000'
        },

        common: feData,
        price: '/zufang/pudong/brp{min}erp{max}/',
        area: '/zufang/pudong/rba{min}rea{max}/',

        dingdingBox: ''
    });
});

require(['common/initTalk'], function(initTalk) {
  initTalk()
});

;;+function() {
    LjUserTrack.send({
        "ljweb_id": "10001",
        "ljweb_mod": "zufang_list_view",
        "ljweb_bl": "spk_0",
        "ljweb_el": "6909",
        "ljweb_value": "",
    });
    var isHaveAgentCard = false
    var clickLinkBl = 'list';
    var resblockId = '';
    if(isHaveAgentCard){
      clickLinkBl = 'list_have_sem_card';
      resblockId = ""
    }
    $(document.body).on("click", "[data-el='zufang']", function() {
        var $m = $(this);
        LjUserTrack.send({
            "ljweb_id": "10002",
            "ljweb_mod": "zufang_list_list",
            "ljweb_bl": clickLinkBl,
            "ljweb_el": "zufang",
            "ljweb_index": $m.attr("data-log_index"),
            "ljweb_url": $m.attr("href"),
            "ljweb_value":resblockId,
            "ljweb_is_focus" : $m.attr("data-is_focus") || 0,
            "ljweb_house_code" : $m.attr('data-housecode')
        });

    });

    $(document.body).on("mousedown", "#suggest-cont [data-log_value]", function() {
        var $m = $(this);
        var channel = $m.attr('data-log_channel');
        LjUserTrack.send({
            "ljweb_id": 10003,
            "ljweb_mod": channel+"_list_search",
            "ljweb_bl": "search",
            "ljweb_el": $m.attr("data-log_value"),
            "ljweb_index": $m.attr("data-log_index"),
            "ljweb_value": $.trim($("#keyword-box").val()),
            "ljweb_url": $m.attr("data-log_url")
        });
    });
    $(document.body).on("mousedown", ".hot-sug[data-bl='sug'] [data-log_value]", function() {
        var $m = $(this);
        var channel = $m.attr('data-log_channel');
        LjUserTrack.send({
            "ljweb_id": 10004,
            "ljweb_mod": channel+"_list_search",
            "ljweb_bl": "search",
            "ljweb_el": $m.attr("data-log_value"),
            "ljweb_index": $m.attr("data-log_index"),
            "ljweb_value": $.trim($("#keyword-box").val()),
            "ljweb_url": $m.attr("href")
        });
    });
    $("#searchForm").on("submit", function() {
        var $m = $(this);
        var channel = $m.find("[data-bl=switch][actdata]").attr('actdata') || 'zufang';
        LjUserTrack.send({
            "ljweb_id": "10008",
            "ljweb_mod": channel+"_list_search",
            "ljweb_bl": "search",
            "ljweb_value": $.trim($("#keyword-box").val())
        });
    });

}();
</script>

<!-- ｛include file='../common/toolbar.tpl'} -->
<script>require(['common/suggestion'], function (suggestion) {window.defaultSuggest = suggestion.init({requestOptions: {cityId: '310000',cityName: '上海'},url: '/api/headerSearch?channel=zufang&q=',main: '#keyword-box',appendTo: '#suggest-cont',redirect: true});});</script><div class="loninContaner"><div class="overlay_bg"></div><div class="panel_login animated" id="dialog"><div class="panel_info"><i class="close_login" >&times</i><div class="panel_tab"><div class="title"><div class="fl">账号密码登录</div></div><div class="clear"></div><div id="con_login_user"><form action="" method="post"><ul><li class="item border-t userName"><input type="text" class="the_input topSpecial users" placeholder="请输入手机号"  maxlength="11" /></li><li class="item border-b pwd"><input type="password" class="the_input password" maxlength="20" placeholder="请输入登录密码"/><em class="password-view"></em></li><li class="item checkVerimg" style="display:none;"><input type="text" class="the_input ver-img" maxlength="6"  placeholder="请输入验证码"/><img class="verImg"></li><li class="item drag" style="display:none;"><div id="drag"></div></li><li class="show-error"><dd>用户名或密码错误</dd></li><li class="li_01"><label class="checkbox-btn"><span class="active"><input type="checkbox" name="remember" value="1" class="mind-login" checked/></span>7天内免登录</label><a href="javascript:;" rel="nofollow" class="toforget">忘记密码</a></li><li class="li_btn"><a class="login-user-btn"  />登录</a></li><li class="footer-link"><a href="javascript:;" rel="nofollow" class="totellogin">手机快捷登录</a></li></ul></form></div><div id="con_login_agent" class="undis"><form action="" method="post"><ul><li class="item"><dd></dd><input type="text" class="the_input users" placeholder="输入经纪人ID号码" /></li><li class="item"><input type="password" class="the_input password"  placeholder="登录密码"/></li><li class="li_01"><label class="checkbox-btn"><span class="active"><input type="checkbox" name="remember" value="1" class="mind-login" checked/></span>7天内免登录</label><a href="https://passport.lianjia.com/register/resources/lianjia/forget.html?service=http://bj.lianjia.com/" rel="nofollow">忘记密码</a></li><li><input class="login-agent-btn" value="立即登录"/></li></ul></form></div></div></div><div class="registered"></div></div><div class="panel_login animated" id="dialog_tel"><div class="panel_info"><i class="close_login">&times</i><div class="panel_tab"><div class="title"><div class="fl">手机快捷登录</div><div class="register_text_tel">别担心，无账号自动注册不会导致手机号被泄露</div></div><div class="clear"></div><div id="con_login_user_tel"><form action="" method="post"><ul><li class="item border-t userName"><input type="text" class="the_input topSpecial users_tel" maxlength="11" placeholder="请输入手机号" /></li><!-- <li class="item pwd"><input type="password" class="the_input password_tel"  placeholder="请输入短信验证码"/></li> --><li class="item checkVerimg" style=""><input type="text" class="the_input ver-img" maxlength="6"  placeholder="请输入验证码"/><img class="verImg"></li><li class="item border-b Verify"><input type="text" class="the_input verifycode" maxlength="6"  placeholder="请输入短信验证码"/><a class="send_verify_code" id="send_verify_code_tel" href="javascript:;" rel="nofollow"><em>获取验证码</em></a></li><li class="send_verify_code_s" id="send_verify_code_tel_s" href="javascript:;" rel="nofollow"><em>没有收到验证码？</em><a class="voice_a">发送语音验证码</a></li><li class="show-error"><dd>用户名或密码错误</dd></li><li class="li_01"><label class="checkbox-btn"><span class="active"><input type="checkbox" name="remember" value="1" class="mind-login" checked/></span>7天内免登录</label></li><li class="li_btn"><a class="login-user-tel-btn"  />登录</a></li><li class="footer-link"><a href="javascript:;" rel="nofollow" class="tologin">账号密码登录</a></li></ul></form></div></div></div><div class="registered"></div></div><div class="panel_login animated" id="dialog_reg"><div class="panel_info"><i class="close_login">&times</i><div class="panel_tab"><div class="title"><div class="fl">手机号码注册</div><label class="fr register_text">已有账号？<a href="javascript:;" rel="nofollow" class="tologin">去登录</a></label></div><div class="clear"></div><div id="con_login_user_reg"><form action="" method="post"><ul><li class="item border-t userName"><input type="text" class="the_input topSpecial users_reg"  maxlength="11" placeholder="请输入手机号" /></li><li class="item checkVerimg" style=""><input type="text" class="the_input ver-img" maxlength="6"  placeholder="请输入验证码"/><img class="verImg"></li><li class="item border-c Verify"><input type="text" class="the_input verifycode" maxlength="6"  placeholder="请输入短信验证码"/><a class="send_verify_code" id="send_verify_code_reg" href="javascript:;" rel="nofollow"><em>获取验证码</em></a></li><li class="item border-b pwd"><input type="password" class="the_input password_reg" maxlength="20"  placeholder="请输入密码（最少8位，数字+字母）"/><em class="password-view"></em></li><li class="send_verify_code_s" id="send_verify_code_reg_s" href="javascript:;" rel="nofollow"><em>没有收到验证码？</em><a class="voice_a">发送语音验证码</a></li><li class="show-error"><dd>用户名或密码错误</dd></li><li class="li_01"><label class="checkbox-btn"><span class="active"><input type="checkbox" name="read" value="1" class="read-protocol" checked/></span>我已阅读并同意</label><a class="toprotocol" href="//www.lianjia.com/zhuanti/protocol" target="_blank" >《链家用户使用协议》</a></li><li class="li_btn"><a class="register-user-btn"  />注册</a></li></ul></form></div></div></div><div class="registered"></div></div><div class="panel_login animated" id="dialog_forget"><div class="panel_info"><i class="close_login">&times</i><div class="panel_tab"><div class="title"><div class="fl">找回密码</div></div><div class="clear"></div><div id="con_forget_user_tel" class="con_forget_user_tel"><form action="" method="post"><ul><li class="item border-t userName"><input type="text" class="the_input topSpecial user_forget_phone" placeholder="请输入手机号"  maxlength="11" /></li><li class="item checkVerimg" style=""><input type="text" class="the_input ver-img" maxlength="6"  placeholder="请输入验证码"/><img class="verImg"></li><li class="item border-b Verify"><input type="text" class="the_input verifycode" maxlength="6"  placeholder="请输入短信验证码"/><a class="send_verify_code" id="send_verify_code_forget" href="javascript:;" rel="nofollow"><em>获取验证码</em></a></li><li class="item border-t pwd" style="margin-top:-1px;"><input type="password" class="the_input password_reg" maxlength="20"  placeholder="请输入密码（最少8位，数字+字母）"/><em class="password-view"></em></li><li class="send_verify_code_s" id="send_verify_code_forget_s"><em>没有收到验证码？</em><a class="voice_a">发送语音验证码</a></li><li class="show-error"><dd>用户名或密码错误</dd></li><li class="li_btn"><a class="user-forget"  />修改密码</a></li></ul></form></div><div id="con_forget_user_pw" class="con_forget_user_pw"><form action="" method="post"><ul><li class="item border-t pwd"><input type="password" class="the_input password_reg" maxlength="20"  placeholder="请输入密码（最少8位，数字+字母）"/><em class="password-view"></em></li><li class="show-error"><dd>用户名或密码错误</dd></li><li class="li_btn"><a class="modify-user-pswd"  />修改密码</a></li></ul></form></div></div></div><div class="registered"></div></div></div>
<!-- LianjiaIM Style --><link property='stylesheet' rel="stylesheet" href="https://s1.ljcdn.com/feroot/pc/asset/lianjiaIM/css/lianjiaim.css?_v=20181206222953"/><script src="//s1.ljcdn.com/web-im-sdk/static/1.1/lianjiaim1.1.min.js?v=20181211"></script><!-- <script src="//s1-ljcdn.test.lianjia.com:8400/web-im-sdk/static/1.1/lianjiaim1.1.min.js?v=20181211"></script> --><script>(function() {var imConf = {"ajaxroot":"\/\/ajax.api.lianjia.com\/","imAppid":"LIANJIA_WEB_20160624","imAppkey":"6dfdcee27d78b1107fceeca55d80b7bd"};let login = require('common/login');$.listener.on('userInfo', function (data) {if (data.code === 1) {data.ucid = '';}window.LJIM = new LianjiaIM({appid: imConf.imAppid,appkey: imConf.imAppkey,login: login.openLoginDialog,is_ljbb: true,userData: data,downAppUrl: '//www.lianjia.com/client/',appDesc: '立即下载链家APP，随时随地聊~',staticRoot: 'https://s1.ljcdn.com/feroot/?_v=20181206222953'})});})();</script><script type="text/javascript">var advert = 'https://s1.ljcdn.com/feroot/pc/asset/common/advert.js?_v=20181206222953';
    $.listener.on('userInfo', function (data) {
      window.loginData = data;
    });
    var mvl = document.createElement('script');
    mvl.type = 'text/javascript';
    mvl.async = true;
    mvl.src = advert;
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(mvl, s);
  </script><script type="text/javascript">(function(){var canonicalURL, curProtocol;var x=document.getElementsByTagName("link");if(x.length > 0){for (i=0;i<x.length;i++){if(x[i].rel.toLowerCase() == 'canonical' && x[i].href){canonicalURL=x[i].href;}}}if (!canonicalURL){curProtocol = window.location.protocol.split(':')[0];}else{curProtocol = canonicalURL.split(':')[0];}if (!canonicalURL) canonicalURL = window.location.href;(function() {var e = /([http|https]:\/\/[a-zA-Z0-9\_\.]+\.baidu\.com)/gi,r = canonicalURL,t = document.referrer;if (!e.test(r)) {var n = (String(curProtocol).toLowerCase() === 'https') ? "https://sp0.baidu.com/9_Q4simg2RQJ8t7jm9iCKT-xh_/s.gif" : "//api.share.baidu.com/s.gif";t ? (n += "?r=" + encodeURIComponent(document.referrer), r && (n += "&l=" + r)) : r && (n += "?l=" + r);var i = new Image;i.src = n}})(window);})();</script><!--cookie mapping--><img src='#' alt="cookie_mapping_url" style="display: none;"></body></html>

"""
response = etree.HTML(wb_data)
for quote in response.xpath('//div[@class="info-panel"]'):
    print getList(quote.xpath('.//h2/a/text()'))
    print getList(quote.xpath('.//h2/a/@href'))

    print getList(quote.xpath('.//div[@class="col-1"]/div[@class="where"]/a/@href'))
    print getList(quote.xpath('.//div[@class="col-1"]/div[@class="where"]/a/span[@class="region"]/text()'))
    print getList(quote.xpath('.//div[@class="col-1"]/div[@class="where"]/span[@class="zone"]/span/text()'))
    print getList(quote.xpath('.//div[@class="col-1"]/div[@class="where"]/span[@class="meters"]/text()'))
    print getList(quote.xpath('.//div[@class="col-1"]/div[@class="where"]/span[not(@class)]/text()'))

    # other
    print getList(quote.xpath('.//div[@class="col-1"]/div[@class="other"]/div[@class="con"]/a/@href'))
    print quote.xpath('.//div[@class="col-1"]/div[@class="other"]/div[@class="con"]')[0].xpath('string(.)')[0].strip()
    # chanquan
    print getList(quote.xpath('.//div[@class="fang-subway-ex"]/span/text()'))

    # col-3

    print getList(quote.xpath('.//div[@class="col-3"]/div[@class="price"]/span[@class="num"]/text()'))
    print getList(quote.xpath('.//div[@class="col-3"]/div[@class="price-pre"]/text()'))

    # col -

    print getList(quote.xpath('.//div[@class="col-2"]/div[@class="square"]/div[not(@class)]/span[@class="num"]/text()')) + "人看房"

    print "***************************************************"


