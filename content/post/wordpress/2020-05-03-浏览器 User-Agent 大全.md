---
title: "浏览器 User-Agent 大全"
date: "2020-05-03"
categories: 
  - "diannaowangruo"
  - "wangyesheji"
tags: 
  - "user-agent"
url: "/archives/1646.html"
---

一、基础知识 Http Header之User-Agent

User Agent中文名为用户代理，是Http协议中的一部分，属于头域的组成部分，User Agent也简称UA。它是一个特殊字符串头，是一种向访问网站提供你所使用的浏览器类型及版本、操作系统及版本、浏览器内核、等信息的标识。通过这个标识，用户所访问的网站可以显示不同的排版从而为用户提供更好的体验或者进行信息统计；例如用手机访问谷歌和电脑访问是不一样的，这些是谷歌根据访问者的UA来判断的。UA可以进行伪装。

浏览器的UA字串的标准格式：浏览器标识 (操作系统标识; 加密等级标识; 浏览器语言) 渲染引擎标识版本信息。但各个浏览器有所不同。

字串说明：

1、浏览器标识

出于兼容及推广等目的，很多浏览器的标识相同，因此浏览器标识并不能说明浏览器的真实版本，真实版本信息在 UA 字串尾部可以找到。

2、操作系统标识

3、加密等级标识

N: 表示无安全加密 I: 表示弱安全加密 U: 表示强安全加密

4、浏览器语言

在首选项 > 常规 > 语言中指定的语言

5、渲染引擎

显示浏览器使用的主流渲染引擎有：Gecko、WebKit、KHTML、Presto、Trident、Tasman等，格式为：渲染引擎/版本信息

6、版本信息

显示浏览器的真实版本信息，格式为：浏览器/版本信息

注： 1、在广告定向设定中，浏览器定向和操作系统定向均是针对User-Agent中的信息进行定向。 2、欲了解更多的User-Agent信息，请参考User-agent 字串史

浏览器User-Agent的详细信息

PC端： safari 5.1 – MAC User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10\_6\_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50

safari 5.1 – Windows User-Agent:Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50

IE 9.0 User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;

IE 8.0 User-Agent:Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)

IE 7.0 User-Agent:Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)

IE 6.0 User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)

Firefox 4.0.1 – MAC User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1

Firefox 4.0.1 – Windows User-Agent:Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1

Opera 11.11 – MAC User-Agent:Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11

Opera 11.11 – Windows User-Agent:Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11

Chrome 17.0 – MAC User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10\_7\_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11

傲游（Maxthon） User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)

腾讯TT User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)

世界之窗（The World） 2.x User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)

世界之窗（The World） 3.x User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)

搜狗浏览器 1.x User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)

360浏览器 User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)

Avant User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)

Green Browser User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)

