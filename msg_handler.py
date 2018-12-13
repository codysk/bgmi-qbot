#!/usr/bin/python
# coding=utf-8

import os
from aiocqhttp import CQHttp

from utils import discuss_set, group_set

class msg_handler(CQHttp):
    def __init__(self, **config_object):
        super(msg_handler, self).__init__(**config_object)

        @self.on_message()
        async def handle_msg(context):
            self.logger.debug(context)
            admin = os.environ.get('admin_qq', '10000')
            if str(context['sender']['user_id']) != str(admin):
                self.logger.debug("user: %s not admin(%s)" % (context['sender']['user_id'], admin))
                return
            message = str(context['message'])
            if not message.startswith('/'):
                return

            message = message[1:]
            cmd = message.split(' ')
            method_name = cmd[0]
            params = cmd[1:]

            if not callable(getattr(self, method_name)):
                return {'reply': "command %s not exist" % (method_name)}

            self.logger.debug("calling %s" % (method_name))
            method =  getattr(self, method_name)
            self.logger.debug(type(method))
            await method(context, params)
        pass

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
