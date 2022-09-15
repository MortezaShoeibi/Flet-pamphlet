import flet
from flet import Page, Text, TextField, Row, Column, ElevatedButton
import requests


def main(page: Page):
    # page general settings
    page.title = 'Crypto price'
    page.vertical_alignment = 'start'
    page.scroll = 'always'

    # page controls.
    symbol = TextField(label="Enter the crypto symbol!", autofocus=True)
    display_price = Column()

    # checks the entered value.
    def check_status(response):

        match response.status_code:
            case 200:
                data = response.json()
                display_price.controls.append(Text(value=f"The {data['symbol']} price is {data['price']}", size=30, color="white", bgcolor="green", weight="bold"))
            case 403:
                display_price.controls.append(Text(value=f"Turn on your VPN", size=30, color="white", bgcolor="pink"))
            case _:
                display_price.controls.append(Text(value=f"Couldn't find anything, are you sure about this '{symbol.value}' symbol?", size=30, color="white", bgcolor="pink"))

    # button.
    def button_clicked(e):
        # upper casing the symbol.value
        symbol.value = str(symbol.value).upper()
        response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={symbol.value}")

        # sends the response variable to be validated.
        check_status(response)

        # sets the symbol value to an empty string.
        symbol.value = '' 
        page.update()
        symbol.focus()

    # adds controls to the page.
    page.add(
        Row(
            [
                symbol,
                ElevatedButton("check price!", on_click=button_clicked),
            ],
            
            alignment="center",
        ),

        Column(
            [
                display_price
            ],
            alignment="center",
            ))


flet.app(port=8000, target=main)
