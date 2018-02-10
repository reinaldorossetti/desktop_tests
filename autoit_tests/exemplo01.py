import autoit
from time import sleep
from expects import *

# Install AutoIt.
# pip install -U pyautoit

# Run Application.
autoit.run(filename="calc.exe")

# Wait open Application.
autoit.win_wait_active(title="Calculadora")

# send commands.
autoit.send("3")
autoit.send("*")
autoit.send("5")
autoit.send("=")
sleep(2)
text = autoit.win_get_text(title="Calculadora")
print(text)

assert "15" in text
expect(text).to(contain("15"))

# close window by send command Alt+F4.
autoit.send("!{F4}")
