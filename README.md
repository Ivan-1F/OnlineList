# OnlineList

一个获取在线玩家列表的[MCDReforged](https://github.com/Fallen-Breath/MCDReforged) API，并自动识别[Carpet](https://github.com/gnembon/fabric-carpet)假人

## 安装

1. 将`OnlineList.py`拖入`/plugins`文件夹
2. 在`/plugins`文件夹内创建`OnlineList`文件夹
3. 在`/plugins/OnlineList`中创建`data.json`

## 命令

- `!!online` 显示在线玩家列表

## 使用

1. 使用`OnlineList = server.get_plugin_instance("OnlineList")`获取插件实例

### 方法：OnlineList.get_online_list()

获取在线玩家列表

#### 返回

- 数据类型：List
- 样例：`[{"name":Alex, "isbot":false}, {"name":Steve, "isbot":false}, {"name":Xe_Kr, "isbot":true}]`

### 方法：OnlineList.is_online(player)

判断一位玩家是否在线

#### 参数

玩家ID

#### 返回

- 数据类型：Bool

## 样例

```python
OnlineList = server.get_plugin_instance('OnlineList')
online_player = OnlineList.get_online_list()
```
