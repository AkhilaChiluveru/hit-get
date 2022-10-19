**List of features:**
1.Build a game where a person can hit an obstacle 
2.On every hit player can obtain score 
3.Apply sound effects to the game 
4.Allow Player and weapon selection
5.Add scoreboard to retain score history 

**MVP Definition:**
Our MVP is-> A player will be able to hit the series of target , which will be destroyed after the collision (Feature 1) 

**User stories : **
Feature 1: 

1.Create a blank screen 
    As a Developer, I will load a blank screen so that I can bring up background screen for the game 
    
2.Add a person 
    As a Developer, I will create a person object, so that a user can see a player on screen 
    
3.Add movement to the person 
    As a Developer, I will add movement to the person, so that player can move around the person on screen  
    
4.Shoot a bullet 
    As a Developer, I will create a bullet so that a player can shoot a bullet 
    
5.Create a target 
    As a Developer, I will create a target so that user can hit it with bullets 
    
6.Create a series of targets to Shoot 
    As a Developer, I will create a running series of targets so that a player can have back to back targets to hit 
    
7.Randomize the target size 
    As a Developer, I will randomize the target size so that the game difficulty will be improved 
    
8.Destroy the target on the strike 
    As a Developer, I will destroy the target on collision so that user will know if he has hit the target successfully or not  

Feature 2: 

1.Create a scoreboard 
    As a Developer, I will create a scoreboard so that user can see scoreboard 
    
2.On every strike update the score 
    As a Developer, I will update the score on collision so that user can see his/her score 
 

Feature 3: 

1.Apply Sound to bullet collision 
    As a Developer, I will add sound effects to bullet collision so that user can hear each successful strike 
    
2.Apply background music to game 
    As a Developer, I will add background music to improve the user experience 


Feature 4: 

1.Create a list of players 
    As a Developer, I will create a player list so that user can select a player as per his/her preference 
    
2.On selection, show new player in the game 
    As a Developer, I will allow the player selection so that user can have variety in game interface  
    
3.Create a list of weapons 
    As a Developer, I will create a weapon list so that user can select a weapon as per his/her preference
    
4.On selection, show new weapon in the game 
    As a Developer, I will allow the weapon selection so that user can have variety in game interface  
    
 

Feature 5: 

1.Create a scoreboard 
    As a Developer, I will create a blank scoreboard so that I can have a board to display the score 
    
2.Show the score history on the scoreboard (High to low) 
    As a Developer, I will maintain score history so that User can refer to the past scores 



**Overall structure your project:**
--hit-get
    --classes
        --background
        --player
        --weapon
        --strike
        --score
     --images
     --sound
    
