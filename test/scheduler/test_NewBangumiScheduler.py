import asyncio
from asynctest import CoroutineMock, patch, TestCase
from importlib import reload


class TestNewBangumiScheduler(TestCase):

    @patch("aiohttp.ClientSession.get")
    @patch("qbot.bot")
    def test_import(self, mock_bot, mock_get):
        mock_get.return_value.__aenter__.return_value.status = 200
        mock_get.return_value.__aenter__.return_value.text = CoroutineMock(side_effect=[
            """
            {
              "version": "2.1.1",
              "latest_version": "2.1.2",
              "frontend_version": "1.1.x",
              "status": "success",
              "lang": "zh_cn",
              "danmaku_api": "",
              "data": [
                {
                  "bangumi_name": "慎重勇者 ~這個勇者明明超TUEEE卻過度謹慎~",
                  "cover": "/bangumi/cover/http/lain.bgm.tv/pic/cover/l/02/3c/266157_5wF3a.jpg",
                  "update_time": "Wed",
                  "name": "慎重勇者 ~這個勇者明明超TUEEE卻過度謹慎~",
                  "status": 1,
                  "updated_time": 1578592819,
                  "subtitle_group": "",
                  "episode": 12,
                  "player": {
                    "1": {
                      "path": "/慎重勇者 ~這個勇者明明超TUEEE卻過度謹慎~/1/[Sakurato.sub][Shinchou Yuusha][01][BIG5][1080P]/[Sakurato.sub][Shinchou Yuusha][01][BIG5][1080P].mp4"
                    }
                  }
                },
                {
                  "bangumi_name": "刀剑神域 Alicization篇 War of Underworld",
                  "cover": "/bangumi/cover/http/lain.bgm.tv/pic/cover/l/dd/a6/279457_TkOjj.jpg",
                  "update_time": "Sat",
                  "name": "刀剑神域 Alicization篇 War of Underworld",
                  "status": 1,
                  "updated_time": 1578333651,
                  "subtitle_group": "",
                  "episode": 12,
                  "player": {
                    "1": {
                      "path": "/刀剑神域 Alicization篇 War of Underworld/1/[SumiSora&CASO&FLsonw][sao-alicization_War_of_Underworld][01][CHT][720P].mp4"
                    }
                  }
                },
                {
                  "bangumi_name": "入間同學入魔了！",
                  "cover": "/bangumi/cover/http/lain.bgm.tv/pic/cover/l/6a/b9/273844_JQ26Q.jpg",
                  "update_time": "Sat",
                  "name": "入間同學入魔了！",
                  "status": 1,
                  "updated_time": 1578254412,
                  "subtitle_group": "",
                  "episode": 14,
                  "player": {
                    "1": {
                      "path": "/入間同學入魔了！/1/[Sakurato.sub][Mairimashita! Iruma-kun][01][BIG5][1080P]/[Sakurato.sub][Mairimashita! Iruma-kun][01][BIG5][1080P].mp4"
                    }
                  }
                },
                {
                  "bangumi_name": "我們真的學不來！第二季",
                  "cover": "/bangumi/cover/http/lain.bgm.tv/pic/cover/l/80/0f/285130_brGSR.jpg",
                  "update_time": "Wed",
                  "name": "我們真的學不來！第二季",
                  "status": 1,
                  "updated_time": 1577570520,
                  "subtitle_group": "",
                  "episode": 13,
                  "player": {
                    "1": {
                      "path": "/我們真的學不來！第二季/1/[Bokutachi wa Benkyou ga Dekinai S2][01][BIG5][1080P].mp4"
                    }
                  }
                },
                {
                  "bangumi_name": "小書痴的下克上",
                  "cover": "/bangumi/cover/http/lain.bgm.tv/pic/cover/l/93/3b/276788_SEeFP.jpg",
                  "update_time": "Wed",
                  "name": "小書痴的下克上",
                  "status": 1,
                  "updated_time": 1577503037,
                  "subtitle_group": "",
                  "episode": 12,
                  "player": {
                    "1": {
                      "path": "/小書痴的下克上/1/[Airota&Nekomoe kissaten] Honzuki no Gekokujou - Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen][01][1080p][CHT].mp4"
                    }
                  }
                },
                {
                  "bangumi_name": "我不是說了能力要平均值嗎！",
                  "cover": "/bangumi/cover/http/lain.bgm.tv/pic/cover/l/2e/97/238962_21617.jpg",
                  "update_time": "Mon",
                  "name": "我不是說了能力要平均值嗎！",
                  "status": 1,
                  "updated_time": 1577383233,
                  "subtitle_group": "",
                  "episode": 12,
                  "player": {
                    "1": {
                      "path": "/我不是說了能力要平均值嗎！/1/[Nekomoe kissaten][Watashi, Nouryoku wa Heikinchi de tte Itta yo ne!][01][1080p][CHT].mp4"
                    },
                    "10": {
                      "path": "/我不是說了能力要平均值嗎！/10/[Nekomoe kissaten][Watashi, Nouryoku wa Heikinchi de tte Itta yo ne!][10][1080p][CHT].mp4"
                    },
                    "11": {
                      "path": "/我不是說了能力要平均值嗎！/11/[Nekomoe kissaten][Watashi, Nouryoku wa Heikinchi de tte Itta yo ne!][11][1080p][CHT].mp4"
                    }
                  }
                },
                {
                  "bangumi_name": "放學後桌遊俱樂部",
                  "cover": "/bangumi/cover/http/lain.bgm.tv/pic/cover/l/0c/90/259790_5y7OS.jpg",
                  "update_time": "Wed",
                  "name": "放學後桌遊俱樂部",
                  "status": 1,
                  "updated_time": 1576922463,
                  "subtitle_group": "",
                  "episode": 12,
                  "player": {
                    "1": {
                      "path": "/放學後桌遊俱樂部/1/[Sakurato.sub][Houkago Saikoro Club][01][BIG5][1080P]/[Sakurato.sub][Houkago Saikoro Club][01][BIG5][1080P].mp4"
                    },
                    "9": {
                      "path": "/放學後桌遊俱樂部/9/[Nekomoe kissaten][Houkago Saikoro Club][09][1080p][CHT].mp4"
                    }
                  }
                }
              ]
            }
            """
        ])
        mock_get.return_value.__aexit__.return_value = None

        mock_bot.logger.info.return_value = None
        import scheduler.NewBangumiScheduler
        self.assertEqual(2, mock_bot.logger.info.call_count)
        pass

    @patch("utils.discuss_set", ['123'])
    @patch("utils.group_set", ['321'])
    @patch("asyncio.get_event_loop")
    @patch("aiohttp.ClientSession.get")
    @patch("qbot.bot")
    async def test_update(self, mock_bot, mock_get, mock_get_event_loop):
        mock_get_event_loop.return_value.run_until_complete.return_value = None
        mock_get.return_value.__aenter__.return_value.status = 200
        mock_get.return_value.__aenter__.return_value.text = CoroutineMock(side_effect=[
            """
            {
              "version": "2.1.1",
              "latest_version": "2.1.2",
              "frontend_version": "1.1.x",
              "status": "success",
              "lang": "zh_cn",
              "danmaku_api": "",
              "data": [
                {
                  "bangumi_name": "慎重勇者 ~這個勇者明明超TUEEE卻過度謹慎~",
                  "cover": "/bangumi/cover/http/lain.bgm.tv/pic/cover/l/02/3c/266157_5wF3a.jpg",
                  "update_time": "Wed",
                  "name": "慎重勇者 ~這個勇者明明超TUEEE卻過度謹慎~",
                  "status": 1,
                  "updated_time": 1578592819,
                  "subtitle_group": "",
                  "episode": 12,
                  "player": {
                    "1": {
                      "path": "/慎重勇者 ~這個勇者明明超TUEEE卻過度謹慎~/1/[Sakurato.sub][Shinchou Yuusha][01][BIG5][1080P]/[Sakurato.sub][Shinchou Yuusha][01][BIG5][1080P].mp4"
                    },
                    "10": {
                      "path": "/慎重勇者 ~這個勇者明明超TUEEE卻過度謹慎~/10/【爱恋&漫猫字幕组】[谨慎勇者][慎重勇者][这个勇者明明超TUEEE却过度谨慎][10][BIG5][720P].mp4"
                    },
                    "11": {
                      "path": "/慎重勇者 ~這個勇者明明超TUEEE卻過度謹慎~/11/[Sakurato.sub][Shinchou Yuusha][11][BIG5][1080P]/[Sakurato.sub][Shinchou Yuusha][11][BIG5][1080P].mp4"
                    },
                    "12": {
                      "path": "/慎重勇者 ~這個勇者明明超TUEEE卻過度謹慎~/12/[Sakurato.sub][Shinchou Yuusha][12][BIG5][1080P]/[Sakurato.sub][Shinchou Yuusha][12][BIG5][1080P].mp4"
                    },
                    "2": {
                      "path": "/慎重勇者 ~這個勇者明明超TUEEE卻過度謹慎~/2/2big5_batch_Mux.mp4"
                    },
                    "3": {
                      "path": "/慎重勇者 ~這個勇者明明超TUEEE卻過度謹慎~/3/【爱恋&漫猫字幕组】[谨慎勇者][慎重勇者][这个勇者明明超TUEEE却过度谨慎][03][BIG5][720P].mp4"
                    },
                    "4": {
                      "path": "/慎重勇者 ~這個勇者明明超TUEEE卻過度謹慎~/4/【爱恋&漫猫字幕组】[谨慎勇者][慎重勇者][这个勇者明明超TUEEE却过度谨慎][04][BIG5][720P].mp4"
                    },
                    "5": {
                      "path": "/慎重勇者 ~這個勇者明明超TUEEE卻過度謹慎~/5/【爱恋&漫猫字幕组】[谨慎勇者][慎重勇者][这个勇者明明超TUEEE却过度谨慎][05][BIG5][720P].mp4"
                    },
                    "6": {
                      "path": "/慎重勇者 ~這個勇者明明超TUEEE卻過度謹慎~/6/【爱恋&漫猫字幕组】[谨慎勇者][慎重勇者][这个勇者明明超TUEEE却过度谨慎][06][BIG5][720P].mp4"
                    },
                    "8": {
                      "path": "/慎重勇者 ~這個勇者明明超TUEEE卻過度謹慎~/8/[Sakurato.sub][Shinchou Yuusha][08][BIG5][1080P]/[Sakurato.sub][Shinchou Yuusha][08][BIG5][1080P].mp4"
                    },
                    "9": {
                      "path": "/慎重勇者 ~這個勇者明明超TUEEE卻過度謹慎~/9/[Sakurato.sub][Shinchou Yuusha][09][BIG5][1080P]/[Sakurato.sub][Shinchou Yuusha][09][BIG5][1080P].mp4"
                    }
                  }
                },
                {
                  "bangumi_name": "刀剑神域 Alicization篇 War of Underworld",
                  "cover": "/bangumi/cover/http/lain.bgm.tv/pic/cover/l/dd/a6/279457_TkOjj.jpg",
                  "update_time": "Sat",
                  "name": "刀剑神域 Alicization篇 War of Underworld",
                  "status": 1,
                  "updated_time": 1578333651,
                  "subtitle_group": "",
                  "episode": 12,
                  "player": {
                    "1": {
                      "path": "/刀剑神域 Alicization篇 War of Underworld/1/[SumiSora&CASO&FLsonw][sao-alicization_War_of_Underworld][01][CHT][720P].mp4"
                    },
                    "10": {
                      "path": "/刀剑神域 Alicization篇 War of Underworld/10/[SumiSora&CASO&FLsnow][sao-alicization_War_of_Underworld][10][CHT][720P].mp4"
                    },
                    "11": {
                      "path": "/刀剑神域 Alicization篇 War of Underworld/11/[SumiSora&CASO&FLsnow][sao-alicization_War_of_Underworld][11][CHT][720P].mp4"
                    },
                    "12": {
                      "path": "/刀剑神域 Alicization篇 War of Underworld/12/[SumiSora&CASO&FLsnow][sao-alicization_War_of_Underworld][12][CHT][720P].mp4"
                    },
                    "2": {
                      "path": "/刀剑神域 Alicization篇 War of Underworld/2/[SumiSora&CASO&FLsonw][sao-alicization_War_of_Underworld][02][CHT][720P].mp4"
                    },
                    "3": {
                      "path": "/刀剑神域 Alicization篇 War of Underworld/3/[SumiSora&CASO&FLsnow][sao-alicization_War_of_Underworld][03][CHT][720P].mp4"
                    },
                    "4": {
                      "path": "/刀剑神域 Alicization篇 War of Underworld/4/[SumiSora&CASO&FLsnow][sao-alicization_War_of_Underworld][04][CHT][720P].mp4"
                    },
                    "5": {
                      "path": "/刀剑神域 Alicization篇 War of Underworld/5/[SumiSora&CASO&FLsnow][sao-alicization_War_of_Underworld][05][CHT][720P].mp4"
                    },
                    "6": {
                      "path": "/刀剑神域 Alicization篇 War of Underworld/6/[SumiSora&CASO&FLsnow][sao-alicization_War_of_Underworld][06][CHT][720P].mp4"
                    },
                    "7": {
                      "path": "/刀剑神域 Alicization篇 War of Underworld/7/[SumiSora&CASO&FLsnow][sao-alicization_War_of_Underworld][07][CHT][720P].mp4"
                    },
                    "8": {
                      "path": "/刀剑神域 Alicization篇 War of Underworld/8/[SumiSora&CASO&FLsnow][sao-alicization_War_of_Underworld][08][CHT][720P].mp4"
                    },
                    "9": {
                      "path": "/刀剑神域 Alicization篇 War of Underworld/9/[SumiSora&CASO&FLsnow][sao-alicization_War_of_Underworld][09][CHT][720P].mp4"
                    }
                  }
                },
                {
                  "bangumi_name": "入間同學入魔了！",
                  "cover": "/bangumi/cover/http/lain.bgm.tv/pic/cover/l/6a/b9/273844_JQ26Q.jpg",
                  "update_time": "Sat",
                  "name": "入間同學入魔了！",
                  "status": 1,
                  "updated_time": 1578254412,
                  "subtitle_group": "",
                  "episode": 14,
                  "player": {
                    "1": {
                      "path": "/入間同學入魔了！/1/[Sakurato.sub][Mairimashita! Iruma-kun][01][BIG5][1080P]/[Sakurato.sub][Mairimashita! Iruma-kun][01][BIG5][1080P].mp4"
                    },
                    "10": {
                      "path": "/入間同學入魔了！/10/[Mairimashita! Iruma-kun][10][BIG5][1080P].mp4"
                    },
                    "11": {
                      "path": "/入間同學入魔了！/11/[Mairimashita! Iruma-kun][11][BIG5][1080P].mp4"
                    },
                    "12": {
                      "path": "/入間同學入魔了！/12/[Mairimashita! Iruma-kun][12][BIG5][1080P].mp4"
                    },
                    "13": {
                      "path": "/入間同學入魔了！/13/[Mairimashita! Iruma-kun][13][BIG5][1080P].mp4"
                    },
                    "14": {
                      "path": "/入間同學入魔了！/14/[Sakurato.sub][Mairimashita! Iruma-kun][14][BIG5][1080P]/[Sakurato.sub][Mairimashita! Iruma-kun][14][BIG5][1080P].mp4"
                    },
                    "2": {
                      "path": "/入間同學入魔了！/2/[Mairimashita! Iruma-kun][02][BIG5][1080P].mp4"
                    },
                    "3": {
                      "path": "/入間同學入魔了！/3/[Mairimashita! Iruma-kun][03][BIG5][1080P].mp4"
                    },
                    "4": {
                      "path": "/入間同學入魔了！/4/[Mairimashita! Iruma-kun][04][BIG5][1080P].mp4"
                    },
                    "5": {
                      "path": "/入間同學入魔了！/5/[Mairimashita! Iruma-kun][05][BIG5][1080P].mp4"
                    },
                    "6": {
                      "path": "/入間同學入魔了！/6/[Mairimashita! Iruma-kun][06][BIG5][1080P].mp4"
                    },
                    "7": {
                      "path": "/入間同學入魔了！/7/[Mairimashita! Iruma-kun][07][BIG5][1080P].mp4"
                    },
                    "8": {
                      "path": "/入間同學入魔了！/8/[Mairimashita! Iruma-kun][08][BIG5][1080P].mp4"
                    }
                  }
                },
                {
                  "bangumi_name": "我們真的學不來！第二季",
                  "cover": "/bangumi/cover/http/lain.bgm.tv/pic/cover/l/80/0f/285130_brGSR.jpg",
                  "update_time": "Wed",
                  "name": "我們真的學不來！第二季",
                  "status": 1,
                  "updated_time": 1577570520,
                  "subtitle_group": "",
                  "episode": 13,
                  "player": {
                    "1": {
                      "path": "/我們真的學不來！第二季/1/[Bokutachi wa Benkyou ga Dekinai S2][01][BIG5][1080P].mp4"
                    },
                    "10": {
                      "path": "/我們真的學不來！第二季/10/[HYSUB]Bokutachi wa Benkyou ga Dekinai![10][BIG5_MP4][1280X720].mp4"
                    },
                    "11": {
                      "path": "/我們真的學不來！第二季/11/[HYSUB]Bokutachi wa Benkyou ga Dekinai![11][BIG5_MP4][1280X720].mp4"
                    },
                    "12": {
                      "path": "/我們真的學不來！第二季/12/[HYSUB]Bokutachi wa Benkyou ga Dekinai![12][BIG5_MP4][1280X720].mp4"
                    },
                    "13": {
                      "path": "/我們真的學不來！第二季/13/[HYSUB]Bokutachi wa Benkyou ga Dekinai![13][BIG5_MP4][1280X720][END].mp4"
                    },
                    "2": {
                      "path": "/我們真的學不來！第二季/2/[HYSUB]Bokutachi wa Benkyou ga Dekinai![02][BIG5_MP4][1280X720].mp4"
                    },
                    "3": {
                      "path": "/我們真的學不來！第二季/3/[HYSUB]Bokutachi wa Benkyou ga Dekinai![03][BIG5_MP4][1280X720].mp4"
                    },
                    "4": {
                      "path": "/我們真的學不來！第二季/4/[Bokutachi wa Benkyou ga Dekinai S2][04][BIG5][1080P].mp4"
                    },
                    "5": {
                      "path": "/我們真的學不來！第二季/5/[HYSUB]Bokutachi wa Benkyou ga Dekinai![05][BIG5_MP4][1280X720].mp4"
                    },
                    "6": {
                      "path": "/我們真的學不來！第二季/6/[HYSUB]Bokutachi wa Benkyou ga Dekinai![06][BIG5_MP4][1280X720].mp4"
                    },
                    "7": {
                      "path": "/我們真的學不來！第二季/7/[HYSUB]Bokutachi wa Benkyou ga Dekinai![07][BIG5_MP4][1280X720].mp4"
                    },
                    "8": {
                      "path": "/我們真的學不來！第二季/8/[HYSUB]Bokutachi wa Benkyou ga Dekinai![08][BIG5_MP4][1280X720].mp4"
                    },
                    "9": {
                      "path": "/我們真的學不來！第二季/9/[HYSUB]Bokutachi wa Benkyou ga Dekinai![09][BIG5_MP4][1280X720].mp4"
                    }
                  }
                },
                {
                  "bangumi_name": "小書痴的下克上",
                  "cover": "/bangumi/cover/http/lain.bgm.tv/pic/cover/l/93/3b/276788_SEeFP.jpg",
                  "update_time": "Wed",
                  "name": "小書痴的下克上",
                  "status": 1,
                  "updated_time": 1577503037,
                  "subtitle_group": "",
                  "episode": 12,
                  "player": {
                    "1": {
                      "path": "/小書痴的下克上/1/[Airota&Nekomoe kissaten] Honzuki no Gekokujou - Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen][01][1080p][CHT].mp4"
                    },
                    "10": {
                      "path": "/小書痴的下克上/10/[DHR][Honzuki no Gekokujou][10][BIG5][720P][AVC_AAC].mp4"
                    },
                    "11": {
                      "path": "/小書痴的下克上/11/[Airota&Nekomoe kissaten] Honzuki no Gekokujou - Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen][11][1080p][CHT].mp4"
                    },
                    "12": {
                      "path": "/小書痴的下克上/12/[Airota&Nekomoe kissaten] Honzuki no Gekokujou - Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen][12][1080p][CHT].mp4"
                    },
                    "2": {
                      "path": "/小書痴的下克上/2/[Airota&Nekomoe kissaten] Honzuki no Gekokujou - Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen][02][720p][CHT].mp4"
                    },
                    "3": {
                      "path": "/小書痴的下克上/3/[Airota&Nekomoe kissaten] Honzuki no Gekokujou - Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen][03][1080p][CHT].mp4"
                    },
                    "4": {
                      "path": "/小書痴的下克上/4/[Airota&Nekomoe kissaten] Honzuki no Gekokujou - Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen][04][1080p][CHT].mp4"
                    },
                    "5": {
                      "path": "/小書痴的下克上/5/[Airota&Nekomoe kissaten] Honzuki no Gekokujou - Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen][05][1080p][CHT].mp4"
                    },
                    "6": {
                      "path": "/小書痴的下克上/6/[DHR][Honzuki no Gekokujou][06][BIG5][720P][AVC_AAC].mp4"
                    },
                    "7": {
                      "path": "/小書痴的下克上/7/[DHR][Honzuki no Gekokujou][07][BIG5][720P][AVC_AAC].mp4"
                    },
                    "8": {
                      "path": "/小書痴的下克上/8/[Airota&Nekomoe kissaten] Honzuki no Gekokujou - Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen][08][1080p][CHT].mp4"
                    },
                    "9": {
                      "path": "/小書痴的下克上/9/[Airota&Nekomoe kissaten] Honzuki no Gekokujou - Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen][09][1080p][CHT].mp4"
                    }
                  }
                },
                {
                  "bangumi_name": "我不是說了能力要平均值嗎！",
                  "cover": "/bangumi/cover/http/lain.bgm.tv/pic/cover/l/2e/97/238962_21617.jpg",
                  "update_time": "Mon",
                  "name": "我不是說了能力要平均值嗎！",
                  "status": 1,
                  "updated_time": 1577383233,
                  "subtitle_group": "",
                  "episode": 12,
                  "player": {
                    "1": {
                      "path": "/我不是說了能力要平均值嗎！/1/[Nekomoe kissaten][Watashi, Nouryoku wa Heikinchi de tte Itta yo ne!][01][1080p][CHT].mp4"
                    },
                    "10": {
                      "path": "/我不是說了能力要平均值嗎！/10/[Nekomoe kissaten][Watashi, Nouryoku wa Heikinchi de tte Itta yo ne!][10][1080p][CHT].mp4"
                    },
                    "11": {
                      "path": "/我不是說了能力要平均值嗎！/11/[Nekomoe kissaten][Watashi, Nouryoku wa Heikinchi de tte Itta yo ne!][11][1080p][CHT].mp4"
                    },
                    "12": {
                      "path": "/我不是說了能力要平均值嗎！/12/[Nekomoe kissaten][Watashi, Nouryoku wa Heikinchi de tte Itta yo ne!][12END][1080p][CHT].mp4"
                    },
                    "2": {
                      "path": "/我不是說了能力要平均值嗎！/2/[Airota][Watashi, Nouryoku wa Heikinchi de tte Itta yo ne!][02][1080p AVC AAC][CHT].mp4"
                    },
                    "3": {
                      "path": "/我不是說了能力要平均值嗎！/3/[DHR][Noukin][03][BIG5][720P][AVC_AAC].mp4"
                    },
                    "4": {
                      "path": "/我不是說了能力要平均值嗎！/4/[DHR][Noukin][04][BIG5][720P][AVC_AAC].mp4"
                    },
                    "6": {
                      "path": "/我不是說了能力要平均值嗎！/6/[DHR][Noukin][06][BIG5][720P][AVC_AAC].mp4"
                    },
                    "7": {
                      "path": "/我不是說了能力要平均值嗎！/7/[Nekomoe kissaten][Watashi, Nouryoku wa Heikinchi de tte Itta yo ne!][07][1080p][CHT].mp4"
                    },
                    "8": {
                      "path": "/我不是說了能力要平均值嗎！/8/[Nekomoe kissaten][Watashi, Nouryoku wa Heikinchi de tte Itta yo ne!][08][720p][CHT].mp4"
                    },
                    "9": {
                      "path": "/我不是說了能力要平均值嗎！/9/[Nekomoe kissaten][Watashi, Nouryoku wa Heikinchi de tte Itta yo ne!][09][720p][CHT].mp4"
                    }
                  }
                },
                {
                  "bangumi_name": "放學後桌遊俱樂部",
                  "cover": "/bangumi/cover/http/lain.bgm.tv/pic/cover/l/0c/90/259790_5y7OS.jpg",
                  "update_time": "Wed",
                  "name": "放學後桌遊俱樂部",
                  "status": 1,
                  "updated_time": 1576922463,
                  "subtitle_group": "",
                  "episode": 12,
                  "player": {
                    "1": {
                      "path": "/放學後桌遊俱樂部/1/[Sakurato.sub][Houkago Saikoro Club][01][BIG5][1080P]/[Sakurato.sub][Houkago Saikoro Club][01][BIG5][1080P].mp4"
                    },
                    "10": {
                      "path": "/放學後桌遊俱樂部/10/[Nekomoe kissaten][Houkago Saikoro Club][10][1080p][CHT].mp4"
                    },
                    "11": {
                      "path": "/放學後桌遊俱樂部/11/[Nekomoe kissaten][Houkago Saikoro Club][11][1080p][CHT].mp4"
                    },
                    "12": {
                      "path": "/放學後桌遊俱樂部/12/[Nekomoe kissaten][Houkago Saikoro Club][12][1080p][CHT].mp4"
                    },
                    "2": {
                      "path": "/放學後桌遊俱樂部/2/[Sakurato.sub][Houkago Saikoro Club][02][BIG5][1080P]/[Sakurato.sub][Houkago Saikoro Club][02][BIG5][1080P].mp4"
                    },
                    "4": {
                      "path": "/放學後桌遊俱樂部/4/[Nekomoe kissaten][Houkago Saikoro Club][04][1080p][CHT].mp4"
                    },
                    "5": {
                      "path": "/放學後桌遊俱樂部/5/[Nekomoe kissaten][Houkago Saikoro Club][05][1080p][CHT].mp4"
                    },
                    "6": {
                      "path": "/放學後桌遊俱樂部/6/[Nekomoe kissaten][Houkago Saikoro Club][06][1080p][CHT].mp4"
                    },
                    "7": {
                      "path": "/放學後桌遊俱樂部/7/[Nekomoe kissaten][Houkago Saikoro Club][07][1080p][CHT].mp4"
                    }
                  }
                }
              ]
            }
            """
        ])
        import scheduler.NewBangumiScheduler
        reload(scheduler.NewBangumiScheduler)
        for coroutine, _ in mock_get_event_loop.return_value.run_until_complete.call_args_list:
            task = asyncio.Task(coroutine[0])
            task.cancel()
        await scheduler.NewBangumiScheduler.check_update()
        mock_get.return_value.__aenter__.return_value.text = CoroutineMock(side_effect=[
            """
            {
              "version": "2.1.1",
              "latest_version": "2.1.2",
              "frontend_version": "1.1.x",
              "status": "success",
              "lang": "zh_cn",
              "danmaku_api": "",
              "data": [
                {
                  "bangumi_name": "慎重勇者 ~這個勇者明明超TUEEE卻過度謹慎~",
                  "cover": "/bangumi/cover/http/lain.bgm.tv/pic/cover/l/02/3c/266157_5wF3a.jpg",
                  "update_time": "Wed",
                  "name": "慎重勇者 ~這個勇者明明超TUEEE卻過度謹慎~",
                  "status": 1,
                  "updated_time": 1578592819,
                  "subtitle_group": "",
                  "episode": 12,
                  "player": {
                    "1": {
                      "path": "/慎重勇者 ~這個勇者明明超TUEEE卻過度謹慎~/1/[Sakurato.sub][Shinchou Yuusha][01][BIG5][1080P]/[Sakurato.sub][Shinchou Yuusha][01][BIG5][1080P].mp4"
                    },
                    "10": {
                      "path": "/慎重勇者 ~這個勇者明明超TUEEE卻過度謹慎~/10/【爱恋&漫猫字幕组】[谨慎勇者][慎重勇者][这个勇者明明超TUEEE却过度谨慎][10][BIG5][720P].mp4"
                    },
                    "11": {
                      "path": "/慎重勇者 ~這個勇者明明超TUEEE卻過度謹慎~/11/[Sakurato.sub][Shinchou Yuusha][11][BIG5][1080P]/[Sakurato.sub][Shinchou Yuusha][11][BIG5][1080P].mp4"
                    },
                    "12": {
                      "path": "/慎重勇者 ~這個勇者明明超TUEEE卻過度謹慎~/12/[Sakurato.sub][Shinchou Yuusha][12][BIG5][1080P]/[Sakurato.sub][Shinchou Yuusha][12][BIG5][1080P].mp4"
                    },
                    "2": {
                      "path": "/慎重勇者 ~這個勇者明明超TUEEE卻過度謹慎~/2/2big5_batch_Mux.mp4"
                    },
                    "3": {
                      "path": "/慎重勇者 ~這個勇者明明超TUEEE卻過度謹慎~/3/【爱恋&漫猫字幕组】[谨慎勇者][慎重勇者][这个勇者明明超TUEEE却过度谨慎][03][BIG5][720P].mp4"
                    },
                    "4": {
                      "path": "/慎重勇者 ~這個勇者明明超TUEEE卻過度謹慎~/4/【爱恋&漫猫字幕组】[谨慎勇者][慎重勇者][这个勇者明明超TUEEE却过度谨慎][04][BIG5][720P].mp4"
                    },
                    "5": {
                      "path": "/慎重勇者 ~這個勇者明明超TUEEE卻過度謹慎~/5/【爱恋&漫猫字幕组】[谨慎勇者][慎重勇者][这个勇者明明超TUEEE却过度谨慎][05][BIG5][720P].mp4"
                    },
                    "6": {
                      "path": "/慎重勇者 ~這個勇者明明超TUEEE卻過度謹慎~/6/【爱恋&漫猫字幕组】[谨慎勇者][慎重勇者][这个勇者明明超TUEEE却过度谨慎][06][BIG5][720P].mp4"
                    },
                    "7": {
                      "path": "/慎重勇者 ~這個勇者明明超TUEEE卻過度謹慎~/7/【爱恋&漫猫字幕组】[谨慎勇者][慎重勇者][这个勇者明明超TUEEE却过度谨慎][07][BIG5][720P].mp4"
                    },
                    "8": {
                      "path": "/慎重勇者 ~這個勇者明明超TUEEE卻過度謹慎~/8/[Sakurato.sub][Shinchou Yuusha][08][BIG5][1080P]/[Sakurato.sub][Shinchou Yuusha][08][BIG5][1080P].mp4"
                    },
                    "9": {
                      "path": "/慎重勇者 ~這個勇者明明超TUEEE卻過度謹慎~/9/[Sakurato.sub][Shinchou Yuusha][09][BIG5][1080P]/[Sakurato.sub][Shinchou Yuusha][09][BIG5][1080P].mp4"
                    }
                  }
                },
                {
                  "bangumi_name": "刀剑神域 Alicization篇 War of Underworld",
                  "cover": "/bangumi/cover/http/lain.bgm.tv/pic/cover/l/dd/a6/279457_TkOjj.jpg",
                  "update_time": "Sat",
                  "name": "刀剑神域 Alicization篇 War of Underworld",
                  "status": 1,
                  "updated_time": 1578333651,
                  "subtitle_group": "",
                  "episode": 12,
                  "player": {
                    "1": {
                      "path": "/刀剑神域 Alicization篇 War of Underworld/1/[SumiSora&CASO&FLsonw][sao-alicization_War_of_Underworld][01][CHT][720P].mp4"
                    },
                    "10": {
                      "path": "/刀剑神域 Alicization篇 War of Underworld/10/[SumiSora&CASO&FLsnow][sao-alicization_War_of_Underworld][10][CHT][720P].mp4"
                    },
                    "11": {
                      "path": "/刀剑神域 Alicization篇 War of Underworld/11/[SumiSora&CASO&FLsnow][sao-alicization_War_of_Underworld][11][CHT][720P].mp4"
                    },
                    "12": {
                      "path": "/刀剑神域 Alicization篇 War of Underworld/12/[SumiSora&CASO&FLsnow][sao-alicization_War_of_Underworld][12][CHT][720P].mp4"
                    },
                    "2": {
                      "path": "/刀剑神域 Alicization篇 War of Underworld/2/[SumiSora&CASO&FLsonw][sao-alicization_War_of_Underworld][02][CHT][720P].mp4"
                    },
                    "3": {
                      "path": "/刀剑神域 Alicization篇 War of Underworld/3/[SumiSora&CASO&FLsnow][sao-alicization_War_of_Underworld][03][CHT][720P].mp4"
                    },
                    "4": {
                      "path": "/刀剑神域 Alicization篇 War of Underworld/4/[SumiSora&CASO&FLsnow][sao-alicization_War_of_Underworld][04][CHT][720P].mp4"
                    },
                    "5": {
                      "path": "/刀剑神域 Alicization篇 War of Underworld/5/[SumiSora&CASO&FLsnow][sao-alicization_War_of_Underworld][05][CHT][720P].mp4"
                    },
                    "6": {
                      "path": "/刀剑神域 Alicization篇 War of Underworld/6/[SumiSora&CASO&FLsnow][sao-alicization_War_of_Underworld][06][CHT][720P].mp4"
                    },
                    "7": {
                      "path": "/刀剑神域 Alicization篇 War of Underworld/7/[SumiSora&CASO&FLsnow][sao-alicization_War_of_Underworld][07][CHT][720P].mp4"
                    },
                    "8": {
                      "path": "/刀剑神域 Alicization篇 War of Underworld/8/[SumiSora&CASO&FLsnow][sao-alicization_War_of_Underworld][08][CHT][720P].mp4"
                    },
                    "9": {
                      "path": "/刀剑神域 Alicization篇 War of Underworld/9/[SumiSora&CASO&FLsnow][sao-alicization_War_of_Underworld][09][CHT][720P].mp4"
                    }
                  }
                },
                {
                  "bangumi_name": "入間同學入魔了！",
                  "cover": "/bangumi/cover/http/lain.bgm.tv/pic/cover/l/6a/b9/273844_JQ26Q.jpg",
                  "update_time": "Sat",
                  "name": "入間同學入魔了！",
                  "status": 1,
                  "updated_time": 1578254412,
                  "subtitle_group": "",
                  "episode": 14,
                  "player": {
                    "1": {
                      "path": "/入間同學入魔了！/1/[Sakurato.sub][Mairimashita! Iruma-kun][01][BIG5][1080P]/[Sakurato.sub][Mairimashita! Iruma-kun][01][BIG5][1080P].mp4"
                    },
                    "10": {
                      "path": "/入間同學入魔了！/10/[Mairimashita! Iruma-kun][10][BIG5][1080P].mp4"
                    },
                    "11": {
                      "path": "/入間同學入魔了！/11/[Mairimashita! Iruma-kun][11][BIG5][1080P].mp4"
                    },
                    "12": {
                      "path": "/入間同學入魔了！/12/[Mairimashita! Iruma-kun][12][BIG5][1080P].mp4"
                    },
                    "13": {
                      "path": "/入間同學入魔了！/13/[Mairimashita! Iruma-kun][13][BIG5][1080P].mp4"
                    },
                    "14": {
                      "path": "/入間同學入魔了！/14/[Sakurato.sub][Mairimashita! Iruma-kun][14][BIG5][1080P]/[Sakurato.sub][Mairimashita! Iruma-kun][14][BIG5][1080P].mp4"
                    },
                    "2": {
                      "path": "/入間同學入魔了！/2/[Mairimashita! Iruma-kun][02][BIG5][1080P].mp4"
                    },
                    "3": {
                      "path": "/入間同學入魔了！/3/[Mairimashita! Iruma-kun][03][BIG5][1080P].mp4"
                    },
                    "4": {
                      "path": "/入間同學入魔了！/4/[Mairimashita! Iruma-kun][04][BIG5][1080P].mp4"
                    },
                    "5": {
                      "path": "/入間同學入魔了！/5/[Mairimashita! Iruma-kun][05][BIG5][1080P].mp4"
                    },
                    "6": {
                      "path": "/入間同學入魔了！/6/[Mairimashita! Iruma-kun][06][BIG5][1080P].mp4"
                    },
                    "7": {
                      "path": "/入間同學入魔了！/7/[Mairimashita! Iruma-kun][07][BIG5][1080P].mp4"
                    },
                    "8": {
                      "path": "/入間同學入魔了！/8/[Mairimashita! Iruma-kun][08][BIG5][1080P].mp4"
                    },
                    "9": {
                      "path": "/入間同學入魔了！/9/[Mairimashita! Iruma-kun][09][BIG5][1080P].mp4"
                    }
                  }
                },
                {
                  "bangumi_name": "我們真的學不來！第二季",
                  "cover": "/bangumi/cover/http/lain.bgm.tv/pic/cover/l/80/0f/285130_brGSR.jpg",
                  "update_time": "Wed",
                  "name": "我們真的學不來！第二季",
                  "status": 1,
                  "updated_time": 1577570520,
                  "subtitle_group": "",
                  "episode": 13,
                  "player": {
                    "1": {
                      "path": "/我們真的學不來！第二季/1/[Bokutachi wa Benkyou ga Dekinai S2][01][BIG5][1080P].mp4"
                    },
                    "10": {
                      "path": "/我們真的學不來！第二季/10/[HYSUB]Bokutachi wa Benkyou ga Dekinai![10][BIG5_MP4][1280X720].mp4"
                    },
                    "11": {
                      "path": "/我們真的學不來！第二季/11/[HYSUB]Bokutachi wa Benkyou ga Dekinai![11][BIG5_MP4][1280X720].mp4"
                    },
                    "12": {
                      "path": "/我們真的學不來！第二季/12/[HYSUB]Bokutachi wa Benkyou ga Dekinai![12][BIG5_MP4][1280X720].mp4"
                    },
                    "13": {
                      "path": "/我們真的學不來！第二季/13/[HYSUB]Bokutachi wa Benkyou ga Dekinai![13][BIG5_MP4][1280X720][END].mp4"
                    },
                    "2": {
                      "path": "/我們真的學不來！第二季/2/[HYSUB]Bokutachi wa Benkyou ga Dekinai![02][BIG5_MP4][1280X720].mp4"
                    },
                    "3": {
                      "path": "/我們真的學不來！第二季/3/[HYSUB]Bokutachi wa Benkyou ga Dekinai![03][BIG5_MP4][1280X720].mp4"
                    },
                    "4": {
                      "path": "/我們真的學不來！第二季/4/[Bokutachi wa Benkyou ga Dekinai S2][04][BIG5][1080P].mp4"
                    },
                    "5": {
                      "path": "/我們真的學不來！第二季/5/[HYSUB]Bokutachi wa Benkyou ga Dekinai![05][BIG5_MP4][1280X720].mp4"
                    },
                    "6": {
                      "path": "/我們真的學不來！第二季/6/[HYSUB]Bokutachi wa Benkyou ga Dekinai![06][BIG5_MP4][1280X720].mp4"
                    },
                    "7": {
                      "path": "/我們真的學不來！第二季/7/[HYSUB]Bokutachi wa Benkyou ga Dekinai![07][BIG5_MP4][1280X720].mp4"
                    },
                    "8": {
                      "path": "/我們真的學不來！第二季/8/[HYSUB]Bokutachi wa Benkyou ga Dekinai![08][BIG5_MP4][1280X720].mp4"
                    },
                    "9": {
                      "path": "/我們真的學不來！第二季/9/[HYSUB]Bokutachi wa Benkyou ga Dekinai![09][BIG5_MP4][1280X720].mp4"
                    }
                  }
                },
                {
                  "bangumi_name": "小書痴的下克上",
                  "cover": "/bangumi/cover/http/lain.bgm.tv/pic/cover/l/93/3b/276788_SEeFP.jpg",
                  "update_time": "Wed",
                  "name": "小書痴的下克上",
                  "status": 1,
                  "updated_time": 1577503037,
                  "subtitle_group": "",
                  "episode": 12,
                  "player": {
                    "1": {
                      "path": "/小書痴的下克上/1/[Airota&Nekomoe kissaten] Honzuki no Gekokujou - Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen][01][1080p][CHT].mp4"
                    },
                    "10": {
                      "path": "/小書痴的下克上/10/[DHR][Honzuki no Gekokujou][10][BIG5][720P][AVC_AAC].mp4"
                    },
                    "11": {
                      "path": "/小書痴的下克上/11/[Airota&Nekomoe kissaten] Honzuki no Gekokujou - Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen][11][1080p][CHT].mp4"
                    },
                    "12": {
                      "path": "/小書痴的下克上/12/[Airota&Nekomoe kissaten] Honzuki no Gekokujou - Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen][12][1080p][CHT].mp4"
                    },
                    "2": {
                      "path": "/小書痴的下克上/2/[Airota&Nekomoe kissaten] Honzuki no Gekokujou - Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen][02][720p][CHT].mp4"
                    },
                    "3": {
                      "path": "/小書痴的下克上/3/[Airota&Nekomoe kissaten] Honzuki no Gekokujou - Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen][03][1080p][CHT].mp4"
                    },
                    "4": {
                      "path": "/小書痴的下克上/4/[Airota&Nekomoe kissaten] Honzuki no Gekokujou - Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen][04][1080p][CHT].mp4"
                    },
                    "5": {
                      "path": "/小書痴的下克上/5/[Airota&Nekomoe kissaten] Honzuki no Gekokujou - Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen][05][1080p][CHT].mp4"
                    },
                    "6": {
                      "path": "/小書痴的下克上/6/[DHR][Honzuki no Gekokujou][06][BIG5][720P][AVC_AAC].mp4"
                    },
                    "7": {
                      "path": "/小書痴的下克上/7/[DHR][Honzuki no Gekokujou][07][BIG5][720P][AVC_AAC].mp4"
                    },
                    "8": {
                      "path": "/小書痴的下克上/8/[Airota&Nekomoe kissaten] Honzuki no Gekokujou - Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen][08][1080p][CHT].mp4"
                    },
                    "9": {
                      "path": "/小書痴的下克上/9/[Airota&Nekomoe kissaten] Honzuki no Gekokujou - Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen][09][1080p][CHT].mp4"
                    }
                  }
                },
                {
                  "bangumi_name": "我不是說了能力要平均值嗎！",
                  "cover": "/bangumi/cover/http/lain.bgm.tv/pic/cover/l/2e/97/238962_21617.jpg",
                  "update_time": "Mon",
                  "name": "我不是說了能力要平均值嗎！",
                  "status": 1,
                  "updated_time": 1577383233,
                  "subtitle_group": "",
                  "episode": 12,
                  "player": {
                    "1": {
                      "path": "/我不是說了能力要平均值嗎！/1/[Nekomoe kissaten][Watashi, Nouryoku wa Heikinchi de tte Itta yo ne!][01][1080p][CHT].mp4"
                    },
                    "10": {
                      "path": "/我不是說了能力要平均值嗎！/10/[Nekomoe kissaten][Watashi, Nouryoku wa Heikinchi de tte Itta yo ne!][10][1080p][CHT].mp4"
                    },
                    "11": {
                      "path": "/我不是說了能力要平均值嗎！/11/[Nekomoe kissaten][Watashi, Nouryoku wa Heikinchi de tte Itta yo ne!][11][1080p][CHT].mp4"
                    },
                    "12": {
                      "path": "/我不是說了能力要平均值嗎！/12/[Nekomoe kissaten][Watashi, Nouryoku wa Heikinchi de tte Itta yo ne!][12END][1080p][CHT].mp4"
                    },
                    "2": {
                      "path": "/我不是說了能力要平均值嗎！/2/[Airota][Watashi, Nouryoku wa Heikinchi de tte Itta yo ne!][02][1080p AVC AAC][CHT].mp4"
                    },
                    "3": {
                      "path": "/我不是說了能力要平均值嗎！/3/[DHR][Noukin][03][BIG5][720P][AVC_AAC].mp4"
                    },
                    "4": {
                      "path": "/我不是說了能力要平均值嗎！/4/[DHR][Noukin][04][BIG5][720P][AVC_AAC].mp4"
                    },
                    "6": {
                      "path": "/我不是說了能力要平均值嗎！/6/[DHR][Noukin][06][BIG5][720P][AVC_AAC].mp4"
                    },
                    "7": {
                      "path": "/我不是說了能力要平均值嗎！/7/[Nekomoe kissaten][Watashi, Nouryoku wa Heikinchi de tte Itta yo ne!][07][1080p][CHT].mp4"
                    },
                    "8": {
                      "path": "/我不是說了能力要平均值嗎！/8/[Nekomoe kissaten][Watashi, Nouryoku wa Heikinchi de tte Itta yo ne!][08][720p][CHT].mp4"
                    },
                    "9": {
                      "path": "/我不是說了能力要平均值嗎！/9/[Nekomoe kissaten][Watashi, Nouryoku wa Heikinchi de tte Itta yo ne!][09][720p][CHT].mp4"
                    }
                  }
                },
                {
                  "bangumi_name": "放學後桌遊俱樂部",
                  "cover": "/bangumi/cover/http/lain.bgm.tv/pic/cover/l/0c/90/259790_5y7OS.jpg",
                  "update_time": "Wed",
                  "name": "放學後桌遊俱樂部",
                  "status": 1,
                  "updated_time": 1576922463,
                  "subtitle_group": "",
                  "episode": 12,
                  "player": {
                    "1": {
                      "path": "/放學後桌遊俱樂部/1/[Sakurato.sub][Houkago Saikoro Club][01][BIG5][1080P]/[Sakurato.sub][Houkago Saikoro Club][01][BIG5][1080P].mp4"
                    },
                    "10": {
                      "path": "/放學後桌遊俱樂部/10/[Nekomoe kissaten][Houkago Saikoro Club][10][1080p][CHT].mp4"
                    },
                    "11": {
                      "path": "/放學後桌遊俱樂部/11/[Nekomoe kissaten][Houkago Saikoro Club][11][1080p][CHT].mp4"
                    },
                    "12": {
                      "path": "/放學後桌遊俱樂部/12/[Nekomoe kissaten][Houkago Saikoro Club][12][1080p][CHT].mp4"
                    },
                    "2": {
                      "path": "/放學後桌遊俱樂部/2/[Sakurato.sub][Houkago Saikoro Club][02][BIG5][1080P]/[Sakurato.sub][Houkago Saikoro Club][02][BIG5][1080P].mp4"
                    },
                    "4": {
                      "path": "/放學後桌遊俱樂部/4/[Nekomoe kissaten][Houkago Saikoro Club][04][1080p][CHT].mp4"
                    },
                    "5": {
                      "path": "/放學後桌遊俱樂部/5/[Nekomoe kissaten][Houkago Saikoro Club][05][1080p][CHT].mp4"
                    },
                    "6": {
                      "path": "/放學後桌遊俱樂部/6/[Nekomoe kissaten][Houkago Saikoro Club][06][1080p][CHT].mp4"
                    },
                    "7": {
                      "path": "/放學後桌遊俱樂部/7/[Nekomoe kissaten][Houkago Saikoro Club][07][1080p][CHT].mp4"
                    },
                    "8": {
                      "path": "/放學後桌遊俱樂部/8/[Nekomoe kissaten][Houkago Saikoro Club][08][1080p][CHT].mp4"
                    },
                    "9": {
                      "path": "/放學後桌遊俱樂部/9/[Nekomoe kissaten][Houkago Saikoro Club][09][1080p][CHT].mp4"
                    }
                  }
                }
              ]
            }
            """
        ])
        mock_bot.send_discuss_msg = CoroutineMock(return_value=None)
        mock_bot.send_group_msg = CoroutineMock(return_value=None)

        await scheduler.NewBangumiScheduler.check_update()

        self.assertEqual('123', mock_bot.send_discuss_msg.call_args[1]['discuss_id'])
        self.assertEqual('321', mock_bot.send_group_msg.call_args[1]['group_id'])
        pass
