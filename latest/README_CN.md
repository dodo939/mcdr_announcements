**中文** | [English](README.md)

# mcdr_announcements

运行于 MCDR 上的定时发送服务器公告的插件。
<br/>使用前在 cmd 或者 powershell 中运行 `pip install pyyaml` 安装 pyyaml 库。

## Star 趋势图

[![Star History Chart](https://api.star-history.com/svg?repos=yfy-dodo939/mcdr_announcements&type=Date)](https://star-history.com/#yfy-dodo939/mcdr_announcements&Date)

## 更新日志

### v1.3.0 更新
+ 我们重写了计时器部分的逻辑，所以它现在**支持查看距离下次显示的剩余时间**了！
  ![效果展示](/src/v1.3.0_0_zh.png)
+ 现在当你执行过`!!an time <seconds>`之后，你不需要再执行`!!an reload`重载插件来刷新时间了！

### v1.2.2 更新
+ 若检测到没有安装pyyaml，则会自动执行`pip install pyyaml`尝试安装缺失的库。(已知的问题: 由于安装过程为非阻塞操作，因此第一次插件可能会在缺失库的情况下运行)
+ 修复了`v1.2.1`版本中服务器启动时控制台出现冗余警告或报错信息的问题

### v1.2.1 更新
+ 现在插件可以记住上次退出时的启用状态，并在下次启动时恢复状态。
+ 取消了插件加载后的首次公告展示。
+ 优化了计时器及一些细节问题。
+ 优化了部分提示文本，添加了部分悬停文本提示。
+ 新增了状态显示及其他指令。

  `!!an help`: 同 `!!an`

  `!!an reload`: 重新加载插件
  
  `!!an status`: 查看当前状态

### v1.2.0 更新
+ 添加了对中文的支持，插件将根据服务端语言偏好自动选择显示语言。
+ 插件格式换用 `*.mcdr` 打包格式，取代之前的 `*.py` 单文件格式。

### v1.1.0 更新

+ 现在可以使用命令来修改配置而不是去修改配置文件了。

  `!!an`:  显示此帮助列表

  `!!an enable`:  启用定时公告

  `!!an disable`:  禁用定时公告

  `!!an set <message>`:  设置公告内容

  <strong>提示:</strong> 使用 `\n` 换行，`&` 作为颜色代码。如果要在命令中使用中文，请在启动命令中加入 `-Dfile.encoding=UTF-8` 参数。例如 `java -Dfile.encoding=UTF-8 -jar server.jar nogui`
  
  `!!an time <seconds>`:  设置间隔时间 (单位: 秒)

+ 现在启用状态默认设置为禁用，首次使用请手动打开。
+ 仅管理员和具有 owner 权限可以执行修改命令。
