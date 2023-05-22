from Data.GAME_VIEW.OBJECT.view import init_view
from Data.GAME_VIEW.OBJECT.button import Button
from Data.GAME_VIEW.OBJECT.text import Text
from Data.GAME_VIEW.util import *
import os

init_pygame()
check_config(config)
print('process id', os.getpid())

if bool(config['system']['COLOR_WEAKNESS_MODE']):
    color_weakness_value = True
else:
    color_weakness_value = False


# 메인 루프
def main_screen():
    SCREEN_WIDTH = int(config['system']['SCREEN_WIDTH'])
    SCREEN_HEIGHT = int(config['system']['SCREEN_HEIGHT'])

    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    BUTTON_WIDTH = (220 * SCREEN_WIDTH) / 1280
    BUTTON_HEIGHT = (50 * SCREEN_WIDTH) / 1280

    center_x = SCREEN_WIDTH / 2 - BUTTON_WIDTH / 2
    center_y = SCREEN_HEIGHT / 2 - BUTTON_HEIGHT / 2

    flag = 0
    
    init_bg(SCREEN, SCREEN_PATH + "start_screen.jpeg", SCREEN_WIDTH, SCREEN_HEIGHT)

    play_button = Button(image=pygame.image.load(BUTTON_PATH + "play_button.png"),
                         pos=(center_x, center_y + set_size(200, SCREEN_WIDTH)),
                         size=(BUTTON_WIDTH, BUTTON_HEIGHT))

    options_button = Button(image=pygame.image.load(BUTTON_PATH + "options_button.png"),
                            pos=(center_x, center_y + set_size(260, SCREEN_WIDTH)),
                            size=(BUTTON_WIDTH, BUTTON_HEIGHT))

    exit_button = Button(image=pygame.image.load(BUTTON_PATH + "exit_button.png"),
                         pos=(center_x, center_y + set_size(320, SCREEN_WIDTH)),
                         size=(BUTTON_WIDTH, BUTTON_HEIGHT))

    achievements_button = Button(image=pygame.image.load(BUTTON_PATH + "achievement_button.png"),
                                 pos=(set_size(30, SCREEN_WIDTH), set_size(30, SCREEN_WIDTH)),
                                 size=(set_size(50, SCREEN_WIDTH), set_size(50, SCREEN_WIDTH)))

    title_text = Text(text_input="UNO GAME",
                      font=FONT_PATH,
                      color=(0, 0, 0),
                      pos=(SCREEN.get_rect().centerx, SCREEN.get_rect().top + 30),
                      size=set_size(70, SCREEN_WIDTH),
                      screen=SCREEN)
    while True:
        init_view(SCREEN, [play_button, options_button, exit_button, achievements_button])
        title_text.init_text()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.rect.collidepoint(event.pos):
                    CLICK_SOUND.play(0)
                    from Data.GAME_VIEW.SCREEN.game_mode import select_game_mode
                    select_game_mode(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT + 5)
                elif options_button.rect.collidepoint(event.pos):
                    CLICK_SOUND.play(0)
                    from Data.GAME_VIEW.SCREEN.option import options
                    options(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
                elif exit_button.rect.collidepoint(event.pos):
                    CLICK_SOUND.play(0)
                    quit()
                elif achievements_button.rect.collidepoint(event.pos):
                    CLICK_SOUND.play(0)
                    from Data.GAME_VIEW.SCREEN.achievement import achievement_screen
                    achievement_screen(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if flag > 1:
                        flag = flag - 1
                elif event.key == pygame.K_DOWN:
                    if flag < 4 :
                        flag = flag + 1
                elif event.key == pygame.K_RETURN:
                    if flag == 1:
                        CLICK_SOUND.play(0)
                        from Data.GAME_VIEW.SCREEN.achievement import achievement_screen
                        achievement_screen(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
                    elif flag == 2 :
                        CLICK_SOUND.play(0)
                        from Data.GAME_VIEW.SCREEN.game_mode import select_game_mode
                        select_game_mode(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT + 5)
                    elif flag == 3 :
                        CLICK_SOUND.play(0)
                        from Data.GAME_VIEW.SCREEN.option import options
                        options(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
                    elif flag == 4:
                        CLICK_SOUND.play(0)
                        quit()
        mouse_pos = pygame.mouse.get_pos()
        
        if achievements_button.rect.collidepoint(mouse_pos) or flag == 1:
            achievements_button.image = pygame.image.load(BUTTON_PATH + "selected_achievement_button.png")
            play_button.image = pygame.image.load(BUTTON_PATH + "play_button.png")
            options_button.image = pygame.image.load(BUTTON_PATH + "options_button.png")
            exit_button.image = pygame.image.load(BUTTON_PATH + "exit_button.png")
        elif play_button.rect.collidepoint(mouse_pos) or flag == 2: 
            achievements_button.image = pygame.image.load(BUTTON_PATH + "achievement_button.png")
            play_button.image = pygame.image.load(BUTTON_PATH + "selected_play_button.png")
            options_button.image = pygame.image.load(BUTTON_PATH + "options_button.png")
            exit_button.image = pygame.image.load(BUTTON_PATH + "exit_button.png")
        elif options_button.rect.collidepoint(mouse_pos) or flag == 3:
            achievements_button.image = pygame.image.load(BUTTON_PATH + "achievement_button.png")
            play_button.image = pygame.image.load(BUTTON_PATH + "play_button.png")
            options_button.image = pygame.image.load(BUTTON_PATH + "selected_options_button.png")
            exit_button.image = pygame.image.load(BUTTON_PATH + "exit_button.png")
        elif exit_button.rect.collidepoint(mouse_pos) or flag == 4:
            achievements_button.image = pygame.image.load(BUTTON_PATH + "achievement_button.png")
            play_button.image = pygame.image.load(BUTTON_PATH + "play_button.png")
            options_button.image = pygame.image.load(BUTTON_PATH + "options_button.png")
            exit_button.image = pygame.image.load(BUTTON_PATH + "selected_exit_button.png")
        else:
            achievements_button.image = pygame.image.load(BUTTON_PATH + "achievement_button.png")
            play_button.image = pygame.image.load(BUTTON_PATH + "play_button.png")
            options_button.image = pygame.image.load(BUTTON_PATH + "options_button.png")
            exit_button.image = pygame.image.load(BUTTON_PATH + "exit_button.png")
        
        pygame.display.update()


MAIN_BGM.set_volume(0.7)
MAIN_BGM.play(-1)
main_screen()
