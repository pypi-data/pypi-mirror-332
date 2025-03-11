from apscheduler.jobstores.redis import RedisJobStore

from fastboost.funboost_config_deafult import BrokerConnConfig,FunboostCommonConfig

from fastboost.timing_job import FunboostBackgroundScheduler

"""
这个是使用redis作为定时任务持久化，支持动态修改/添加/删除定时任务
"""

jobstores = {
    "default": RedisJobStore(db=BrokerConnConfig.REDIS_DB, host=BrokerConnConfig.REDIS_HOST,
                             port=BrokerConnConfig.REDIS_PORT, password=BrokerConnConfig.REDIS_PASSWORD,
                             username=BrokerConnConfig.REDIS_USERNAME)
}

funboost_background_scheduler_redis_store = FunboostBackgroundScheduler(timezone=FunboostCommonConfig.TIMEZONE, daemon=False, jobstores=jobstores)





"""

跨python解释器 跨机器动态修改定时任务配置的例子在

test_frame/test_apschedual/test_aps_redis_store.py
test_frame/test_apschedual/test_change_aps_conf.py

"""