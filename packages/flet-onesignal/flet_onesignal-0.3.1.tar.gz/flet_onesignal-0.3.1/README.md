# Flet OneSignal

---

## Description

Flutter OneSignal package integration for Python Flet.

[Flet OneSignal](https://pub.dev/packages?q=flet_onesignal) in the official package repository for Dart and Flutter apps.

---

## Installation

**Using POETRY**

```console
$ poetry add flet-onesignal
```

**Using PIP**

```console
$ pip install flet-onesignal
```

**Using UV**

```console
$ uv add flet-onesignal
```

---

## Example configuration in the `pyproject.toml` file.

[More in ](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/) Support for flet build command.

```toml
[project]
name = "flet-onesignal-example"
version = "0.1.0"
description = "flet-onesignal-example"
readme = "README.md"
requires-python = ">=3.12"
authors = [
    { name = "developer", email = "you@example.com" }
]

dependencies = [
    "flet>=0.26.0",
    "flet-onesignal>=0.3.0",
]

[tool.uv]
dev-dependencies = [
    "flet[all]>=0.26.0",
]

```

### Example of in-app usage

```Python
import flet as ft
import flet_onesignal as fos
from functools import partial

ONESIGNAL_APP_ID = "example-123a-12a3-1a23-abcd1ef23g45"


async def main(page: ft.Page):
    page.appbar = ft.AppBar(title=ft.Text("OneSignal Test"), bgcolor=ft.Colors.BLUE_700, color=ft.Colors.WHITE)
    get_onesignal_id = ft.TextField(label='Get OneSignal ID', read_only=True)
    get_external_id = ft.TextField(label='Get External User ID', read_only=True, ignore_pointers=True)
    set_external_id = ft.TextField(label='Set External User ID', hint_text='User ID')
    language = ft.TextField(label='Language', hint_text='Language Code (en)', value='en', color=ft.Colors.GREEN)

    def handle_notification_opened(e):
        #Access the data of the clicked notification
        list_view.content.controls.append(ft.Text(f"Notification opened: {e.notification_opened}"))
        list_view.update()

    def handle_notification_received(e):
        # Access the data of the received notification
        list_view.content.controls.append(ft.Text(f"Notification received: {e.notification_received}"))
        list_view.update()

    def handle_click_in_app_messages(e):
        # Access the data of the received notification in app messages
        list_view.content.controls.append(ft.Text(f"Notification click_in_app_messages: {e.click_in_app_messages}"))
        list_view.update()

    def get_id(e):
        result = onesignal.get_onesignal_id()
        get_onesignal_id.value = result
        get_onesignal_id.update()

    def get_external_user_id(e):
        result = onesignal.get_external_user_id()
        get_external_id.value = result
        get_external_id.update()

    def handle_login(e, external_user_id):
        message = "Login failed"

        if not external_user_id.value:
            message = "Please enter external user ID"

        if external_user_id.value:
            result = onesignal.login(external_user_id.value)
            if result:
                message = "Login successful"

        list_view.content.controls.append(ft.Text(message))
        list_view.update()

    def handle_logout(e):
        onesignal.logout()
        set_external_id.value = None
        set_external_id.update()

    def set_language(e, language_code):
        result = onesignal.set_language(language_code.value)
        list_view.content.controls.append(ft.Text(result))
        list_view.update()
        print(result)

    def handle_error(e):
        #handle_error
        list_view.content.controls.append(ft.Text(f"Error: {e.data}"))
        list_view.update()

    onesignal = fos.OneSignal(
        settings=fos.OneSignalSettings(app_id=ONESIGNAL_APP_ID),
        on_notification_opened=handle_notification_opened,
        on_notification_received=handle_notification_received,
        on_click_in_app_messages=handle_click_in_app_messages,
        on_error=handle_error,
    )

    container = ft.Container(
        alignment=ft.alignment.bottom_center,
        content=ft.Row(
            scroll=ft.ScrollMode.ADAPTIVE,
            expand=True,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.ElevatedButton(
                    text='Get OneSignal Id',
                    on_click=get_id
                ),
                ft.ElevatedButton(
                    'Get External User Id',
                    on_click=get_external_user_id
                ),
                ft.ElevatedButton(
                    text='Set External User Id',
                    on_click=partial(handle_login, external_user_id=set_external_id)
                ),
                ft.ElevatedButton(
                    text='Logout External User Id',
                    on_click=handle_logout
                ),
                ft.ElevatedButton(
                    text='Set Language',
                    on_click=partial(set_language, language_code=language)
                ),
            ]
        )
    )

    list_view = ft.Container(
        expand=True,
        content=ft.ListView(
            padding=ft.padding.all(10),
            spacing=5,
        )
    )
    page.overlay.append(onesignal)

    page.add(
        # onesignal,
        list_view,
        get_onesignal_id,
        get_external_id,
        set_external_id,
        language,
        container,
    )


if __name__ == "__main__":
    ft.app(target=main)

```
