import json

Prefix = "!!online"
PluginName = "OnlineList"
DataPath = "plugins/" + PluginName + "/data.json"
ConfigFilePath = "plugins/config/" + PluginName + ".json"

# global
data = []
carpet_player = False
start_with = []
blacklist = []
whitelist = []
flag = True

def load_config():
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

    carpet_player = config["carpet_player"]
    start_with = config["start_with"]
    blacklist = config["blacklist"]
    whitelist = config["whitelist"]

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

def on_load(server, module):
    server.add_help_message(Prefix, "获取在线玩家列表并自动识别bot")
    load_config()

def on_player_joined(server, player):
    global flag
    if not flag:
        # carpet_player
        add_data(player, True)
        # print("bot(carpet_player)")
        return
    global data
    global carpet_player
    global start_with
    global blacklist
    global whitelist
    load_config()
    load_data()
    lplayer = player.lower()
    for i in range(0, len(whitelist)):
        if lplayer == whitelist[i]:
            add_data(player, False)
            # print("whitelist")
            return
    for i in range(0, len(blacklist)):
        if lplayer == blacklist[i]:
            add_data(player, True)
            # print("blacklist")
            return
    for i in range(0, len(start_with)):
        if lplayer.startswith(start_with[i]):
            add_data(player, True)
            # print("startwith " + start_with[i])
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
    global carpet_player
    content = info.content
    if carpet_player:
        raw_content = info.raw_content
        if "[local] logged in with entity id" in raw_content:
            load_config()
            global flag
            # server.say("假人")
            flag = False
            return

    splited_content = content.split()
    if splited_content[0] != Prefix:
        return
    if content == Prefix:
        show_list(server, info)
        return
    server.reply(info, "§c格式错误§r")
    return


