from application import settings

# ================================================= #
# ***************** 插件配置区开始 *******************
# ================================================= #
# 路由配置
plugins_url_patterns = [
    {"re_path": r'api/dvadmin_celery/', "include": "dvadmin3_celery.urls"}
]
# app 配置
apps = ['django_celery_beat', 'django_celery_results', 'dvadmin3_celery']
# 租户模式中，public模式共享app配置
tenant_shared_apps = []
# ================================================= #
# ******************* 插件配置区结束 *****************
# ================================================= #

if not hasattr(settings, 'CACHES'):
    _DEFAULT_CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": f'{settings.REDIS_URL}/{getattr(settings, "REDIS_DB") or 1}',
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            }
        },
    }
else:
    _DEFAULT_CACHES = settings.CACHES

if not hasattr(settings, 'REDIS_URL'):
    raise Exception("请配置redis地址，否则celery无法使用！")

# ********** 赋值到 settings 中 **********
settings.CACHES = _DEFAULT_CACHES
settings.INSTALLED_APPS += [app for app in apps if app not in settings.INSTALLED_APPS]
settings.TENANT_SHARED_APPS += tenant_shared_apps
# ********** celery 配置 **********
if not hasattr(settings, 'CELERY_BROKER_URL'):
    settings.CELERY_BROKER_URL = f'{settings.REDIS_URL}/{getattr(settings, "CELERY_BROKER_DB") or 2}'

# ********** 执行结果保存位置 **********
if not hasattr(settings, 'CELERY_RESULT_BACKEND'):
    settings.CELERY_RESULT_BACKEND = 'django-db'
if not hasattr(settings, 'CELERY_RESULT_EXTENDED'):
    settings.CELERY_RESULT_EXTENDED = True

# ********** Backend数据库 **********
if not hasattr(settings, 'CELERY_BEAT_SCHEDULER'):
    settings.CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers.DatabaseScheduler'

# ********** 注册路由 **********
settings.PLUGINS_URL_PATTERNS += plugins_url_patterns

# ********** Backend数据库 **********
if not hasattr(settings, 'CELERYBEAT_SCHEDULER'):
    settings.CELERYBEAT_SCHEDULER = 'django_celery_beat.schedulers.DatabaseScheduler'
# 避免时区的问题
CELERY_ENABLE_UTC = False
DJANGO_CELERY_BEAT_TZ_AWARE = False
# 避免celery启动时，连接redis失败
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
# celery4版本的 默认使用 JSON 作为 serializer ，而 celery3 版本的默认使用 pickle。
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['pickle', 'json']