移动设备端： safari iOS 4.33 – iPhone User-Agent:Mozilla/5.0 (iPhone; U; CPU iPhone OS 4\_3\_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5

safari iOS 4.33 – iPod Touch User-Agent:Mozilla/5.0 (iPod; U; CPU iPhone OS 4\_3\_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5

safari iOS 4.33 – iPad User-Agent:Mozilla/5.0 (iPad; U; CPU OS 4\_3\_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5

Android N1 User-Agent: Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1

Android QQ浏览器 For android User-Agent: MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1

Android Opera Mobile User-Agent: Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10

Android Pad Moto Xoom User-Agent: Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13

BlackBerry User-Agent: Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+

WebOS HP Touchpad User-Agent: Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0

Nokia N97 User-Agent: Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124

Windows Phone Mango User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)

UC无 User-Agent: UCWEB7.0.2.37/28/999

UC标准 User-Agent: NOKIA5700/ UCWEB7.0.2.37/28/999

UCOpenwave User-Agent: Openwave/ UCWEB7.0.2.37/28/999

UC Opera User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999

用户追踪之基础技术——Cookie

前言

Cookie是如此的重要，以至于我们后面要讲到的回头客定向、访客频次定向、用户定向等等都需要基于此技术才可以实现，并且我们日常工作中所能见到的第三方监测工具如doubleclick、99click、秒针等也都要利用cookie技术，网站分析工具如GA、百度统计、CNZZ等也需要利用cookie。如果没有Cookie，互联网广告市场将受到巨大打击，尤其对于目前我们谈论的精准广告而言。如果没有Cookie，网站分析也不从做起，遑论优化了。

Cookie是什么

Cookie在英文中是小甜品的意思，但在计算机语言中，Cookie指的是当你浏览某网站时，网站存储在你电脑上的一个小文本文件，伴随着用户请求和页面在 Web 服务器和浏览器之间传递。它记录了你的用户ID，密码、浏览过的网页、停留的时间等信息，用于用户身份的辨别。Cookie通常是以user@domain格式命名的，user是你的本地用户名，domain是所访问的网站的域名。

为什么要Cookie

因为HTTP协议是无状态的，对于一个浏览器发出的请求，服务器无法区分是不是同一个来源，无法知道上一次用户做了什么。所以，需要额外的数据用于维护会话。 Cookie 正是这样的一段随HTTP请求一起被传递的额外数据，用于维护浏览器和服务器的会话。我们可以想象一个场景，你没有登录京东时在京东上购物，选择了3件商品放入购物车，在结算时，京东为什么还能知道这三件商品是什么？没错，是Cookie！

Cookie的工作原理

Cookie利用网页代码中的HTTP头信息，伴随着用户请求和页面在 Web 服务器和浏览器之间传递。例如：当你在浏览器地址栏中键入了Amazon的URL，浏览器会向Amazon发送一个读取网页的请求，并将结果在显示器上显示。在发送之前，该网页在你的电脑上寻找Amazon网站设置的Cookie文件，如果找到，浏览器会把Cookie文件中的数据连同前面输入的URL一同发送到Amazon服务器。服务器收到Cookie数据，就会在他的数据库中检索你的ID，你的购物记录、个人喜好等信息，并记录下新的内容，增加到数据库和Cookie文件中去。如果没有检测到Cookie或者你的Cookie信息与数据库中的信息不符合，则说明你是第一次浏览该网站，服务器的CGI程序将为你创建新的ID信息，并保存到数据库中。（此例子来源于百度百科——Cookie）

关于Cookie的一些知识点

1、Cookie是基于浏览器的，因此当电脑上安装多个浏览器时，服务器会生成多个Cookie。虽然是同一个人，但服务器是识别为多个用户。 2、Cookie是基于浏览器的，因此当同一台电脑有多个人使用时，服务器也只会生成一个Cookie。虽然是多个人，但服务器会认为是一个用户。 3、Cookie是无法跨设备进行设置的。比如我们在单位和家里分别使用两台电脑，即使我们使用同一种同一版本的浏览器，我们还是生成了两个Cookie，服务器会认为是两个用户。（PS：现在有些浏览器可以同步数据，比如Chrome、Friefox，可以避免这种问题）

请注意：以上所说的Cooke指的全部是Http Cookie。有一种Cookie——Flash Cookie，可以解决多浏览器的问题。

关于Flash Cookie

FlashCookie是由FlashPlayer控制的客户端共享存储技术，鉴于目前Flash技术的普遍性，几乎所有的网站都采用，所以具有同Http Cookie一样的作用。在技术上，通过使用JavaScript与ActionScript可以将Http Cookie和Flash Cookie进行互通。

Flash cookie的优势在于： 1、跨浏览器 不管用户的计算机上安装了多少个浏览器或者浏览器的不同版本，使用Flash Cookie能够使所有的浏览器共用一个Cookie。 2、不易删除 所有的浏览器均提供了清除Http Cookie的快捷方式，但Flash Cookie并没有此种方式，并且其保存位置非常隐蔽，网民难以删除。 3、容量更大 Flash Cookie可以容纳最多100千字节的数据，而一个标准的HTTP Cookie只有4千字节。

作为网络广告行业的销售人员，了解以上知识就已经绰绰有余了。如果想了解更多，可以接着往下看。

Cookie的数量

1、大多数浏览器支持最大为 4096 字节的 Cookie。因此最好用 Cookie 来存储用户 ID 之类的标识符，用户的详细信息则通过用户 ID从数据库或其他数据源中读取。 2、浏览器还限制站点可以在用户计算机上存储的 Cookie 的数量。大多数浏览器只允许每个站点存储 20 个 Cookie；当存储更多 Cookie时，最旧的 Cookie 便会被丢弃。有些浏览器还会对它们将接受的来自所有站点的 Cookie 总数作出绝对限制，通常为 300 个。

Cookie的失效时间

1、浏览器的Cookie设置会决定是否保存Cookie数据。如果浏览器不允许Cookie保存，则关掉浏览器后，这些数据就消失。 2、如果浏览器允许保存Cookie，那么Cookie的时间由服务器的设置决定。Cookie有一个Expires（有效期）属性，这个属性决定了Cookie的保存时间，服务器可以通过设定Expires字段的数值，来改变Cookie的保存时间。如果不设置该属性，那么Cookie只在浏览网页期间有效，关闭浏览器，这些Cookie自动消失，绝大多数网站属于这种情况。通常情况下，Cookie包含Server、Expires、Name、value这几个字段，其中对服务器有用的只是Name和value字段，Expires等字段的内容仅仅是为了告诉浏览器如何处理这些Cookies。

Cookie的样例

1、Cookie的名称

2、Cookie的内容

3、从页面代码监测工具看Cookie

Cookie的位置

1、Http Cookie的位置 Windows 9X系统 C:WindowsCookies Windows NT/2000/XP系统 C:Documents and Settings用户名Cookies win7系统 C:Users_AppDataRoamingMicrosoftWindowsCookies_ OS X系统 ～/Users/用户名/Library/Cookies

2、Flash Cookie的位置

非Win7系统 C:Documents and Settings\[username你的用户名\]Application DataMacromediaFlash Player#SharedObjects

Win7 C:Users\[username你的用户名\]Application DataMacromediaFlash Player 其中：Users可能显示为“用户”

OS X系统 ~/Users/用户名/Library/Preferences/Macromedia/Flash Player/#SharedObjects ~/Users/用户名/Library/Preferences/Macromedia/Flash Player/macromedia.com/support/flashplayer/sys/

第一方Cookie和第三方Cookie

大多数的第三方监测工具和网站分析工具都会采用第三方Cookie。所谓第一方和第三方的说法，是用来确定Cookie的归属的，这个归属是指Cookie中记录的域（domain）。第一方和第三方的唯一区别只是：Cookie中的域名是否和被访问网站的域一样，是就是第一方，否就是第三方。举个例子：如果你访问网站www.chinawebanalytics.cn的时候，网站在你的电脑上设置了一个Cookie，里面的记录的域名也是www.chinawebanalytics.cn，那么这个Cookie就是第一方的，归你访问的网站www.chinawebanalytics.cn所有。而如果你访问网站www.chinawebanalytics.cn时，在你的计算机中设置的Cookie的域名是www.abc.com，那么这个Cookie就是第三方Cookie，归www.abc.com所有。

所以，第一方Cookie并不一定需要由某个网站自己的服务器给自己建立，别的网站也能为它建立；而且，第一方Cookie也不一定是能由某个网站自己读取的，它完全可能由第三方读取。（以上内容和例子来自于捍卫Cookie——没有Cookie，我们什么都没有了）

二、定向技术介绍 语言定向

1、语言的来源

简单理解，语言指的是用户的浏览器语言，是从浏览器的Http Header的Accept-Language的字段来的。

2、浏览器的Accept-Language是由浏览器的语言设置所决定的。

3、浏览器的默认语言设置和浏览器语言无关，默认继承操作系统的语言。

浏览器定向

浏览器定向同样需要依赖于各个浏览器在打开页面时所传输的Http header信息中的User-Agent，关于User-Agent的说明，请参见Http header之User-Agent。 User-Agent的详细信息，请参见浏览器User-Agent的详细信息。

我们来了解User-Agent中浏览器及版本识别的方法：

一、浏览器的使用率说明：

——数据来源于CNZZ数据中心

我们针对以上的浏览器进行说明，另外再针对移动设备上的几款浏览器进行说明。

二、浏览器识别

1、IE浏览器（以IE 9.0 为例）

PC端：User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; 移动设备：User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)

由于遨游、世界之窗、360浏览器、腾讯浏览器以及搜狗浏览器、Avant、Green Browser均采用IE的内核，因此IE浏览器判断的标准是”MSIE“字段，MSIE字段后面的数字为版本号，但同时还需要判断不包含”Maxthon“、”The world“、”360SE“、”TencentTraveler“、”SE“、”Avant“等字段（Green Browser没有明显标识）。移动设备还需要判断IEMobile+版本号。

2、360浏览器

PC端：User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; InfoPath.2; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; 360SE) 移动设备：暂无

