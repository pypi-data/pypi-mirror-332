import setuptools

setuptools.setup(
    name="gru",
    version="0.0.1rc26-dev1",
    install_requires=[
        "requests>=2.31.0",
        "typing==3.7.4.3",
        "chardet==5.1.0",
        "click>=8.1.7",
        "fire>=0.7.0",
        "pydantic>=2.6.3",
        "cookiecutter>=2.6.0",
        "langgraph>=0.2.50",
        "fastapi>=0.115.5",
        "uvicorn>=0.32.0",
        "langgraph-checkpoint-postgres>=2.0.3",
        "psycopg[binary,pool]",
        "celery>=5.5.0rc4", # TODO: change to 5.5.0 stable version as soon as it is released
        "redis>=5.2.0",
        "websockets>=14.1",
        "termcolor>=2.5.0",
        "PyGithub>=2.5.0",
        "pika==1.3.2",
        "pymilvus==2.5.4"

    ],
    entry_points={
        "console_scripts": [
            "yugenml = gru.cookiecutter.mlops_templates_cli:mlops_template_cli",
            "yserve = gru.ml_serving.server:serve",
            "gru = gru.cli:main",
            "canso = gru.canso_cli:main",
        ],
    },
    include_package_data=True,
    packages=setuptools.find_packages(),
)
