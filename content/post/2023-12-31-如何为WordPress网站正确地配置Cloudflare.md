---
title: "如何为WordPress网站正确地配置Cloudflare"
date: "2023-12-31"
categories: 
  - "wangyesheji"
tags: 
  - "cloudflare"
  - "wordpress"
url: "/archives/2580.html"
---

通过在您的站点前充当\[反向代理\]，Cloudflare是一种一体化的安全和性能产品，被全球超过12%的网站使用。作为WordPress 用户，将Cloudflare添加到您的网站有助于提高网站性能并减少恶意机器人和黑客的影响。

正确配置后，对您站点的所有请求将首先到达Cloudflare服务器，然后该服务器将确定是否应将请求转发到源服务器、从缓存中提供服务、阻止或使用自定义规则进行处理。

在本指南中，我们将深入探讨WordPress的最佳Cloudflare设置，讨论缓存和安全设置，并向您展示如何为WordPress多站点安装配置Cloudflare 。

1. **如何为WordPress配置Cloudflare**
2. **Cloudflare WordPress插件**
3. **WordPress的Cloudflare自动平台优化**
4. **Cloudflare Argo和Railgun**
5. **如何为WordPress多站点配置Cloudflare**

### 如何为WordPress配置Cloudflare

Cloudflare提供了多种安全和性能优势，但并非所有这些优势都与WordPress完全兼容。让我们深入了解Cloudflare的设置，以确定适合您的WordPress网站的最佳功能。

1. **SSL**
2. **速度**
3. **缓存**
4. **防火墙**

#### SSL

Cloudflare支持四种SSL/TLS加密模式——Off, Flexible, Full和Full (Strict)。

- **Off –**不加密。
- **Flexible –**仅加密浏览器和Cloudflare之间的连接。
- **Full –**端到端加密，但允许在源服务器上使用自签名证书。
- **Ful (Strict) –**端到端加密，需要来自Cloudflare的免费原始证书或来自受信任CA（证书颁发机构）的证书。我们建议使用Full (Strict) SSL模式以获得最大的安全性。