360浏览器的判断标准是”360SE”字段，没有版本表示。

3、搜狗浏览器

PC端：User-Agent:Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0) 移动设备：暂无

搜狗浏览器的判断标准是”SE“、”MetaSr“字段，版本号为SE后面的数字。

4、Chrome

PC端：Mozilla/5.0 (Macintosh; Intel Mac OS X 10\_7\_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11

移动设备：User-Agent: Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC\_Wildfire\_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1

PC端chrome浏览器的判断标准是chrome字段，chrome后面的数字为版本号；移动端的chrome浏览器判断”android“、”linux“、”mobile safari“等字段，version后面的数字为版本号。

5、Safari

PC端：User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10\_6\_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50

移动设备：User-Agent:Mozilla/5.0 (iPhone; U; CPU iPhone OS 4\_3\_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5

由于Chrome及Nokia’s Series 60 browser也使用WebKit内核，因此Safari浏览器的判断必须是：包含safari字段，同时不包含chrome等信息，确定后”version/“后面的数字即为版本号。在以上条件下包含Mobile字段的即为移动设备上的Safari浏览器。

6、腾讯浏览器

PC端：User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; TencentTraveler 4.0; .NET CLR 2.0.50727)

移动设备：User-Agent: MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1

腾讯浏览器的判断标准是”TencentTraveler“或者”QQBrowser“，TencentTraveler或QQBrowser后面的数字为版本号。

7、Firefox

PC端：User-Agent:Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1

移动设备：User-Agent: Mozilla/5.0 (Androdi; Linux armv7l; rv:5.0) Gecko/ Firefox/5.0 fennec/5.0

Firefox的判断标准是Firefox字段，firefox后面的数字为版本号。

8、The world

PC端：User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)

