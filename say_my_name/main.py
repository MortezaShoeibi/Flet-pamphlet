import flet  # import flet after installing.
from flet import Page, Text, TextField, Column, ElevatedButton

def main(page: Page):
    # page general settings.
    page.title = 'Say my name'
    page.vertical_alignment = 'start'

    # page controls.
    e_name = TextField(label="Say my name!", autofocus=True)
    my_name = Text(value="morteza shoeibi")
    correct_answer = Text(value="-you're God damn right!")
    incorrect_answer = Text(value="-No, you're God damn wrong! check my github profile!")
    line = Text(value='-------------------------')
    display_name = Column()

    # button.
    def button_clicked(e):
        # checks the entered value.
        if str(e_name.value).lower() == my_name.value:
            display_name.controls.append(Text(value="Morteza Shoeibi"))
            display_name.controls.append(Text(value=correct_answer.value))
        else:
            display_name.controls.append(Text(value=e_name.value))
            display_name.controls.append(Text(value=incorrect_answer.value))
        display_name.controls.append(line)
        e_name.value = '' # sets the e_name to an empty string.
        page.update()
        e_name.focus()

            
    # adds controls to the page.
    page.add(Column([
        e_name,
        ElevatedButton("Say my name!", on_click=button_clicked),
        display_name,
        ]))


flet.app(port=8000, target=main) # set 'view=flet.WEB_BROWSER' to run this program on a web page.
