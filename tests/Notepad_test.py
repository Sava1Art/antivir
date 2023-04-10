import configuration
from Utilities import WindowsUtilities
from WindowsApps.Notepad import Notepad


def test_notepad_new_file():
    app = WindowsUtilities.create_app(configuration.NOTEPAD_DIRECTORY)
    assert WindowsUtilities.is_app_existing(app, "Notepad"), "Notepad isn't opened"
    notepad = Notepad(app)
    notepad.create_new_file()
    assert WindowsUtilities.is_app_existing(app, "new"), "New file isn't created"
    notepad.type_text("test")
    last_saved_file = notepad.save_file()
    assert WindowsUtilities.is_app_existing(app, last_saved_file), "File isn't saved"
    notepad.exit()
    assert not WindowsUtilities.is_app_existing(app, "Notepad"), "Notepad isn't closed"


def test_notepad_existing_file():
    app = WindowsUtilities.create_app(configuration.NOTEPAD_DIRECTORY)
    assert WindowsUtilities.is_app_existing(app, "Notepad"), "Notepad isn't opened"
    notepad = Notepad(app)
    notepad.open_file(rf"{configuration.FILE_DIRECTORY}\{configuration.FILE_NAME}.txt")
    assert WindowsUtilities.is_app_existing(app, configuration.FILE_NAME), "File isn't opened"
    notepad.exit()
    assert not WindowsUtilities.is_app_existing(app, "Notepad"), "Notepad isn't closed"
