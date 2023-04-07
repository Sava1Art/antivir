from pywinauto import Application


def is_app_existing(app, name):
    for wnd in app.windows():
        if name in wnd.window_text():
            return True
    return False


def create_app(directory):
    app = Application(backend="uia").start(rf'{directory}')
    app.Dialog.wait('ready')
    app.Dialog.set_focus()
    return app
