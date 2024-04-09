import logging
import os
import threading
import time

from mcdreforged.api.all import *
from mcdr_announcements.utils import _tr
logger = logging.Logger("log")
try:
    import yaml
except ModuleNotFoundError:
    logger.warning("Requirement not found! Trying installing pyyaml...")
    os.system("pip install pyyaml")

timer = True
isEnabled = False
isFirstMsg = True
message = []
time_interval = 0
time_current = 0


def send(server: ServerInterface):
    global isFirstMsg, time_current
    while timer:
        time.sleep(1)
        time_current += 1
        if time_current >= time_interval:
            time_current = 0
            if isEnabled and not isFirstMsg:
                for t in message:
                    server.say(t)
            isFirstMsg = False


def an_help(context: PlayerCommandSource):
    server = context.get_server()
    info = context.get_info()
    server.reply(info, "§2-------- Announcements v1.2.2 --------")
    server.reply(info, RText("§7!!an [help]§r").set_hover_text(_tr("command.hover_hint")).set_click_event(RAction.suggest_command, "!!an") + ' ' + _tr("help.help"))
    server.reply(info, RText("§7!!an status§r").set_hover_text(_tr("command.hover_hint")).set_click_event(RAction.suggest_command, "!!an status") + ' ' + _tr("help.status"))
    server.reply(info, RText("§7!!an enable§r").set_hover_text(_tr("command.hover_hint")).set_click_event(RAction.suggest_command, "!!an enable") + ' ' + _tr("help.enable"))
    server.reply(info, RText("§7!!an disable§r").set_hover_text(_tr("command.hover_hint")).set_click_event(RAction.suggest_command, "!!an disable") + ' ' + _tr("help.disable"))
    server.reply(info, RText("§7!!an reload§r").set_hover_text(_tr("command.hover_hint")).set_click_event(RAction.suggest_command, "!!an reload") + ' ' + _tr("help.reload"))
    server.reply(info, RText("§7!!an set §6<message>§r").set_hover_text(_tr("command.hover_hint")).set_click_event(RAction.suggest_command, "!!an set ") + ' ' + _tr("help.set"))
    server.reply(info, RText("§7!!an time §6<seconds>§r").set_hover_text(_tr("command.hover_hint")).set_click_event(RAction.suggest_command, "!!an time ") + ' ' + _tr("help.time"))
    server.reply(info, _tr("status.title"))
    if isEnabled:
        server.reply(info, _tr("status.enabled"))
    else:
        server.reply(info, _tr("status.disabled"))
    server.reply(info, _tr("status.time", time_interval))
    if isEnabled:
        server.say(_tr("status.left_time", time_interval - time_current))
    server.reply(info, _tr("status.text"))
    for t in message:
        server.reply(info, "§7 - §r" + t)


def an_status(context: PlayerCommandSource):
    server = context.get_server()
    info = context.get_info()
    if context.is_console:
        server.reply(info, _tr("status.title"))
        if isEnabled:
            server.reply(info, _tr("status.enabled"))
        else:
            server.reply(info, _tr("status.disabled"))
        server.reply(info, _tr("status.time", time_interval))
        server.reply(info, _tr("status.text"))
        for t in message:
            server.reply(info, "§7 - §r" + t)
    else:
        server.say(_tr("status.title"))
        if isEnabled:
            server.say(_tr("status.enabled"))
        else:
            server.say(_tr("status.disabled"))
        server.say(_tr("status.time", time_interval))
        if isEnabled:
            server.say(_tr("status.left_time", time_interval - time_current))
        server.say(_tr("status.text"))
        for t in message:
            server.say("§7 - §r" + t)


def an_disable(context: PlayerCommandSource):
    server = context.get_server()
    info = context.get_info()
    if not context.has_permission_higher_than(2):
        server.reply(info, _tr("command.no_permission"))
        return
    global isEnabled
    isEnabled = False
    with open("config//announcements_config.yml", mode='r', encoding='utf-8') as f:
        temp = yaml.safe_load(f)
        temp["enable"] = False
    with open("config//announcements_config.yml", mode='w', encoding='utf-8') as f:
        yaml.safe_dump(temp, f)
    server.reply(info, _tr("command.off"))


