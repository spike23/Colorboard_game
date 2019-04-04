# Colorboard game
***
*A simple matching game for children uses a board that is a sequence of
colored squares. Each player has a game piece. Players alternate turns,
drawing cards containing either one colored square or two colored squares of
the same color. Players move their pieces forward on the board to the next
square that matches the single color on the card, or forward to the second
matching square if the card contains two colored squares, or forward to the
last square on the board if there is no square matching the description above.
A player wins if his piece lands on the last square of the board. It is possible
for all the cards to be drawn and still not have a winner.
This problem represents colors with capital letters from A-Z. Below is a
diagram of a sample board.*
***
__Python version: 3.5__  
__Django: 2.2__
***
**Installation:**  
* ***clone project from git (git clone https://github.com/spike23/Colorboard_game.git)***
* ***open Colorboard_game directory*** 
* ***create virtual env and then activate your env***
* ***pip install -r requirements.txt***
* ***run migration command: python manage.py migrate***
* ***create superuser if you want to check/edit data in admin interface with command: python manage.py createsuperuser***
* ***load test data with command: python manage.py loaddata test_input.json***
* ***run application with command: python manage.py runserver***
* ***you can test app on localhost:8000 or 127.0.0.1:8000, just choose some case***
***