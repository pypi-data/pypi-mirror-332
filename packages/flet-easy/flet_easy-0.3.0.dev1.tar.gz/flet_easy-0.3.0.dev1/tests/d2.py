import flet as ft


def navigation_change(e: ft.ControlEvent):
    index = e.control.selected_index

    if index == 0:
        e.page.go("/")
    elif index == 1:
        e.page.go("/2")


t = ft.View(
    navigation_bar=ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME),
            ft.NavigationBarDestination(icon=ft.Icons.DASHBOARD),
        ],
        on_change=navigation_change,
    ),
    appbar=ft.AppBar(title=ft.Text("Test", size=50), bgcolor=ft.Colors.RED),
)


def main(page: ft.Page):
    page.title = "Test"
    page.theme = ft.Theme(
        page_transitions=ft.PageTransitionsTheme(
            android=ft.PageTransitionTheme.NONE,
            ios=ft.PageTransitionTheme.NONE,
            macos=ft.PageTransitionTheme.NONE,
            linux=ft.PageTransitionTheme.NONE,
            windows=ft.PageTransitionTheme.NONE,
        )
    )

    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()
        if e.route == "/":
            page.views.append(
                ft.View(
                    controls=[
                        ft.Text("Test World!"),
                    ],
                    appbar=t.appbar,
                    navigation_bar=t.navigation_bar,
                )
            )
        elif e.route == "/2":
            page.views.append(
                ft.View(
                    controls=[
                        ft.Text("Test-2 World!"),
                    ],
                    appbar=t.appbar,
                    navigation_bar=t.navigation_bar,
                )
            )

        page.update()

    page.on_route_change = route_change
    page.go("/")


if __name__ == "__main__":
    ft.app(target=main)