def an_enable(context: PlayerCommandSource):
    server = context.get_server()
    info = context.get_info()
    if not context.has_permission_higher_than(2):
        server.reply(info, _tr("command.no_permission"))
        return
    global isEnabled
    isEnabled = True
    with open("config//announcements_config.yml", mode='r', encoding='utf-8') as f:
        temp = yaml.safe_load(f)
        temp["enable"] = True
    with open("config//announcements_config.yml", mode='w', encoding='utf-8') as f:
        yaml.safe_dump(temp, f)
    server.reply(info, _tr("command.on"))


def an_reload(context: PlayerCommandSource):
    server = context.get_server()
    info = context.get_info()
    if not context.has_permission_higher_than(2):
        server.reply(info, _tr("command.no_permission"))
        return
    server.reload_plugin("mcdr_announcements")


def an_set(context: PlayerCommandSource):
    server = context.get_server()
    info = context.get_info()
    if not context.has_permission_higher_than(2):
        server.reply(info, _tr("command.no_permission"))
        return
    global message
    msg = context.get_info().content.replace('&', '§')[9:].split('\\n')
    message = msg
    with open("config//announcements_config.yml", mode='r', encoding='utf-8') as f:
        temp = yaml.safe_load(f)
        temp["message"] = msg
    with open("config//announcements_config.yml", mode='w', encoding='utf-8') as f:
        yaml.safe_dump(temp, f)
    server.reply(info, _tr("command.message"))


def an_time(context: PlayerCommandSource):
    server = context.get_server()
    info = context.get_info()
    if not context.has_permission_higher_than(2):
        server.reply(info, _tr("command.no_permission"))
        return
    global time_interval
    interval = int(context.get_info().content.split()[2])
    if interval <= 0:
        server.reply(info, _tr("command.time_below_zero"))
        return
    time_interval = interval
    with open("config//announcements_config.yml", mode='r', encoding='utf-8') as f:
        temp = yaml.safe_load(f)
        temp["time_interval"] = interval
    with open("config//announcements_config.yml", mode='w', encoding='utf-8') as f:
        yaml.safe_dump(temp, f)
    server.reply(info, _tr("command.time", interval))


def on_load(server: ServerInterface, old):
    # commands
    builder = SimpleCommandBuilder()
    builder.command("!!an", an_help)
    builder.command("!!an help", an_help)
    builder.command("!!an status", an_status)
    builder.command("!!an disable", an_disable)
    builder.command("!!an enable", an_enable)
    builder.command("!!an reload", an_reload)
    builder.command("!!an set <message>", an_set)
    builder.command("!!an time <interval>", an_time)
    
    builder.arg("message", GreedyText)
    builder.arg("interval", Integer)
    
    builder.register(server)
    
    global message, time_interval, isEnabled
    if not os.path.exists("config//announcements_config.yml"):
        with open("config//announcements_config.yml", mode='w+', encoding='utf-8') as f:
            f.write(_tr("default"))
    with open("config//announcements_config.yml", mode='r', encoding='utf-8') as f:
        info = yaml.safe_load(f)
        time_interval = info["time_interval"]
        message = info["message"]
    if "enable" in info:
        isEnabled = info["enable"]
    else:
        info["enable"] = False
        with open("config//announcements_config.yml", mode='w', encoding='utf-8') as f:
            yaml.safe_dump(info, f)
    sender = threading.Thread(target=send, daemon=True, args=(server,))
    sender.start()
    logger.info("[Announcements] Plugin loaded")
    logger.info("-------- Announcements Status --------")
    if isEnabled:
        logger.info("Enable: True")
    else:
        logger.info("Enable: False")
    logger.info(f"Interval: {time_interval} second(s)")
    logger.info("Content: ")
    for t in message:
        logger.info(" - " + t)


def on_unload(server: ServerInterface):
    global timer
    timer = False
    server.say(_tr("plugin.unload"))
