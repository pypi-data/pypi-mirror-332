import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="dvadmin3-celery",
    version="3.1.7",
    author="DVAdmin",
    author_email="liqiang@django-vue-admin.com",
    description="适用于 django3-vue-admin 的celery异步插件",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitee.com/huge-dream/dvadmin3-celery",
    packages=setuptools.find_packages(),
    python_requires='>=3.7, <4',
    install_requires=["django-celery-beat==2.7.0",
                      "tenant-schemas-celery==3.0.0",
                      "django-redis==5.4.0"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'celery.result_backends': [
            'django-db = django_celery_results.backends:DatabaseBackend',
            'django-cache = django_celery_results.backends:CacheBackend',
        ],
    },
    include_package_data=True
)