# NavCreate
直接改源码太麻烦, 看久了眼睛都花啦, 于是就写了这个.
这是一个生成 index.html 页面的 Python 脚本, 目的是为了更改[这个项目](https://github.com/WebStackPage/WebStackPage.github.io)的网站导航中的内容. 在该 Python 脚本的开头有 logo, favicon 等的设置, 请自行更改.
## 使用方式
像 markdown 那样用 `#` 符号生成目录, `#` 是一级目录, `##` 是二级目录, 以此类推, **注意 `#` 后要跟着一个空格** . 然后标题下跟着内容, 内容格式是
```markdown
网站地址,网站图标,网站名称,网站描述
```
将这些内容放在和脚本同一个目录的 text.txt 文件中, 然后执行脚本, 就会在 out.txt 中生成源码.
上面的使用方式可能描述还是不太清楚, 我举个例子
![](https://cdn.jsdelivr.net/gh/yunwanjia-cloud/NavCreate/1.png)
如果写成这样, 那么会生成这样的页面
![](https://cdn.jsdelivr.net/gh/yunwanjia-cloud/NavCreate/2.png)