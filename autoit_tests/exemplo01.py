import autoit
from time import sleep
from expects import *

autoit.run(filename="calc.exe")
autoit.win_wait_active(title="Calculadora")
autoit.send("3")
autoit.send("*")
autoit.send("5")
autoit.send("=")
sleep(2)
text = autoit.win_get_text("Calculadora")
print(text)

assert "15" in text
expect(text).to(contain("15"))