对于希望在其WordPress网站上使用Cloudflare的用户，我们建议[在宝塔面板中生成免费的Let’s Encrypt SSL证书](https://www.wbolt.com/how-to-install-ssl-certificate.html)，并在Cloudflare中使用Full或Full (Strict) 选项。

或者，您还可以生成Cloudflare原始证书以安装在您的原始服务器上。如果您的主机不提供免费的SSL证书，则在您的服务器上安装Cloudflare原始证书将允许您使用Full (Strict) SSL模式。

如果您使用在子域上托管站点，而根域使用Cloudflare的Flexible SSL，则可以使用Cloudflare页面规则强制子域使用Full或Full (Strict) SSL。

![](https://img-cloud.zhoujie218.top/2023/12/31/65917a247f948.webp)

为具有Cloudflare页面规则的子域启用Full (Strict) SSL

此选项允许您使用Cloudflare的Flexible SSL，同时确保子域的Cloudflare Full (Strict) SSL。

**始终使用HTTPS**

我们建议启用此选项以自动[将所有HTTP请求转发到HTTPS](https://www.wbolt.com/redirect-http-to-https.html)。

**HSTS**

HSTS代表“HTTP Strict Transport Security”，用于强制Web浏览器使用安全的HTTPS连接。在Cloudflare上启用HSTS可确保[HTTP请求](https://www.wbolt.com/make-fewer-http-requests.html)永远不会到达您的源服务器。如果您的站点已设置为使用HTTPS，我们建议您也在源服务器上[配置HSTS](https://www.wbolt.com/hsts-strict-transport-security.html)。

**最低TLS版本**

[TLS（传输层安全性）](https://www.wbolt.com/tls-1-3.html)是一种加密协议，允许通过网络安全传输数据。默认情况下，Cloudflare为协议版本设置TLS 1.0。某些安全标准（例如 PCI DSS 3.2）需要更新版本的TLS协议以实现合规性。如果您的站点需要某个TLS版本，您可以通过转到**SSL/TLS > Edge Certificates > Minimum TLS Version**来更改设置。

**自动HTTPS重写**

此功能检查HTML代码中的HTTP资源URL以查看它们是否可通过HTTPS访问。如果是这样，它们将使用HTTPS变体自动重写。自动HTTPS重写对于确保没有混合内容错误的安全浏览体验非常有用。

#### 速度（Speed）

大多数与性能相关的Cloudflare设置，例如资产缩小和图像优化，都可以在“Speed”选项卡中找到。

**图像大小调整（仅限商业计划）**

Cloudflare的图像大小调整功能仅适用于商业计划用户。在您的WordPress主题中正确实施后，此功能可用于将图像缩略图生成offload到Cloudflare。与WordPress中的内置缩略图生成功能相比，这有几个好处。

对于动态生成图像大小的站点，使用Cloudflare的图像大小调整功能可以降低CPU使用率——这允许您的站点在不增加CPU资源的情况下为更多并发用户提供服务。Cloudflare图像大小调整还有助于减少磁盘空间使用，因为缩略图不必存储在服务器上。

Cloudflare图像大小调整通过在图像前添加端点来工作。请看下面的示例，该示例显示了该功能的工作原理。

原始图片网址

`https://yourdomain.com/wp-content/uploads/2020/01/picture.jpg`

调整大小的图像URL

`https://yourdomain.com/cdn-cgi/image/fit=contain,format=auto,metadata=none,onerror=redirect,quality=70,width=720/https://yourdomain.com/wp-content/uploads/2020/01/picture.jpg`

可以调整“宽度”参数以动态生成不同的缩略图大小，而无需在源服务器上增加任何额外的资源负载。如果您正在寻找类似于Cloudflare的图像大小调整功能的独立服务，Imgix和Cloudinary是不错的选择。

不要忘记查看我们关于[优化网络图像](https://www.wbolt.com/how-to-optimize-images-for-web-and-performance.html)的深入指南。

**Polish（仅限专业版）**

Cloudflare Polish是一种图像优化服务，可自动压缩[JPG](https://www.wbolt.com/jpg-vs-jpeg.html)、PNG、[GIF](https://www.wbolt.com/how-to-use-gifs-on-wordpress.html)和其他图像文件。图像在Cloudflare边缘处理，这意味着托管WordPress站点的服务器没有性能负担。Polish还支持[Google的WEBP格式](https://www.wbolt.com/how-to-use-webp-images-on-wordpress.html) ——这意味着优化的WEBP图像将自动提供给支持该格式的Chrome、Brave和其他浏览器。

出于几个原因，Polish是WordPress网站的一项有用功能。如果您使用的是[ShortPixel](https://www.wbolt.com/go?_=e9641f45b7aHR0cHM6Ly9zaG9ydHBpeGVsLmNvbS8%3D)或[Imagify](https://www.wbolt.com/go?_=f390bda346aHR0cHM6Ly9pbWFnaWZ5LmlvLw%3D%3D)等图像优化插件，Polish可以显着降低服务器的CPU使用率——这可以为访问者带来更稳定的浏览体验。由于Polish的图像是在服务器外存储和缓存的，因此您不必担心用尽磁盘空间来存储图像的WEBP版本。

**Auto Minify**

Cloudflare的Auto Minify功能会自动缩小缓存的CSS、JSS和HTML资产。如果您不使用[Autoptimize](https://www.wbolt.com/autoptimize-settings.html)或[WP-Rocket](https://www.wbolt.com/how-to-install-configure-wp-rocket.html)等WordPress插件来缩小资产，我们建议您在Cloudflare中启用自动缩小功能。

**Brotli**

Brotli是GZIP的替代方案，[GZIP](https://www.wbolt.com/enable-gzip-compression.html)是一种压缩算法，可在将Web请求提供给访问者之前减小它们的大小。与GZIP相比，Brotli提供了更高的压缩比，这意味着用户的页面加载速度更快。问题是并非所有的网络浏览器都支持Brotli压缩。无论如何，我们建议启用Cloudflare的Brotli功能，因为来自不受支持的浏览器的请求只会退回到GZIP压缩。

**增强的HTTP/2优先级（仅限专业版）**

[HTTP/2](https://www.wbolt.com/what-is-http2.html)的引入通过并行化和多路复用为网站带来了显着的性能提升。Cloudflare增强的HTTP/2优先级功能更进一步，它通过智能解析您网站的HTML来确定加载资产的顺序以获得最佳性能。根据[Cloudflare](https://www.wbolt.com/go?_=416a5a040baHR0cHM6Ly9ibG9nLmNsb3VkZmxhcmUuY29tL2JldHRlci1odHRwLTItcHJpb3JpdGl6YXRpb24tZm9yLWEtZmFzdGVyLXdlYi8%3D)的说法，增强的HTTP/2优先级可以将页面加载时间减少多达50%。

**Mirage（仅限专业版）**

Mirage是一项针对移动和低带宽连接的[图像优化功能。](https://www.wbolt.com/how-to-optimize-images-for-web-and-performance.html)启用Mirage后，在初始页面加载期间，图像将替换为低分辨率占位符。页面加载后，全分辨率图像被延迟加载。

Mirage还能够将多个图像请求组合成一个请求，从而减少完全加载页面所需的往返次数。如果您的网站使用大量图片并针对移动设备较多的人群，Cloudflare Mirage可以对性能产生积极影响。

**Rocket Loader**

Rocket Loader是一项通过异步加载JavaScript资源来加快加载时间的功能。这有效地[减少了页面的渲染阻塞内容](https://www.wbolt.com/eliminate-render-blocking-javascript-css.html)，从而加快了页面加载时间。我们建议您在启用Rocket Loader的情况下测试您的网站，看看它是否能提高您的页面速度。如果您的WordPress站点依赖于以特定顺序加载的JavaScript资产，您可以通过向脚本标签添加属性`data-cfasync="false"`来绕过Rocket Loader。

#### 缓存（Caching）

默认情况下，Cloudflare会缓存CSS 、JS和图像文件等静态资产。请注意，默认情况下，Cloudflare不会缓存您网站生成的HTML。

**缓存级别**

我们建议将缓存级别保留为“Standard”，这允许使用唯一查询字符串访问资产的更新版本。

**浏览器缓存有效期**

如果你的服务器本身已经设置了浏览器缓存有效期，我们建议将浏览器缓存过期设置设置为“Respect Existing Headers”。如果您想用更短的过期时间覆盖此设置，请随时更改此设置。

#### 防火墙（Firewall）

如果您的主机不提供可自定义的防火墙，Cloudflare的免费计划包括一个允许五个自定义规则的基本防火墙。防火墙规则可以配置为阻止特定的IP地址、用户代理、请求方法、HTTP引用，甚至国家。

例如，如果您发现您的WooCommerce商店从目标市场以外的国家/地区收到大量虚假订单，您可以使用Cloudflare的免费防火墙来阻止来自整个国家/地区的流量。

Cloudflare的Pro计划具有更强大的Web应用程序防火墙 (WAF)。WAF提供专门的托管规则集，有助于进一步保护您的站点。例如，有一些针对WordPress和PHP站点的规则集。

![](https://img-cloud.zhoujie218.top/2023/12/31/65917a31de707.webp)

用于WordPress的Cloudflare托管规则集

对于大多数WordPress网站，Cloudflare的免费计划提供的安全级别就足够了。但是，如果您正在运行需要更多保护的任务关键型业务站点，Cloudflare的专业级WAF和托管规则集可以帮助进一步保护您的站点。

（推荐阅读：[Sucuri vs Wordfence](https://www.wbolt.com/wordfence-vs-sucuri.html)）

#### 网络（Network）

在Cloudflare的“Network”设置中，我们建议启用HTTP/2、[HTTP/3](https://www.wbolt.com/http3.html)（使用QUIC）和0-RTT连接恢复。

正如我们前面提到的，HTTP/2通过并行化和多路复用为HTTP/1.1带来了一些改进。类似地， HTTP/3通过使用称为QUIC的新的基于UDP的协议而不是传统的TCP，[进一步扩展了HTTP/2的性能](https://www.wbolt.com/http3.html)。

![](https://img-cloud.zhoujie218.top/2023/12/31/65917a31de707.webp)

启用HTTP/2、HTTP/3和0-RTT连接恢复

安全的HTTP/3连接还受益于优化的握手例程，从而缩短了连接时间。在Cloudflare仪表盘中启用HTTP/3后，受支持的客户端将能够使用HTTP/3连接到Cloudflare服务器。

最后，Cloudflare的0-RTT连接恢复功能缩短了之前连接到您网站的访问者的加载时间。

#### 页面规则（Page Rules）

Cloudflare的页面规则功能允许您自定义特定URL的设置。页面规则对于禁用某些资产的缓存、更改所选页面的安全级别等很有用。Cloudflare页面规则有两个关键组件——URL匹配模式和对匹配的URL执行的操作。在下面的屏幕截图中，您可以看到将www URL重定向到非www版本的Cloudflare页面规则。

![](https://img-cloud.zhoujie218.top/2023/12/31/659179556c148.webp)

Cloudflare转发URL页面规则

此规则匹配以 `www.brianonwp.com`开头的URL。请注意星号字符的包含，它允许您创建通配符匹配模式。把星号想象成“这里的任何东西”。在URL模式下，您可以看到该页面规则配置为301将所有匹配的请求重定向到`https://brianonwp.com/$1`，其中“$1”是指匹配模式中的“第一个通配符”。

使用像这样的页面规则，请求`www.brianli.com/specific-page/`将被重定向到`brianli.com/specific-page/`.

使用Cloudflare页面规则，您可以将特定设置应用于任何匹配的URL。查看下面可应用于页面规则的设置列表。某些设置甚至可以组合成一个页面规则！

- **Always Online –**启用或禁用Cloudflare的“Always Online”功能，如果发现原始服务器离线，该功能会提供页面的静态HTML副本。
- **Always Use HTTPS –**对匹配的URL强制使用HTTPS。
- **Auto Minify –**启用或禁用HTML、CSS和JS缩小。
- **Automatic HTTPS Rewrites –**启用将HTML中的HTTP URL重写为HTTPS版本。
- **Browser Cache TTL –**指定匹配URL上的浏览器缓存TTL。例如，您可以为不同类型的文件设置不同的浏览器缓存TTL。
- **Browser Integrity Check –**启用或禁用Cloudflare的“Browser Integrity Check”功能，该功能检查HTTP标头以清除机器人和恶意流量。
- **Cache Deception Armor –**启用或禁用Cloudflare的“Cache Deception Armor”功能，该功能通过确保资产的文件扩展名与其“Content-Type”匹配来防止[Web缓存欺骗攻击](https://www.wbolt.com/go?_=726af218fbaHR0cHM6Ly9ibG9nLmNsb3VkZmxhcmUuY29tL3dlYi1jYWNoZS1kZWNlcHRpb24tYXR0YWNrLXJldmlzaXRlZC8%3D)。
- **Cache Level –**配置匹配URL的缓存级别。
- **Disable Apps –**禁用Cloudflare应用程序集成以匹配URL。
- **Disable Performance –**禁用匹配URL的性能相关功能。
- **Disable Railgun –**禁用Railgun以匹配URL。
- **Disable Security –**禁用匹配URL的安全功能。
- **Edge Cache TTL –**指定边缘缓存TTL（资产在Cloudflare的边缘网络上缓存的时间量）。
- **Email Obfuscation –**启用或禁用Cloudflare的电子邮件混淆脚本，该脚本通过扰乱电子邮件地址来减少成功的机器人抓取。
- **Forwarding URL –**创建一个301或302重定向到另一个URL。
- **IP Geolocation Header –**启用或禁用Cloudflare的IP地理位置HTTP标头。
- **Opportunistic Encryption –**允许客户端通过安全的TLS通道访问HTTP URL。
- **Origin Cache Control –**指定您希望Cloudflare如何响应源服务器的“Cache-Control”指令。
- **Rocket Loader –**在匹配的URL上启用或禁用Rocket Loader。
- **Security Level –**指定匹配URL的安全级别。
- **Server Side Excludes –**`<!--sse-->`启用或禁用Cloudflare的“服务器端排除”功能，该功能可让您通过在标签中包装HTML来隐藏可疑流量中的敏感信息。
- **SSL –**指定匹配URL的SSL级别（disabled, flexible, full, or full strict）。

### Cloudflare WordPress插件

Cloudflare团队维护一个[官方的WordPress插件](https://www.wbolt.com/go?_=742870ac52aHR0cHM6Ly93b3JkcHJlc3Mub3JnL3BsdWdpbnMvY2xvdWRmbGFyZS8%3D)。虽然这个插件不是绝对要求，但它确实提供了一些不错的功能，包括WordPress优化的Cloudflare设置、WordPress特定的安全规则集、自动缓存清除、HTTP/2服务器推送等。

![](https://img-cloud.zhoujie218.top/2023/12/31/6591795572e43.webp)

Cloudflare WordPress插件设置

### WordPress的Cloudflare自动平台优化

[Cloudflare的WordPress自动平台优化 (APO)](https://www.wbolt.com/cloudflare-apo-wordpress.html)是针对WordPress网站的专用性能优化服务。Cloudflare APO的工作原理是直接在Cloudflare边缘网络上缓存您的WordPress站点的HTML页面。这是对CDN上静态资产（CSS、JS、图像等）的典型缓存的一大飞跃。在我们的基准测试中，我们发现启用Cloudflare APO会导致性能提高70-300%，具体取决于测试位置。

Cloudflare APO for WordPress通过将页面的HTML副本存储在Workers KV中来工作，Workers KV是一种全球分布的键值存储服务。启用APO后，对您站点的请求将由Workers KV或Cloudflare的边缘缓存而不是您的源服务器提供服务。这是WordPress性能领域向前迈出的一大步，因为有了APO，WordPress站点不再受源服务器位置的限制。

![](https://img-cloud.zhoujie218.top/2023/12/31/65917a3d43599.webp)

在Cloudflare仪表盘中为WordPress启用自动平台优化

以前，使用传统的CDN设置，HTML页面仍然必须由源服务器提供服务。例如，如果您网站的源服务器位于美国，则来自伦敦的访问者必须等待从美国发送的HTML文档。使用APO，HTML和其他静态资产由靠近伦敦的Cloudflare数据中心提供。

Cloudflare APO与传统博客、新闻站点、登录页面和其他不依赖动态功能的站点（WooCommerce商店、论坛等）最兼容。APO会自动绕过Cloudflare对登录用户和包含某些cookie的页面（例如WooCommerce）的HTML缓存。APO作为Cloudflare Pro、Business和Enterprise计划的免费服务提供。对于免费的Cloudflare用户，APO是每月5美元的附加组件。

如果您有兴趣了解有关Cloudflare APO的更多信息，请[在此处查看我们的深入指南](https://www.wbolt.com/cloudflare-apo-wordpress.html)。

### Cloudflare Argo和Railgun

Cloudflare提供额外的性能产品，可能有助于进一步[提升您的WordPress网站的性能](https://www.wbolt.com/speed-up-wordpress.html)。这些功能需要支付额外费用，但如果您想在网站优化方面加倍努力，它们可能值得一看。

#### Argo

Argo是一项Cloudflare附加服务，可为您的网站提供“智能路由”。启用Argo后，流量将围绕Cloudflare网络中的拥塞区域进行路由。在我们的测试中，Argo将页面加载时间减少了20-30%。如果您是Cloudflare用户，希望在性能优化方面更加努力，那么试用Argo可能会产生积极的结果。

#### Railgun

Cloudflare的Railgun是一种WAN产品，可在您的服务器和Cloudflare的服务器之间建立安全隧道。Railgun旨在通过仅提供请求之间的整体差异来加速未缓存内容的交付。例如，如果页面A和页面B具有相同的页眉和页脚结构，但正文内容不同，Railgun会意识到这一点，并仅通过高度压缩的二进制数据流来处理差异。

Railgun仅适用于Cloudflare的商业和企业计划，并且需要您的网络主机在您站点的服务器上安装其他软件。对于大多数用户来说，使用Cloudflare保持快速加载时间不需要Railgun加速。但是，如果您正在运行无法缓存的高流量WooCommerce商店或论坛，Railgun可能有助于提高您的网站速度。

### 如何为WordPress多站点配置Cloudflare

如果您将Cloudflare与WordPress多站点一起使用，则在设置时应考虑一些特殊注意事项。

#### SSL设置

为了演示适用于WordPress多站点的Cloudflare SSL设置，我们创建了一个测试子域多站点，因为如果您使用子目录多站点，您应该不会遇到任何SSL问题。

这是我们的测试子域WordPress多站点的结构：

- 主站点 – brianwp.com和www.brianwp.com
- 子站点 1 – site1.brianwp.com
- 子站点 2 – site2.brianwp.com

首选，我们需要为多站点添加了域。

同样，域已在Cloudflare中配置了适当的A记录。Cloudflare代理也已启用，如橙色云图标所示。

![](https://img-cloud.zhoujie218.top/2023/12/31/65917957c1c85.webp)

WordPress多站点的Cloudflare DNS记录

要在Ful (Strict) SSL模式下使用Cloudflare，所有关联的域都必须存在于源服务器的SSL证书上。有两种方法可以做到这一点。

**让我们加密或付费SSL**

如果您的主机支持免费的[Let’s Encrypt SSL](https://www.wbolt.com/how-ssl-works.html)，请继续生成涵盖所有多站点域的SSL证书。

在宝塔面板上，你可以轻松生成涵盖所有域的SSL证书。

![](https://img-cloud.zhoujie218.top/2023/12/31/65917957cdf2c.webp)

在宝塔面板中为您的多站点生成SSL证书

**Cloudflare Origin SSL证书**

或者，您可以生成涵盖多站点域的Cloudflare Origin SSL证书。要生成原始证书，请导航到SSL/TLS > Origin Server，然后单击“Create Certificate”。

![](https://img-cloud.zhoujie218.top/2023/12/31/659179581e380.webp)

生成Cloudflare原始证书

原始证书生成菜单分为三个部分。在第一部分中，选择“Let Cloudflare generate a private key and a CSR”，除非您有特定理由提供自己的凭据。

在第二部分中，输入SSL证书需要覆盖的域和子域。您只能为Cloudflare帐户中的域生成证书。

最后，在第三部分，选择证书有效期。

设置包含所有多站点域的正确SSL证书后，您将能够在推荐的Full (Strict) SSL模式下使用Cloudflare。如果您将来需要向多站点添加其他域或子域，请务必生成涵盖其他域的新SSL证书。

#### WordPress多站点的页面规则

Cloudflare的其他安全和性能功能全局适用于您的根域下的所有子域。换句话说，如果我们的主站点brianwp.com启用了CSS缩小，那么site1.brianwp.com和site2.wpbrianli.com也将启用它。

在某些情况下，此默认行为可能会导致问题。例如，您可能不想仅仅因为它与单个子站点不兼容而全局禁用HTML、CSS和JS优化。要解决此问题，您可以使用自定义页面规则有选择地禁用特定子域的功能。

在下面的示例中，我们设置了一个针对`*site2.brianwp.com/*`页面规则. `*`字符用于指定通配符行为。您可以将其`*`视为“这里的任何东西”。

对于此页面规则，我们禁用了HTML、CSS和JS的自动缩小，禁用了Rocket Loader，绕过了Cloudflare缓存，并关闭了自动HTTPS重写。

![](https://img-cloud.zhoujie218.top/2023/12/31/65917a85a1133.webp)

创建选择性Cloudflare页面规则以定位WordPress子网站

如果您使用Cloudflare的免费计划，请注意它仅附带三个页面规则。如果您需要对多个子站点进行选择性调整，则需要升级到Pro计划或[购买额外的页面规则](https://www.wbolt.com/go?_=b04b4f30b4aHR0cHM6Ly9zdXBwb3J0LmNsb3VkZmxhcmUuY29tL2hjL2VuLXVzL2FydGljbGVzLzIyNTg5NDQyOC1Ib3ctVG8tQnV5LUFkZGl0aW9uYWwtUGFnZS1SdWxlcw%3D%3D)。

### 小结

了解如何为您的WordPress网站配置Cloudflare以及如何与您的托管堆栈正确集成可以对您的网站速度和安全性产生积极影响。
