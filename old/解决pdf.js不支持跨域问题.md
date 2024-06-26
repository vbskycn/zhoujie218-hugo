# 解决pdf.js不支持跨域问题



## pdf.js是什么

PDF.js是一个使用HTML5构建的可移植文档格式（PDF）查看器。





## 解决跨域问题

首先直接打开任何一个链接pdf文件是不存在跨域问题的，正是因为pdf.js需要通过ajax以文件流的形式去解析才造成了跨域问题。

当pdf.js从 [http://localhost](http://localhost/) 请求 http://localhost:8081/files/demo.pdf , 很遗憾啊，pdf.js发出了个警告：

```
file origin does not match viewer's
```

因为当前源与目标源不一样，pdf.js直接拦截了。



### **解决方法一（代理方式）：**

在[http://localhost](http://localhost/) 服务器配置代理，nginx如下：

```
location /files {
  proxy_pass http://localhost:8081/;
}
```

使用方法，不要带上前缀

```
http://localhost/pdf.js/web/viewer.html?file=/demo.pdf
```

**这种方法有缺点：**

1、不能使用完整链接，如：http://localhost:8081/files/demo.pdf

2、如果目标存在多个目录需要增加配置，如： /files/demo.pdf 、 /pdf/demo.pdf

------



### **解决方法二（配置CORS跨域）：**

在目标服务器 [http://localhost:8081](http://localhost:8081/) 新增下面头部即可。

```
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: GET, POST, PUT, OPTIONS
Access-Control-Expose-Headers: Accept-Ranges, Content-Encoding, Content-Length, Content-Range
```

nginx（其他服务器类似）：

```bash
location / {
  add_header Access-Control-Allow-Origin '*';
  add_header Access-Control-Allow-Methods 'GET, POST, PUT, OPTIONS';
  add_header Access-Control-Expose-Headers 'Accept-Ranges, Content-Encoding, Content-Length, Content-Range';
}
```

使用方法：

```
http://localhost/pdf.js/web/viewer.html?file=http://localhost:8081/demo.pdf
```

以为这样就大功告成了吗？ 很遗憾，还是报了之前的错误

```
file origin does not match viewer's
```

翻了翻官方文档，然而没有找到解决方案。但是并不能主档我前进，现在只好从源码入手。

在viewer.js文件里搜索关键字 （file origin does not match），哈哈真的有 （本来就有的好吗）。



贴下关键代码, 在3422行左右：

```javascript
  validateFileURL = function (file) {
    if (!file) {
      return;
    }

    try {
      const viewerOrigin = new URL(window.location.href).origin || "null";

      if (HOSTED_VIEWER_ORIGINS.includes(viewerOrigin)) {
        return;
      }

      const fileOrigin = new URL(file, window.location.href).origin;

      if (fileOrigin !== viewerOrigin) {
        throw new Error("file origin does not match viewer's");
      }
    } catch (ex) {
      PDFViewerApplication.l10n.get("loading_error").then(msg => {
        PDFViewerApplication._documentError(msg, {
          message: ex?.message
        });
      });
      throw ex;
    }
  };
}
```

这里使用了try捕捉错误，注意第2个条件语句，因为当前源与目标源不一样，所以抛出了异常。

```
if (fileOrigin !== viewerOrigin) {
//  throw new Error('file origin does not match viewer\'s');
}
```

![image-20240524085629289](https://img-cloud.zhoujie218.top/2024/05/24/664fe5c602f86.png)

很好解决，只要把throw这行注释即可。 这就到此结束了，完美解决跨域问题。

![img](https://img-cloud.zhoujie218.top/2024/05/24/664fe59428c92.jpeg)

------

还有一种解决方法（**不推荐**），网上基本答案都是这个，后端将文件转成流的形式传输给前端，然后前端处理文件流去展示。

这种方式非常的粗糙，最终还是存在跨域问题, 估计是没看源码才用的这种方法。



## 总结

解决问题还是需要有耐心才行，如果找不到解决方法那么就从源码入手即可。