---
title: "如何设置WordPress文章特色图像(Featured Image)"
date: "2016-06-17"
categories: 
  - "diannaowangruo"
  - "wangyesheji"
tags: 
  - "wordpress"
url: "/archives/213.html"
---

在主题的functions.php中添加如下代码

<table border="0" cellspacing="0" cellpadding="0"><tbody><tr><td class="gutter"><p class="line number1 index0 alt2">1</p><p class="line number2 index1 alt1">2</p><p class="line number3 index2 alt2">3</p><p class="line number4 index3 alt1">4</p></td><td class="code"><p class="line number1 index0 alt2"><code class="php comments">//使WordPress支持post thumbnail</code></p><p class="line number2 index1 alt1"><code class="php keyword">if</code> <code class="php plain">( function_exists( </code><code class="php string">'add_theme_support'</code> <code class="php plain">) ) {</code></p><p class="line number3 index2 alt2"><code class="php spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="php plain">add_theme_support( </code><code class="php string">'post-thumbnails'</code> <code class="php plain">);</code></p><p class="line number4 index3 alt1"><code class="php plain">}</code></p></td></tr></tbody></table>

**注意：**这段代码应当加载functions.php的body中，不要写进函数里。

<table border="0" cellspacing="0" cellpadding="0"><tbody><tr><td class="gutter"><p class="line number1 index0 alt2">1</p></td><td class="code"><p class="line number1 index0 alt2"><code class="php plain">add_image_size( </code><code class="php variable">$name</code><code class="php plain">, </code><code class="php variable">$width</code><code class="php plain">, </code><code class="php variable">$height</code><code class="php plain">, </code><code class="php variable">$crop</code> <code class="php plain">);</code></p></td></tr></tbody></table>

在functions.php中，写在add\_theme\_support()之后,完整代码如下

<table border="0" cellspacing="0" cellpadding="0"><tbody><tr><td class="gutter"><p class="line number1 index0 alt2">1</p><p class="line number2 index1 alt1">2</p><p class="line number3 index2 alt2">3</p><p class="line number4 index3 alt1">4</p><p class="line number5 index4 alt2">5</p><p class="line number6 index5 alt1">6</p><p class="line number7 index6 alt2">7</p><p class="line number8 index7 alt1">8</p></td><td class="code"><p class="line number1 index0 alt2"><code class="php comments">//add post thumbnails</code></p><p class="line number2 index1 alt1"><code class="php keyword">if</code> <code class="php plain">( function_exists( </code><code class="php string">'add_theme_support'</code> <code class="php plain">) ) {</code></p><p class="line number3 index2 alt2"><code class="php spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="php plain">add_theme_support( </code><code class="php string">'post-thumbnails'</code> <code class="php plain">);</code></p><p class="line number4 index3 alt1"><code class="php plain">}</code></p><p class="line number6 index5 alt1"><code class="php keyword">if</code> <code class="php plain">( function_exists( </code><code class="php string">'add_image_size'</code> <code class="php plain">) ) {</code></p><p class="line number7 index6 alt2"><code class="php spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="php plain">add_image_size( </code><code class="php string">'customized-post-thumb'</code><code class="php plain">, 100, 120 );</code></p><p class="line number8 index7 alt1"><code class="php plain">}</code></p></td></tr></tbody></table>

创建几个不同的缩略图尺寸，用到的函数：

