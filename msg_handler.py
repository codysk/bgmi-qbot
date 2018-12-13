#!/usr/bin/python
# coding=utf-8

import os, json
from aiocqhttp import CQHttp


class msg_handler(CQHttp):
    def __init__(self, **config_object):
        super(msg_handler, self).__init__(**config_object)

        @self.on_message()
        async def handle_msg(context):
            if context['sender']['user_id'] != os.environ.get('admin_qq', '10000'):
                return

            self.logger.debug(context)
            return {'reply': "echo " + json.dumps(context)}
        pass
