import flet as ft
from flet import colors 
from deep_translator import GoogleTranslator as gt

lang=[
    {'lang':'en','idioma':'English'},
    {'lang':'fr','idioma':'French'},
    {'lang':'de','idioma':'German'},
    {'lang':'es','idioma':'Espanish'},
    {'lang':'pt','idioma':'Portuguese'},
    {'lang':'ru','idioma':'Russian'},
    {'lang':'it','idioma':'Italian'},
    {'lang':'zh-TW','idioma':'Chinese'},

    ]

def main(page:ft.Page):
    
 page.window_resizable=False
 page.window_width=500
 page.window_height=500
 
 
 drop=ft.Dropdown(
    label='Idiomas',
    options=[
     ft.dropdown.Option(lg['lang'],text=lg['idioma'])
     for lg in lang]
 )
 

 text=ft.TextField(label='Insira seu texto',multiline=True,max_lines=3,autocorrect=True,border_color=colors.BLACK)
 view=ft.Text(value='', size=20, weight=ft.FontWeight.W_500,selectable=True)
 
 def traduzir(e):
    traslator=gt(source='auto', target=drop.value)
    view.value=traslator.translate(text=text.value)
    view.update()

 btn=ft.ElevatedButton(text='Traduzir',on_click=traduzir, width=150,style=ft.ButtonStyle(padding=20,bgcolor=colors.BLACK,color=colors.WHITE))  
 
 title=ft.Row(
     alignment=ft.alignment.center,
     controls=[
      ft.Container(
        content=ft.Text(
                 value='Translator',
                 size=40,
                 weight=ft.FontWeight.W_600,
                 color=colors.WHITE,
                 
        ),
        width=500,
        bgcolor=colors.BLACK,
        border_radius=10,
        margin=0,
        padding=10
        
        ), ],
      width=500,
      spacing=3,
      
      
      
 )
 
 container=ft.Row(
     controls=[
         drop,
         btn
     ]
 )
 
 section=ft.Column(
     spacing=10,
     controls=[ 
         title,
         container,
         text,
         view
     ]
 )

 page.add(section)
   
    
ft.app(target=main)