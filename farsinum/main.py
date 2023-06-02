import flet
from flet import Page, Text, TextField, Row, Column, ElevatedButton
import requests


def main(page: Page):
    page.title = 'Farsinum app'
    page.vertical_alignment = 'start'
    page.scroll = 'always'


    number_entry = TextField(label="Enter the a number", autofocus=True)
    display_text = Column()


    def process(e):
        number = number_entry.value
        response = requests.get(f"https://farsinum.ir/api/converter?number={number}")
        data = response.json()
        
        if data['status'] != 200:
            display_text.controls.append(
            Text(
                    value=f"{data['description']}",
                    size=20, 
                    color="white", 
                    bgcolor="pink", 
                    weight="bold"
                )
            )
        else:
            display_text.controls.append(
                Text(
                        value=f"{data['text']}", 
                        size=20, 
                        color="white", 
                        bgcolor="green", 
                        weight="bold"
                    )
                )

        
        number_entry.value = '' 
        page.update()
        number_entry.focus()

    page.add(
        Row(
            [
                number_entry,
                ElevatedButton("Get in Farsi!", on_click=process),
            ],
            
            alignment="center",
        ),

        Column(
            [
                display_text
            ],
            alignment="center",
            ))


flet.app(port=5432, target=main)