移动设备：暂无

Theworld浏览器的判断标准是”The world“字段，没有标示版本号。

需要注意的是：The world 2.x版本的User-Agent中没有”The world“的字段。

9、遨游

PC端：User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)

移动设备：暂无

遨游浏览器的判断标准是”Maxthon“，Maxthon后面的数字为版本号。

10、Opera

PC端：User-Agent:Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11

移动设备：User-Agent: Opera/9.80 (Android 2.3.4; Linux; Opera mobi/adr-1107051709; U; zh-cn) Presto/2.8.149 Version/11.10

opera浏览器的判断标准是opera字段，opera字段后面的数字为版本号。

11、UC浏览器

UC Web有多种模式浏览方式，对应的User-Agent为：

UC无 User-Agent: UCWEB7.0.2.37/28/999

UC标准 User-Agent: NOKIA5700/ UCWEB7.0.2.37/28/999

UCOpenwave User-Agent: Openwave/ UCWEB7.0.2.37/28/999

UC Opera User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999

UC浏览器的判断标准是”UCWEB“字段，UCWEB后面的数字为版本号。

操作系统定向

操作系统定向依赖于各个浏览器在打开页面时所传输的http header信息中的User-Agent，关于User-Agent的说明，请参见Http header之User-Agent。 User-Agent的详细信息，请参见浏览器User-Agent的详细信息。

我们来了解User-Agent中的不同操作系统的识别方法。

PC端：

移动设备端：

地域定向

地域定向依赖于对IP地址的识别，而IP协议是互联网的基础协议，因此从网络诞生的第一天起，地域定向就可以被使用了。

欲详细了解IP协议，请查看百度百科——TCP/IP协议。有关IP地址的详细信息，请查看百度百科——IP。

通俗来讲，IP地址就是互联网上的门牌号，接入互联网的所有主机就是我们的一个个住所，其中有个人的，有单位的。个人住所一家一个门牌号，单位的多家公用一个门牌号，由于规划的原因，有的住所会有多个门牌号，也是规划的原因，门牌号有时会发生变化。IP地址也有此特点，一台主机可以具有多个IP地址，而多台主机也可以公用一个IP地址。

现实中，不管如何规划，通过门牌号我们能找到我们要找的住所，也能清楚住所所在的具体位置。同样，在网络中，通过IP地址我们也能定位到我们所需要找的主机，并且清楚知道主机所在的地理位置。这样我们就能进行广告的地域定向了。

从技术层面讲，地域定向的工作逻辑是：

当一个请求发送给服务器时，服务器根据配置（以Apache为例，在Apache Httpd中进行配置）记录下请求的相关数据，组成日志文件，日志基本会包括请求时间、请求IP、请求的URL、请求的Reffer、请求的User-Agent以及其他信息，将收集到的IP地址与已有的IP数据库进行比对，即可以确定请求者的地理位置了，比如山西省太原市。

