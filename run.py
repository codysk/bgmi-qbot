#!/usr/bin/python
# coding=utf-8

from qbot import bot
import msg_handler

msg_handler.init_msg_handler()

if __name__ == '__main__':
    bot.run(host='0.0.0.0', port=8080)
    pass
