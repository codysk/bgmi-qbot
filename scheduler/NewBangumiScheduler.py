#!/usr/bin/python
# coding=utf-8

import os, json
from aiohttp import ClientSession
from apscheduler.schedulers.blocking import BlockingScheduler

schedulers = BlockingScheduler()

prev_bangumi_list = []

async def check_update():
    is_first = (len(prev_bangumi_list) == 0)
    api_url = os.environ.get('bgmi_api', 'http://127.0.0.1/api/index')
    async with ClientSession() as client:
        content = await fetch(client, api_url)

    updated_list = []
    api_data = json.loads(content)
    bangumi_list = api_data['data']
    for bangumi in bangumi_list:
        bangumi_name = bangumi['bangumi_name']
        for episode in bangumi['player'].keys():
            bangumi_episode_key = '%s_episode_%s'

            if bangumi_episode_key not in prev_bangumi_list:
                if not is_first:
                    updated_list.append('%s[%02d]' % (bangumi_name, episode))
                prev_bangumi_list.append(bangumi_episode_key)
                pass
            pass
        pass

    if not len(updated_list) == 0:
        # TODO: Send notify message
        pass

    pass

async def fetch(client: ClientSession, url):
    async with client.get(url=url) as resp:
        assert resp.status == 200
        return await resp.text()