国内目前免费的IP库有 QQ IP数据库 纯真版，即我们通常所说的纯真IP库，收集了包括中国电信、中国网通、长城宽带、网通宽带、聚友宽带等 ISP 的最新准确 IP 地址数据，包括最全的网吧数据。IP数据库每5天更新一次，企业可以在此基础上修正后使用。

目前的地域定向更多的是针对省份以及地级城市的定向，针对县级市或者区级的定向基本上都十分不准确。

回头客定向

随着电商网站的火爆，从2010年开始，互联网广告行业出现了一种定向方式——回头客定向。回头客定向是随着精准理念的发展而提出来的。顾名思义，回头客定向是指针对到达过广告主网站的某一个点的用户或者发生过某一个行为的用户进行定向。

从概念中，我们可以发现回头客定向的三个基本点：1、到达过；2、某一个点或某个行为；3、定向投放。这三点也是回头客定向和人群定向的区别之处。

从营销的角度讲，针对不同到达深度的用户或者不同行为的用户，我们需要采取的营销策略可能会有不同。我们以电商网站的购物流程来举例子。电商网站的购物流程分为以下几个步骤：

1、针对浏览过商品的人，我们应该分析他的浏览记录，发现他感兴趣的商品，然后通过广告将他感兴趣的商品推送到他的面前（如果要做到非常完美，针对每个用户有不同的广告显示，需要有哪些条件？大家可以评论，我们一起交流）。

2、针对已经将商品加入购物车的人，此时可能更重要的是给他一张电子优惠券，以促进其下单。

3、针对到达过注册或者登录界面，但未完成注册和登录的人，给他一个商品即将售馨或者即将涨价的倒计时更能促进其回来下单。

4、针对到过填写配送地址页面但没有提交订单的人，提示免邮递费用或者直接告诉他“你还差一步就将完成订单”，可能会是一个好的方法。

5、已经提交订单的人，是我们的老客户了，此时应该推荐关联的商品信息，以促进其二次消费。

所以，进行回头客定向的投放，一定是要有以下三个步骤的：

1、设置回头客人群的监测。支持回头客定向的系统必须能够支持对各个点的监测，因此提取监测代码在此是必须的。好的系统可以利用一个监测代码，通过数据分析得出不同监测点的回头客（大家说如何做到？）；差的系统就提供不同监测点的设置功能，每个监测点提取不同的监测代码。

2、整理针对各个监测点用户的独特营销诉求。制作针对不同回头客的不同创意。

3、利用投放系统，对回头客进行定向的广告投放。

一般来讲，定向越准确，能得到的量就会越少，因此，在做回头客定向时，不应该再选择媒体进行投放。从另一个角度理解，回头客定向已经是最领先精准的目标用户定向了，此时媒介选择的意义也大大弱化了。

以上所说的是纯正意义上的回头客定向，鉴于回头客定向受人欢迎的精准的概念和可怜的流量，有些人或公司权衡后会将回头客定义的非常广泛，比如到过网站的人、点过广告的人、看过广告的人都算作回头客，这只是又一次的中国特色而已。这种事情多了，反而于精准广告市场的发展不利。

人群定向

人群定向其实就是目标人群定向，在营销学中，产品定位以及人群细分是非常重要的理念，这种理念也已经得到了市场的认可，因此每一种产品在设计、生产之初就已经确定了自己的目标人群。从我们的广告投放、市场宣传来讲，一定是希望能给对目标人群进行，花费在目标人群之外的推广都是浪费的。

但在以往的媒介中，想要完全的识别用户，以确定是否目标人群并不是容易的事情，甚至从理论上说是完全做不到的，只能通过不同的媒介手段去尽量的靠近目标人群（电视、广播、杂志都是如何确定自己的受众的呢？有人讨论嘛？）。但即使这样，也产生了一句广告界最著名的话语——我知道广告费浪费了一半，但我不知道到底是哪一半。

在互联网时代，通过技术的力量，可以无限的接近、近乎准确的判断每一个人的属性，从而为广告主目标群体定向服务。但是，互联网也只是无限的接近，而不是确切的能标示出个人的属性。目前，最接近的应该是类似于罗维邓白氏之类公司的数据 （顺便说一句，央视315晚会的曝光，对罗维邓白氏公司只能是免费的广告，而不是打击）。

