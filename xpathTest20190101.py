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
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><meta http-equiv="X-UA-Compatible" content="IE=edge" /><meta http-equiv="Cache-Control" content="no-transform" /><meta http-equiv="Cache-Control" content="no-siteapp" /><meta http-equiv="Content-language" content="zh-CN" /><meta name="format-detection" content="telephone=no" /><meta name="applicable-device" content="pc"><link rel="alternate" media="only screen and (max-width: 640px)" href="https://m.lianjia.com/sh/ershoufang/rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/" >
<meta name="mobile-agent" content="format=html5;url=https://m.lianjia.com/sh/ershoufang/rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/"><script>
ljConf = {
    city_id: '310000',
    city_abbr: 'sh',
    city_name: '上海',
    channel: 'ershoufang',
    page: 'ershoufang_search',
    pageConfig: {"ajaxroot":"https:\/\/ajax.api.lianjia.com\/","imAppid":"LIANJIA_WEB_20160624","imAppkey":"6dfdcee27d78b1107fceeca55d80b7bd"},
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
<script src="https://s1.ljcdn.com/feroot/pc/asset/common/tingyun-rum.js?_v=2018122819393752"></script><title>上海永泰花苑二手房网|个人房源房屋出售</title>
<meta name="description" content="上海链家网永泰花苑二手房出售频道,为用户买上海二手房的用户提供真实房源及房源、户型、周边配套等信息,并推荐优质永泰花苑二手房房源,购买上海永泰花苑二手房,就选链家网上海站上海二手房出售频道." />
<meta name="keywords" content="上海永泰花苑二手房出售,上海永泰花苑二手房网,永泰花苑二手房上海,上海永泰花苑二手房买卖,上海买永泰花苑二手房" />
<link href="/favicon.ico" type="image/x-icon" rel=icon><link href="/favicon.ico" type="image/x-icon" rel="shortcut icon"><link rel="stylesheet" href="https://s1.ljcdn.com/feroot/pc/asset/common.css?_v=2018122819393752">
<link rel="stylesheet" href="https://s1.ljcdn.com/feroot/pc/asset/ershoufang/sellList/index.css?_v=2018122819393752">
<!--[if lt IE 9]><script type="text/javascript" src="https://s1.ljcdn.com/feroot/dep/common-require/html5.js?_v=2018122819393752"></script><![endif]-->
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
        ljweb_channel: 'ershoufang',
        ljweb_page: 'ershoufang_search',
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

<div class="banner"><div class="container"><ul class="channelList"><li><a href="//www.lianjia.com/">首页</a></li><li  class="selected"><a href="https://sh.lianjia.com/ershoufang/" >二手房</a></li><li  class=""><a href="https://sh.fang.lianjia.com/" >新房</a></li><li  class=""><a href="https://sh.lianjia.com/zufang/" >租房</a></li><li  class=""><a href="https://us.lianjia.com" >海外</a></li><li  class=""><a href="https://shang.lianjia.com/sh" >商业办公</a></li><li  class=""><a href="https://sh.lianjia.com/xiaoqu/" >小区</a></li><li  class=""><a href="https://sh.lianjia.com/jingjiren/" >经纪人</a></li><li  class=""><a href="https://sh.lianjia.com/wenda/" >指南</a><div class="childList"><a href="https://sh.lianjia.com/wenda/" >问答</a><a href="https://news.lianjia.com/sh/baike/" >百科</a></div></li><li  class=""><a href="https://sh.lianjia.com/tool.html" target="_blank">工具</a></li><li  class=""><a href="https://sh.lianjia.com/yezhu/" target="_blank">发布房源</a></li></ul><div class="banner-right"><div class="login" id="userInfoContainer"><i></i><a href="https://upassport.lianjia.com/login?service=https%3A%2F%2Fwww.lianjia.com%2Fuser%2Fchecklogin%3Fredirect%3Dhttps%253A%252F%252Fsh.lianjia.com%252Fershoufang%252Frs%2525E6%2525B0%2525B8%2525E6%2525B3%2525B0%2525E8%25258A%2525B1%2525E8%25258B%252591%252F" id="loginBtn" rel="nofollow">登录</a>/<a href="https://passport.lianjia.com/register/resources/lianjia/register.html?service=https%3A%2F%2Fwww.lianjia.com%2Fuser%2Fchecklogin%3Fredirect%3Dhttps%253A%252F%252Fsh.lianjia.com%252Fershoufang%252Frs%2525E6%2525B0%2525B8%2525E6%2525B3%2525B0%2525E8%25258A%2525B1%2525E8%25258B%252591%252F" id="registerBtn" rel="nofollow">注册</a></div><div class="phone"><i></i><span>热线电话1010-9666</span></div></div></div></div>


<script type="text/template" id="userInfoTpl">
  <i></i>
  <%if(isAgent){%>
    <a id="userNameContainer" href="<%=$.env.fixedUrl('//agent.lianjia.com/')%>"><%=username%></a>
  <%}else{%>
    <a id="userNameContainer" href="<%=$.env.fixedUrl('//user.lianjia.com/')%>" rel="nofollow"><%=username%></a>
  <%}%>
  <span id="tipContainer"></span>
  &nbsp;&nbsp;<a href="<%=logoutUrl%>">退出</a>
  <span id="pushNewsListContainer"></span>
</script>
<script type="text/template" id="pushNewsListTpl">
  <div class="pushNewsList">
    <%for(var i in group_by_type){%>
      <%if(group_by_type[i].unread !== 0 && pushMsgMap.hasOwnProperty(i)){%>
        <a href="<%=pushMsgMap[i].url%>"><%=$.replaceTpl(pushMsgMap[i].text, {unread:group_by_type[i].unread})%></a>
      <%}%>
    <%}%>
  </div>
</script>

<div class="header"><div class="menu"><div class="menuLeft"><a href="/ershoufang/" class="logo"></a><ul class="typeList"><li class="selected"><a href="/ershoufang/"  title="上海在售二手房" >在售</a></li><li ><a href="/chengjiao/"  title="上海成交二手房" >成交</a></li><li ><a href="/xiaoqu/"  title="上海小区二手房" >小区</a></li><li ><a href="/ditu/"  title="上海地图找房二手房" target="_blank">地图找房</a></li></ul></div><div class="app"><a href="//www.lianjia.com/client/" target="_blank"><i></i>下载链家APP<span class="layer-qrcode"><span class="icon-qrcode"><img width="124" height="124" src="//ajax.api.lianjia.com/qr/getDownloadQr?location=menu_app&ljweb_channel_key=ershoufang_search" alt="下载链家app"></span><span class="txt">使用链家APP</span><span class="sub-txt">随时随地查看新上房源</span></span></a></div></div><div class="search"><div class="input" log-mod="search"><form id="searchForm" action='/ershoufang/rs'><input type="text" id="searchInput" value="永泰花苑" autocomplete="off"><div class="inputRightPart"><div class="save" id="savedSearchMsg"><span id="savedSearchCount">0</span>条已保存搜索<span id="savedSearchArrow" class="downArrow"></span></div><button type='submit' class="searchButton" data-bl="search" data-el="search">&nbsp;<i></i>&nbsp;</button></div></form><div class="searchMsg" id="searchMsgContainer"></div></div></div></div>


<script type="text/template" id="hotSearchTpl">
  <div class="searchMsgTitle">
    <span class="searchMsgName">热门搜索</span>
  </div>
  <ul data-bl="sug" data-el="history">
    <%for(var i =0; i < list.length; i++){%>
    <li>
      <a role="addHistory" href="<%=list[i].url%>" data-log_index="<%=i+1%>" data-log_value="<%=list[i].string%>" class="sug--search_item">
        <span class="msgListTitle" role="historyKey"><%=list[i].string%></span>
      </a>
    </li>
    <%}%>
  </ul>
</script>
<script type="text/template" id="searchHistoryTpl">
  <div class="searchMsgTitle">
    <span class="searchMsgName">搜索历史</span>
    <div class="searchMsgTitleRightPart">
      <a href="#" id="clearSearchHistory" class="manage">清除历史记录</a>
    </div>
  </div>
  <ul data-bl="sug" data-el="history">
  <%for(var i = 0; i < list.length; i++){%>
    <li>
      <a href="<%=list[i].url%>" role="addHistory" data-log_index="<%=i+1%>" data-log_value="<%=$.encodeHTML(list[i].name)%>" class="sug--search_item">
        <span class="msgListTitle" role="historyKey"><%=$.encodeHTML(list[i].name)%></span>
        <%if(list[i].newCount) {%>
          <span class="msgListAdd"><%=list[i].newCount%>套新增房源</span>
        <%}%>
      </a>
    </li>
  <%}%>
  </ul>
</script>
<script type="text/template" id="searchSuggestionTpl">
  <div class="searchMsgTitle">
    <span class="searchMsgName">你可能在找</span>
  </div>
  <ul data-bl="sug" data-el="sug">
  <%for(var i = 0;i < list.length;i++){%>
    <li>
      <a href="<%=list[i].url%>" role="addHistory" data-log_index="<%=i+1%>" data-log_value="<%=list[i].title%>">
        <span class="msgListTitle">
          <span role="historyKey"><%=list[i].title%></span>
          <%if(list[i].region){%>
            <span class="msgListArea"><%=list[i].region%></span>
          <%}%>
        </span>
        <%if(type === 'sell'){%>
          <span class="msgListAdd">约<%=list[i].count%>套在售</span>
        <%}else if(type === 'deal'){%>
          <span class="msgListAdd">约<%=list[i].count%>套成交</span>
        <%}%>
      </a>
    </li>
  <%}%>
  </ul>
</script>
<script type="text/template" id="savedSearchTpl">
  <div class="searchMsgTitle">
    <span class="searchMsgName">已保存搜索</span>
    <div class="searchMsgTitleRightPart">
    <%if(totalCount){%>
      <a class="totalNew">查看<%=totalCount%>套新增房源</a>
    <%}%>
      <a href="<%=userCenterUrl%>" class="manage">管理</a>
    </div>
  </div>
  <ul data-bl="sug" data-el="history">
    <%for(var i = 0; i < savedData.length; i++){
      var title = savedData[i].query ? savedData[i].query + '&nbsp;' : '';
      title = title + savedData[i].title.join('&nbsp;');
    %>
      <li>
        <a href="<%=savedData[i].url%>" role="savedSearch" data-log_index="<%=i+1%>" data-log_value="<%=title%>" class="sug--search_item">
          <span class="msgListTitle"><%=title%></span>
          <%if(savedData[i].unread && savedData[i].unread !== 0){%>
          <span class="msgListAdd">新增<%=savedData[i].unread%>套</span>
          <%}%>
        </a>
      </li>
    <%}%>
  </ul>
</script>

<script>
  var hotSearchData = {
    channel:[{"name":"\u4e8c\u624b\u623f","action":"ershoufang","channel":"ershoufang","checked":1,"tipsHot":{"query":[{"string":"\u4e0a\u6d77\u5eb7\u57ce","url":"http:\/\/sh.lianjia.com\/ershoufang\/rs%E4%B8%8A%E6%B5%B7%E5%BA%B7%E5%9F%8E\/"},{"string":"\u6167\u829d\u6e56\u82b1\u56ed","url":"http:\/\/sh.lianjia.com\/ershoufang\/rs%E6%85%A7%E8%8A%9D%E6%B9%96%E8%8A%B1%E5%9B%AD\/"},{"string":"\u5965\u6797\u5339\u514b\u82b1\u56ed","url":"http:\/\/sh.lianjia.com\/ershoufang\/rs%E5%A5%A5%E6%9E%97%E5%8C%B9%E5%85%8B%E8%8A%B1%E5%9B%AD\/"},{"string":"\u4e2d\u8fdc\u4e24\u6e7e\u57ce","url":"http:\/\/sh.lianjia.com\/ershoufang\/rs%E4%B8%AD%E8%BF%9C%E4%B8%A4%E6%B9%BE%E5%9F%8E\/"},{"string":"\u4e1c\u65b9\u66fc\u54c8\u987f","url":"http:\/\/sh.lianjia.com\/ershoufang\/rs%E4%B8%9C%E6%96%B9%E6%9B%BC%E5%93%88%E9%A1%BF\/"},{"string":"\u65b0\u6e56\u660e\u73e0\u57ce","url":"http:\/\/sh.lianjia.com\/ershoufang\/rs%E6%96%B0%E6%B9%96%E6%98%8E%E7%8F%A0%E5%9F%8E\/"},{"string":"\u7ecf\u7eac\u57ce\u5e02\u7eff\u6d32","url":"http:\/\/sh.lianjia.com\/ershoufang\/rs%E7%BB%8F%E7%BA%AC%E5%9F%8E%E5%B8%82%E7%BB%BF%E6%B4%B2\/"},{"string":"\u4fdd\u5229\u897f\u5b50\u6e7e","url":"http:\/\/sh.lianjia.com\/ershoufang\/rs%E4%BF%9D%E5%88%A9%E8%A5%BF%E5%AD%90%E6%B9%BE\/"}],"tips":"\u8bf7\u8f93\u5165\u533a\u57df\u3001\u677f\u5757\u6216\u5c0f\u533a\u540d\u5f00\u59cb\u627e\u623f"}},{"name":"\u5c0f\u533a","action":"xiaoqu","channel":"xiaoqu","checked":0,"tipsHot":{"query":[{"string":"\u5965\u6797\u5339\u514b\u82b1\u56ed","url":"http:\/\/sh.lianjia.com\/xiaoqu\/rs%E5%A5%A5%E6%9E%97%E5%8C%B9%E5%85%8B%E8%8A%B1%E5%9B%AD\/"},{"string":"\u4e16\u8302\u6ee8\u6c5f\u82b1\u56ed","url":"http:\/\/sh.lianjia.com\/xiaoqu\/rs%E4%B8%96%E8%8C%82%E6%BB%A8%E6%B1%9F%E8%8A%B1%E5%9B%AD\/"},{"string":"\u4fdd\u5229\u897f\u5b50\u6e7e","url":"http:\/\/sh.lianjia.com\/xiaoqu\/rs%E4%BF%9D%E5%88%A9%E8%A5%BF%E5%AD%90%E6%B9%BE\/"},{"string":"\u65b0\u9ad8\u82d1","url":"http:\/\/sh.lianjia.com\/xiaoqu\/rs%E6%96%B0%E9%AB%98%E8%8B%91\/"},{"string":"\u4e5d\u57ce\u6e56\u6ee8\u56fd\u9645","url":"http:\/\/sh.lianjia.com\/xiaoqu\/rs%E4%B9%9D%E5%9F%8E%E6%B9%96%E6%BB%A8%E5%9B%BD%E9%99%85\/"},{"string":"\u540c\u6da6\u83f2\u8bd7\u827e\u4f26","url":"http:\/\/sh.lianjia.com\/xiaoqu\/rs%E5%90%8C%E6%B6%A6%E8%8F%B2%E8%AF%97%E8%89%BE%E4%BC%A6\/"},{"string":"\u4ec1\u6052\u6ee8\u6c5f\u56ed","url":"http:\/\/sh.lianjia.com\/xiaoqu\/rs%E4%BB%81%E6%81%92%E6%BB%A8%E6%B1%9F%E5%9B%AD\/"}],"tips":"\u8bf7\u8f93\u5165\u5c0f\u533a\u540d\u5f00\u59cb\u67e5\u627e\u5c0f\u533a"}},{"name":"\u6210\u4ea4","action":"chengjiao","channel":"chengjiao","checked":0,"tipsHot":null},{"name":"\u65b0\u623f","action":"loupan","channel":"xinfang","checked":0,"tipsHot":{"query":[{"string":"\u897f\u73af\u4e2d\u5fc3\u661f\u4fe1\u540d\u90b8","url":"http:\/\/sh.fang.lianjia.com\/loupan\/rs%E8%A5%BF%E7%8E%AF%E4%B8%AD%E5%BF%83%E6%98%9F%E4%BF%A1%E5%90%8D%E9%82%B8\/"},{"string":"\u8def\u52b2\u4f58\u5c71\u9662\u5b50","url":"http:\/\/sh.fang.lianjia.com\/loupan\/rs%E8%B7%AF%E5%8A%B2%E4%BD%98%E5%B1%B1%E9%99%A2%E5%AD%90\/"},{"string":"\u4e2d\u9a8f\u5929\u60a6","url":"http:\/\/sh.fang.lianjia.com\/loupan\/rs%E4%B8%AD%E9%AA%8F%E5%A4%A9%E6%82%A6\/"},{"string":"\u79b9\u6d32\u5e9c","url":"http:\/\/sh.fang.lianjia.com\/loupan\/rs%E7%A6%B9%E6%B4%B2%E5%BA%9C\/"},{"string":"\u81fb\u6c34\u5cb8","url":"http:\/\/sh.fang.lianjia.com\/loupan\/rs%E8%87%BB%E6%B0%B4%E5%B2%B8\/"},{"string":"\u5c1a\u666f\u4e3d\u56ed","url":"http:\/\/sh.fang.lianjia.com\/loupan\/rs%E5%B0%9A%E6%99%AF%E4%B8%BD%E5%9B%AD\/"}],"tips":"\u8bf7\u8f93\u5165\u697c\u76d8\u540d\u79f0\u5f00\u59cb\u627e\u623f"}},{"name":"\u79df\u623f","action":"zufang","channel":"zufang","checked":0,"tipsHot":{"query":[{"string":"\u9759\u5b89\u65b0\u57ce","url":"http:\/\/sh.lianjia.com\/zufang\/rs%E9%9D%99%E5%AE%89%E6%96%B0%E5%9F%8E\/"},{"string":"\u5927\u534e\u9526\u7ee3\u534e\u57ce","url":"http:\/\/sh.lianjia.com\/zufang\/rs%E5%A4%A7%E5%8D%8E%E9%94%A6%E7%BB%A3%E5%8D%8E%E5%9F%8E\/"},{"string":"\u4e2d\u8fdc\u4e24\u6e7e\u57ce","url":"http:\/\/sh.lianjia.com\/zufang\/rs%E4%B8%AD%E8%BF%9C%E4%B8%A4%E6%B9%BE%E5%9F%8E\/"},{"string":"\u745e\u8679\u65b0\u57ce","url":"http:\/\/sh.lianjia.com\/zufang\/rs%E7%91%9E%E8%99%B9%E6%96%B0%E5%9F%8E\/"},{"string":"\u9633\u5149\u5a01\u5c3c\u65af","url":"http:\/\/sh.lianjia.com\/zufang\/rs%E9%98%B3%E5%85%89%E5%A8%81%E5%B0%BC%E6%96%AF\/"},{"string":"\u4e0a\u6d77\u5eb7\u57ce","url":"http:\/\/sh.lianjia.com\/zufang\/rs%E4%B8%8A%E6%B5%B7%E5%BA%B7%E5%9F%8E\/"}],"tips":"\u8bf7\u8f93\u5165\u533a\u57df\u3001\u677f\u5757\u6216\u5c0f\u533a\u540d\u5f00\u59cb\u627e\u623f"}},{"name":"\u7ecf\u7eaa\u4eba","action":"jingjiren","channel":"jingjiren","checked":0,"tipsHot":{"query":[],"tips":"\u8bf7\u8f93\u5165\u5546\u5708\u3001\u5c0f\u533a\u6216\u7ecf\u7eaa\u4eba\u7684\u59d3\u540d\u3001\u7535\u8bdd..."}}],
    curChannel:'ershoufang'
  };
</script>
<div ><div class="m-filter">
  
  <div class="list-more">
                                                                                        <dl class=" " >
          <h2><dt title="上海小区在售二手房">小区</dt></h2>
          <dd>
                                                                    <a href="/ershoufang/c5011000010470rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">永泰花苑</span>
                                  <span class="cnt">(18)</span>
                              </a>
                                                          </dd>
        </dl>
                                                                                                                                                                                                                <dl class=" hasmore" >
          <h2><dt title="上海售价在售二手房">售价</dt></h2>
          <dd>
                                                                                                                  <a href="javascript:;" class="nolink" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">200万以下</span>
                              </a>
                                                                    <a href="/ershoufang/p2rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">200-300万</span>
                                  <span class="cnt">(2)</span>
                              </a>
                                                                    <a href="/ershoufang/p3rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">300-400万</span>
                                  <span class="cnt">(10)</span>
                              </a>
                                                                    <a href="/ershoufang/p4rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">400-500万</span>
                                  <span class="cnt">(2)</span>
                              </a>
                                                                    <a href="/ershoufang/p5rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">500-800万</span>
                                  <span class="cnt">(4)</span>
                              </a>
                                                                                                                  <a href="javascript:;" class="nolink" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">800-1000万</span>
                              </a>
                                                                                                                  <a href="javascript:;" class="nolink" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">1000万以上</span>
                              </a>
                                                              <span class="customFilter mt" data-role="price">
                <input type="text" role="minValue" value="">
                <span>-</span>
                <input type="text" role="maxValue" value="">&nbsp;
                                  <span>万</span>
                                <button class="btn-range hide" data-url="/ershoufang/bp{min}ep{max}rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/">确定</button>
              </span>
                                                  <span class="btn-showmore">+ 更多及自定义</span>
                      </dd>
        </dl>
                                                                                                                                                                                                                <dl class=" hasmore" >
          <h2><dt title="上海面积在售二手房">面积</dt></h2>
          <dd>
                                                                                                                  <a href="javascript:;" class="nolink" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">50平以下</span>
                              </a>
                                                                    <a href="/ershoufang/a2rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">50-70平</span>
                                  <span class="cnt">(3)</span>
                              </a>
                                                                    <a href="/ershoufang/a3rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">70-90平</span>
                                  <span class="cnt">(10)</span>
                              </a>
                                                                    <a href="/ershoufang/a4rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">90-110平</span>
                                  <span class="cnt">(2)</span>
                              </a>
                                                                    <a href="/ershoufang/a5rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">110-130平</span>
                                  <span class="cnt">(1)</span>
                              </a>
                                                                    <a href="/ershoufang/a6rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">130-150平</span>
                                  <span class="cnt">(2)</span>
                              </a>
                                                                                                                  <a href="javascript:;" class="nolink" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">150平以上</span>
                              </a>
                                                              <span class="customFilter mt" data-role="area">
                <input type="text" role="minValue" value="">
                <span>-</span>
                <input type="text" role="maxValue" value="">&nbsp;
                                  <span>平</span>
                                <button class="btn-range hide" data-url="/ershoufang/ba{min}ea{max}rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/">确定</button>
              </span>
                                                  <span class="btn-showmore">+ 更多及自定义</span>
                      </dd>
        </dl>
                                                                                                                                                                            <dl class=" " >
          <h2><dt title="上海房型在售二手房">房型</dt></h2>
          <dd>
                                                                    <a href="/ershoufang/l1rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">一室</span>
                                  <span class="cnt">(3)</span>
                              </a>
                                                                    <a href="/ershoufang/l2rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">二室</span>
                                  <span class="cnt">(10)</span>
                              </a>
                                                                    <a href="/ershoufang/l3rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">三室</span>
                                  <span class="cnt">(5)</span>
                              </a>
                                                                                                                  <a href="javascript:;" class="nolink" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">四室</span>
                              </a>
                                                                                                                  <a href="javascript:;" class="nolink" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">五室</span>
                              </a>
                                                                                                                  <a href="javascript:;" class="nolink" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">五室以上</span>
                              </a>
                                                          </dd>
        </dl>
                                                                                                                                                          <dl class="hide " data-role="hide-row">
          <h2><dt title="上海用途在售二手房">用途</dt></h2>
          <dd>
                                                                    <a href="/ershoufang/sf1rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">普通住宅</span>
                                  <span class="cnt">(18)</span>
                              </a>
                                                                                                                  <a href="javascript:;" class="nolink" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">商业类</span>
                              </a>
                                                                                                                  <a href="javascript:;" class="nolink" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">别墅</span>
                              </a>
                                                                                                                  <a href="javascript:;" class="nolink" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">四合院</span>
                              </a>
                                                                                                                  <a href="javascript:;" class="nolink" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">其他</span>
                              </a>
                                                          </dd>
        </dl>
                                                                                                                                        <dl class="hide " data-role="hide-row">
          <h2><dt title="上海权属在售二手房">权属</dt></h2>
          <dd>
                                                                    <a href="/ershoufang/dp1rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">商品房</span>
                                  <span class="cnt">(11)</span>
                              </a>
                                                                                                                  <a href="javascript:;" class="nolink" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">公房</span>
                              </a>
                                                                                                                  <a href="javascript:;" class="nolink" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">经适房</span>
                              </a>
                                                                    <a href="/ershoufang/dp4rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">其他</span>
                                  <span class="cnt">(7)</span>
                              </a>
                                                          </dd>
        </dl>
                                                                                                                      <dl class="hide " data-role="hide-row">
          <h2><dt title="上海楼层在售二手房">楼层</dt></h2>
          <dd>
                                                                    <a href="/ershoufang/lc1rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">低楼层</span>
                                  <span class="cnt">(8)</span>
                              </a>
                                                                    <a href="/ershoufang/lc2rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">中楼层</span>
                                  <span class="cnt">(4)</span>
                              </a>
                                                                    <a href="/ershoufang/lc3rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">高楼层</span>
                                  <span class="cnt">(6)</span>
                              </a>
                                                          </dd>
        </dl>
                                                                                                                                                          <dl class="hide " data-role="hide-row">
          <h2><dt title="上海朝向在售二手房">朝向</dt></h2>
          <dd>
                                                                                                                  <a href="javascript:;" class="nolink" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">朝东</span>
                              </a>
                                                                    <a href="/ershoufang/f2rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">朝南</span>
                                  <span class="cnt">(18)</span>
                              </a>
                                                                                                                  <a href="javascript:;" class="nolink" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">朝西</span>
                              </a>
                                                                    <a href="/ershoufang/f4rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">朝北</span>
                                  <span class="cnt">(9)</span>
                              </a>
                                                                    <a href="/ershoufang/f5rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">南北</span>
                                  <span class="cnt">(18)</span>
                              </a>
                                                          </dd>
        </dl>
                                                                                                                                                          <dl class="hide " data-role="hide-row">
          <h2><dt title="上海楼龄在售二手房">楼龄</dt></h2>
          <dd>
                                                                                                                  <a href="javascript:;" class="nolink" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">5年以内</span>
                              </a>
                                                                                                                  <a href="javascript:;" class="nolink" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">10年以内</span>
                              </a>
                                                                    <a href="/ershoufang/y3rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">15年以内</span>
                                  <span class="cnt">(16)</span>
                              </a>
                                                                    <a href="/ershoufang/y4rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">20年以内</span>
                                  <span class="cnt">(18)</span>
                              </a>
                                                                                                                  <a href="javascript:;" class="nolink" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">20年以上</span>
                              </a>
                                                          </dd>
        </dl>
                                                                                                                      <dl class="hide " data-role="hide-row">
          <h2><dt title="上海类型在售二手房">类型</dt></h2>
          <dd>
                                                                                                                  <a href="javascript:;" class="nolink" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">塔楼</span>
                              </a>
                                                                    <a href="/ershoufang/bt2rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">板楼</span>
                                  <span class="cnt">(18)</span>
                              </a>
                                                                                                                  <a href="javascript:;" class="nolink" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">板塔结合</span>
                              </a>
                                                          </dd>
        </dl>
                                                                                                    <dl class="hide " data-role="hide-row">
          <h2><dt title="上海电梯在售二手房">电梯</dt></h2>
          <dd>
                                                                    <a href="/ershoufang/ie2rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">有电梯</span>
                                  <span class="cnt">(18)</span>
                              </a>
                                                                                                                  <a href="javascript:;" class="nolink" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">无电梯</span>
                              </a>
                                                          </dd>
        </dl>
                                                                                                                      <dl class="hide " data-role="hide-row">
          <h2><dt title="上海装修在售二手房">装修</dt></h2>
          <dd>
                                                                    <a href="/ershoufang/de1rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">精装修</span>
                                  <span class="cnt">(6)</span>
                              </a>
                                                                    <a href="/ershoufang/de2rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">普通装修</span>
                                  <span class="cnt">(4)</span>
                              </a>
                                                                    <a href="/ershoufang/de3rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">毛坯房</span>
                                  <span class="cnt">(2)</span>
                              </a>
                                                          </dd>
        </dl>
            </div>
    <div class="more btn-more">更多选项<span class="arrow"></span></div>
  </div>
</div><div class="content "><!-- 左侧内容 --><div class="leftContent"><div class="orderFilter"><div class="orderTag"><ul><li class='selected'><h3><a href="/ershoufang/rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/">默认排序</span></a></h3></li><li ><h3><a href="/ershoufang/co32rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/">最新</span></a></h3></li><li ><h3><a href="/ershoufang/co21rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/">总价</a></h3></li><li ><h3><a href="/ershoufang/co41rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/">房屋单价</a></h3></li><li ><h3><a href="/ershoufang/co11rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/">面积</a></h3></li><li ><h3><a href="/ershoufang/co52rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/">带看较多</span></a></h3></li></ul><div class="orderType" id="switchView"><span class="list" title="列表模式"></span><span class="img" title="大图模式"></span></div></div><div class="filterAgain"><div class="title">筛选：</div><ul><li ><h3><a href="/ershoufang/ty1rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/"><span class="checkbox"></span>满两年</a></h3></li><li ><h3><a href="/ershoufang/mw1rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/"><span class="checkbox"></span>满五年</a></h3></li><li ><h3><a href="/ershoufang/fh1rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/"><span class="checkbox"></span>优选</a></h3></li><li ><h3><a href="/ershoufang/tt2rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/"><span class="checkbox"></span>新上</a></h3></li><li ><h3><a href="/ershoufang/tt1rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/"><span class="checkbox"></span>独家</a></h3></li><li ><h3><a href="/ershoufang/tt4rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/"><span class="checkbox"></span>随时看房<div class="info"><i></i><div class="infoContent min-wid">经纪人持有该房源钥匙，您可以随时预约看房</div></div></a></h3></li><li ><h3><a href="/ershoufang/tt8rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/"><span class="checkbox"></span>VR房源</a></h3></li><li ><h3><a href="/ershoufang/hu1rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/"><span class="checkbox"></span>不看商业类</a></h3></li><li ><h3><a href="/ershoufang/nb1rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/"><span class="checkbox"></span>不看地下室</a></h3></li><li ><h3><a href="/ershoufang/ng1rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/"><span class="checkbox"></span>不看车位</a></h3></li></ul></div></div><div class="resultDes clear"><h2 class="total fl">共找到<span> 18 </span>套上海二手房</h2><div class="button fr"><div class="clearBtn hide"><script>with(document)write('<a href="/ershoufang/"><span></span>清空条件</a>');</script></div><div class="saveBtn"><a href="#" id="saveBtn"><span></span>保存搜索</a></div></div></div><div id="newAddHouseContainer"></div><!--卡片吊顶--><div class="top_sem_card"></div><script type="text/template" id="top_sem_card_tpl" ><div class="sem_container LOGVIEWDATA" data-lj_view_evtid="11694" data-lj_action_e_plan='<%=data.digV%>'  data-lj_action_Item_id="zaishou_xuantingdiaodingzhanwei" data-lj_data_type="<%=data.type%>" data-lj_data_resblock_id="<%=data.info && data.info.id%>" data-lj_data_agent_ucid="<%=data.agentUcid%>" >
        <a href="<%=data.agentUrl%>" target="_blank" class="LOGCLICKDATA" id="agent_pic" 
          data-lj_evtid="11697" 
          data-lj_action_pid="lianjiaweb"
          data-lj_action_event="WebClick" 
          data-lj_action_source_type="在售房源列表页–悬停吊顶展位经纪人头像/名字点击" 
          data-lj_action_e_plan='<%=data.digV%>'  
          data-lj_action_Item_id="zaishou_xuantingdiaodingzhanwei_agent" 
          data-lj_data_type="<%=data.type%>" 
          data-lj_data_resblock_id="<%=data.info && data.info.id%>" 
          data-lj_data_agent_ucid="<%=data.agentUcid%>">
          <div class="sem_agent_avatar">
            <img src="<%=data.photoPath%>.45x45.jpg" alt="">
          </div>
        </a>
        <div class="sem_agent_info">
          <a target="_blank" href="<%=data.agentUrl%>" class="LOGCLICKDATA im-talk" 
          data-lj_evtid="11697"
          data-lj_action_pid="lianjiaweb"
          data-lj_action_event="WebClick" 
          data-lj_action_source_type="在售房源列表页–悬停吊顶展位经纪人头像/名字点击"  
          data-lj_action_e_plan='<%=data.digV%>'  
          data-lj_action_Item_id="zaishou_xuantingdiaodingzhanwei_agent" 
          data-lj_data_type="<%=data.type%>" 
          data-lj_data_resblock_id="<%=data.info && data.info.id%>" 
          data-lj_data_agent_ucid="<%=data.agentUcid%>">
            <p class="sem_agent_name"><%=data.name%></p>
          </a>
          <%if (data.agentVipLevel){ %>
              <span class="ico-vip"></span>
          <% } %>
          <p class="sem_agent_desc"><%=data.desc%></p>
        </div>
        <span class="agent_chat LOGCLICKDATA im-talk" data-bl="agent_im" data-ucid="<%=data.agentUcid%>" data-source-port="PC:ershou_ershoufang_list_top" data-source-extends="<%=JSON.stringify(extend)%>" data-msg-payload="<%=imInfo.payload%>" 
        data-lj_evtid="11696" 
        data-lj_action_e_plan='<%=data.digV%>'  
        data-lj_action_Item_id="zaishou_xuantingdiaodingzhanwei_IM" data-lj_data_type="<%=data.type%>" data-lj_data_resblock_id="<%=data.info && data.info.id%>" data-lj_data_agent_ucid="<%=data.agentUcid%>">
          <i></i>
          <span>在线咨询</span>
        </span>
        <div class="sem_phone LOGCLICKDATA fr" data-lj_evtid="11695"  data-lj_action_e_plan='<%=data.digV%>'  data-lj_action_Item_id="zaishou_xuantingdiaodingzhanwei_400" data-lj_data_type="<%=data.type%>" data-lj_data_resblock_id="<%=data.info && data.info.id%>" data-lj_data_agent_ucid="<%=data.agentUcid%>">
          <span class="sem_phone_label">咨询电话：</span>
          <span><%=data.fourPhoneOne%></span>
        </div>
      </div>
</script><div id="sem_card"></div><script type="text/template" id="sem_card_tpl" semParamsStr="&semResblockId=5011000010470&semShequId=5600&semType=community&semSource=ershou_shequ" semState="1" ><div class="agentCardPush LOGVIEW LOGVIEWDATA"  data-lj_view_evtid="11942" data-lj_action_e_plan='<%=data.digV%>'  data-lj_action_Item_id="zaishou_xuantingdiaodingzhanwei" data-lj_data_type="<%=data.type%>" data-lj_data_resblock_id="<%=data.info && data.info.id%>" data-lj_data_agent_ucid="<%=data.agentUcid%>" log-mod="ershoufang_list_semcard" data-bl="agent" data-el="<%=data.agentUcid%>" data-log_id="20001" data-log_value="<%=data.info && data.info.id%>" data-log_source="<%=data.ljwebSource%>" data-log_statId="<%=data.ljwebStatId%>" >
  <% if (data.info){ %>
  <div class="agentCardSemInfo">
      <div class="agentCardSemInfoTop">
        <div class="agentCardSemInfoName">
            <a class="agentCardResblockTitle LOGCLICK" data-bl="agent_resblock_name"  data-log_value="<%=data.info && data.info.id%>" data-log_source="<%=data.ljwebSource%>" data-log_statId="<%=data.ljwebStatId%>" target="_blank" href="<%=data.info && data.info.url%>"><%=data.info && data.info.name%></a>
            <span class="agentCardResblockSubTitle"><%=data.info && data.info.districtName%><%=data.info && data.info.bizcircleName%></span>
            <% if(data.info && data.info.url){ %>
              <a href="<%=data.info && data.info.url%>" target="_blank" class="agentCardResblockLink LOGCLICK" data-bl="agent_resblock_info"  data-log_value="<%=data.info && data.info.id%>" data-log_source="<%=data.ljwebSource%>" data-log_statId="<%=data.ljwebStatId%>">查看小区详情</a>
            <% } %>
        </div>
      </div>
      <div class="agentCardDetail">
        <div class="agentCardDetailItem price">
          <div class="agentCardDetailTitle">小区均价</div>
          <a href="<%=data.info && data.info.fangjiaUrl%>" target="_blank" class="agentCardDetailInfo LOGCLICK" data-bl="agent_resblock_avg" data-log_value="<%=data.info && data.info.id%>" data-log_source="<%=data.ljwebSource%>" data-log_statId="<%=data.ljwebStatId%>"><%=data.info && data.info.unitPrice%>元/平米</a>
        </div>
        <div class="agentCardDetailItem">
          <div class="agentCardDetailTitle">正在出售</div>
          <div class="agentCardDetailInfo"><%=data.info && data.info.sellNum%>套</div>
        </div>
        <div class="agentCardDetailItem">
          <div class="agentCardDetailTitle">近90天成交</div>
          <a href="<%=data.info && data.info.soldUrl%>" target="_blank" class="agentCardDetailInfo LOGCLICK" data-bl="agent_resblock_sale" data-log_value="<%=data.info && data.info.id%>" data-log_source="<%=data.ljwebSource%>" data-log_statId="<%=data.ljwebStatId%>"><%=data['info']['90saleCount']%>套</a>
        </div>
        <div class="agentCardDetailItem">
          <div class="agentCardDetailTitle">近30天带看</div>
          <div class="agentCardDetailInfo"><%=data.info && data.info.day30See%>次</div>
        </div>
      </div>
  </div>
  <% } %>
  <div class="agentCardAgentInfo">
    <a href="<%=data.agentUrl%>" target="_blank" class="agentCardAgentImg LOGCLICK LOGCLICKDATA" data-lj_evtid="11938"  data-lj_action_e_plan='<%=data.digV%>'  data-lj_action_Item_id="zaishou_xuantingdiaodingzhanwei_agent" data-lj_data_type="<%=data.type%>" data-lj_data_resblock_id="<%=data.info && data.info.id%>" data-lj_data_agent_ucid="<%=data.agentUcid%>" data-bl="agent"  data-log_value="<%=data.info && data.info.id%>" data-log_source="<%=data.ljwebSource%>" data-log_statId="<%=data.ljwebStatId%>"><img src="<%=data.photoPath%>.66x66.jpg" alt="小区顾问"></a>
    <div class="cardAgentInfo">
      <div class="cardAgentNameContainer">
        <a target="_blank" href="<%=data.agentUrl%>" class="cardAgentName LOGCLICK  LOGCLICKDATA fl" data-lj_evtid="11938"  data-lj_action_e_plan='<%=data.digV%>'  data-lj_action_Item_id="zaishou_xuantingdiaodingzhanwei_agent" data-lj_data_type="<%=data.type%>" data-lj_data_resblock_id="<%=data.info && data.info.id%>" data-lj_data_agent_ucid="<%=data.agentUcid%>" data-bl="agent"  data-log_value="<%=data.info && data.info.id%>" data-log_source="<%=data.ljwebSource%>" data-log_statId="<%=data.ljwebStatId%>"><%=data.name%></a>
        <%if (data.agentVipLevel){ %>
        <span class="ico-vip"></span>
        <% } %>
        <div class="cardAgentPhone fr"><%=data.fourPhoneOne%></div>
      </div>
      <div class="cardAgentDesc"><%=data.desc%></div>
    </div>
      <span class="agent_chat LOGCLICKDATA im-talk LOGCLICKDATA" data-lj_evtid="11939"  data-lj_action_e_plan='<%=data.digV%>'  data-lj_action_Item_id="zaishou_xuantingdiaodingzhanwei_agent" data-lj_data_type="<%=data.type%>" data-lj_data_resblock_id="<%=data.info && data.info.id%>" data-lj_data_agent_ucid="<%=data.agentUcid%>" data-bl="agent_im" data-ucid="<%=data.agentUcid%>" data-source-port="<%=imInfo.port%>" data-digV='<%=data.digV%>' data-msg-payload="<%=imInfo.payload%>" data-source-extends=<%=JSON.stringify(extend)%> >
        <i></i>
        <span>在线咨询</span>
      </span>
  </div>
</div>
</script>
<div class="bigImgList" style="display: none;" log-mod="list"><div class="item" data-houseid="107100396672">
<a class="img" href="https://sh.lianjia.com/ershoufang/107100396672.html" target="_blank" data-bl="list" data-log_index="1" data-housecode="107100396672" data-is_focus="1"  data-el="ershoufang"><img class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2018122819393752" data-original="https://image1.ljcdn.com/310000-inspection/test-16a54529-8fcc-4566-9597-42302c1cdf0a.png.296x216.jpg.437x300.jpg"><div class="btn-follow follow" data-hid="107100396672"><span class="star"></span><span class="follow-text">关注</span></div><div class="leftArrow"><span></span></div><div class="rightArrow"><span></span></div>
<div class="price"><span>358</span>万
</div></a>
<a class="title" href="https://sh.lianjia.com/ershoufang/107100396672.html" target="_blank" data-bl="list" data-log_index="1" data-housecode="107100396672" data-is_focus="1"  data-el="ershoufang">永泰花苑南北两房，动迁房，一个点个税</a>
<div class="info">三林<span>/</span>2室1厅<span>/</span>73.16平米<span>/</span>南 北<span>/</span>简装<span>/</span>有电梯

</div>
<div class="tag">
    <span class="vr">VR房源</span>
    <span class="haskey">随时看房</span>
</div></div><div class="item" data-houseid="107100857965"><a class="img" href="https://sh.lianjia.com/ershoufang/107100857965.html" target="_blank" data-bl="list" data-log_index="2" data-housecode="107100857965" data-is_focus="1"  data-el="ershoufang"><img class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2018122819393752" data-original="https://image1.ljcdn.com/310000-inspection/prod-6c747029-9194-4e6d-911b-d4db975d75cb.jpg.296x216.jpg.437x300.jpg"><div class="btn-follow follow" data-hid="107100857965"><span class="star"></span><span class="follow-text">关注</span></div><div class="leftArrow"><span></span></div><div class="rightArrow"><span></span></div><div class="price"><span>372</span>万</div></a><a class="title" href="https://sh.lianjia.com/ershoufang/107100857965.html" target="_blank" data-bl="list" data-log_index="2" data-housecode="107100857965" data-is_focus="1"  data-el="ershoufang">永泰花苑 2室1厅 372万</a><div class="info">三林<span>/</span>2室1厅<span>/</span>74.01平米<span>/</span>南<span>/</span>其他<span>/</span>有电梯</div><div class="tag"><span class="vr">VR房源</span><span class="haskey">随时看房</span></div></div><div class="item" data-houseid="107100760342"><a class="img" href="https://sh.lianjia.com/ershoufang/107100760342.html" target="_blank" data-bl="list" data-log_index="3" data-housecode="107100760342" data-is_focus=""  data-el="ershoufang"><img class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2018122819393752" data-original="https://image1.ljcdn.com/310000-inspection/test-e1fd6bfc-0a56-4431-a14a-dbe9669ac582.png.296x216.jpg.437x300.jpg"><div class="btn-follow follow" data-hid="107100760342"><span class="star"></span><span class="follow-text">关注</span></div><div class="leftArrow"><span></span></div><div class="rightArrow"><span></span></div><div class="price"><span>390</span>万</div></a><a class="title" href="https://sh.lianjia.com/ershoufang/107100760342.html" target="_blank" data-bl="list" data-log_index="3" data-housecode="107100760342" data-is_focus=""  data-el="ershoufang">三林地铁11号线 双南两房 看房方便 诚意出售</a><div class="info">三林<span>/</span>2室1厅<span>/</span>73.9平米<span>/</span>南<span>/</span>精装<span>/</span>有电梯</div><div class="tag"><span class="subway">近地铁</span><span class="vr">VR房源</span><span class="five">房本满两年</span><span class="haskey">随时看房</span></div></div><div class="item" data-houseid="107100852490"><a class="img" href="https://sh.lianjia.com/ershoufang/107100852490.html" target="_blank" data-bl="list" data-log_index="4" data-housecode="107100852490" data-is_focus=""  data-el="ershoufang"><img class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2018122819393752" data-original="https://image1.ljcdn.com/310000-inspection/prod-53f80a19-f12a-4cd5-827f-a6554ec5f9b3.jpg.296x216.jpg.437x300.jpg"><div class="btn-follow follow" data-hid="107100852490"><span class="star"></span><span class="follow-text">关注</span></div><div class="leftArrow"><span></span></div><div class="rightArrow"><span></span></div><div class="price"><span>498</span>万</div></a><a class="title" href="https://sh.lianjia.com/ershoufang/107100852490.html" target="_blank" data-bl="list" data-log_index="4" data-housecode="107100852490" data-is_focus=""  data-el="ershoufang">只要契税+配套完善+业主诚意+前滩板块+交通便利</a><div class="info">三林<span>/</span>3室2厅<span>/</span>96.8平米<span>/</span>南<span>/</span>简装<span>/</span>有电梯</div><div class="tag"><span class="subway">近地铁</span><span class="vr">VR房源</span><span class="taxfree">房本满五年</span></div></div><div class="item" data-houseid="107100111854"><a class="img" href="https://sh.lianjia.com/ershoufang/107100111854.html" target="_blank" data-bl="list" data-log_index="5" data-housecode="107100111854" data-is_focus=""  data-el="ershoufang"><img class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2018122819393752" data-original="https://image1.ljcdn.com/310000-inspection/test-7474363c-0ffb-4710-91a9-3be2fb83499a.png.296x216.jpg.437x300.jpg"><div class="btn-follow follow" data-hid="107100111854"><span class="star"></span><span class="follow-text">关注</span></div><div class="leftArrow"><span></span></div><div class="rightArrow"><span></span></div><div class="price"><span>665</span>万</div></a><a class="title" href="https://sh.lianjia.com/ershoufang/107100111854.html" target="_blank" data-bl="list" data-log_index="5" data-housecode="107100111854" data-is_focus=""  data-el="ershoufang">永泰花苑.稀有毛坯电梯复式.地铁11号800米，配套成熟</a><div class="info">三林<span>/</span>3室3厅<span>/</span>136.72平米<span>/</span>南 北<span>/</span>毛坯<span>/</span>有电梯</div><div class="tag"><span class="subway">近地铁</span><span class="vr">VR房源</span><span class="haskey">随时看房</span></div></div><div class="item" data-houseid="107100868343"><a class="img" href="https://sh.lianjia.com/ershoufang/107100868343.html" target="_blank" data-bl="list" data-log_index="6" data-housecode="107100868343" data-is_focus=""  data-el="ershoufang"><img class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2018122819393752" data-original="https://image1.ljcdn.com/310000-inspection/prod-83c311bc-3d9d-4ee7-b6f6-26916074deca.jpg.296x216.jpg.437x300.jpg"><div class="btn-follow follow" data-hid="107100868343"><span class="star"></span><span class="follow-text">关注</span></div><div class="leftArrow"><span></span></div><div class="rightArrow"><span></span></div><div class="price"><span>397</span>万</div></a><a class="title" href="https://sh.lianjia.com/ershoufang/107100868343.html" target="_blank" data-bl="list" data-log_index="6" data-housecode="107100868343" data-is_focus=""  data-el="ershoufang">前滩板块 地铁11号线 南北两房 精装修 带地暖 视野宽</a><div class="info">三林<span>/</span>2室1厅<span>/</span>72.27平米<span>/</span>南 北<span>/</span>其他<span>/</span>有电梯</div><div class="tag"><span class="subway">近地铁</span><span class="vr">VR房源</span><span class="five">房本满两年</span></div></div><div class="item" data-houseid="107100679680"><a class="img" href="https://sh.lianjia.com/ershoufang/107100679680.html" target="_blank" data-bl="list" data-log_index="7" data-housecode="107100679680" data-is_focus="1"  data-el="ershoufang"><img class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2018122819393752" data-original="https://image1.ljcdn.com/310000-inspection/test-3a0f0897-43a2-4ac3-ace4-3f5bb341c815.png.296x216.jpg.437x300.jpg"><div class="btn-follow follow" data-hid="107100679680"><span class="star"></span><span class="follow-text">关注</span></div><div class="leftArrow"><span></span></div><div class="rightArrow"><span></span></div><div class="price"><span>385</span>万</div></a><a class="title" href="https://sh.lianjia.com/ershoufang/107100679680.html" target="_blank" data-bl="list" data-log_index="7" data-housecode="107100679680" data-is_focus="1"  data-el="ershoufang">永泰花苑 大两房总价低 位置成熟 精装修诚意出售</a><div class="info">三林<span>/</span>2室1厅<span>/</span>73.56平米<span>/</span>南<span>/</span>精装<span>/</span>有电梯</div><div class="tag"><span class="subway">近地铁</span><span class="vr">VR房源</span></div></div><div class="item" data-houseid="107100740920"><a class="img" href="https://sh.lianjia.com/ershoufang/107100740920.html" target="_blank" data-bl="list" data-log_index="8" data-housecode="107100740920" data-is_focus=""  data-el="ershoufang"><img class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2018122819393752" data-original="https://image1.ljcdn.com/310000-inspection/test-ef16bd03-6f7d-4656-ba2e-b3965210d7dc.png.296x216.jpg.437x300.jpg"><div class="btn-follow follow" data-hid="107100740920"><span class="star"></span><span class="follow-text">关注</span></div><div class="leftArrow"><span></span></div><div class="rightArrow"><span></span></div><div class="price"><span>660</span>万</div></a><a class="title" href="https://sh.lianjia.com/ershoufang/107100740920.html" target="_blank" data-bl="list" data-log_index="8" data-housecode="107100740920" data-is_focus=""  data-el="ershoufang">永泰花苑 3室2厅 660万</a><div class="info">三林<span>/</span>3室2厅<span>/</span>134.25平米<span>/</span>南 北<span>/</span>精装<span>/</span>有电梯</div><div class="tag"><span class="subway">近地铁</span><span class="vr">VR房源</span></div></div><div class="item" data-houseid="107100512564"><a class="img" href="https://sh.lianjia.com/ershoufang/107100512564.html" target="_blank" data-bl="list" data-log_index="9" data-housecode="107100512564" data-is_focus=""  data-el="ershoufang"><img class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2018122819393752" data-original="https://image1.ljcdn.com/310000-inspection/test-b447d0f1-bd5b-4aab-a93a-c668e36df6fd.png.296x216.jpg.437x300.jpg"><div class="btn-follow follow" data-hid="107100512564"><span class="star"></span><span class="follow-text">关注</span></div><div class="leftArrow"><span></span></div><div class="rightArrow"><span></span></div><div class="price"><span>385</span>万</div></a><a class="title" href="https://sh.lianjia.com/ershoufang/107100512564.html" target="_blank" data-bl="list" data-log_index="9" data-housecode="107100512564" data-is_focus=""  data-el="ershoufang">永泰花苑 三年装修 南北通透 明亮干净 婚装出售</a><div class="info">三林<span>/</span>2室1厅<span>/</span>73.64平米<span>/</span>南 北<span>/</span>精装<span>/</span>有电梯</div><div class="tag"><span class="vr">VR房源</span></div></div><div class="item" data-houseid="107100839777"><a class="img" href="https://sh.lianjia.com/ershoufang/107100839777.html" target="_blank" data-bl="list" data-log_index="10" data-housecode="107100839777" data-is_focus=""  data-el="ershoufang"><img class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2018122819393752" data-original="https://image1.ljcdn.com/310000-inspection/prod-43f61941-51f4-44ea-9058-9822edd99159.jpg.296x216.jpg.437x300.jpg"><div class="btn-follow follow" data-hid="107100839777"><span class="star"></span><span class="follow-text">关注</span></div><div class="leftArrow"><span></span></div><div class="rightArrow"><span></span></div><div class="price"><span>385</span>万</div></a><a class="title" href="https://sh.lianjia.com/ershoufang/107100839777.html" target="_blank" data-bl="list" data-log_index="10" data-housecode="107100839777" data-is_focus=""  data-el="ershoufang">永泰花苑 装修好 带新空调 一年前的装修 大两房</a><div class="info">三林<span>/</span>2室1厅<span>/</span>72.72平米<span>/</span>南<span>/</span>其他<span>/</span>有电梯</div><div class="tag"><span class="vr">VR房源</span></div></div><div class="item" data-houseid="107100713831"><a class="img" href="https://sh.lianjia.com/ershoufang/107100713831.html" target="_blank" data-bl="list" data-log_index="11" data-housecode="107100713831" data-is_focus=""  data-el="ershoufang"><img class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2018122819393752" data-original="https://image1.ljcdn.com/310000-inspection/test-faddb335-590f-4674-aa52-96991bc37c5d.jpg.296x216.jpg.437x300.jpg"><div class="btn-follow follow" data-hid="107100713831"><span class="star"></span><span class="follow-text">关注</span></div><div class="leftArrow"><span></span></div><div class="rightArrow"><span></span></div><div class="price"><span>520</span>万</div></a><a class="title" href="https://sh.lianjia.com/ershoufang/107100713831.html" target="_blank" data-bl="list" data-log_index="11" data-housecode="107100713831" data-is_focus=""  data-el="ershoufang">永泰花苑板式三房 位置前后开阔 精装修</a><div class="info">三林<span>/</span>3室2厅<span>/</span>98平米<span>/</span>南 北<span>/</span>精装<span>/</span>有电梯</div><div class="tag"><span class="subway">近地铁</span><span class="vr">VR房源</span></div></div><div class="item" data-houseid="107100408424"><a class="img" href="https://sh.lianjia.com/ershoufang/107100408424.html" target="_blank" data-bl="list" data-log_index="12" data-housecode="107100408424" data-is_focus=""  data-el="ershoufang"><img class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2018122819393752" data-original="https://image1.ljcdn.com/shfdfs-image/20171206/b25ed9ce-8ce8-4acd-97fd-eb33114a3c28.jpg.296x216.jpg.437x300.jpg"><div class="btn-follow follow" data-hid="107100408424"><span class="star"></span><span class="follow-text">关注</span></div><div class="leftArrow"><span></span></div><div class="rightArrow"><span></span></div><div class="price"><span>300</span>万</div></a><a class="title" href="https://sh.lianjia.com/ershoufang/107100408424.html" target="_blank" data-bl="list" data-log_index="12" data-housecode="107100408424" data-is_focus=""  data-el="ershoufang">永泰花苑 1室1厅 300万</a><div class="info">三林<span>/</span>1室1厅<span>/</span>54.78平米<span>/</span>南<span>/</span>其他<span>/</span>有电梯</div><div class="tag"><span class="five">房本满两年</span></div></div><div class="item" data-houseid="107100705380"><a class="img" href="https://sh.lianjia.com/ershoufang/107100705380.html" target="_blank" data-bl="list" data-log_index="13" data-housecode="107100705380" data-is_focus=""  data-el="ershoufang"><img class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2018122819393752" data-original="https://image1.ljcdn.com/310000-inspection/4ccee553-ba9d-4ab8-801a-55cede3b2fd2.jpg.296x216.jpg.437x300.jpg"><div class="btn-follow follow" data-hid="107100705380"><span class="star"></span><span class="follow-text">关注</span></div><div class="leftArrow"><span></span></div><div class="rightArrow"><span></span></div><div class="price"><span>400</span>万</div></a><a class="title" href="https://sh.lianjia.com/ershoufang/107100705380.html" target="_blank" data-bl="list" data-log_index="13" data-housecode="107100705380" data-is_focus=""  data-el="ershoufang">小区 采光好 *明户型 交通便利小区 前后小区花园</a><div class="info">三林<span>/</span>2室1厅<span>/</span>75.34平米<span>/</span>南 北<span>/</span>简装<span>/</span>有电梯</div><div class="tag"><span class="taxfree">房本满五年</span></div></div><div class="item" data-houseid="107100369892"><a class="img" href="https://sh.lianjia.com/ershoufang/107100369892.html" target="_blank" data-bl="list" data-log_index="14" data-housecode="107100369892" data-is_focus=""  data-el="ershoufang"><img class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2018122819393752" data-original="https://image1.ljcdn.com/310000-inspection/753cb0c1-96e3-42d9-b308-5d08745e9cb1.jpg.296x216.jpg.437x300.jpg"><div class="btn-follow follow" data-hid="107100369892"><span class="star"></span><span class="follow-text">关注</span></div><div class="leftArrow"><span></span></div><div class="rightArrow"><span></span></div><div class="price"><span>348</span>万</div></a><a class="title" href="https://sh.lianjia.com/ershoufang/107100369892.html" target="_blank" data-bl="list" data-log_index="14" data-housecode="107100369892" data-is_focus=""  data-el="ershoufang">动迁性质免增值税 底楼垫高 可做入户花园</a><div class="info">三林<span>/</span>2室1厅<span>/</span>72.76平米<span>/</span>南<span>/</span>简装<span>/</span>有电梯</div><div class="tag"><span class="subway">近地铁</span></div></div><div class="item" data-houseid="107100718595"><a class="img" href="https://sh.lianjia.com/ershoufang/107100718595.html" target="_blank" data-bl="list" data-log_index="15" data-housecode="107100718595" data-is_focus=""  data-el="ershoufang"><img class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2018122819393752" data-original="https://image1.ljcdn.com/310000-inspection/test-a8413813-cb5b-4c75-8552-030249f0fe71.png.296x216.jpg.437x300.jpg"><div class="btn-follow follow" data-hid="107100718595"><span class="star"></span><span class="follow-text">关注</span></div><div class="leftArrow"><span></span></div><div class="rightArrow"><span></span></div><div class="price"><span>600</span>万</div></a><a class="title" href="https://sh.lianjia.com/ershoufang/107100718595.html" target="_blank" data-bl="list" data-log_index="15" data-housecode="107100718595" data-is_focus=""  data-el="ershoufang">永泰花苑，小区位置好，少有的税少复式，业主诚售</a><div class="info">三林<span>/</span>3室2厅<span>/</span>119.78平米<span>/</span>南 北<span>/</span>精装<span>/</span>有电梯</div><div class="tag"><span class="taxfree">房本满五年</span></div></div><div class="item" data-houseid="107100426560"><a class="img" href="https://sh.lianjia.com/ershoufang/107100426560.html" target="_blank" data-bl="list" data-log_index="16" data-housecode="107100426560" data-is_focus=""  data-el="ershoufang"><img class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2018122819393752" data-original="https://image1.ljcdn.com/x-se/hdic-frame/1f3e09da-c176-430b-b231-f054e5212f67.png.280x210.jpg.437x300.jpg"><div class="btn-follow follow" data-hid="107100426560"><span class="star"></span><span class="follow-text">关注</span></div><div class="leftArrow"><span></span></div><div class="rightArrow"><span></span></div><div class="price"><span>375</span>万</div></a><a class="title" href="https://sh.lianjia.com/ershoufang/107100426560.html" target="_blank" data-bl="list" data-log_index="16" data-housecode="107100426560" data-is_focus=""  data-el="ershoufang">近地铁 中房开发品质 三林热门高档住宅 11号线三林站</a><div class="info">三林<span>/</span>2室1厅<span>/</span>72.59平米<span>/</span>南 北<span>/</span>毛坯<span>/</span>有电梯</div><div class="tag"><span class="subway">近地铁</span><span class="taxfree">房本满五年</span></div></div><div class="item" data-houseid="107100767149"><a class="img" href="https://sh.lianjia.com/ershoufang/107100767149.html" target="_blank" data-bl="list" data-log_index="17" data-housecode="107100767149" data-is_focus=""  data-el="ershoufang"><img class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2018122819393752" data-original="https://image1.ljcdn.com/x-se/hdic-frame/f65f4d49-23bc-4f9c-8c74-925fd2ee5b44.png.280x210.jpg.437x300.jpg"><div class="btn-follow follow" data-hid="107100767149"><span class="star"></span><span class="follow-text">关注</span></div><div class="leftArrow"><span></span></div><div class="rightArrow"><span></span></div><div class="price"><span>290</span>万</div></a><a class="title" href="https://sh.lianjia.com/ershoufang/107100767149.html" target="_blank" data-bl="list" data-log_index="17" data-housecode="107100767149" data-is_focus=""  data-el="ershoufang">次新小区，房东诚心出售，价格可谈，动迁所得</a><div class="info">三林<span>/</span>1室1厅<span>/</span>54.55平米<span>/</span>南<span>/</span>其他<span>/</span>有电梯</div><div class="tag"><span class="taxfree">房本满五年</span></div></div><div class="item" data-houseid="107100609516"><a class="img" href="https://sh.lianjia.com/ershoufang/107100609516.html" target="_blank" data-bl="list" data-log_index="18" data-housecode="107100609516" data-is_focus=""  data-el="ershoufang"><img class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2018122819393752" data-original=""><div class="btn-follow follow" data-hid="107100609516"><span class="star"></span><span class="follow-text">关注</span></div><div class="leftArrow"><span></span></div><div class="rightArrow"><span></span></div><div class="price"><span>280</span>万</div></a><a class="title" href="https://sh.lianjia.com/ershoufang/107100609516.html" target="_blank" data-bl="list" data-log_index="18" data-housecode="107100609516" data-is_focus=""  data-el="ershoufang">永泰花苑 1室1厅 280万</a><div class="info">三林<span>/</span>1室1厅<span>/</span>59.03平米<span>/</span>南<span>/</span>其他<span>/</span>有电梯</div><div class="tag"><span class="taxfree">房本满五年</span></div></div></div>

<ul class="sellListContent" log-mod="list">
<li class="clear LOGCLICKDATA" >
    <a class="noresultRecommend img " 
        href="https://sh.lianjia.com/ershoufang/107100396672.html" 
        target="_blank"data-log_index="1" 
        data-el="ershoufang" 
        data-housecode="107100396672" 
        data-is_focus="1" 
        data-sl="">
        
        
        <div class="focus_tag"></div><!-- 热推标签、埋点 -->
        <img src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrlogo.png?_v=2018122819393752" class="vr_item">
            <img class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2018122819393752" data-original="https://image1.ljcdn.com/310000-inspection/test-16a54529-8fcc-4566-9597-42302c1cdf0a.png.296x216.jpg" alt="永泰花苑南北两房，动迁房，一个点个税">
    </a>
    <div class="info clear">
        <div class="title">
            <a class="" href="https://sh.lianjia.com/ershoufang/107100396672.html" target="_blank" data-log_index="1"  data-el="ershoufang" data-housecode="107100396672" data-is_focus="1" data-sl="">
                永泰花苑南北两房，动迁房，一个点个税
            </a>
                <!-- 拆分标签 -->
        </div>
        <div class="address">
                <div class="houseInfo">
                    <span class="houseIcon"></span>
                    <a href="https://sh.lianjia.com/xiaoqu/5011000010470/" target="_blank" data-log_index="1" data-el="region">
                    永泰花苑 
                    </a>
                     | 2室1厅 | 73.16平米 | 南 北 | 简装 | 有电梯
                </div>
        </div>
        <div class="flood">
                <div class="positionInfo">
                    <span class="positionIcon"></span>
                    低楼层(共11层)2005年建板楼  -  
                    <a href="https://sh.lianjia.com/ershoufang/sanlin/" target="_blank">三林</a>
                </div>
        </div>
            <div class="followInfo">
                <span class="starIcon"></span>
                179人关注 / 共16次带看 / 6个月以前发布
            </div>
            <div class="tag">
                <span class="vr">VR房源</span>
                <span class="haskey">随时看房</span>
            </div>
            <div class="priceInfo">
                <div class="totalPrice">
                    <span>358</span>万
                </div>
                <div class="unitPrice" data-hid="107100396672" data-rid="5011000010470" data-price="48934">
                    <span>单价48934元/平米</span>
                </div>
            </div>
        </div>
        <div class="listButtonContainer">
            <div class="btn-follow followBtn" data-hid="107100396672">
                <span class="follow-text">关注</span>
            </div>
            <div class="compareBtn LOGCLICK" data-hid="107100396672" log-mod="107100396672" data-log_evtid="10230">
                加入对比
            </div>348万
        </div>
    </li>
    <li class="clear LOGCLICKDATA" ><a class="noresultRecommend img " href="https://sh.lianjia.com/ershoufang/107100857965.html" target="_blank"data-log_index="2" data-el="ershoufang" data-housecode="107100857965" data-is_focus="1" data-sl=""><div class="focus_tag"></div><!-- 热推标签、埋点 --><img src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrlogo.png?_v=2018122819393752" class="vr_item"><img class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2018122819393752" data-original="https://image1.ljcdn.com/310000-inspection/prod-6c747029-9194-4e6d-911b-d4db975d75cb.jpg.296x216.jpg" alt="永泰花苑 2室1厅 372万"></a><div class="info clear"><div class="title"><a class="" href="https://sh.lianjia.com/ershoufang/107100857965.html" target="_blank" data-log_index="2"  data-el="ershoufang" data-housecode="107100857965" data-is_focus="1" data-sl="">永泰花苑 2室1厅 372万</a><!-- 拆分标签 --></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span><a href="https://sh.lianjia.com/xiaoqu/5011000010470/" target="_blank" data-log_index="2" data-el="region">永泰花苑 </a> | 2室1厅 | 74.01平米 | 南 | 其他 | 有电梯</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>低楼层(共11层)2005年建板楼  -  <a href="https://sh.lianjia.com/ershoufang/sanlin/" target="_blank">三林</a></div></div><div class="followInfo"><span class="starIcon"></span>27人关注 / 共34次带看 / 29天以前发布</div><div class="tag"><span class="vr">VR房源</span><span class="haskey">随时看房</span></div><div class="priceInfo"><div class="totalPrice"><span>372</span>万</div><div class="unitPrice" data-hid="107100857965" data-rid="5011000010470" data-price="50264"><span>单价50264元/平米</span></div></div></div><div class="listButtonContainer"><div class="btn-follow followBtn" data-hid="107100857965"><span class="follow-text">关注</span></div><div class="compareBtn LOGCLICK" data-hid="107100857965" log-mod="107100857965" data-log_evtid="10230">加入对比</div></div></li><li class="clear LOGCLICKDATA" ><a class="noresultRecommend img " href="https://sh.lianjia.com/ershoufang/107100760342.html" target="_blank"data-log_index="3" data-el="ershoufang" data-housecode="107100760342" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrlogo.png?_v=2018122819393752" class="vr_item"><img class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2018122819393752" data-original="https://image1.ljcdn.com/310000-inspection/test-e1fd6bfc-0a56-4431-a14a-dbe9669ac582.png.296x216.jpg" alt="三林地铁11号线 双南两房 看房方便 诚意出售"></a><div class="info clear"><div class="title"><a class="" href="https://sh.lianjia.com/ershoufang/107100760342.html" target="_blank" data-log_index="3"  data-el="ershoufang" data-housecode="107100760342" data-is_focus="" data-sl="">三林地铁11号线 双南两房 看房方便 诚意出售</a><!-- 拆分标签 --></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span><a href="https://sh.lianjia.com/xiaoqu/5011000010470/" target="_blank" data-log_index="3" data-el="region">永泰花苑 </a> | 2室1厅 | 73.9平米 | 南 | 精装 | 有电梯</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>中楼层(共11层)2004年建板楼  -  <a href="https://sh.lianjia.com/ershoufang/sanlin/" target="_blank">三林</a></div></div><div class="followInfo"><span class="starIcon"></span>64人关注 / 共53次带看 / 2个月以前发布</div><div class="tag"><span class="subway">近地铁</span><span class="vr">VR房源</span><span class="five">房本满两年</span><span class="haskey">随时看房</span></div><div class="priceInfo"><div class="totalPrice"><span>390</span>万</div><div class="unitPrice" data-hid="107100760342" data-rid="5011000010470" data-price="52775"><span>单价52775元/平米</span></div></div></div><div class="listButtonContainer"><div class="btn-follow followBtn" data-hid="107100760342"><span class="follow-text">关注</span></div><div class="compareBtn LOGCLICK" data-hid="107100760342" log-mod="107100760342" data-log_evtid="10230">加入对比</div></div></li><li class="clear LOGCLICKDATA" ><a class="noresultRecommend img " href="https://sh.lianjia.com/ershoufang/107100852490.html" target="_blank"data-log_index="4" data-el="ershoufang" data-housecode="107100852490" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrlogo.png?_v=2018122819393752" class="vr_item"><img class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2018122819393752" data-original="https://image1.ljcdn.com/310000-inspection/prod-53f80a19-f12a-4cd5-827f-a6554ec5f9b3.jpg.296x216.jpg" alt="只要契税+配套完善+业主诚意+前滩板块+交通便利"></a><div class="info clear"><div class="title"><a class="" href="https://sh.lianjia.com/ershoufang/107100852490.html" target="_blank" data-log_index="4"  data-el="ershoufang" data-housecode="107100852490" data-is_focus="" data-sl="">只要契税+配套完善+业主诚意+前滩板块+交通便利</a><!-- 拆分标签 --></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span><a href="https://sh.lianjia.com/xiaoqu/5011000010470/" target="_blank" data-log_index="4" data-el="region">永泰花苑 </a> | 3室2厅 | 96.8平米 | 南 | 简装 | 有电梯</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>低楼层(共18层)2005年建板楼  -  <a href="https://sh.lianjia.com/ershoufang/sanlin/" target="_blank">三林</a></div></div><div class="followInfo"><span class="starIcon"></span>11人关注 / 共1次带看 / 31天以前发布</div><div class="tag"><span class="subway">近地铁</span><span class="vr">VR房源</span><span class="taxfree">房本满五年</span></div><div class="priceInfo"><div class="totalPrice"><span>498</span>万</div><div class="unitPrice" data-hid="107100852490" data-rid="5011000010470" data-price="51447"><span>单价51447元/平米</span></div></div></div><div class="listButtonContainer"><div class="btn-follow followBtn" data-hid="107100852490"><span class="follow-text">关注</span></div><div class="compareBtn LOGCLICK" data-hid="107100852490" log-mod="107100852490" data-log_evtid="10230">加入对比</div></div></li><li class="clear LOGCLICKDATA" ><a class="noresultRecommend img " href="https://sh.lianjia.com/ershoufang/107100111854.html" target="_blank"data-log_index="5" data-el="ershoufang" data-housecode="107100111854" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrlogo.png?_v=2018122819393752" class="vr_item"><img class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2018122819393752" data-original="https://image1.ljcdn.com/310000-inspection/test-7474363c-0ffb-4710-91a9-3be2fb83499a.png.296x216.jpg" alt="永泰花苑.稀有毛坯电梯复式.地铁11号800米，配套成熟"></a><div class="info clear"><div class="title"><a class="" href="https://sh.lianjia.com/ershoufang/107100111854.html" target="_blank" data-log_index="5"  data-el="ershoufang" data-housecode="107100111854" data-is_focus="" data-sl="">永泰花苑.稀有毛坯电梯复式.地铁11号800米，配套成熟</a><!-- 拆分标签 --></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span><a href="https://sh.lianjia.com/xiaoqu/5011000010470/" target="_blank" data-log_index="5" data-el="region">永泰花苑 </a> | 3室3厅 | 136.72平米 | 南 北 | 毛坯 | 有电梯</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>高楼层(共11层)2006年建板楼  -  <a href="https://sh.lianjia.com/ershoufang/sanlin/" target="_blank">三林</a></div></div><div class="followInfo"><span class="starIcon"></span>376人关注 / 共11次带看 / 9个月以前发布</div><div class="tag"><span class="subway">近地铁</span><span class="vr">VR房源</span><span class="haskey">随时看房</span></div><div class="priceInfo"><div class="totalPrice"><span>665</span>万</div><div class="unitPrice" data-hid="107100111854" data-rid="5011000010470" data-price="48640"><span>单价48640元/平米</span></div></div></div><div class="listButtonContainer"><div class="btn-follow followBtn" data-hid="107100111854"><span class="follow-text">关注</span></div><div class="compareBtn LOGCLICK" data-hid="107100111854" log-mod="107100111854" data-log_evtid="10230">加入对比</div></div></li><li class="clear LOGCLICKDATA" ><a class="noresultRecommend img " href="https://sh.lianjia.com/ershoufang/107100868343.html" target="_blank"data-log_index="6" data-el="ershoufang" data-housecode="107100868343" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrlogo.png?_v=2018122819393752" class="vr_item"><img class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2018122819393752" data-original="https://image1.ljcdn.com/310000-inspection/prod-83c311bc-3d9d-4ee7-b6f6-26916074deca.jpg.296x216.jpg" alt="前滩板块 地铁11号线 南北两房 精装修 带地暖 视野宽"></a><div class="info clear"><div class="title"><a class="" href="https://sh.lianjia.com/ershoufang/107100868343.html" target="_blank" data-log_index="6"  data-el="ershoufang" data-housecode="107100868343" data-is_focus="" data-sl="">前滩板块 地铁11号线 南北两房 精装修 带地暖 视野宽</a><!-- 拆分标签 --></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span><a href="https://sh.lianjia.com/xiaoqu/5011000010470/" target="_blank" data-log_index="6" data-el="region">永泰花苑 </a> | 2室1厅 | 72.27平米 | 南 北 | 其他 | 有电梯</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>低楼层(共11层)2004年建板楼  -  <a href="https://sh.lianjia.com/ershoufang/sanlin/" target="_blank">三林</a></div></div><div class="followInfo"><span class="starIcon"></span>33人关注 / 共7次带看 / 24天以前发布</div><div class="tag"><span class="subway">近地铁</span><span class="vr">VR房源</span><span class="five">房本满两年</span></div><div class="priceInfo"><div class="totalPrice"><span>397</span>万</div><div class="unitPrice" data-hid="107100868343" data-rid="5011000010470" data-price="54933"><span>单价54933元/平米</span></div></div></div><div class="listButtonContainer"><div class="btn-follow followBtn" data-hid="107100868343"><span class="follow-text">关注</span></div><div class="compareBtn LOGCLICK" data-hid="107100868343" log-mod="107100868343" data-log_evtid="10230">加入对比</div></div></li><li class="clear LOGCLICKDATA" ><a class="noresultRecommend img " href="https://sh.lianjia.com/ershoufang/107100679680.html" target="_blank"data-log_index="7" data-el="ershoufang" data-housecode="107100679680" data-is_focus="1" data-sl=""><div class="focus_tag"></div><!-- 热推标签、埋点 --><img src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrlogo.png?_v=2018122819393752" class="vr_item"><img class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2018122819393752" data-original="https://image1.ljcdn.com/310000-inspection/test-3a0f0897-43a2-4ac3-ace4-3f5bb341c815.png.296x216.jpg" alt="永泰花苑 大两房总价低 位置成熟 精装修诚意出售"></a><div class="info clear"><div class="title"><a class="" href="https://sh.lianjia.com/ershoufang/107100679680.html" target="_blank" data-log_index="7"  data-el="ershoufang" data-housecode="107100679680" data-is_focus="1" data-sl="">永泰花苑 大两房总价低 位置成熟 精装修诚意出售</a><!-- 拆分标签 --></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span><a href="https://sh.lianjia.com/xiaoqu/5011000010470/" target="_blank" data-log_index="7" data-el="region">永泰花苑 </a> | 2室1厅 | 73.56平米 | 南 | 精装 | 有电梯</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>高楼层(共11层)2005年建板楼  -  <a href="https://sh.lianjia.com/ershoufang/sanlin/" target="_blank">三林</a></div></div><div class="followInfo"><span class="starIcon"></span>79人关注 / 共12次带看 / 3个月以前发布</div><div class="tag"><span class="subway">近地铁</span><span class="vr">VR房源</span></div><div class="priceInfo"><div class="totalPrice"><span>385</span>万</div><div class="unitPrice" data-hid="107100679680" data-rid="5011000010470" data-price="52339"><span>单价52339元/平米</span></div></div></div><div class="listButtonContainer"><div class="btn-follow followBtn" data-hid="107100679680"><span class="follow-text">关注</span></div><div class="compareBtn LOGCLICK" data-hid="107100679680" log-mod="107100679680" data-log_evtid="10230">加入对比</div></div></li><li class="clear LOGCLICKDATA" ><a class="noresultRecommend img " href="https://sh.lianjia.com/ershoufang/107100740920.html" target="_blank"data-log_index="8" data-el="ershoufang" data-housecode="107100740920" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrlogo.png?_v=2018122819393752" class="vr_item"><img class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2018122819393752" data-original="https://image1.ljcdn.com/310000-inspection/test-ef16bd03-6f7d-4656-ba2e-b3965210d7dc.png.296x216.jpg" alt="永泰花苑 3室2厅 660万"></a><div class="info clear"><div class="title"><a class="" href="https://sh.lianjia.com/ershoufang/107100740920.html" target="_blank" data-log_index="8"  data-el="ershoufang" data-housecode="107100740920" data-is_focus="" data-sl="">永泰花苑 3室2厅 660万</a><!-- 拆分标签 --></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span><a href="https://sh.lianjia.com/xiaoqu/5011000010470/" target="_blank" data-log_index="8" data-el="region">永泰花苑 </a> | 3室2厅 | 134.25平米 | 南 北 | 精装 | 有电梯</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>高楼层(共11层)2005年建板楼  -  <a href="https://sh.lianjia.com/ershoufang/sanlin/" target="_blank">三林</a></div></div><div class="followInfo"><span class="starIcon"></span>71人关注 / 共7次带看 / 2个月以前发布</div><div class="tag"><span class="subway">近地铁</span><span class="vr">VR房源</span></div><div class="priceInfo"><div class="totalPrice"><span>660</span>万</div><div class="unitPrice" data-hid="107100740920" data-rid="5011000010470" data-price="49163"><span>单价49163元/平米</span></div></div></div><div class="listButtonContainer"><div class="btn-follow followBtn" data-hid="107100740920"><span class="follow-text">关注</span></div><div class="compareBtn LOGCLICK" data-hid="107100740920" log-mod="107100740920" data-log_evtid="10230">加入对比</div></div></li><li class="clear LOGCLICKDATA" ><a class="noresultRecommend img " href="https://sh.lianjia.com/ershoufang/107100512564.html" target="_blank"data-log_index="9" data-el="ershoufang" data-housecode="107100512564" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrlogo.png?_v=2018122819393752" class="vr_item"><img class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2018122819393752" data-original="https://image1.ljcdn.com/310000-inspection/test-b447d0f1-bd5b-4aab-a93a-c668e36df6fd.png.296x216.jpg" alt="永泰花苑 三年装修 南北通透 明亮干净 婚装出售"></a><div class="info clear"><div class="title"><a class="" href="https://sh.lianjia.com/ershoufang/107100512564.html" target="_blank" data-log_index="9"  data-el="ershoufang" data-housecode="107100512564" data-is_focus="" data-sl="">永泰花苑 三年装修 南北通透 明亮干净 婚装出售</a><!-- 拆分标签 --><span class="yezhushuo tagBlock">房主自荐</span></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span><a href="https://sh.lianjia.com/xiaoqu/5011000010470/" target="_blank" data-log_index="9" data-el="region">永泰花苑 </a> | 2室1厅 | 73.64平米 | 南 北 | 精装 | 有电梯</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>中楼层(共11层)2004年建板楼  -  <a href="https://sh.lianjia.com/ershoufang/sanlin/" target="_blank">三林</a></div></div><div class="followInfo"><span class="starIcon"></span>134人关注 / 共9次带看 / 4个月以前发布</div><div class="tag"><span class="vr">VR房源</span></div><div class="priceInfo"><div class="totalPrice"><span>385</span>万</div><div class="unitPrice" data-hid="107100512564" data-rid="5011000010470" data-price="52282"><span>单价52282元/平米</span></div></div></div><div class="listButtonContainer"><div class="btn-follow followBtn" data-hid="107100512564"><span class="follow-text">关注</span></div><div class="compareBtn LOGCLICK" data-hid="107100512564" log-mod="107100512564" data-log_evtid="10230">加入对比</div></div></li><li class="clear LOGCLICKDATA" ><a class="noresultRecommend img " href="https://sh.lianjia.com/ershoufang/107100839777.html" target="_blank"data-log_index="10" data-el="ershoufang" data-housecode="107100839777" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrlogo.png?_v=2018122819393752" class="vr_item"><img class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2018122819393752" data-original="https://image1.ljcdn.com/310000-inspection/prod-43f61941-51f4-44ea-9058-9822edd99159.jpg.296x216.jpg" alt="永泰花苑 装修好 带新空调 一年前的装修 大两房"></a><div class="info clear"><div class="title"><a class="" href="https://sh.lianjia.com/ershoufang/107100839777.html" target="_blank" data-log_index="10"  data-el="ershoufang" data-housecode="107100839777" data-is_focus="" data-sl="">永泰花苑 装修好 带新空调 一年前的装修 大两房</a><!-- 拆分标签 --></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span><a href="https://sh.lianjia.com/xiaoqu/5011000010470/" target="_blank" data-log_index="10" data-el="region">永泰花苑 </a> | 2室1厅 | 72.72平米 | 南 | 其他 | 有电梯</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>高楼层(共11层)2004年建板楼  -  <a href="https://sh.lianjia.com/ershoufang/sanlin/" target="_blank">三林</a></div></div><div class="followInfo"><span class="starIcon"></span>12人关注 / 共2次带看 / 1个月以前发布</div><div class="tag"><span class="vr">VR房源</span></div><div class="priceInfo"><div class="totalPrice"><span>385</span>万</div><div class="unitPrice" data-hid="107100839777" data-rid="5011000010470" data-price="52943"><span>单价52943元/平米</span></div></div></div><div class="listButtonContainer"><div class="btn-follow followBtn" data-hid="107100839777"><span class="follow-text">关注</span></div><div class="compareBtn LOGCLICK" data-hid="107100839777" log-mod="107100839777" data-log_evtid="10230">加入对比</div></div></li><li class="clear LOGCLICKDATA" ><a class="noresultRecommend img " href="https://sh.lianjia.com/ershoufang/107100713831.html" target="_blank"data-log_index="11" data-el="ershoufang" data-housecode="107100713831" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img src="https://s1.ljcdn.com/feroot/pc/asset/img/vr/vrlogo.png?_v=2018122819393752" class="vr_item"><img class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2018122819393752" data-original="https://image1.ljcdn.com/310000-inspection/test-faddb335-590f-4674-aa52-96991bc37c5d.jpg.296x216.jpg" alt="永泰花苑板式三房 位置前后开阔 精装修"></a><div class="info clear"><div class="title"><a class="" href="https://sh.lianjia.com/ershoufang/107100713831.html" target="_blank" data-log_index="11"  data-el="ershoufang" data-housecode="107100713831" data-is_focus="" data-sl="">永泰花苑板式三房 位置前后开阔 精装修</a><!-- 拆分标签 --></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span><a href="https://sh.lianjia.com/xiaoqu/5011000010470/" target="_blank" data-log_index="11" data-el="region">永泰花苑 </a> | 3室2厅 | 98平米 | 南 北 | 精装 | 有电梯</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>低楼层(共18层)2005年建板楼  -  <a href="https://sh.lianjia.com/ershoufang/sanlin/" target="_blank">三林</a></div></div><div class="followInfo"><span class="starIcon"></span>12人关注 / 共0次带看 / 2个月以前发布</div><div class="tag"><span class="subway">近地铁</span><span class="vr">VR房源</span></div><div class="priceInfo"><div class="totalPrice"><span>520</span>万</div><div class="unitPrice" data-hid="107100713831" data-rid="5011000010470" data-price="53062"><span>单价53062元/平米</span></div></div></div><div class="listButtonContainer"><div class="btn-follow followBtn" data-hid="107100713831"><span class="follow-text">关注</span></div><div class="compareBtn LOGCLICK" data-hid="107100713831" log-mod="107100713831" data-log_evtid="10230">加入对比</div></div></li><li class="clear LOGCLICKDATA" ><a class="noresultRecommend img " href="https://sh.lianjia.com/ershoufang/107100408424.html" target="_blank"data-log_index="12" data-el="ershoufang" data-housecode="107100408424" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2018122819393752" data-original="https://image1.ljcdn.com/shfdfs-image/20171206/b25ed9ce-8ce8-4acd-97fd-eb33114a3c28.jpg.296x216.jpg" alt="永泰花苑 1室1厅 300万"></a><div class="info clear"><div class="title"><a class="" href="https://sh.lianjia.com/ershoufang/107100408424.html" target="_blank" data-log_index="12"  data-el="ershoufang" data-housecode="107100408424" data-is_focus="" data-sl="">永泰花苑 1室1厅 300万</a><!-- 拆分标签 --></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span><a href="https://sh.lianjia.com/xiaoqu/5011000010470/" target="_blank" data-log_index="12" data-el="region">永泰花苑 </a> | 1室1厅 | 54.78平米 | 南 | 其他 | 有电梯</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>高楼层(共11层)2004年建板楼  -  <a href="https://sh.lianjia.com/ershoufang/sanlin/" target="_blank">三林</a></div></div><div class="followInfo"><span class="starIcon"></span>26人关注 / 共3次带看 / 6个月以前发布</div><div class="tag"><span class="five">房本满两年</span></div><div class="priceInfo"><div class="totalPrice"><span>300</span>万</div><div class="unitPrice" data-hid="107100408424" data-rid="5011000010470" data-price="54765"><span>单价54765元/平米</span></div></div></div><div class="listButtonContainer"><div class="btn-follow followBtn" data-hid="107100408424"><span class="follow-text">关注</span></div><div class="compareBtn LOGCLICK" data-hid="107100408424" log-mod="107100408424" data-log_evtid="10230">加入对比</div></div></li><li class="clear LOGCLICKDATA" ><a class="noresultRecommend img " href="https://sh.lianjia.com/ershoufang/107100705380.html" target="_blank"data-log_index="13" data-el="ershoufang" data-housecode="107100705380" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2018122819393752" data-original="https://image1.ljcdn.com/310000-inspection/4ccee553-ba9d-4ab8-801a-55cede3b2fd2.jpg.296x216.jpg" alt="小区 采光好 *明户型 交通便利小区 前后小区花园"></a><div class="info clear"><div class="title"><a class="" href="https://sh.lianjia.com/ershoufang/107100705380.html" target="_blank" data-log_index="13"  data-el="ershoufang" data-housecode="107100705380" data-is_focus="" data-sl="">小区 采光好 *明户型 交通便利小区 前后小区花园</a><!-- 拆分标签 --></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span><a href="https://sh.lianjia.com/xiaoqu/5011000010470/" target="_blank" data-log_index="13" data-el="region">永泰花苑 </a> | 2室1厅 | 75.34平米 | 南 北 | 简装 | 有电梯</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>中楼层(共11层)2005年建板楼  -  <a href="https://sh.lianjia.com/ershoufang/sanlin/" target="_blank">三林</a></div></div><div class="followInfo"><span class="starIcon"></span>37人关注 / 共7次带看 / 2个月以前发布</div><div class="tag"><span class="taxfree">房本满五年</span></div><div class="priceInfo"><div class="totalPrice"><span>400</span>万</div><div class="unitPrice" data-hid="107100705380" data-rid="5011000010470" data-price="53093"><span>单价53093元/平米</span></div></div></div><div class="listButtonContainer"><div class="btn-follow followBtn" data-hid="107100705380"><span class="follow-text">关注</span></div><div class="compareBtn LOGCLICK" data-hid="107100705380" log-mod="107100705380" data-log_evtid="10230">加入对比</div></div></li><li class="clear LOGCLICKDATA" ><a class="noresultRecommend img " href="https://sh.lianjia.com/ershoufang/107100369892.html" target="_blank"data-log_index="14" data-el="ershoufang" data-housecode="107100369892" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2018122819393752" data-original="https://image1.ljcdn.com/310000-inspection/753cb0c1-96e3-42d9-b308-5d08745e9cb1.jpg.296x216.jpg" alt="动迁性质免增值税 底楼垫高 可做入户花园"></a><div class="info clear"><div class="title"><a class="" href="https://sh.lianjia.com/ershoufang/107100369892.html" target="_blank" data-log_index="14"  data-el="ershoufang" data-housecode="107100369892" data-is_focus="" data-sl="">动迁性质免增值税 底楼垫高 可做入户花园</a><!-- 拆分标签 --></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span><a href="https://sh.lianjia.com/xiaoqu/5011000010470/" target="_blank" data-log_index="14" data-el="region">永泰花苑 </a> | 2室1厅 | 72.76平米 | 南 | 简装 | 有电梯</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>低楼层(共11层)2005年建板楼  -  <a href="https://sh.lianjia.com/ershoufang/sanlin/" target="_blank">三林</a></div></div><div class="followInfo"><span class="starIcon"></span>55人关注 / 共3次带看 / 6个月以前发布</div><div class="tag"><span class="subway">近地铁</span></div><div class="priceInfo"><div class="totalPrice"><span>348</span>万</div><div class="unitPrice" data-hid="107100369892" data-rid="5011000010470" data-price="47829"><span>单价47829元/平米</span></div></div></div><div class="listButtonContainer"><div class="btn-follow followBtn" data-hid="107100369892"><span class="follow-text">关注</span></div><div class="compareBtn LOGCLICK" data-hid="107100369892" log-mod="107100369892" data-log_evtid="10230">加入对比</div></div></li><li class="clear LOGCLICKDATA" ><a class="noresultRecommend img " href="https://sh.lianjia.com/ershoufang/107100718595.html" target="_blank"data-log_index="15" data-el="ershoufang" data-housecode="107100718595" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2018122819393752" data-original="https://image1.ljcdn.com/310000-inspection/test-a8413813-cb5b-4c75-8552-030249f0fe71.png.296x216.jpg" alt="永泰花苑，小区位置好，少有的税少复式，业主诚售"></a><div class="info clear"><div class="title"><a class="" href="https://sh.lianjia.com/ershoufang/107100718595.html" target="_blank" data-log_index="15"  data-el="ershoufang" data-housecode="107100718595" data-is_focus="" data-sl="">永泰花苑，小区位置好，少有的税少复式，业主诚售</a><!-- 拆分标签 --></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span><a href="https://sh.lianjia.com/xiaoqu/5011000010470/" target="_blank" data-log_index="15" data-el="region">永泰花苑 </a> | 3室2厅 | 119.78平米 | 南 北 | 精装 | 有电梯</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>高楼层(共11层)2005年建板楼  -  <a href="https://sh.lianjia.com/ershoufang/sanlin/" target="_blank">三林</a></div></div><div class="followInfo"><span class="starIcon"></span>85人关注 / 共6次带看 / 2个月以前发布</div><div class="tag"><span class="taxfree">房本满五年</span></div><div class="priceInfo"><div class="totalPrice"><span>600</span>万</div><div class="unitPrice" data-hid="107100718595" data-rid="5011000010470" data-price="50092"><span>单价50092元/平米</span></div></div></div><div class="listButtonContainer"><div class="btn-follow followBtn" data-hid="107100718595"><span class="follow-text">关注</span></div><div class="compareBtn LOGCLICK" data-hid="107100718595" log-mod="107100718595" data-log_evtid="10230">加入对比</div></div></li><li class="clear LOGCLICKDATA" ><a class="noresultRecommend img " href="https://sh.lianjia.com/ershoufang/107100426560.html" target="_blank"data-log_index="16" data-el="ershoufang" data-housecode="107100426560" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2018122819393752" data-original="https://image1.ljcdn.com/x-se/hdic-frame/1f3e09da-c176-430b-b231-f054e5212f67.png.280x210.jpg" alt="近地铁 中房开发品质 三林热门高档住宅 11号线三林站"></a><div class="info clear"><div class="title"><a class="" href="https://sh.lianjia.com/ershoufang/107100426560.html" target="_blank" data-log_index="16"  data-el="ershoufang" data-housecode="107100426560" data-is_focus="" data-sl="">近地铁 中房开发品质 三林热门高档住宅 11号线三林站</a><!-- 拆分标签 --></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span><a href="https://sh.lianjia.com/xiaoqu/5011000010470/" target="_blank" data-log_index="16" data-el="region">永泰花苑 </a> | 2室1厅 | 72.59平米 | 南 北 | 毛坯 | 有电梯</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>低楼层(共11层)2004年建板楼  -  <a href="https://sh.lianjia.com/ershoufang/sanlin/" target="_blank">三林</a></div></div><div class="followInfo"><span class="starIcon"></span>26人关注 / 共1次带看 / 5个月以前发布</div><div class="tag"><span class="subway">近地铁</span><span class="taxfree">房本满五年</span></div><div class="priceInfo"><div class="totalPrice"><span>375</span>万</div><div class="unitPrice" data-hid="107100426560" data-rid="5011000010470" data-price="51661"><span>单价51661元/平米</span></div></div></div><div class="listButtonContainer"><div class="btn-follow followBtn" data-hid="107100426560"><span class="follow-text">关注</span></div><div class="compareBtn LOGCLICK" data-hid="107100426560" log-mod="107100426560" data-log_evtid="10230">加入对比</div></div></li><li class="clear LOGCLICKDATA" ><a class="noresultRecommend img " href="https://sh.lianjia.com/ershoufang/107100767149.html" target="_blank"data-log_index="17" data-el="ershoufang" data-housecode="107100767149" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2018122819393752" data-original="https://image1.ljcdn.com/x-se/hdic-frame/f65f4d49-23bc-4f9c-8c74-925fd2ee5b44.png.280x210.jpg" alt="次新小区，房东诚心出售，价格可谈，动迁所得"></a><div class="info clear"><div class="title"><a class="" href="https://sh.lianjia.com/ershoufang/107100767149.html" target="_blank" data-log_index="17"  data-el="ershoufang" data-housecode="107100767149" data-is_focus="" data-sl="">次新小区，房东诚心出售，价格可谈，动迁所得</a><!-- 拆分标签 --></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span><a href="https://sh.lianjia.com/xiaoqu/5011000010470/" target="_blank" data-log_index="17" data-el="region">永泰花苑 </a> | 1室1厅 | 54.55平米 | 南 | 其他 | 有电梯</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>中楼层(共11层)2005年建板楼  -  <a href="https://sh.lianjia.com/ershoufang/sanlin/" target="_blank">三林</a></div></div><div class="followInfo"><span class="starIcon"></span>26人关注 / 共5次带看 / 2个月以前发布</div><div class="tag"><span class="taxfree">房本满五年</span></div><div class="priceInfo"><div class="totalPrice"><span>290</span>万</div><div class="unitPrice" data-hid="107100767149" data-rid="5011000010470" data-price="53163"><span>单价53163元/平米</span></div></div></div><div class="listButtonContainer"><div class="btn-follow followBtn" data-hid="107100767149"><span class="follow-text">关注</span></div><div class="compareBtn LOGCLICK" data-hid="107100767149" log-mod="107100767149" data-log_evtid="10230">加入对比</div></div></li><li class="clear LOGCLICKDATA" ><a class="noresultRecommend img " href="https://sh.lianjia.com/ershoufang/107100609516.html" target="_blank"data-log_index="18" data-el="ershoufang" data-housecode="107100609516" data-is_focus="" data-sl=""><!-- 热推标签、埋点 --><img class="lj-lazy" src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=2018122819393752" data-original="" alt="永泰花苑 1室1厅 280万"></a><div class="info clear"><div class="title"><a class="" href="https://sh.lianjia.com/ershoufang/107100609516.html" target="_blank" data-log_index="18"  data-el="ershoufang" data-housecode="107100609516" data-is_focus="" data-sl="">永泰花苑 1室1厅 280万</a><!-- 拆分标签 --></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span><a href="https://sh.lianjia.com/xiaoqu/5011000010470/" target="_blank" data-log_index="18" data-el="region">永泰花苑 </a> | 1室1厅 | 59.03平米 | 南 | 其他 | 有电梯</div></div><div class="flood"><div class="positionInfo"><span class="positionIcon"></span>低楼层(共11层)2005年建板楼  -  <a href="https://sh.lianjia.com/ershoufang/sanlin/" target="_blank">三林</a></div></div><div class="followInfo"><span class="starIcon"></span>18人关注 / 共1次带看 / 3个月以前发布</div><div class="tag"><span class="taxfree">房本满五年</span></div><div class="priceInfo"><div class="totalPrice"><span>280</span>万</div><div class="unitPrice" data-hid="107100609516" data-rid="5011000010470" data-price="47434"><span>单价47434元/平米</span></div></div></div><div class="listButtonContainer"><div class="btn-follow followBtn" data-hid="107100609516"><span class="follow-text">关注</span></div><div class="compareBtn LOGCLICK" data-hid="107100609516" log-mod="107100609516" data-log_evtid="10230">加入对比</div></div></li></ul><!-- 无搜索结果 --><div id="noResultPush"></div><div class="contentBottom clear" ><div class="crumbs fl"><a href="/">链家网上海站</a><span >&nbsp;&gt;&nbsp;</span><h1><a href="/ershoufang/">上海二手房</a></h1></div><div class="page-box fr"><div class="page-box house-lst-page-box" comp-module='page' page-url="/ershoufang/pg{page}rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/"page-data='{"totalPage":1,"curPage":1}'></div>


</div></div><div style="display:none;"><p></p><p></p><p></p></div></div><!-- 右侧sidebar --><div class="rightLayout"><div class="rightContent"><div class="map"><div class="pic"></div><button id="btn-map" data-keyword="永泰花苑">地图找 永泰花苑</button></div><div class="price" id='priceSideBarContainer' log-mod="recommand_price"></div><div class="suggestAgent" id='suggestAgentContainer' log-mod="ershoufang_list_recommend-agent"></div><div class="suggestHouse" id="suggestHouseContainer" log-mod="recommand_house"></div><div class="suggestCommunity" id="suggestCommunityContainer" log-mod="ershoufang_list_recommend-community"></div><div class="wenda zixun" id="pushZixunContainer" log-mod="recommand_zixun"></div><div class="wenda SCROLLVIEWLOG" id="pushWendaContainer" log-mod="recommand_wenda"></div><div class="wenda SCROLLVIEWLOG" id="pushBaikeContainer" log-mod="recommand_baike"></div><div class="download"><div class="title">下载链家APP</div><div class="qr-code"><img width="94" height="94" src="//ajax.api.lianjia.com/qr/getDownloadQr?location=right&ljweb_channel_key=ershoufang_search" alt="下载链家app"><div class="text"><p>扫描上方二维码</p><p>随时查看新房源</p><p class="get-more"><a href="//www.lianjia.com/client/">了解更多<img width="9" height="9" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEUAAACcn6Gfn5+an5+bnqCbnqGfn5+cn6EV6DbuAAAAB3RSTlMA0BAw8LAgvf5k9AAAAEdJREFUKM9jIBOkBqMJhBcqoAmUC6EKmJSjKWEWR1eiiK6ECZsSA3QlzuhKSihRghDA0EJ/BWIoCgzh4YMIZALRYBrMQAkAAF5bGMBkrwzqAAAAAElFTkSuQmCC"></a></p></div></div></div><div class="download download-fixed" style="display: none;"><div class="title">下载链家APP</div><div class="qr-code"><img width="94" height="94" src="//ajax.api.lianjia.com/qr/getDownloadQr?location=right&ljweb_channel_key=ershoufang_search" alt="下载链家app"><div class="text"><p>扫描上方二维码</p><p>随时查看新房源</p><p class="get-more"><a href="//www.lianjia.com/client/">了解更多<img width="9" height="9" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEUAAACcn6Gfn5+an5+bnqCbnqGfn5+cn6EV6DbuAAAAB3RSTlMA0BAw8LAgvf5k9AAAAEdJREFUKM9jIBOkBqMJhBcqoAmUC6EKmJSjKWEWR1eiiK6ECZsSA3QlzuhKSihRghDA0EJ/BWIoCgzh4YMIZALRYBrMQAkAAF5bGMBkrwzqAAAAAElFTkSuQmCC"></a></p></div></div></div></div></div><div style="clear:both"></div></div><div id="pushCommunity" class="pushCommunity" log-mod="ershoufang_list_recommend-community"></div><div id="newHousePush" class="newHousePush"></div><div class="saveMegmask"></div><div class="saveok"><div class="fl"></div><div class="fr"><span>已成功保存搜索条件！</span><p>您可在搜索框右侧下拉列表中快速使用该条件。该条件有新房源出现时，我们将会用站内提醒的方式来通知您</p><label class="close">确定</label></div></div><div class="saveerror"><div class="fl"></div><div class="fr"><span>你的搜索条件已达到上限！</span><p>您可在搜索框右侧下拉列表中快速使用该条件。该条件有新房源出现时，我们将会用站内提醒的方式来通知您。</p><a href="//user.lianjia.com/site/searchlist/" rel="nofollow">个人中心</a><label  class="close">取消</label></div></div><div class="pagination_group_a"><a href="/ershoufang/rs%E6%B0%B8%E6%B3%B0%E8%8A%B1%E8%8B%91/"></a></div><div class="footer"><div class="wrapper"><div class="f-title"><div class="fl"><ul><li><a href="https://sh.lianjia.com/about/aboutlianjia/" rel="nofollow" target="_blank">关于链家</a></li><li><a href="https://sh.lianjia.com/about/contactus/" rel="nofollow" target="_blank">联系我们</a></li><li><a href="http://join.lianjia.com/" rel="nofollow" target="_blank">加入我们</a></li><li><a href="https://www.lianjia.com/privacy/" rel="nofollow" target="_blank">隐私声明</a></li><li><a href="https://sh.lianjia.com/sitemap/" target="_blank">网站地图</a></li><li><a href="https://page.lianjia.com/subject/youlian.html" rel="nofollow" target="_blank">友情链接</a></li></ul></div><div class="fr">官方客服 1010 9666</div></div><div class="lianjia-link-box"><div class="fl"><div class="tab"><span  class="hover">二手房</span><span >楼盘</span><span >小区</span><span >区域租房</span><span >小区租房</span></div><div class="link-list"><div><dd><a target="_blank" href="https://fs.lianjia.com/ershoufang/">佛山二手房</a><a target="_blank" href="https://hf.lianjia.com/ershoufang/">合肥二手房</a><a target="_blank" href="https://sjz.lianjia.com/ershoufang/">石家庄二手房</a><a target="_blank" href="https://bh.lianjia.com/ershoufang/">北海二手房</a><a target="_blank" href="https://nj.lianjia.com/ershoufang/">南京二手房</a><a target="_blank" href="https://cc.lianjia.com/ershoufang/">长春二手房</a><a target="_blank" href="https://quanzhou.lianjia.com/ershoufang/">泉州二手房</a><a target="_blank" href="https://sr.lianjia.com/ershoufang/">上饶二手房</a><a target="_blank" href="https://wx.lianjia.com/ershoufang/">无锡二手房</a><a target="_blank" href="https://sy.lianjia.com/ershoufang/">沈阳二手房</a><a target="_blank" href="https://yc.lianjia.com/ershoufang/">盐城二手房</a><a target="_blank" href="https://hanzhong.lianjia.com/ershoufang/">汉中二手房</a><a target="_blank" href="https://hui.lianjia.com/ershoufang/">惠州二手房</a><a target="_blank" href="https://tj.lianjia.com/ershoufang/">天津二手房</a><a target="_blank" href="https://su.lianjia.com/ershoufang/">苏州二手房</a><a target="_blank" href="https://dazhou.lianjia.com/ershoufang/">达州二手房</a><a target="_blank" href="https://dd.lianjia.com/ershoufang/">丹东二手房</a><a target="_blank" href="https://weihai.lianjia.com/ershoufang/">威海二手房</a><a target="_blank" href="https://cd.lianjia.com/ershoufang/">成都二手房</a><a target="_blank" href="https://hrb.lianjia.com/ershoufang/">哈尔滨二手房</a><a target="_blank" href="https://xy.lianjia.com/ershoufang/">襄阳二手房</a><a target="_blank" href="https://cs.lianjia.com/ershoufang/">长沙二手房</a><a target="_blank" href="https://luoyang.lianjia.com/ershoufang/">洛阳二手房</a><a target="_blank" href="https://zhangzhou.lianjia.com/ershoufang/">漳州二手房</a><a target="_blank" href="https://bj.lianjia.com/ershoufang/">北京二手房</a><a target="_blank" href="https://san.lianjia.com/ershoufang/">三亚二手房</a><a target="_blank" href="https://taizhou.lianjia.com/ershoufang/">台州二手房</a><a target="_blank" href="https://nt.lianjia.com/ershoufang/">南通二手房</a><a target="_blank" href="https://lz.lianjia.com/ershoufang/">兰州二手房</a><a target="_blank" href="https://yichang.lianjia.com/ershoufang/">宜昌二手房</a><a target="_blank" href="https://hz.lianjia.com/ershoufang/">杭州二手房</a><a target="_blank" href="https://nb.lianjia.com/ershoufang/">宁波二手房</a><a target="_blank" href="https://liangshan.lianjia.com/ershoufang/">凉山二手房</a><a target="_blank" href="https://wz.lianjia.com/ershoufang/">温州二手房</a><a target="_blank" href="https://zb.lianjia.com/ershoufang/">淄博二手房</a><a target="_blank" href="https://nn.lianjia.com/ershoufang/">南宁二手房</a><a target="_blank" href="https://jn.lianjia.com/ershoufang/">济南二手房</a><a target="_blank" href="https://mianyang.lianjia.com/ershoufang/">绵阳二手房</a><a target="_blank" href="https://jian.lianjia.com/ershoufang/">吉安二手房</a><a target="_blank" href="https://gz.lianjia.com/ershoufang/">广州二手房</a></dd></div><div><dd><a target="_blank" href="https://ms.fang.lianjia.com/loupan/">眉山楼盘</a><a target="_blank" href="https://sy.fang.lianjia.com/loupan/">沈阳楼盘</a><a target="_blank" href="https://gy.fang.lianjia.com/loupan/">贵阳楼盘</a><a target="_blank" href="https://zjk.fang.lianjia.com/loupan/">张家口楼盘</a><a target="_blank" href="https://hk.fang.lianjia.com/loupan/">海口楼盘</a><a target="_blank" href="https://zh.fang.lianjia.com/loupan/">珠海楼盘</a><a target="_blank" href="https://xt.fang.lianjia.com/loupan/">邢台楼盘</a><a target="_blank" href="https://qhd.fang.lianjia.com/loupan/">秦皇岛楼盘</a><a target="_blank" href="https://da.fang.lianjia.com/loupan/">定安楼盘</a><a target="_blank" href="https://zz.fang.lianjia.com/loupan/">郑州楼盘</a><a target="_blank" href="https://jn.fang.lianjia.com/loupan/">济南楼盘</a><a target="_blank" href="https://cc.fang.lianjia.com/loupan/">长春楼盘</a><a target="_blank" href="https://zhangzhou.fang.lianjia.com/loupan/">漳州楼盘</a><a target="_blank" href="https://jx.fang.lianjia.com/loupan/">嘉兴楼盘</a><a target="_blank" href="https://km.fang.lianjia.com/loupan/">昆明楼盘</a><a target="_blank" href="https://leshan.fang.lianjia.com/loupan/">乐山楼盘</a><a target="_blank" href="https://qd.fang.lianjia.com/loupan/">青岛楼盘</a><a target="_blank" href="https://lf.fang.lianjia.com/loupan/">廊坊楼盘</a><a target="_blank" href="https://cq.fang.lianjia.com/loupan/">重庆楼盘</a><a target="_blank" href="https://xn.fang.lianjia.com/loupan/">咸宁楼盘</a><a target="_blank" href="https://qz.fang.lianjia.com/loupan/">琼中楼盘</a><a target="_blank" href="https://ly.fang.lianjia.com/loupan/">龙岩楼盘</a><a target="_blank" href="https://ls.fang.lianjia.com/loupan/">陵水楼盘</a><a target="_blank" href="https://hz.fang.lianjia.com/loupan/">杭州楼盘</a><a target="_blank" href="https://hf.fang.lianjia.com/loupan/">合肥楼盘</a><a target="_blank" href="https://cm.fang.lianjia.com/loupan/">澄迈楼盘</a><a target="_blank" href="https://wc.fang.lianjia.com/loupan/">文昌楼盘</a><a target="_blank" href="https://jz.fang.lianjia.com/loupan/">晋中楼盘</a><a target="_blank" href="https://hd.fang.lianjia.com/loupan/">邯郸楼盘</a><a target="_blank" href="https://sjz.fang.lianjia.com/loupan/">石家庄楼盘</a><a target="_blank" href="https://cs.fang.lianjia.com/loupan/">长沙楼盘</a><a target="_blank" href="https://dali.fang.lianjia.com/loupan/">大理楼盘</a><a target="_blank" href="https://xsbn.fang.lianjia.com/loupan/">西双版纳楼盘</a><a target="_blank" href="https://nj.fang.lianjia.com/loupan/">南京楼盘</a><a target="_blank" href="https://wzs.fang.lianjia.com/loupan/">五指山楼盘</a><a target="_blank" href="https://bj.fang.lianjia.com/loupan/">北京楼盘</a><a target="_blank" href="https://qh.fang.lianjia.com/loupan/">琼海楼盘</a><a target="_blank" href="https://hui.fang.lianjia.com/loupan/">惠州楼盘</a><a target="_blank" href="https://lg.fang.lianjia.com/loupan/">临高楼盘</a><a target="_blank" href="https://nt.fang.lianjia.com/loupan/">南通楼盘</a></dd></div><div><dd><a target="_blank" href="https://nc.lianjia.com/xiaoqu/">南昌小区二手房</a><a target="_blank" href="https://luoyang.lianjia.com/xiaoqu/">洛阳小区二手房</a><a target="_blank" href="https://xinxiang.lianjia.com/xiaoqu/">新乡小区二手房</a><a target="_blank" href="https://zhanjiang.lianjia.com/xiaoqu/">湛江小区二手房</a><a target="_blank" href="https://mianyang.lianjia.com/xiaoqu/">绵阳小区二手房</a><a target="_blank" href="https://hui.lianjia.com/xiaoqu/">惠州小区二手房</a><a target="_blank" href="https://jx.lianjia.com/xiaoqu/">嘉兴小区二手房</a><a target="_blank" href="https://mas.lianjia.com/xiaoqu/">马鞍山小区二手房</a><a target="_blank" href="https://gy.lianjia.com/xiaoqu/">贵阳小区二手房</a><a target="_blank" href="https://quanzhou.lianjia.com/xiaoqu/">泉州小区二手房</a><a target="_blank" href="https://jn.lianjia.com/xiaoqu/">济南小区二手房</a><a target="_blank" href="https://cc.lianjia.com/xiaoqu/">长春小区二手房</a><a target="_blank" href="https://xc.lianjia.com/xiaoqu/">许昌小区二手房</a><a target="_blank" href="https://yinchuan.lianjia.com/xiaoqu/">银川小区二手房</a><a target="_blank" href="https://jiangmen.lianjia.com/xiaoqu/">江门小区二手房</a><a target="_blank" href="https://cq.lianjia.com/xiaoqu/">重庆小区二手房</a><a target="_blank" href="https://jh.lianjia.com/xiaoqu/">金华小区二手房</a><a target="_blank" href="https://gl.lianjia.com/xiaoqu/">桂林小区二手房</a><a target="_blank" href="https://zs.lianjia.com/xiaoqu/">中山小区二手房</a><a target="_blank" href="https://hhht.lianjia.com/xiaoqu/">呼和浩特小区二手房</a><a target="_blank" href="https://kf.lianjia.com/xiaoqu/">开封小区二手房</a><a target="_blank" href="https://xianyang.lianjia.com/xiaoqu/">咸阳小区二手房</a><a target="_blank" href="https://gz.lianjia.com/xiaoqu/">广州小区二手房</a><a target="_blank" href="https://qd.lianjia.com/xiaoqu/">青岛小区二手房</a><a target="_blank" href="https://nt.lianjia.com/xiaoqu/">南通小区二手房</a><a target="_blank" href="https://yichang.lianjia.com/xiaoqu/">宜昌小区二手房</a><a target="_blank" href="https://nb.lianjia.com/xiaoqu/">宁波小区二手房</a><a target="_blank" href="https://jian.lianjia.com/xiaoqu/">吉安小区二手房</a><a target="_blank" href="https://yc.lianjia.com/xiaoqu/">盐城小区二手房</a><a target="_blank" href="https://linyi.lianjia.com/xiaoqu/">临沂小区二手房</a><a target="_blank" href="https://sr.lianjia.com/xiaoqu/">上饶小区二手房</a><a target="_blank" href="https://jl.lianjia.com/xiaoqu/">吉林小区二手房</a><a target="_blank" href="https://zhangzhou.lianjia.com/xiaoqu/">漳州小区二手房</a><a target="_blank" href="https://changzhou.lianjia.com/xiaoqu/">常州小区二手房</a><a target="_blank" href="https://hz.lianjia.com/xiaoqu/">杭州小区二手房</a><a target="_blank" href="https://cd.lianjia.com/xiaoqu/">成都小区二手房</a><a target="_blank" href="https://yt.lianjia.com/xiaoqu/">烟台小区二手房</a><a target="_blank" href="https://aq.lianjia.com/xiaoqu/">安庆小区二手房</a><a target="_blank" href="https://huangshi.lianjia.com/xiaoqu/">黄石小区二手房</a><a target="_blank" href="https://su.lianjia.com/xiaoqu/">苏州小区二手房</a></dd></div><div><dd><a target="_blank" href="https://sz.zu.ke.com/ditiezufang/li2415414406450926s100021247/">景田租房</a><a target="_blank" href="https://bj.zu.ke.com/ditiezufang/li46461179s20702/">来广营租房</a><a target="_blank" href="https://xm.zu.ke.com/zufang/gulangyu/">鼓浪屿租房</a><a target="_blank" href="https://bj.zu.ke.com/ditiezufang/li656s43137680/">陶然亭租房</a><a target="_blank" href="https://sz.zu.ke.com/ditiezufang/li110460692s100021226/">桃园租房</a><a target="_blank" href="https://sjz.zu.ke.com/zufang/erzhong/">二中租房</a><a target="_blank" href="https://nj.zu.ke.com/zufang/lishui/">溧水租房</a><a target="_blank" href="https://bj.zu.ke.com/zufang/wudaokou/">五道口租房</a><a target="_blank" href="https://hz.zu.ke.com/apartment/7940.html "> 秀里华庭</a><a target="_blank" href="https://bj.zu.ke.com/zufang/bajiao1/">八角租房</a><a target="_blank" href="https://sz.zu.ke.com/ditiezufang/li2415414406450926s2415414841585702/">下梅林租房</a><a target="_blank" href="https://ty.zu.ke.com/zufang/yingzequ/">迎泽区租房</a><a target="_blank" href="https://zz.zu.ke.com/zz/apartment/10507.html "> 正弘数码公寓</a><a target="_blank" href="https://sy.zu.ke.com/zufang/hepingqu/">和平区租房</a><a target="_blank" href="https://sh.zu.ke.com/zufang/waigaoqiao/">外高桥租房</a><a target="_blank" href="https://tj.zu.ke.com/zufang/hebei/">河北租房</a><a target="_blank" href="https://gz.zu.ke.com/zufang/luochongwei/">罗冲围租房</a><a target="_blank" href="https://zs.zu.ke.com/zufang/tanzhouzhen/">坦洲镇租房</a><a target="_blank" href="https://sh.zu.ke.com/zufang/putuo/">普陀租房</a><a target="_blank" href="https://dg.zu.ke.com/zufang/weiyuan/">威远租房</a><a target="_blank" href="https://zs.zu.ke.com/zufang/guzhenzhen1/">古镇镇租房</a><a target="_blank" href="https://bj.zu.ke.com/ditiezufang/li653s20669/">通州北苑租房</a><a target="_blank" href="https://sh.zu.ke.com/zufang/zhabei/">闸北租房</a><a target="_blank" href="https://wh.zu.ke.com/zufang/houhu/">后湖租房</a><a target="_blank" href="https://fs.zu.ke.com/zufang/lecong/">乐从租房</a><a target="_blank" href="https://qd.zu.ke.com/zufang/jiaozhou1/">胶州租房</a><a target="_blank" href="https://hz.zu.ke.com/zufang/renhe2/">仁和租房</a><a target="_blank" href="https://gz.zu.ke.com/ditiezufang/li110460686s100021120/">赤岗租房</a><a target="_blank" href="https://qd.zu.ke.com/zufang/pingdu1/">平度租房</a><a target="_blank" href="https://su.zu.ke.com/zufang/xiangshan/">香山租房</a><a target="_blank" href="https://cd.zu.ke.com/zufang/chengyulijiao/">成渝立交租房</a><a target="_blank" href="https://nj.zu.ke.com/zufang/gaoxinqu2/">高新区租房</a><a target="_blank" href="https://sz.zu.ke.com/ditiezufang/li110460696s100021312/">大学城租房</a><a target="_blank" href="https://hz.zu.ke.com/ditiezufang/li110460707s100021560/">西湖文化广场租房</a><a target="_blank" href="https://gz.zu.ke.com/ditiezufang/li110460685s100021057/">车陂南租房</a><a target="_blank" href="https://qd.zu.ke.com/zufang/jiaonan1/">胶南租房</a><a target="_blank" href="https://dl.zu.ke.com/ditiezufang/li110458006s100020989/">开发区租房</a><a target="_blank" href="https://nj.zu.ke.com/apartment/1365.html "> 建宁路</a><a target="_blank" href="https://sh.zu.ke.com/zufang/wujing/">吴泾租房</a><a target="_blank" href="https://sh.zu.ke.com/zufang/pudong/">浦东租房</a></dd></div><div><dd><a target="_blank" href="https://xy.zu.ke.com/zufang/c8752130866727546/">电信小区租房
</a><a target="_blank" href="https://huangshi.zu.ke.com/zufang/c8873130766065993/">城市花园租房
</a><a target="_blank" href="https://cq.zu.ke.com/zufang/c3611099910319/">世纪新村租房
</a><a target="_blank" href="https://jx.zu.ke.com/zufang/c8220032561102473/">亲亲家园租房
</a><a target="_blank" href="https://jx.zu.ke.com/zufang/c8220033811449866/">亲亲家园租房
</a><a target="_blank" href="https://sh.zu.ke.com/zufang/c5011000019631/">锦园小区租房
</a><a target="_blank" href="https://luoyang.zu.ke.com/zufang/c8858130867784552/">阳光新城租房
</a><a target="_blank" href="https://hz.zu.ke.com/zufang/c1811047236615/">中天西城纪租房
</a><a target="_blank" href="https://sjz.zu.ke.com/zufang/c3220024371256407/">安联青年城租房
</a><a target="_blank" href="https://bj.zu.ke.com/zufang/c1111027374271/">富力爱丁堡公馆租房
</a><a target="_blank" href="https://hrb.zu.ke.com/zufang/c4220033015199001/">红旗大街租房
</a><a target="_blank" href="https://xy.zu.ke.com/zufang/c8752131159284771/">华龙小区租房
</a><a target="_blank" href="https://gz.zu.ke.com/zufang/c2111103317036/">东风广场租房
</a><a target="_blank" href="https://huangshi.zu.ke.com/zufang/c8873132198054142/">锦绣江南租房
</a><a target="_blank" href="https://dl.zu.ke.com/zufang/c1311063597572/">小平岛租房
</a><a target="_blank" href="https://sz.zu.ke.com/zufang/c2411049023431/">金港华庭租房
</a><a target="_blank" href="https://sy.zu.ke.com/zufang/c3111058006329/">假日蓝湾租房
</a><a target="_blank" href="https://zhuzhou.zu.ke.com/zufang/c8881130539575734/">蓝天花园租房
</a><a target="_blank" href="https://hrb.zu.ke.com/zufang/c4220031706019141/">师大嘉园租房
</a><a target="_blank" href="https://qd.zu.ke.com/zufang/c1511041240796/">东方花园租房
</a><a target="_blank" href="https://sz.zu.ke.com/zufang/c2411063479536/">新一代国际公寓租房
</a><a target="_blank" href="https://bj.zu.ke.com/zufang/c1111027380302/">望京花园东区租房
</a><a target="_blank" href="https://sz.zu.ke.com/zufang/c2411050608894/">西岸观邸租房
</a><a target="_blank" href="https://lz.zu.ke.com/zufang/c8748129735942176/">和平新村租房
</a><a target="_blank" href="https://bj.zu.ke.com/zufang/c1111027379489/">世茂工三租房
</a><a target="_blank" href="https://hrb.zu.ke.com/zufang/c4220031800460539/">朝阳小区租房
</a><a target="_blank" href="https://sr.zu.ke.com/zufang/c8847131084832845/">绿苑小区租房
</a><a target="_blank" href="https://sjz.zu.ke.com/zufang/c327013610303297/">新都汇租房
</a><a target="_blank" href="https://zz.zu.ke.com/zufang/c3311058230995/">名门盛世租房
</a><a target="_blank" href="https://zb.zu.ke.com/zufang/c8848129359460211/">世纪花园租房
</a><a target="_blank" href="https://jx.zu.ke.com/zufang/c8220028352397526/">亲亲家园租房
</a><a target="_blank" href="https://sh.zu.ke.com/zufang/c509821540057366/">阳光花苑租房
</a><a target="_blank" href="https://sh.zu.ke.com/zufang/c5011000002419/">科盛公寓租房
</a><a target="_blank" href="https://hrb.zu.ke.com/zufang/c4220031656732381/">枫蓝国际租房
</a><a target="_blank" href="https://sh.zu.ke.com/zufang/c5011000012501/">昆阳小区租房
</a><a target="_blank" href="https://xianyang.zu.ke.com/zufang/c895311060375198/">铁路小区租房
</a><a target="_blank" href="https://yichang.zu.ke.com/zufang/c8751130892952062/">江临天下租房
</a><a target="_blank" href="https://cq.zu.ke.com/zufang/c3611100655394/">阳光小区租房
</a><a target="_blank" href="https://su.zu.ke.com/zufang/c2311054366380/">绿城花园租房
</a><a target="_blank" href="https://zb.zu.ke.com/zufang/c8848129368896864/">世纪花园租房
</a></dd></div></div></div><div class="clear"></div></div><div class="bottom"><div class="copyright fl">链家网（北京）科技有限公司 | 网络经营许可证 京ICP备16057509号-2 | © Copyright©2010-2019 链家网Lianjia.com版权所有</div><div style="width:300px;color: #888c8e;font-size: 12px;line-height: 20px;"><a target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010802024019" style="display:inline-block;text-decoration:none;height:20px;line-height:20px;"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/home/beian.png?_v=2018122819393752"" style="float:left;"><p style="float:left;height:20px;line-height:20px;margin: 0px 0px 0px 5px;color: #888c8e;">京公网安备 11010802024019号</p></a></div></div></div></div>

<script src="https://s1.ljcdn.com/feroot/pc/asset/base/fe.js?_v=2018122819393752"></script><script src="https://s1.ljcdn.com/feroot/pc/asset/common/common.js?_v=2018122819393752"></script><div style="display:none"><script src="https://s1.ljcdn.com/feroot/dep/ljanalytics.js?_v=2018122819393752"></script></div><div id="only" data-city="sh" data-page="ershoufang_search"></div>
<script>var path = 'https://s1.ljcdn.com/feroot/pc/asset?_v=2018122819393752'.split("?");require.config({baseUrl: path[0],paths: {'echarts' : '../../dep/echarts-1.4.1/build/echarts','echarts/chart/bar' : '../../dep/echarts-1.4.1/build/echarts','echarts/chart/line' : '../../dep/echarts-1.4.1/build/echarts','echarts/chart/pie' : '../../dep/echarts-1.4.1/build/echarts','echarts3' : '../../dep/echarts3/echarts3','common': 'common','jquery-ui': '../../dep/jquery-ui/jquery-ui.min','zeroclipboard': '../../dep/zeroclipboard-2.2.0/ZeroClipboard'},urlArgs:  path[1]});var feData = {"cityName": "北京","getFavHouseUrl":       "/api/gethousefav","setFavHouseUrl":       "/api/sethousefav","getLastSearch":        "/api/getlastsearch","getCommunityHistory":  "/api/getcommunityhistory","verifyHouse":          "/api/verifyHouse","getUser":              "/api/getUser","verifyCode":           "/verifycode/getVerifyCode","complaint":            "/api/complaint","getDecoration":        "/api/getDecoration","trendData" :           "/site/getpicinfo"}</script>
<script type="text/template" id="priceSideBarTpl">
<%if(tag !== 'school'){%>
  <div class="title"><%=name%>最新参考均价</div>
  <div class="priceMap" id="priceChartContainer"></div>
  <a href="<%=fangjia_url%>" class="unitPrice" target="_blank">
    <span><%=month_trans%></span>元/平米
  </a>
  <div class="info">
    <a href="<%=fangjia_url%>" target="_blank">环比上月均价<%=month_trans_ratio>=0?'上涨':'下降'%> <%=month_trans_ratio%>%</a>
    <a href="<%=chengjiao_url%>" target="_blank">/ 近90天成交<%=sold_90_day%>套</a>
    <%if(tag === '小区'){%>
    <div>
      <a class="cardMoreDetail" href="<%=url%>" target="_blank">查看小区详情>></a>
    </div>
    <%}%>
  </div>
<%}else{%>
  <a class="title" href="<%=url%>" target="_blank"><%=name%></a>
  <div class="unitPrice school">
    <span><%=min_unit_price%></span>万元起
  </div>
  <div class="info">
    <a href="<%=url%>" target="_blank">本学区目前有在售二手房<%=sell_num%>套，划片小区<%=resblock_nums%>个</a>
    <a class="cardMoreDetail" href="<%=url%>"  target="_blank">查看学区详情>></a>
  </div>
<%}%>
</script>

<script type="text/template" id="suggestAgentTpl">
  <div class="title">推荐置业顾问</div>
  <div class="agent">
    <a class="img <%= (desc.search('学区') > -1) ? '': 'LOGVIEW LOGCLICK'%>" href="<%=url%>" target="_blank" data-bl="agent_<%= (desc.search('学区') > -1) ? 'school': 'community'%>" data-el="<%=ucid%>" data-log_id="20001">
      <img src="<%=photo_url%>" alt="">
    </a>
    <div class="info">
      <div class="name">
        <a href="<%=url%>" target="_blank" data-bl="agent_<%= (desc.search('学区') > -1) ? 'school': 'community'%>" data-el="<%=ucid%>" class="<%= (desc.search('学区') > -1) ? '': 'LOGCLICK'%>" data-log_id="20001"><%=name%></a>
        <a class="lianjiaim-createtalk im-talk <%= (desc.search('学区') > -1) ? '': 'LOGCLICK'%>" style="padding: 1px 0 !important;" title="在线咨询" data-ucid="<%=ucid%>" data-bl="agentim_<%= (desc.search('学区') > -1) ? 'school': 'community'%>" data-el="<%=ucid%>" data-log_id="20001" data-source-port="PC:ershou_ershoufang_list_xiaoquguwen" data-source-extends=<%=JSON.stringify(communityId)%>></a>
      </div>
      <div class="phone"><%=phone%></div>
    </div>
  </div>
  <div class="agentInfo" title="<%=desc%>"><%=formatDesc%></div>
</script>
<script type="text/template" id="suggestHouseTpl">
  <a class="img" href="<%=url%>" target="_blank" data-bl="list" data-log_index="<%=index+1%>">
    <img src="<%=img_url%>" alt="">
    <div class="cover"></div>
    <div class="title">
      <span><%=title%></span>&nbsp;
    </div>
  </a>
  <div class="pointContainer">
  <%for(var i = 0; i < total; i++){%>
    <%if(index === i){%>
      <span data-index="<%=i%>" class="point selected"></span>
    <%}else{%>
      <span data-index="<%=i%>" class="point"></span>
    <%}%>
  <%}%>
  </div>
</script>
<script type="text/template" id="suggestCommunityTpl">
  <div class="title">小区推荐</div>
  <ul>
  <%for(var i = 0; i < list.length; i++){%>
    <li>
      <a href="<%=list[i].url%>" class="img LOGVIEW LOGCLICK" data-log_id="30001" target="_blank" data-log_index="<%=i+1%>" data-bl="<%=$.trim($('.list-more dl:first dt').text()) === '小区' ? 'community' : 'bizcircle'%>" data-el="">
        <%if(list[i].pic) {%>
          <img src="<%=list[i].picUri%>.280x210.jpg">
        <%}else{%>
          <span class="noimg">暂无图片</span>
        <%}%>
        <div class="price">
          <%if(list[i].price!=0 && list[i].price) {%><%=parseFloat(list[i].price, 10).toFixed()%>元/平<%}else{%>暂无均价<%}%>
        </div>
      </a>
      <div class="info clear">
        <a href="<%=list[i].url%>" target="_blank" class="fl"><%=list[i].name%></a>
        <div class="fr"><%=list[i].sellNum%>套在售</div>
      </div>
      <div class="desc"><%=list[i].desc%></div>
    </li>
  <%}%>
  </ul>
</script>
<script type="text/template" id="pushZhuanjiaTpl">
  <span class="name">推荐学区顾问</span>
  <span class="fl pic">
    <img src='<%=list.photoPath%>'>
  </span>
  <span class="fl">
    <a href="<%=list.agentUrl%>" target="_blank"><%=list.name%></a>
    <a class="lianjiaim-createtalk im-talk" style="display: none;" title="在线咨询" data-ucid="<%=list.agent_ucid%>"></a>
    <p class="tel"><%=list.phoneNumber%></p>
  </span>
  <p class="tips">
    <%=list.desc%>
  </p>
</script>

<script type="text/template" id="pushXuexiaoTpl">
  <div class="title"><%=data.regionName%>近期热门学校</div>
  <ul>
  <% var list = data.list;for(var i = 0;i < list.length; i++){%>
    <li class="li<%=i%>">
      <i></i>
      <a class="info" href="<%=list[i].viewUrl%>" target="_blank"><%=list[i].schoolName%></a>
      <span><%=list[i].viewCount%>浏览</span>
    </li>
  <%}%>
  </ul>
</script>
<script type="text/template" id="pushChenjiaoTpl">
  <div class="title"><%=data.regionName%>近期成交</div>
  <ul>
  <% var list = data.list; for(var i = 0;i < list.length; i++){%>
    <li class="li<%=i%>">
      <i></i>
      <a class="info" href="<%=list[i].viewUrl%>" target="_blank"><%=list[i].schoolName%></a>
      <span><%=list[i].dealCount%>套</span>
    </li>
  <%}%>
  </ul>
</script>
<script type="text/template" id="pushXuequTpl">
  <div class="title">热点精选</div>
  <ul>
  <%for(var i = 0;i < list.length; i++){%>
    <li>
      <a class="info" href="<%=list[i].pc_url%>" target="_blank"><%=list[i].title%></a>
    </li>
  <%}%>
  </ul>
</script>
<script type="text/template" id="pushZixunTpl">
  <div class="title">热点精选</div>
  <ul>
  <%for(var i = 0;i < list.length; i++){%>
    <li>
      <a class="info" href="<%=list[i].url%>" target="_blank" data-bl="list" data-log_index="<%=i+1%>">
        <i class="opt<%=i%>"><%=i+1%></i><span><%=list[i].question_title%></span>
      </a>
    </li>
  <%}%>
  </ul>
</script>
<script type="text/template" id="pushWendaTpl">
  <div class="title">热门问答</div>
  <ul>
  <%for(var i = 0;i < list.length; i++){%>
    <li>
      <a class="info" href="<%=list[i].url%>" target="_blank" data-bl="list" data-log_index="<%=i+1%>"><%=list[i].question_title%></a>
      <span class="answer_count"><%=list[i].answer_count%>个回答 / </span><span class="time"><%=list[i].mtime%></span>
    </li>
  <%}%>
  </ul>
</script>
<script type="text/template" id="pushBaikeTpl">
  <div class="list-baike">
    <div class="title">热门百科
      <a href="<%=baike_data['more_url']%>" class="btn-more" target="_blank">更多</a>
    </div>
    <div class="bd">
      <%for(var i = 0;i < baike_data['data'].length; i++){%>
        <div class="item"><a href="<%=baike_data['data'][i].url%>" target="_blank" class="tit"><%=baike_data['data'][i].title%></a><div class="sub-tit"><%=baike_data['data'][i].summary%></div><span class="arrow"></span></div>
      <%}%>
    </div>
  </div>
</script>
<script type="text/template" id="newAddHouseTpl">
  <div class="newAddHouse">
    自从您上次浏览（<%=time%>）之后，该搜索条件下新增加了<%=count%>套房源
    <a href="<%=url%>" class="LOGNEWERSHOUFANGSHOW" <%=logText%>><%=linkText%></a>
    <span class="newHouseRightClose">x</span>
  </div>
</script>
<script type="text/template" id="pushXinfangTpl">
  <div class="newHousePushContainer">
    <h3>推荐楼盘</h3>
    <ul log-mod="ershoufang_list_newHouseRecommand">
      <%for(var i = 0; i < list.length; i++){%>
        <li>
          <a class="pic LOGVIEW LOGCLICK" href="<%=list[i].view_url%>" target="_blank" data-bl="list" data-log_id="40001" data-el="<%=strategy_version%>" data-log_index="<%=i+1%>">
            <span class="bg"></span>
            <%if(list[i].cover_pic){%>
              <img src="<%=list[i].cover_pic%>.218x150.jpg">
            <%}else{%>
              <div class="mark"></div>
            <%}%>
            <div class="description" ><%=list[i].district_name%>－<%=list[i].resblock_name%></div>
          </a>
          <%if(list[i].rooms){%>
            <p class="area">
              <%=list[i].rooms%>
              <%if(list[i].min_frame_area != '' && list[i].max_frame_area != ''){%>
                &nbsp;-&nbsp;
                <%=list[i].min_frame_area%>~<%=list[i].max_frame_area%>平
              <%}%>
            </p>
          <%}%>
          <div class="price">
            <%if(list[i].show_price && list[i].show_price != 0){%>
              <i><%=list[i].show_price%></i>
              <%=list[i].show_price_unit%>
            <%}else{%>
              价格待定
            <%}%>
          </div>
        </li>
      <%}%>
    </ul>
  </div>
</script>

<script type="text/javascript">
require(['ershoufang/sellList/index'], function (main) {
  main({
    sidebar:{"type":"resblock","cityId":310000,"uuid":"a7ad8b25-df36-4b00-8ab6-ac1f0fe123df","ucid":null,"id":"5011000010470"},
    url:'/web/ershoufang/sidebar',
    xuequUrl : '/web/ershoufang/sidebarxuequ',
    ifXuqu: "\/ershoufang\/",
    ids: '107100396672,107100857965,107100760342,107100852490,107100111854,107100868343,107100679680,107100740920,107100512564,107100839777,107100713831,107100408424,107100705380,107100369892,107100718595,107100426560,107100767149,107100609516',
    SIRKeyword:"",
    count: 18,
    pageNum:1,
    cid: "5011000010470",
    bid: null,
    ucid: '',
    uuid: 'a7ad8b25-df36-4b00-8ab6-ac1f0fe123df',
    group: '-1',
    loadingImg: 'https://s1.ljcdn.com/feroot/pc/asset/ershoufang/sellDetail/img/loading.gif?_v=2018122819393752',
    qrImg: '//ajax.api.lianjia.com/qr/getDownloadQr'
  });

});

require(['common/initTalk'], function(initTalk) {
  initTalk()
});

;;+function() {
    LjUserTrack.send({
        "ljweb_id": "10001",
        "ljweb_mod": "ershoufang_list_view",
        "ljweb_bl": "spk_0",
        "ljweb_el": "18",
        "ljweb_value": "5011000010470",
    });
    var isHaveAgentCard = false
    var clickLinkBl = 'list';
    var resblockId = '';
    var communityId = '';
    if(isHaveAgentCard){
      clickLinkBl = 'list_have_sem_card';
      resblockId = "5011000010470"
      communityId = ""
    }
    $(document.body).on("click", "[data-el='ershoufang']", function() {
        var $m = $(this);
        LjUserTrack.send({
            "ljweb_id": "10002",
            "ljweb_mod": "ershoufang_list_list",
            "ljweb_bl": clickLinkBl,
            "ljweb_el": "ershoufang",
            "ljweb_index": $m.attr("data-log_index"),
            "ljweb_url": $m.attr("href"),
            "ljweb_value":resblockId,
            "ljweb_is_focus" : $m.attr("data-is_focus") || 0,
            "ljweb_house_code" : $m.attr('data-housecode')
        });

    });

    $(document.body).on("mousedown", ".input [data-bl='sug'] [data-log_value]", function() {
        var $m = $(this);
        var actionId = $m.closest('[data-bl="sug"]').attr("data-el") === 'history' ? '10004' : '10003';
        LjUserTrack.send({
            "ljweb_id": actionId,
            "ljweb_mod": "ershoufang_list_search",
            "ljweb_bl": "search",
            "ljweb_el": $m.attr("data-log_value"),
            "ljweb_index": $m.attr("data-log_index"),
            "ljweb_value": $.trim($("#searchInput").val()),
            "ljweb_url": $m.attr("href")
        });
    });
    $("#searchForm").on("submit", function() {
        var $m = $(this);
        LjUserTrack.send({
            "ljweb_id": "10008",
            "ljweb_mod": "ershoufang_list_search",
            "ljweb_bl": "search",
            "ljweb_value": $.trim($("#searchInput").val())
        });
    });

}();
</script>
<script>require(['common/suggestion'], function (suggestion) {window.defaultSuggest = suggestion.init({requestOptions: {cityId: '310000',cityName: '上海'},url: '/api/headerSearch?channel=ershoufang&q=',main: '#keyword-box',appendTo: '#suggest-cont',redirect: true});});</script><div class="loninContaner"><div class="overlay_bg"></div><div class="panel_login animated" id="dialog"><div class="panel_info"><i class="close_login" >&times</i><div class="panel_tab"><div class="title"><div class="fl">账号密码登录</div></div><div class="clear"></div><div id="con_login_user"><form action="" method="post"><ul><li class="item border-t userName"><input type="text" class="the_input topSpecial users" placeholder="请输入手机号"  maxlength="11" /></li><li class="item border-b pwd"><input type="password" class="the_input password" maxlength="20" placeholder="请输入登录密码"/><em class="password-view"></em></li><li class="item checkVerimg" style="display:none;"><input type="text" class="the_input ver-img" maxlength="6"  placeholder="请输入验证码"/><img class="verImg"></li><li class="item drag" style="display:none;"><div id="drag"></div></li><li class="show-error"><dd>用户名或密码错误</dd></li><li class="li_01"><label class="checkbox-btn"><span class="active"><input type="checkbox" name="remember" value="1" class="mind-login" checked/></span>7天内免登录</label><a href="javascript:;" rel="nofollow" class="toforget">忘记密码</a></li><li class="li_btn"><a class="login-user-btn"  />登录</a></li><li class="footer-link"><a href="javascript:;" rel="nofollow" class="totellogin">手机快捷登录</a></li></ul></form></div><div id="con_login_agent" class="undis"><form action="" method="post"><ul><li class="item"><dd></dd><input type="text" class="the_input users" placeholder="输入经纪人ID号码" /></li><li class="item"><input type="password" class="the_input password"  placeholder="登录密码"/></li><li class="li_01"><label class="checkbox-btn"><span class="active"><input type="checkbox" name="remember" value="1" class="mind-login" checked/></span>7天内免登录</label><a href="https://passport.lianjia.com/register/resources/lianjia/forget.html?service=http://bj.lianjia.com/" rel="nofollow">忘记密码</a></li><li><input class="login-agent-btn" value="立即登录"/></li></ul></form></div></div></div><div class="registered"></div></div><div class="panel_login animated" id="dialog_tel"><div class="panel_info"><i class="close_login">&times</i><div class="panel_tab"><div class="title"><div class="fl">手机快捷登录</div><div class="register_text_tel">别担心，无账号自动注册不会导致手机号被泄露</div></div><div class="clear"></div><div id="con_login_user_tel"><form action="" method="post"><ul><li class="item border-t userName"><input type="text" class="the_input topSpecial users_tel" maxlength="11" placeholder="请输入手机号" /></li><!-- <li class="item pwd"><input type="password" class="the_input password_tel"  placeholder="请输入短信验证码"/></li> --><li class="item checkVerimg" style=""><input type="text" class="the_input ver-img" maxlength="6"  placeholder="请输入验证码"/><img class="verImg"></li><li class="item border-b Verify"><input type="text" class="the_input verifycode" maxlength="6"  placeholder="请输入短信验证码"/><a class="send_verify_code" id="send_verify_code_tel" href="javascript:;" rel="nofollow"><em>获取验证码</em></a></li><li class="send_verify_code_s" id="send_verify_code_tel_s" href="javascript:;" rel="nofollow"><em>没有收到验证码？</em><a class="voice_a">发送语音验证码</a></li><li class="show-error"><dd>用户名或密码错误</dd></li><li class="li_01"><label class="checkbox-btn"><span class="active"><input type="checkbox" name="remember" value="1" class="mind-login" checked/></span>7天内免登录</label></li><li class="li_btn"><a class="login-user-tel-btn"  />登录</a></li><li class="footer-link"><a href="javascript:;" rel="nofollow" class="tologin">账号密码登录</a></li></ul></form></div></div></div><div class="registered"></div></div><div class="panel_login animated" id="dialog_reg"><div class="panel_info"><i class="close_login">&times</i><div class="panel_tab"><div class="title"><div class="fl">手机号码注册</div><label class="fr register_text">已有账号？<a href="javascript:;" rel="nofollow" class="tologin">去登录</a></label></div><div class="clear"></div><div id="con_login_user_reg"><form action="" method="post"><ul><li class="item border-t userName"><input type="text" class="the_input topSpecial users_reg"  maxlength="11" placeholder="请输入手机号" /></li><li class="item checkVerimg" style=""><input type="text" class="the_input ver-img" maxlength="6"  placeholder="请输入验证码"/><img class="verImg"></li><li class="item border-c Verify"><input type="text" class="the_input verifycode" maxlength="6"  placeholder="请输入短信验证码"/><a class="send_verify_code" id="send_verify_code_reg" href="javascript:;" rel="nofollow"><em>获取验证码</em></a></li><li class="item border-b pwd"><input type="password" class="the_input password_reg" maxlength="20"  placeholder="请输入密码（最少8位，数字+字母）"/><em class="password-view"></em></li><li class="send_verify_code_s" id="send_verify_code_reg_s" href="javascript:;" rel="nofollow"><em>没有收到验证码？</em><a class="voice_a">发送语音验证码</a></li><li class="show-error"><dd>用户名或密码错误</dd></li><li class="li_01"><label class="checkbox-btn"><span class="active"><input type="checkbox" name="read" value="1" class="read-protocol" checked/></span>我已阅读并同意</label><a class="toprotocol" href="//www.lianjia.com/zhuanti/protocol" target="_blank" >《链家用户使用协议》</a></li><li class="li_btn"><a class="register-user-btn"  />注册</a></li></ul></form></div></div></div><div class="registered"></div></div><div class="panel_login animated" id="dialog_forget"><div class="panel_info"><i class="close_login">&times</i><div class="panel_tab"><div class="title"><div class="fl">找回密码</div></div><div class="clear"></div><div id="con_forget_user_tel" class="con_forget_user_tel"><form action="" method="post"><ul><li class="item border-t userName"><input type="text" class="the_input topSpecial user_forget_phone" placeholder="请输入手机号"  maxlength="11" /></li><li class="item checkVerimg" style=""><input type="text" class="the_input ver-img" maxlength="6"  placeholder="请输入验证码"/><img class="verImg"></li><li class="item border-b Verify"><input type="text" class="the_input verifycode" maxlength="6"  placeholder="请输入短信验证码"/><a class="send_verify_code" id="send_verify_code_forget" href="javascript:;" rel="nofollow"><em>获取验证码</em></a></li><li class="item border-t pwd" style="margin-top:-1px;"><input type="password" class="the_input password_reg" maxlength="20"  placeholder="请输入密码（最少8位，数字+字母）"/><em class="password-view"></em></li><li class="send_verify_code_s" id="send_verify_code_forget_s"><em>没有收到验证码？</em><a class="voice_a">发送语音验证码</a></li><li class="show-error"><dd>用户名或密码错误</dd></li><li class="li_btn"><a class="user-forget"  />修改密码</a></li></ul></form></div><div id="con_forget_user_pw" class="con_forget_user_pw"><form action="" method="post"><ul><li class="item border-t pwd"><input type="password" class="the_input password_reg" maxlength="20"  placeholder="请输入密码（最少8位，数字+字母）"/><em class="password-view"></em></li><li class="show-error"><dd>用户名或密码错误</dd></li><li class="li_btn"><a class="modify-user-pswd"  />修改密码</a></li></ul></form></div></div></div><div class="registered"></div></div></div>
<!-- LianjiaIM Style --><link property='stylesheet' rel="stylesheet" href="https://s1.ljcdn.com/feroot/pc/asset/lianjiaIM/css/lianjiaim.css?_v=2018122819393752"/><script src="//s1.ljcdn.com/web-im-sdk/static/1.1/lianjiaim1.1.min.js?v=20190101"></script><!-- <script src="//s1-ljcdn.test.lianjia.com:8400/web-im-sdk/static/1.1/lianjiaim1.1.min.js?v=20190101"></script> --><script>(function() {var imConf = {"ajaxroot":"https:\/\/ajax.api.lianjia.com\/","imAppid":"LIANJIA_WEB_20160624","imAppkey":"6dfdcee27d78b1107fceeca55d80b7bd"};let login = require('common/login');$.listener.on('userInfo', function (data) {if (data.code === 1) {data.ucid = '';}window.LJIM = new LianjiaIM({appid: imConf.imAppid,appkey: imConf.imAppkey,login: login.openLoginDialog,is_ljbb: true,userData: data,downAppUrl: '//www.lianjia.com/client/',appDesc: '立即下载链家APP，随时随地聊~',staticRoot: 'https://s1.ljcdn.com/feroot/?_v=2018122819393752'})});})();</script><script type="text/javascript">var advert = 'https://s1.ljcdn.com/feroot/pc/asset/common/advert.js?_v=2018122819393752';
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
for quote in response.xpath('//ul[@class="sellListContent"]'):
    print getList(quote.xpath('.//a[@class="noresultRecommend img "]/@href'))
    print getList(quote.xpath('.//a[@class="noresultRecommend img "]/@data-housecode'))


    print getList(quote.xpath('.//div[@class="info clear"]/div[@class="title"]/a/text()'))

    print getList(quote.xpath('.//div[@class="info clear"]/div[@class="address"]/div[@class="houseInfo"]/a/text()'))
    print getList(quote.xpath('.//div[@class="info clear"]/div[@class="address"]/div[@class="houseInfo"]/a/@href'))
    a = quote.xpath('.//div[@class="info clear"]/div[@class="address"]/div[@class="houseInfo"]/a')


    # for i in quote.xpath('.//div[@class="info clear"]/div[@class="address"]/div[@class="houseInfo"]/*[not(name()="a")]'):
    #     print i.xpath('string(.)').strip()
    print quote.xpath('.//div[@class="info clear"]/div[@class="address"]/div[@class="houseInfo"]')[0]\
        .xpath('string(.)') \
        .replace("\n", "") \
        .replace("  ", "")

    # positionInfo
    print quote.xpath('.//div[@class="info clear"]/div[@class="flood"]/div[@class="positionInfo"]')[0]\
        .xpath('string(.)')\
        .replace("\n", "")\
        .replace("  ", "")
    print getList(quote.xpath('.//div[@class="info clear"]/div[@class="flood"]/div[@class="positionInfo"]/a/@href'))

    print quote.xpath('.//div[@class="info clear"]/div[@class="followInfo"]')[0].xpath('string(.)') \
        .replace("\n", "")\
        .replace("  ", "")

    print quote.xpath('.//div[@class="info clear"]/div[@class="tag"]')[0].xpath('string(.)') \
        .replace("\n", "") \
        .replace("  ", "")
    print quote.xpath('.//div[@class="info clear"]/div[@class="priceInfo"]/div[@class="totalPrice"]/span/text()')[0]
    print quote.xpath('.//div[@class="info clear"]/div[@class="priceInfo"]/div[@class="totalPrice"]')[0].xpath('string(.)').replace("\n", "") \
        .replace("  ", "")

    print quote.xpath('.//div[@class="info clear"]/div[@class="priceInfo"]/div[@class="unitPrice"]/span/text()')[0]



    print "***************************************************"

# for quote in response.xpath('//div[@class="content__list--item"]'):
#     print getList(quote.xpath('.//div/p[@class="content__list--item--title twoline"]/a/text()'))
#     print getList(quote.xpath('.//div/p[@class="content__list--item--title twoline"]/a/@href'))
#
#     print getList(quote.xpath('.//div/p[@class="content__list--item--des"]/a[position()=1]/@href'))
#     print getList(quote.xpath('.//div/p[@class="content__list--item--des"]/a[position()=1]/text()'))
#     print getList(quote.xpath('.//div/p[@class="content__list--item--des"]/a[position()=2]/@href'))
#     print getList(quote.xpath('.//div/p[@class="content__list--item--des"]/a[position()=2]/text()'))
#
#     print "***************************************************"
#
# print "/zufang/SH2136750194585780224.html"[8:-5]
