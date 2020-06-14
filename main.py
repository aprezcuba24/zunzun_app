import os
from zunzun import Router, create_config_scope, Config
from injector import Injector, singleton

ENV = os.getenv("ZUNZUN_ENV", "dev")

injector = Injector()
injector.binder.bind(Config, to=Config("config", ENV), scope=singleton)

config = create_config_scope()

router = injector.get(Router)

import app.controllers  # noqa
