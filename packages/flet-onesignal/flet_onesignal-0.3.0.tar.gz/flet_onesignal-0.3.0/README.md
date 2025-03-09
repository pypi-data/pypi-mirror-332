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
    "flet-onesignal>=0.2.0",
]

[tool.uv]
dev-dependencies = [
    "flet[all]>=0.26.0",
]

```

### Example of in-app usage

```Python
import flet as ft
from flet_onesignal.flet_onesignal import FletOneSignal

ONESIGNAL_APP_ID = ''   # https://onesignal.com     <---


def main(page: ft.Page):
    onesignal = FletOneSignal(app_id=ONESIGNAL_APP_ID)

    title = ft.Text(
        value='FletOneSignal - Test',
        size=20,
    )

    message = ft.Text(
        value='Push notification message here',
        size=20,
    )

    container = ft.Container(
        expand=True,
        alignment=ft.alignment.center,
        content=ft.Column(
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                title,
                ft.Container(
                    width=page.width * 0.3,
                    content=ft.Divider(color=ft.Colors.BLACK),
                ),
                message
            ]
        )
    )

    page.add(
        onesignal,
        container
    )


if __name__ == "__main__":
    ft.app(target=main)

```