言归正传，我们来说说互联网的人群定向。互联网公司通常讲的人群定向并不单单包括人口的自然属性（demographic），还包括人群兴趣（interest）、人群行为（behavior）、购物行为（purchasing）。

注：此处我们说的人群行为指的是对广告的行为，比如浏览广告，点击广告以及转发、下载广告等交互行为。目前市场上经常有一些公司标榜行为定向，但让其展开一说，就只是说对用户的浏览行为进行定向，非常正确、毫无破绽的说法，但细问却还是这一句。这只能说明这种公司忽悠而无真章的事实（大家说说为什么能说明？）。

对于真正提供定向的公司，不管各个公司都提供什么样的人群定向，以上所说的4类属性或行为都是基于cookies技术（了解Cookie），通过对用户长期的互联网浏览行为数据进行分析所得出的。由于各公司的资源优势不同，因此目前没有一个公司能够建立健全的数据。

自然属性（demographic）

自然属性包括性别、年龄、学历、地域、婚姻状况、家庭状况（是否有小孩，小孩年龄等）、收入（个人收入、家庭收入）、行业、职业等信息。单纯通过互联网浏览行为并不能分析到如此全面且准确的信息，目前还主要以找到真实的样本进行建模分析为主。自然属性数据以艾瑞的数据最为准确。

人群兴趣（interest）

人群兴趣在每个公司会有不同的认知。目前，兴趣数据属悠易最好，悠易的数据是公开的，可以通过悠易受众引擎查看。

人群行为（behavior）

上面注解所说的人群行为仅仅是行为中的一种，如果有搜索引擎的资源，则可以加入搜索行为的监测（如百度的搜客定向——对在百度搜索过已添加关键词的人，在其浏览指定的投放网站时投放客户推广组下的创意。）；如果有微博数据，则可以加入关注与被关注的行为（新浪有此打算吗？），因此人群行为各公司的定义差异是最大的。

购物行为（purchasing）

购物行为指的是作为消费者角色，互联网用户的消费数据。毋庸置疑，购物数据如果淘宝是第二，也没人可以自称第一。

在广告系统中，用户的所有属性或行为应该是可以进行自由组合设定的。但以上所有的属性或行为就可以全方面的了解用户了吗？并不是！这是一个发散性的命题，每个人会有不同的见解。比如我们还可以加入用户的设备（PC、Pad、移动设备等），通过用户上网通道来描述用户。还有其他的角度吗，大家留言讨论吧！

并发次数 在按天售卖或者按时间售卖的时代，是不需要考虑并发次数的。只是在按照展现次数（CPM）售卖的时候，我们才有可能需要考虑广告并发的设置。

在按照CPM（何为CPM）售卖时，广告投放的速度可以有两种——尽快投放和匀速投放。尽快投放很好理解，就是尽快投放完规定的量。匀速投放就是在规定的时间内均匀的投放完规定的量。举个例子，一天之内投放1000个CPM，选择尽快投放就意味着广告在第x小时投放完毕，那么(24-x)的时间内就不会再看到广告；而匀速投放意味着我们需要在第23小时59分时还看到广告。这个如何做到呢？此时就需要利用并发次数的设定了。

并发次数指的是广告某个时间周期内播放的次数，其目的是为了保证广告的匀速投放。并发次数的计算方法为：广告投放量/投放时长。注意：此处的时长根据需要，可以按照秒、分、刻等单位来计算。并发次数的规则需要广告投放核心的支持，当在规定的时长内，广告未达到并发次数时，广告可以展现。达到设置次数后，则不予以展现。

一个思考题：如果一个广告一天内要求投放1000CPM，而媒体的PV一天正好是1000CPM，那么尽快投放是否能够跑完广告的规定量？匀速投放是否能够跑完广告规定的量？如果跑不完，我们需要怎么做，才可以跑完？

时段定向

每一个广告活动，每一次宣传活动，都会有周期的设定。在一个投放活动被制订出来后，在每种媒介、每个媒体上的投放周期就已经确定了。电视、广播、报纸杂志是以节目的播放时间、广告顺序以及报刊杂志的期数来决定投放的周期的。互联网广告则以开始日期、结束日期以及投放时段来决定投放周期的（需要注意的是：投放时间是以服务器的时间为准的）。 说明：互联网的时间使用的是UTC时间体系，北京时间=UTC+8。（关于UTC时间和GMT时间以及北京时间的关系）

