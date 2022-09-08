import flet
from flet import AppBar, ElevatedButton, Row, Page, Text, View, colors

def main(page: Page):
    # page general settings
    page.title = "Morteza Shoeibi"
    page.scroll = "always"
    

    def route_change(route):
        page.views.clear()
        page.views.append(
            # shows this content in the home page.
            View(
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=colors.SURFACE_VARIANT),
                    Row(
                        [
                            Text("This is the home page of my flet based web app.\n click these buttons to see the other pages!", size=20),
                        ],
                    ),
                    Row(
                        [
                            ElevatedButton("AboutMe", on_click=lambda _: page.go("/about-me")),
                            ElevatedButton("ContactMe", on_click=lambda _: page.go("/contact-me")),
                        ],
                    )
                ],
            )
        )
        # checks the url to show the content of about me page.
        if page.route == "/about-me":
            page.views.append(
                View(
                    "/about-me",
                    [
                        AppBar(title=Text("About ME"), bgcolor=colors.SURFACE_VARIANT),
                        Row(
                            [
                                Text("""
                                according to my LinkedIn page:\n
                                I'm a Pythonic minded Python programmer with a high level of understanding JavaScript programming language,
                                familiar with HTML and CSS markup languages, proficient in Git and working with it professionally,
                                proficient in regex and how to work with it professionally, proficient in Vim editor(I can actually exit it),
                                proficient in networking concepts and principles, proficient in GNU/Linux operating system and its tools,
                                fluent in English Arabic and Persian languages and have experienced team and individual work.
                                """, size=20)
                            ],
                            alignment="center",
                        ),
                        Row(
                            [
                                ElevatedButton("Home", on_click=lambda _: page.go("/")),
                            ],
                            alignment="center",
                        ),
                    ],
                )
            )
        # checks the url to show the content of contact me page.
        elif page.route == "/contact-me":
            page.views.append(
                View(
                    "/contact-me",
                    [
                        AppBar(title=Text("Contact Me"), bgcolor=colors.SURFACE_VARIANT),
                        Row(
                            [
                                Text("Email me:\nmortezashoeibi77@gamil.com", size=20),
                            ],
                            alignment="center",
                        ),
                        Row(
                            [
                                ElevatedButton("Home", on_click=lambda _: page.go("/")),
                            ],
                            alignment="center"
                        ),
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    # page route setup
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


flet.app(port=800, target=main, view=flet.WEB_BROWSER)