[Post Thumbnail功能详细说明](http://codex.wordpress.org/Function_Reference/the_post_thumbnail)

### 如何调用特色图像

在post模板中

<table border="0" cellspacing="0" cellpadding="0"><tbody><tr><td class="gutter"><p class="line number1 index0 alt2">1</p><p class="line number2 index1 alt1">2</p><p class="line number3 index2 alt2">3</p><p class="line number4 index3 alt1">4</p><p class="line number5 index4 alt2">5</p><p class="line number6 index5 alt1">6</p></td><td class="code"><p class="line number1 index0 alt2"><code class="php plain">&lt;?php</code></p><p class="line number2 index1 alt1"><code class="php keyword">if</code> <code class="php plain">( has_post_thumbnail() ) { </code><code class="php comments">// check if the post has a Post Thumbnail assigned to it.</code></p><p class="line number3 index2 alt2"><code class="php spaces">&nbsp;&nbsp;</code><code class="php plain">the_post_thumbnail();</code></p><p class="line number4 index3 alt1"><code class="php plain">}</code></p><p class="line number5 index4 alt2"><code class="php plain">?&gt;</code></p><p class="line number6 index5 alt1"><code class="php plain">&lt;?php the_content(); ?&gt;</code></p></td></tr></tbody></table>

可以调用不同尺寸的图片

<table border="0" cellspacing="0" cellpadding="0"><tbody><tr><td class="gutter"><p class="line number1 index0 alt2">1</p><p class="line number2 index1 alt1">2</p><p class="line number3 index2 alt2">3</p><p class="line number4 index3 alt1">4</p><p class="line number5 index4 alt2">5</p><p class="line number6 index5 alt1">6</p><p class="line number7 index6 alt2">7</p><p class="line number8 index7 alt1">8</p></td><td class="code"><p class="line number1 index0 alt2"><code class="php plain">the_post_thumbnail();&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </code><code class="php comments">// 无参数，默认调用Thumbnail</code></p><p class="line number3 index2 alt2"><code class="php plain">the_post_thumbnail(</code><code class="php string">'thumbnail'</code><code class="php plain">);&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </code><code class="php comments">// Thumbnail (默认尺寸 150px x 150px max)</code></p><p class="line number4 index3 alt1"><code class="php plain">the_post_thumbnail(</code><code class="php string">'medium'</code><code class="php plain">);&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </code><code class="php comments">// Medium resolution (default 300px x 300px max)</code></p><p class="line number5 index4 alt2"><code class="php plain">the_post_thumbnail(</code><code class="php string">'large'</code><code class="php plain">);&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </code><code class="php comments">// Large resolution (default 640px x 640px max)</code></p><p class="line number6 index5 alt1"><code class="php plain">the_post_thumbnail(</code><code class="php string">'full'</code><code class="php plain">);&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </code><code class="php comments">// Full resolution (original size uploaded)</code></p><p class="line number8 index7 alt1"><code class="php plain">the_post_thumbnail( </code><code class="php keyword">array</code><code class="php plain">(100,100) );&nbsp; </code><code class="php comments">// Other resolutions</code></p></td></tr></tbody></table>

### 如何从后台修改缩略图尺寸

\[caption id="attachment\_2227" align="aligncenter" width="500"\][![从后台修改缩略图尺寸](https://img-cloud.zhoujie218.top/wp-content/uploads/2021/11/20211101045445527.gif "media")](https://img-cloud.zhoujie218.top/wp-content/uploads/2021/11/20211101045445527.gif) 从后台修改缩略图尺寸\[/caption\]

访问**后台>>设置>>媒体**，缩略图大小这一项就是特色图像（Featured Image or Thumbnail）的尺寸，也就是the\_post\_thumbnail()不加参数时调用的图片的尺寸。根据需要修改其参数即可。上传图片时WordPress会自定生成这个尺寸的图片。

### 为文章添加特色图片的三种方法

编辑文章时我们有三种方式添加特色

1. 上传图片时点击“**作为特色图像**”进行设置，如下图所示，点击后显示“**完成**”即表示设置成功。设置好的特色图像会在右侧栏目中显示出来。

\[caption id="attachment\_2228" align="aligncenter" width="500"\][![上传图片时设置特色图片](https://img-cloud.zhoujie218.top/wp-content/uploads/2021/11/20211101045446874.gif "上传图片时设置特色图片")](https://img-cloud.zhoujie218.top/wp-content/uploads/2021/11/20211101045446874.gif) 上传图片时设置特色图片\[/caption\]

2. 点击右侧栏目中的特色图像设置，如下图所示，点击“**设置特色图像**”按钮后弹出与方法一一样的界面，设置方法也相同

\[caption id="attachment\_2229" align="aligncenter" width="291"\][![从右侧工具栏设置特色图像](https://img-cloud.zhoujie218.top/wp-content/uploads/2021/11/20211101045447544.gif "从右侧工具栏设置特色图像")](https://img-cloud.zhoujie218.top/wp-content/uploads/2021/11/20211101045447544.gif) 从右侧工具栏设置特色图像\[/caption\]

3. 如果你没有用上述两种方法设置，那么你也许希望从文章中已经存在的图片中选取一张作为特色图像，WordPress考虑的很周到，你可以轻松选择文中已有的图像。

点击右侧工具栏的**设置特色图像**按钮，弹出如下所示对话框，选项卡切换到**相册**，就可以看到所有文中已经插入的图片，点击显示就会出现和方法一一样的界面，照着方法一设置即可。

\[caption id="attachment\_2230" align="aligncenter" width="500"\][![选项卡切换到“相册”](https://img-cloud.zhoujie218.top/wp-content/uploads/2021/11/20211101045447964.gif "选项卡切换到“相册”")](https://img-cloud.zhoujie218.top/wp-content/uploads/2021/11/20211101045447964.gif) 选项卡切换到“相册”\[/caption\]
