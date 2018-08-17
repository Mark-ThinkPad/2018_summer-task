# 暑假作业(Docker)

---

## 目录

<!-- TOC -->

- [暑假作业(Docker)](#暑假作业docker)
    - [目录](#目录)
    - [开发环境](#开发环境)
    - [安装](#安装)
    - [学习方案](#学习方案)
    - [学习内容](#学习内容)
        - [PDF版文件已经上传至码云](#pdf版文件已经上传至码云)
        - [使用镜像](#使用镜像)
            - [安装好之后要按照惯例运行一下hello-world(瓦鲁多)](#安装好之后要按照惯例运行一下hello-world瓦鲁多)
            - [获取镜像](#获取镜像)
            - [运行镜像](#运行镜像)
            - [列出镜像](#列出镜像)
            - [镜像体积](#镜像体积)
            - [注意虚悬镜像](#注意虚悬镜像)
            - [查看中间层镜像](#查看中间层镜像)
            - [列出部分镜像](#列出部分镜像)
            - [以特定格式显示](#以特定格式显示)
            - [删除本地镜像](#删除本地镜像)
            - [后面的内容懒得打了, 直接上实践成果](#后面的内容懒得打了-直接上实践成果)

<!-- /TOC -->

---

## 开发环境

- **Ubuntu Mate 18.04**

- 补充一句, 由于这个文档需要大量的图片, 但是把github当做图床速度实在是硬伤, 码云库里面的图片链接在markdown里的显示效果是禁止访问, 目前的解决方案是使用`cmd markdown 会员服务`自动生成图片链接, 速度不错, 比github不知道高到哪里去了, 有一个想法是使用我的Linux云服务器搭建一个图床(阿里云和腾讯云各一台学生机, 两台目前都是闲置状态), 不过我学C++再加上社会实践报告.....真让人头大, 感觉假期不够用了诶(笑)

---


## 安装

- Ubuntu虽然有着*声名远扬*的`系统内部错误`, 但是好处是教程比较好找, 于是跟着教程安装了最新的`docker18.06`(Ubuntu官方源里还是17.12, Ubuntu应用商店里还是17.06))
- 还稀里糊涂的跟着教程弄了一个阿里云docker镜像加速器[https://kmfov9mt.mirror.aliyuncs.com](https://kmfov9mt.mirror.aliyuncs.com)

---

## 学习方案

- 啃官方文档, Chrome浏览器自动翻译

这个翻译笑死哈哈哈哈, 仿生, 奇妙的, 泊坞窗哈哈哈哈哈哈哈哈哈, Chrome大兄弟你认真一点

![0](http://static.zybuluo.com/Mark201802/rfvclxl2juf2ath7m3f7d1i3/2018-08-03%2016-04-53%20%E5%88%9B%E5%BB%BA%E7%9A%84%E6%88%AA%E5%9B%BE.png)

- 换了个地方看文档,`看云`,可以说是国内版的gitbook了

[Docker-从入门到实践](https://www.kancloud.cn/docker_practice/docker_practice/)

![1](http://static.zybuluo.com/Mark201802/xqasttqf75hbswbh7idoihyv/2018-08-03%2017-44-08%20%E5%88%9B%E5%BB%BA%E7%9A%84%E6%88%AA%E5%9B%BE.png)

下载PDF或者去GitHub看可以获得根据docker18.x编写的最新版, 推荐使用福昕阅读器Linux版

---

## 学习内容

### PDF版文件已经上传至码云

[docker_practice](https://gitee.com/Mark-ThinkPad/2018_Summer_Holiday/blob/master/task/Docker/docker_practice.pdf)


### 使用镜像

---

#### 安装好之后要按照惯例运行一下hello-world(瓦鲁多)

![2]( http://static.zybuluo.com/Mark201802/tyjsj6ti89v19v6j7uurvykq/2018-08-04%2022-43-18%20%E5%88%9B%E5%BB%BA%E7%9A%84%E6%88%AA%E5%9B%BE.png)

---

#### 获取镜像

- 从 `Docker` 镜像仓库获取镜像的命令是 `docker pull` 。其命令格式为：
`docker pull [选项] [Docker Registry 地址[:端口号]/]仓库名[:标签]`

- Docker 镜像仓库地址：地址的格式一般是 `<域名/IP>[:端口号]` 。默认地址是 `Docker
Hub`

- 仓库名：如之前所说，这里的仓库名是两段式名称，即 `<用户名>/<软件名>` 。对于 `Docker
Hub`，如果不给出用户名，则默认为 `library` ，也就是官方镜像

- 动手!

![3](http://static.zybuluo.com/Mark201802/fy15dn297qwatlcbgkky8nvm/image.png)

上面的命令中没有给出 Docker 镜像仓库地址，因此将会从 Docker Hub 获取镜像。而镜像名
称是 ubuntu:16.04 ，因此将会获取官方镜像 library/ubuntu 仓库中标签为 16.04 的镜
像。

从下载过程中可以看到我们之前提及的分层存储的概念，镜像是由多层存储所构成。下载也
是一层层的去下载，并非单一文件。下载过程中给出了每一层的 ID 的前 12 位。并且下载结
束后，给出该镜像完整的 sha256 的摘要，以确保下载一致性。

在使用上面命令的时候，你可能会发现，你所看到的层 ID 以及 sha256 的摘要和这里的不一
样。这是因为官方镜像是一直在维护的，有任何新的 bug，或者版本更新，都会进行修复再
以原来的标签发布，这样可以确保任何使用这个标签的用户可以获得更安全、更稳定的镜像。
(Ctrl C + Ctrl V)

---

#### 运行镜像

- 启动ubuntu16.04镜像里面的 `bash` 并且进行交互式操作

![4](http://static.zybuluo.com/Mark201802/agdzlu8ogrmhhk9z9g4p1ni0/image.png)

---

#### 列出镜像

![5](http://static.zybuluo.com/Mark201802/hs8q4pyb6pz01yoip2hoahly/image.png)

---

#### 镜像体积

![6](http://static.zybuluo.com/Mark201802/od2yw1r7lf6pnzoy9jcw1u23/image.png)

---

#### 注意虚悬镜像

![7](http://static.zybuluo.com/Mark201802/5mj1rgjqq0p2smcfv72c29zv/image.png)

没有更新过镜像所以暂时还找不到虚悬镜像

- 删除虚悬镜像 `docker image prune` 

---

#### 查看中间层镜像

![8](http://static.zybuluo.com/Mark201802/c1neqev4qtquvz3qoyn0gsug/image.png)

- `-a` 参数会添加对中间层镜像的显示, `ls` 只是显示顶层镜像

---

#### 列出部分镜像

- 根据仓库名列出镜像 eg: `docker image ls ubuntu`
- 列出某个特定镜像 eg: `docker image ls ubuntu:16.04`
- 使用过滤器参数 `-f` eg: `docker image ls -f since=mongo:3.2` 查看在mongo:3.2 之后建立的镜像, 查看之前用 `before`, 还资磁用label来过滤, eg: `docker image ls -f label=com.example.version=0.1`

---

#### 以特定格式显示

- `docker image ls -q`

![9](http://static.zybuluo.com/Mark201802/lfm5owghgdv20rnebslbas5y/image.png)

- `docker image ls --format "{{.ID}}: {{.Repository}}"`

![10](http://static.zybuluo.com/Mark201802/y1o1nafk1177q5bo9zp7jk41/image.png)

- `docker image ls --format "table {{.ID}}\t{{.Repository}}\t{{.Tag}}` 打算以表格等距显示，并且有标题行，和默认一样，不过自己定义列

![11](http://static.zybuluo.com/Mark201802/2aagzz2oe0sqe5h90eeuhvlc/image.png)

---

#### 删除本地镜像

- `docker image rm [选项] <镜像1> [<镜像2> ...]`

> 其中，`<镜像>` 可以是 `镜像短 ID` 、 `镜像长 ID` 、 `镜像名` 或者 `镜像摘要`

> docker image ls 默认列出的就已经是短 ID 了，一般取前3个字符以上，只要足够区分于别的镜像就可以了

![12](http://static.zybuluo.com/Mark201802/azulw29ogn45h95cxkh5h6zq/image.png)

- 强迫症请先使用这条命令

![13](http://static.zybuluo.com/Mark201802/ym9hn1x4pwowl19qp3hxljep/image.png)

- 还有一些骚操作

`docker image rm $(docker image ls -q redis)` 删除所有仓库名为 redis 的镜像

`docker image rm $(docker image ls -q -f before=mongo:3.2)` 删除所有在 mongo:3.2 之前的镜像

---

#### 后面的内容懒得打了, 直接上实践成果

- 采用任务导向型的方式来实践, 预定目标是使用DockerHub来制作属于自己的一份镜像, 如果做的好就在我的阿里云服务器上部署一下

- 思路是pull官方的ubuntu18.04的镜像, 下载安装必要的软件, 搭建开发环境, 成绩查询系统的代码迁移并修改运行

- 最后呢, docker容器的网络配置接连翻车, 但是在我主机上运行这个docker镜像都没有问题, 我fff 佛慈悲, 于是直接在服务器上部署了, 链接地址: [http://112.74.63.169:80](http://112.74.63.169:80)

- 我的docker终极完成打包镜像版: [https://cloud.docker.com/swarm/mark8102/repository/docker/mark8102/tech_testing/general](https://cloud.docker.com/swarm/mark8102/repository/docker/mark8102/tech_testing/general)

v0就是了, 下面那个myubuntu18.04是初始镜像, 超级超级小

![14](http://static.zybuluo.com/Mark201802/dlpt52mxrsujxjgt4sxhbr21/image.png)