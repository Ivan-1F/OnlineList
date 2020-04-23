# OnlineList
一个获取在线玩家列表的[MCDReforged](https://github.com/Fallen-Breath/MCDReforged) API，并自动识别[Carpet](https://github.com/gnembon/fabric-carpet)假人

# 安装

1. 将`OnlineList.py`拖入`/plugins`文件夹
2. 在`/plugins`文件夹内创建`OnlineList`文件夹
3. 在`/plugins/OnlineList`中创建`data.json`

# 命令

- `!!online` 显示在线玩家列表

# 使用

1. 使用`server.get_plugin_instance("OnlineList")`获取插件实例
2. 使用`List = OnlineList.get_online_list()`获取在线玩家列表

一个运用了这个API的插件：[Where](https://github.com/wyf0762/Where)

## 返回数据

- 数据类型：List
- 样例：`[{"name":Alex, "isbot":false}, {"name":Steve, "isbot":false}, {"name":Xe_Kr, "isbot":true}]`

## 样例

```python
OnlineList = server.get_plugin_instance('OnlineList')
online_player = OnlineList.get_online_list()
```
