#!/usr/bin/python
# coding=utf-8

import os
from qbot import bot


def init_msg_handler():
    @bot.on_message()
    async def handle_msg(context):
        print(context)
        return {'reply': "reply" + context['message']}
