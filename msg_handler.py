#!/usr/bin/python
# coding=utf-8

import os
import types
import asyncio
import aiohttp
import json
from aiohttp import ClientSession
from aiocqhttp import CQHttp

from utils import discuss_set, group_set


class msg_handler(CQHttp):
    def __init__(self, **config_object):
        super(msg_handler, self).__init__(**config_object)
        self.admin_command_handler = admin_command_handler(self)

        @self.on_message()
        async def handle_msg(context):
            self.logger.debug(context)
            message = str(context['message'])
            if not message.startswith('/'):
                return

            message = message[1:]
            cmd = message.split(' ')
            method_name = cmd[0]
            params = cmd[1:]

            # CQHTTP warped undefined method as functools.partial
            # so check method exist need check it type as method
            self.logger.debug("calling %s" % (method_name))
            method = self.get_command_method(method_name, is_admin=self.is_admin(context=context))
            self.logger.debug(type(method))
            if not callable(method) or not isinstance(method, types.MethodType):
                return {'reply': "command %s not exist" % (method_name)}

            await method(context, params)

        pass

    def get_command_method(self, item, is_admin=False):
        method = None
        if is_admin and not callable(method):
            method = getattr(self.admin_command_handler, item)
        return method

    def is_admin(self, context):
        admin = os.environ.get('admin_qq', '10000')
        if str(context['sender']['user_id']) != str(admin):
            self.logger.debug("user: %s not admin(%s)" % (context['sender']['user_id'], admin))
            return False
        self.logger.debug("user: %s is admin(%s) √" % (context['sender']['user_id'], admin))
        return True


class admin_command_handler:
    def __init__(self, cqhttp):
        self.cqhttp = cqhttp

    async def set(self, context, params):
        message_type = str(context['message_type'])

        if message_type == 'discuss':
            discuss_set.add(str(context['discuss_id']))
            await self.send(context=context,
                            message='discuss %s add to subscript list' % (str(context['discuss_id'])))

        if message_type == 'group':
            group_set.add(str(context['group_id']))
            await self.send(context=context,
                            message='group %s add to subscript list' % (str(context['group_id'])))
        pass

    async def getlist(self, context, params):
        await self.send(context=context,
                        message='discuss subscript list: %s' % (','.join(discuss_set)))
        await self.send(context=context,
                        message='group subscript list: %s' % (','.join(group_set)))
        pass

    async def remove(self, context, params):
        if len(params) < 2:
            await self.send(context=context,
                            message='Usage: /remove <discuss/group> <id> [<id> <id> ...]')
            return
        list_name = params[0]
        id_list = params[1:]
        if list_name == 'discuss':
            for _id in id_list:
                discuss_set.remove(_id)
                pass
            await self.send(context=context,
                            message='deleted discuss %s' % (','.join(id_list)))
            pass
        if list_name == 'group':
            for _id in id_list:
                group_set.remove(_id)
                pass
            await self.send(context=context,
                            message='deleted group %s' % (','.join(id_list)))
            pass

    def __getattr__(self, name):
        return getattr(self.cqhttp, name)


class public_command_handler:
    def __init__(self, cqhttp):
        self.cqhttp = cqhttp

    async def ping(self, context, params):
        await self.send(context=context,
                        message='pong')

    async def status(self, context, params):
        api_url = os.environ.get('bgmi_api', 'http://127.0.0.1/api/index')
        self.logger.debug('checking status...')

        try:
            async with ClientSession() as client:
                content = await fetch(client, api_url)
        except asyncio.TimeoutError as _:
            await self.send(context=context, message='bgmi api fetch timeout!')
            return
        except (
                aiohttp.client_exceptions.ClientConnectionError,
                ConnectionError,
                ConnectionAbortedError,
                ConnectionRefusedError,
                ConnectionResetError
        ) as _:
            await self.send(context=context, message='bgmi api connect failed!')
            return

        json.load(content)
        api_data = json.loads(content)

        current_bangumi_episode = ["%s[%s]" % (bangumi['bangumi_name'], bangumi['episode']) for bangumi in
                                   api_data['data']]

        message = "当前订阅的番剧有:\n" \
                  "%s" % ('\n'.join(current_bangumi_episode))

        await self.send(context=context,
                        message=message)

    def __getattr__(self, name):
        return getattr(self.cqhttp, name)


async def fetch(client: ClientSession, url):
    async with client.get(url=url) as resp:
        assert resp.status == 200
        return await resp.text()
