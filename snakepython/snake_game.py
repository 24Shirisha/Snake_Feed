import pygame # type: ignore
import time
import random

pygame.init()

color_1 = (255,255,255) #white
color_2 = (255,255,102) #yellow
color_3 = (0,0,0) #black
color_4 = (213,200,80)
color_5 = (0,255,0) #green
color_6 = (255,0,0,) #red

box_len = 900
box_height = 600

add_caption  = pygame.display.set_mode((box_len, box_height))
pygame.display.set_caption("FEED SNAKE")

timer = pygame.time.Clock()

snake_block = 10
snake_speed = 15

display_style  = pygame.font.SysFont("arial", 30, "bold")
score_font = pygame.font.SysFont("arial", 45, "bold")

#setting a score while playing the game
def final_score(score):
    value = score_font.render("Enjoy the feeding snake ..... Score: " + str(score), True, color_2)
    add_caption.blit(value, [0, 0])

#making a sanke
def make_snake(snake_block, list_snake):
    for x in list_snake:
        pygame.draw.rect(add_caption, color_5, [x[0], x[1], snake_block, snake_block])
        
        
#meesage to be display at the end of a game
def display_msg(msg, color):
    mssg = display_style.render(msg, True, color)
    add_caption.blit(mssg, [box_len/6, box_height/3])

#main function to start a game
def game_start():
    game_over = False
    game_close = False
    
    value_x1 = box_len / 2
    value_y1 = box_height / 2
    
    new_x1 = 0
    new_y1 = 0
    
    list_snake = []
    snake_len = 1
    
#making variables to get food to the snake only inside the box of given length and height
    foodx_pos = round(random.randrange(0, box_len - snake_block) / 10.0) * 10.0
    foody_pos = round(random.randrange(0, box_height - snake_block) / 10.0) * 10.0
    
    while not game_over:
        while game_close:
            add_caption.fill(color_6)
            display_msg("You lost! You want to play again Press C or else press Q", color_4)
            final_score(snake_len - 1)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_start()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN: #controling keyboards keys to play the game
                if event.key == pygame.K_LEFT:
                    new_x1 = -snake_block
                    new_y1 = 0
                elif event.key == pygame.K_RIGHT:
                    new_x1 = snake_block
                    new_y1 = 0
                elif event.key == pygame.K_UP:
                    new_y1 = -snake_block
                    new_x1 = 0
                elif event.key == pygame.K_DOWN:
                    new_y1 = snake_block
                    new_x1 = 0
        
        if value_x1 >= box_len or value_x1 < 0 or value_y1 >= box_height or value_y1 < 0:
            game_close = True
    
        value_x1 = value_x1+new_x1
        value_y1 = value_y1+new_y1
        add_caption.fill(color_6)
        pygame.draw.rect(add_caption, color_3, [foodx_pos, foody_pos, snake_block, snake_block]) 
        snake_head = [value_x1, value_y1] #increasing size of snake
        list_snake.append(snake_head) 
        if len(list_snake) > snake_len:
            del list_snake[0]
    
        for x in list_snake[:-1]: #if snake not eaten any food
            if x == snake_head:
                game_close = True
        
        make_snake(snake_block, list_snake)
        final_score(snake_len - 1)
    
    
        pygame.display.update()
    
        if value_x1 == foodx_pos and value_y1 == foody_pos:
            foodx_pos = round(random.randrange(0, box_len - snake_block) / 10.0) * 10.0
            foody_pos = round(random.randrange(0, box_height - snake_block) / 10.0) * 10.0
            snake_len = snake_len+1
    
        timer.tick(snake_speed)
    pygame.quit()
    quit()

game_start()
        

                   
                
                
                       
            
            
    
    
      
    
