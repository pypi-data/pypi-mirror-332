
# DO NOT EDIT THIS FILE -- AUTOGENERATED BY PANTS
# Target: tobikodata/http_client:dist

from setuptools import setup

setup(**{
    'author': 'TobikoData Inc.',
    'author_email': 'engineering@tobikodata.com',
    'install_requires': (
        'Authlib',
        'httpx',
        'pydantic>=2.0.0',
        'rich[jupyter]',
        'ruamel.yaml',
        'tenacity',
        'tobiko-cloud-helpers==202510.26.0',
        'typing_extensions',
    ),
    'name': 'tobiko-cloud-api-client',
    'namespace_packages': (
    ),
    'package_data': {
    },
    'packages': (
        'tobikodata',
        'tobikodata.http_client',
        'tobikodata.http_client.api_models.v1',
    ),
    'python_requires': '<3.13,>=3.9',
    'version': '202510.26.0',
})
