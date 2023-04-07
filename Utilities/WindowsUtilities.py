from pywinauto import Application


def is_app_existing(app, name):
    result = False
    for wnd in app.windows():
        if name in wnd.window_text():
            result = True
            break
    return result


def create_app(directory):
    app = Application(backend="uia").start(rf'{directory}')
    app.Dialog.wait('ready')
    app.Dialog.set_focus()
    return app
