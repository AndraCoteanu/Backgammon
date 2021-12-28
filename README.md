# Backgammon
___________________________________________________________________________
## @author: Coteanu Andra, 3A4
### python game project made for Python Programming class at FII, UAIC
___________________________________________________________________________

In the main menu, the user can choose to see the instructions or start a game either with the pc, or with a friend besides him.

The first approach I took was using pygame, but that didn't work out because of the workarounds needed for buttons so I took another shoot and now the GUI is made using tkinter.

- the instructions button will open up a wikipedia web bage with the game rules
- other options will start a game either player vs player or player vs pc

For the actual game, the scene will look something like this:
![map](https://user-images.githubusercontent.com/72747266/144769219-ba2386c4-35f1-4df6-92fd-d3400786b39d.png)

The ideal dimmensions for the pieces should be 60x60 so they would fit like on a real life backgammon board.

After more testing of the GUI I changed the dimmensions. After starting a game this is how the board will look like:
![image](https://user-images.githubusercontent.com/72747266/145659357-552457b7-9d3d-4f7e-af25-f0a4bb21481f.png)

- on the left and right side of the screen we can see each player's statistics: name, color, how many pieces the other player took out and how many pieces he mananged to take out so far
- the pieces colors are randomized at the start of the game
- on the screen is the actuall board with the pieces
- in the center of the board, on the left side is the "roll" button, to roll the dice and on the right side we can see what we rolled
- unfortunatelly, tkinter doesn't understand transparent background for labels and buttons (but at least it helps to see the pieces more clearer)



![image](https://user-images.githubusercontent.com/72747266/147503518-69ba33c4-cdeb-41f3-b4fc-5d399772eed8.png)


Player vs Player flow:

![image](https://user-images.githubusercontent.com/72747266/147604365-b6ca44a9-3362-498a-8ab0-06bbe3fa531c.png)

![image](https://user-images.githubusercontent.com/72747266/147604416-1cc5aa83-de77-49ab-b6b1-7c381e6dc09b.png)

![image](https://user-images.githubusercontent.com/72747266/147604454-669b9ce5-a390-43ae-a527-3cdd7b652822.png)

![image](https://user-images.githubusercontent.com/72747266/147604492-2f3208bf-c664-472c-a707-fa13b9c6114c.png)



Tipuri de avertizari pentru jucatori:

![image](https://user-images.githubusercontent.com/72747266/147604446-c30ccf6f-ad79-4f97-893a-281cf19e26b9.png)

![image](https://user-images.githubusercontent.com/72747266/147604466-ed0dd08a-6960-4d5b-a64c-3c935bc7c01a.png)

![image](https://user-images.githubusercontent.com/72747266/147604570-92ed3662-913f-4575-9727-e279cd71a1c3.png)




Disclaimer: all UI/UX used was found in a form or another on the internet and I altered and edited it based on my and the project needs.
