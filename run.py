#!/usr/bin/python
# coding=utf-8

from qbot import bot
from scheduler.NewBangumiScheduler import schedulers

if __name__ == '__main__':
    schedulers.start()
    bot.run(host='0.0.0.0', port=8080)
    pass
