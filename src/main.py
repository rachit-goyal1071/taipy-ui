from taipy.gui import Gui
from pages import *


pages = {
    "/": root_page,
    "pages": pages
}


if __name__ == "__main__":

    gui = Gui(pages=pages)
    gui.run(title="ui")
