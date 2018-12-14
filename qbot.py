#!/usr/bin/python
# coding=utf-8

import os, logging
from msg_handler import msg_handler

api_root = os.environ.get('api_root', 'http://127.0.0.1:5700/')
access_token = os.environ.get('access_token', False)
secret = os.environ.get('secret', False)

enable_http_post = os.environ.get('enable_http_post', False)

param_dict = {'api_root': api_root}
if access_token:
    param_dict['access_token'] = access_token
if secret:
    param_dict['secret'] = secret
param_dict['enable_http_post'] = enable_http_post

bot = msg_handler(**param_dict)
bot.logger.setLevel(level=getattr(logging, os.environ.get('log_level', 'ERROR')))


if __name__ == '__main__':
    print(bot)


