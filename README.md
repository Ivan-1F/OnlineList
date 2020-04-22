# OnlineList
一个获取在线玩家列表的[MCDReforged](https://github.com/Fallen-Breath/MCDReforged) API，可以自定义bot判定规则并可以自动识别[Carpet](https://github.com/gnembon/fabric-carpet)假人

# 安装

1. 将`OnlineList.py`拖入`/plugins`文件夹
2. 在`/plugins`文件夹内创建`OnlineList`文件夹
3. 在`/plugins/OnlineList`中创建`data.json`
4. 在`/plugins/config`中创建`OnlineList.json`

# 命令

- `!!online` 显示在线玩家列表

# 使用

1. 使用`server.get_plugin_instance("OnlineList")`获取插件实例
2. 使用`List = OnlineList.get_online_list()`获取在线玩家列表

## 返回数据

- 数据类型：List
- 样例：`[{"name":Alex, "isbot":false}, {"name":Steve, "isbot":false}, {"name":Xe_Kr, "isbot":true}]`

## 样例

```python
OnlineList = server.get_plugin_instance('OnlineList')
online_player = OnlineList.get_online_list()
```

# 配置文件

## carpet_player

默认值：`true`

是否将地毯假人标记为bot

## start_with

将ID以这些字符串开头的玩家标记为bot

## blacklist

始终将这些ID标记为bot

## whitelist

始终不将这些ID标记为bot

