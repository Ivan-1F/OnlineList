import json

Prefix = "!!online"
PluginName = "OnlineList"
DataPath = "plugins/" + PluginName + "/data.json"
ConfigFilePath = "plugins/config/" + PluginName + ".json"

# global
data = []
flag = False

def load_data():
    global data
    try:
        with open(DataPath) as file:
            data = json.load(file, encoding='utf8')
    except:
        return

def save_data():
    global data
    try:
        with open(DataPath, "w") as file:
            json.dump(data, file)
    except:
        return

def add_data(name, isbot):
    global data
    load_data()
    new = {"name" : name, "isbot" : isbot}
    data.append(new)
    save_data()

def delete_data(name):
    global data
    load_data()
    for i in range(0, len(data)):
        if data[i]["name"] == name:
            del data[i]
            save_data()
            return

def show_list(server, info):
    global data
    load_data()
    server.reply(info, "§a在线列表：§r")
    for i in range(0, len(data)):
        msg = data[i]["name"]
        if data[i]["isbot"]:
            msg += " §6(bot)§r"
        server.reply(info, msg)

def get_online_list():
    global data
    load_data()
    return data

def is_online(player):
    online_list = get_online_list()
    for i in range(0, len(online_list)):
        if player == online_list[i]["name"]:
            return True
    return False

def is_bot(player):
    online_list = get_online_list()
    for i in range(0, len(online_list)):
        if player == online_list[i]["name"]:
            if online_list[i]["isbot"]
                return True
    return False

def on_load(server, module):
    server.add_help_message(Prefix, "获取在线玩家列表并自动识别bot")

def on_player_joined(server, player):
    global flag
    if flag:
        # carpet_player
        add_data(player, True)
        # print("bot(carpet_player)")
        return

    # normal player
    add_data(player, False)
    # print("[OnlineList]" + player + " joined the game")
    return

def on_player_left(server, player):
    global data
    load_data()
    delete_data(player)
    # print("[OnlineList]" + player + " left the game")

def on_info(server, info):
    raw_content = info.raw_content
    if "[local] logged in with entity id" in raw_content:
        global flag
        flag = True
        return

    content = info.content
    splited_content = content.split()

    if splited_content[0] != Prefix:
        return
    if content == Prefix:
        show_list(server, info)
        return
    server.reply(info, "§c格式错误§r")
    return


