import autoit
from time import sleep
from expects import *

# Install AutoIt.
# pip install -U pyautoit
# pip install expects

# Run Application.
autoit.run(filename="notepad.exe")

title_app = "Sem título - Bloco de notas"
title_save = "Salvar como"
confirm = "Confirmar Salvar como"
new_file = "autoit exemplo.txt"
new_title = "autoit exemplo.txt - Bloco de notas"

# Wait open Application.
autoit.win_wait_active(title=title_app)

# # send commands for window active.
autoit.send("3")
autoit.send("*")
autoit.send("10")
autoit.send("=")
autoit.send("30")

sleep(2)
text = autoit.win_get_text(title=title_app)
print(text)

expect(text).to(contain("3*10=30"))

# open menu
autoit.send("!a")

sleep(2)
autoit.send("{DOWN 3}")
autoit.send("{ENTER}")

autoit.win_wait_active(title=title_save)
autoit.control_set_text(title=title_save,control="[CLASS:Edit; INSTANCE:1]", control_text=new_file)

autoit.control_click(title_save,"[CLASS:Button; INSTANCE:1]")
sleep(3)

try:
    autoit.control_focus(confirm, "[CLASS:Button; INSTANCE:1]")
    autoit.control_click(confirm, "[CLASS:Button; INSTANCE:1]")
except:
    print("Tela de confirmar não encontrada!")

sleep(3)
autoit.win_wait_active(title=new_title)
result = autoit.win_get_title(title=new_title)
result = autoit.win_activate
print(result)
expect(result).to(contain(new_title))
autoit.win_close(title=new_title)
