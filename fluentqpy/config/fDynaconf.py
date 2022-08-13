#!/usr/bin/env python
# -*- coding:utf-8 -*-


from dynaconf import Dynaconf

fsettings = Dynaconf(
    envvar_prefix="qpy",
    settings_files=["settings.toml", ".secrets.toml"],
    environments=True,
    load_dotenv=True,
    env_switcher="CURR_ENV",  # to switch environments `export ENV_FOR_DYNACONF=production`
    dotenv_path="../config/.env",  # custom path for .env file to be loaded
    includes=["../config/more_settings.toml"],
)

fsettings.validators.validate()



