from app.app import App
from zunzun import AppRegister, ZunzunApp, maker, orm
import main

register = main.injector.get(AppRegister)
register.add([App, ZunzunApp, maker.MakerApp, orm.OrmApp])
commands = register.commands()

if __name__ == "__main__":
    commands()
