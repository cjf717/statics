# git-CDN-静态文件

## 访问方法
- 默认提供的节点：cdn.jsdelivr.net（被和谐，不稳定）

- 可用的jsDelivr节点
常用于加速 GitHub/npm 项目，可通过更改节点改善项目在国内的可用性。

|节点|描述|可用性|
|----|----|----|
|gcore.jsdelivr.net|Gcore 节点|可用性高|
|testingcf.jsdelivr.net|Cloudflare 节点|可用性高|
|quantil.jsdelivr.net|Quantil 节点|可用性一般|
|fastly.jsdelivr.net|Fastly 节点|可用性一般|

- 第三方提供的jsDelivr节点
以下是一些第三方提供的 jsDelivr 节点，可用于国内访问。

|节点|描述|
|----|----|
|jsd.cdn.zzko.cn|    国内CDN    |
|jsd.onmicrosoft.cn|    国内CDN    |
|jsdelivr.b-cdn.net|    台湾CDN    |
|cdn.jsdelivr.us|    Anycast    |

- 访问地址
  * 默认版本：https://cdn.jsdelivr.net/gh/cjf717/statics/
  * 最后更新版本：https://cdn.jsdelivr.net/gh/cjf717/statics@latest/
  * 指定分支版本：https://cdn.jsdelivr.net/gh/cjf717/statics@master/
  * 指定标签版本：https://cdn.jsdelivr.net/gh/cjf717/statics@0.1/

## 强制更新
Github文件已更改，jsdelivr CDN没更新。
是因为 jsdelivr CDN 缓存的原因，一般来说是 24小时刷新缓存，但是这样太慢了！

不过 jsdelivr CDN 也提供手动刷新缓存的方法：

```shell
# 假设你的文件 URL 是这样：
https://cdn.jsdelivr.net/xxx/xxx...
 
# 那么把域名中的 cdn 改为 purge 即可：
https://purge.jsdelivr.net/xxx/xxx...
```

然后访问这个文件新 URL 就会提示你刷新成功！记得在调用的网页中强刷新一下

但是这种方式貌似短时间只能用一次，之后更改文件后，在使用就不生效了