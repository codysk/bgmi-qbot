#!/usr/bin/python
# coding=utf-8

import os, json
from aiohttp import ClientSession
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from utils import discuss_set, group_set
from qbot import bot

prev_bangumi_key_list = []

async def check_update():

    bot.logger.debug('checking update...')

    is_first = (len(prev_bangumi_key_list) == 0)
    # is_first = False    # For debug
    api_url = os.environ.get('bgmi_api', 'http://127.0.0.1/api/index')
    async with ClientSession() as client:
        content = await fetch(client, api_url)

    updated_list = []
    new_bangumi_key_list = []
    api_data = json.loads(content)
    bot.logger.debug(api_data)
    bangumi_list = api_data['data']
    for bangumi in bangumi_list:
        bot.logger.debug(bangumi)
        bangumi_name = bangumi['bangumi_name']
        for episode in bangumi['player'].keys():
            bangumi_episode_key = '%s_episode_%s' % (bangumi_name, episode)
            new_bangumi_key_list.append(bangumi_episode_key)

            if bangumi_episode_key not in prev_bangumi_key_list:
                if not is_first:
                    updated_list.append('%s[%02d]' % (bangumi_name, int(episode)))
                pass
            pass

        pass

    bot.logger.debug(updated_list)
    # update prev list
    prev_bangumi_key_list.clear()
    prev_bangumi_key_list.extend(new_bangumi_key_list)

    if not len(updated_list) == 0:
        message = '有番组更新了~\n' \
                  '%s' % ('\n'.join(updated_list))

        # send to discuss
        for discuss_id in list(discuss_set):
            bot.logger.debug('send to discuss: %s' %(discuss_id))
            await bot.send_discuss_msg(discuss_id=discuss_id, message=message)

        # send to group
        for group_id in list(group_set):
            bot.logger.debug('send to group: %s' % (group_id))
            await bot.send_group_msg(group_id=group_id, message=message)
        pass

    pass

async def fetch(client: ClientSession, url):
    async with client.get(url=url) as resp:
        assert resp.status == 200
        return await resp.text()



schedulers = AsyncIOScheduler()

schedulers.add_job(check_update, 'cron', second='0', minute='*/30')