问题：在广告系统设计时，怎样设计可以使用户方便快捷的设置每天不同的投放时段？

网页定向

网页定向指的是针对特定的URL进行定向，使广告投放在指定的URL上。网页定向是互联网广告定向中不常使用的定向。

网页定向最核心的技术有两个：

1、如何获取当前页的URL，注意是当前页非Http Header中的Reffer。当前页URL需要通过加在页面上的JS代码获得，设计时需要考虑到如果JS代码被放在iFrame中的情况，甚至会被放置到好几层嵌套的iFrame上（这样放置代码的媒体更多为了作弊，可以参见在线广告作弊手段一览【见下】）。

2、广告系统在定向设置时需要考虑到URL匹配问题。左匹配、右匹配、包含、不包含、通配符等。匹配规则需要在广告投放核心进行处理。

访客频次

频次是广告投放中一个非常重要的概念。网络广告的频次和其他媒介投放时的频次概念是一致的。

频次是指个人或家庭接触广告信息的次数。在传统的电视媒介中，我们不能准确的控制每一个人接触广告信息的次数，只能是通过总收视点除以到达率计算得出。但是在网络广告中，一个人可以接触广告信息的最高频次是可以严格控制的，实现严格控制的基础技术也是cookie，可见cookie对于互联网广告精准投放的重要性。

在网络广告的投放中，频次的控制对象比其他媒介更广泛，频次可以控制广告的浏览、点击、完整浏览，甚至是广告的转发、下载等其他的行为，因此互联网的频次指的是访客与广告发生互动的最高次数，而互动的行为设定则需要能够在广告系统中进行设置。当然经常还是对广告的浏览进行频次设置，我们也以此举例。

网络广告频次控制的原理非常简单。当用户通过浏览器访问页面时，会请求放置在页面的广告位代码，广告位代码和服务器进行交互，广告位代码将用户的cookie信息（包含对广告的访问次数）传给服务器（如果没有cookie，服务器会生成一个），服务器进行频次的匹配，超过频次设定的广告将不会被投放，在同时判断了其他定向条件后，服务器回传适合的广告到浏览器进行投放，在返回信息的同时，还会将用户cookie上此广告的浏览次数加1。通过这种方式，网络广告实现了精确的频次控制。

广告投放中，并不是频次越高越好，过少的接触不会在接触的用户心中产生印象，过多的接触反而会使接触的用户产生不快，厌恶。1972年，美国心理学家赫尔伯特.克鲁格曼经过研究，确立了消费者接触广告三次的心理学关系：第一次好奇：“这是什么？”第二次是认识：“干什么用的？”第三次是判断：“对广告产生什么印象？”。当然，因为产品、市场、品牌、竞争、创意以及媒体等不同，在频次设置上也会有所不同，不过，对广告的有效接触频次限定一般都是以3次为底限的。

为了了解广告的投放效果，在报表中，广告系统一般会提供平均接触频次、频次分布图。

讨论：频次分布图是什么样子？设计时需要注意什么？

关键词定向

我们所讲的关键词定向实际上就是Google AdWords中的内容相关广告（Contextual）。

关键词定向实现必须具备以下能力：

抓取网页内容并进行分析的能力

分析时需要考虑到页面的结构、html标签、链接等影响，对页面的正文进行分析，得到最恰当的一些关键词来描述页面所表达的内容。关键词定向是否有效的瓶颈即在于此。

需要注意的是，由于实时快速分析页面的要求非常高，当页面足够多的时候，系统执行效率会非常的低下，因此必须具有提前抓取有可能出现广告页面的能力。

当然，实时快速分析同样重要。

广告系统中设置广告投放关键词的能力

需要能够确保操作人员可以方便快捷的在系统中进行关键词的设置（正向选择、反向排除），如果能够提供对之前投放的关键词效果分析及推荐更好。

投放核心快速匹配投放能力

将1的分析结果和2的投放设置进行快速匹配并进行投放，这是最根本的要求。

关键词定向的效果：

———————————————— 版权声明：本文为CSDN博主「Jaybo\_」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。 原文链接：[](https://blog.csdn.net/u012195214/article/details/78889602)[https://blog.csdn.net/u012195214/article/details/78889602](https://blog.csdn.net/u012195214/article/details/78889602)
