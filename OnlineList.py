import json

Prefix = "!!online"
PluginName = "OnlineList"
DataPath = "plugins/" + PluginName + "/data.json"
ConfigFilePath = "plugins/config/" + PluginName + ".json"
data = []
carpet_player = False
start_with = []
blacklist = []
whitelist = []

def load_config(server):
    global carpet_player
    global start_with
    global blacklist
    global whitelist
    try:
        with open(ConfigFilePath) as file:
            # print("open ok")
            config = json.load(file, encoding='utf8')
            # print("json load ok")
    except:
        return

    print(config)
    carpet_player = config["carpet_player"]
    start_with = config["start_with"]
    blacklist = config["blacklist"]
    whitelist = config["whitelist"]

    print("[OnlineList] 配置文件加载成功")

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
    ret = []
    for i in range(0, len(data)):
        ret.append(data[i]["name"])
    return ret

def on_load(server, module):
    server.add_help_message(Prefix, "获取在线玩家列表并自动识别bot")
    load_config()

def on_player_joined(server, player):
    global data
    global carpet_player
    global start_with
    global blacklist
    global whitelist
    load_config()
    load_data()
    add_data(player, False)
    # print("[OnlineList]" + player + " joined the game")

def on_player_left(server, player):
    global data
    load_data(server)
    delete_data(player)
    # print("[OnlineList]" + player + " left the game")

def on_info(server, info):
    content = info.content
    splited_content = content.split()
    if splited_content[0] != Prefix:
        return
    if content == Prefix:
        show_list(server, info)
    if content == Prefix + " reload":
        load_config(server)
        server.say("[OnlineList] §a配置文件加载成功§r")
    else:
        server.reply(info, "§c格式错误§r")
        return


