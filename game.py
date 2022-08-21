import sys
import pygame

from time import sleep
import pygame.font


class Button:
    def __init__(self, screen, msg):
        """Inicjalizajca początkowych wartości """
        # Zaciągnięcie obiektu scren
        self.screen = screen
        # Utworzenie prostokąta obiektu
        self.screen_rect = self.screen.get_rect()
        # Nadanie wartości wysokości szerokości kolorów przycisku
        self.wight, self.height = 200, 50
        self.text_color = (255, 255, 255)
        self.bg_color = (0, 0, 255)
        # Nadanie stylu i rozmiaru czcionki
        self.font = pygame.font.SysFont(None, 48)
        # Utworzenie prostokąta przycisku
        self.rect = pygame.Rect(0, 0, self.wight, self.height)
        # Ustawienie środka przycisku na środku ekranu
        self.rect.center = self.screen_rect.center
        # Przygotowanie wiadomości
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """ Umieszczenie komunikatu w wygenerowanym obrazie i wyśrodkowanie komunikatu na przycisku"""
        # Utworzenie obrazu komunikatu
        self.msg_image = self.font.render(msg, True, self.text_color, self.bg_color)
        # Utworzenie obiektu prostokąta obrazu komunikatu
        self.msg_image_rect = self.msg_image.get_rect()
        # Umieszczenie komunikatu w środku przycisku
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """ Wyświetlenie pustego przycisku, a następnie komunikat na nim  """
        self.screen.fill(self.bg_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)




class Settings:
    """ Klasa ustawień podsrtawowych"""
    def __init__(self):
        # Nadaje wartości szerokości wysokości i koloru tła
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (233, 233, 233)
        # A dam se tutaj szerokości, wysokość, szybkość pocisku jak bym miał coś zmienić
        self.bullet_width = 30
        self.bullet_height = 30
        self. bullet_speed = 1
        # Ustawienia wroga
        self.enemy_wight = 30
        self.enemy_height = 30
        self.enemy_color = (0, 0, 255)
        self.enemy_speed_factor = 2
        # Czy gra jest aktywna
        self.game_active = False
        # Ile mamy szns
        self.lives = 1








def check_events():
    """ Sprawdza zdażenia generowane przez klawiature i mysz"""
    for event in pygame.event.get():
        # jeżeli wystąpi naciśnięcie krzyżyka zamykam
        if event.type == pygame.QUIT:
            sys.exit()
        # sprawdza reakcje na wciśnięcie przycisku
        elif event.type == pygame.KEYDOWN:
            reset_time_one()
        # reakcja na zwolnienie gusika
        elif event.type == pygame.KEYUP:
            reset_time_one()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            reset_time_one()






def run_game():
    # Inicjalizuje pygame
    pygame.init()
    # Tworze obiekt klasy ustawień
    ai_settings = Settings()
    # Tworze okno gry
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # Nadaje nagłówek gry
    pygame.display.set_caption("ECP")

    # Utworzenie przycisku
    play_button = Button(screen, "GRA")


# Rozpoczęcie głównej pętli zdażeń
    while True:
        # Oczekuje na zdażenie nadawane przez klawiature i mysz
        check_events(ai_settings, screen, play_button,)
        if ai_settings.lives <= 0:
            ai_settings.game_active = False
        if not ai_settings.game_active:
            continue


        if ai_settings.game_active:
            continue


        # Wypełnienie ekranu
        screen.fill(ai_settings.bg_colour)

        # Jeżeli wykożystałeś życia wyświetla się przycisk gra i czeka na reakcje
        if not ai_settings.game_active:
            play_button.draw_button()
        # Odświerzanie ekranu
        pygame.display.flip()





# Włączenie zdefiniowanej  gry
run_game()
