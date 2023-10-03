#  Example fi/le showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 480))

clock = pygame.time.Clock()
running = True
dt = 0
def get_font(size, bold=False):
    if bold:
        return pygame.font.Font("atkinson-bold.ttf", size)
    else:
        return pygame.font.Font("atkinson.ttf", size)

logo = pygame.transform.scale(pygame.image.load("librart.png"), (160, 160))

pygame.display.set_caption("Library Manager")
pygame.display.set_icon(logo)

class Button:
    def __init__(self, text, pos, size, w=280):
        self.text = text
        self.pos = pos
        self.size = size
        self.w = w
        self.button_font = get_font(size)
        self.button_text = self.button_font.render(text, True, "black")

    def draw(self):
        button_rect = self.button_text.get_rect(center=self.pos)
        self.rect = button_rect.inflate(self.w/2 - button_rect.w/2, 10)
        pygame.draw.rect(screen, "black", self.rect, 2,  border_radius=10)
        screen.blit(self.button_text, button_rect)


    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.button_text = self.button_font.render(self.text, True, "red")
        else:
            self.button_text = self.button_font.render(self.text, True, "black")
    

width = screen.get_width()
height = screen.get_height()

# player_pos = pygame.Vector2(
# screen.get_width() / 2, screen.get_height() / 2)


class Screen:
    pass

class HomeScreen(Screen):
    def __init__(self):
        super().__init__()
        self.admin = Button("Admin", (width/3, 350), 36)
        self.user = Button("User", (2*width/3, 350), 36)  
    
    def draw(self):
        font = get_font(64, True)
        text = font.render("Library Manager", True, "black")
        rect = text.get_rect(center=(width/2, 230))
        screen.blit(text, rect)

        image_rect = logo.get_rect(center=(width/2, 100))
        screen.blit(logo, image_rect)

        # buttons
        self.admin.draw()
        self.admin.update()

        self.user.draw()
        self.user.update()

class AdminScreen(Screen):
    def __init__(self):
        super().__init__()
        self.add = Button("Add Book", (width/3, 350), 36)
        self.remove = Button("Remove Book", (2*width/3, 350), 36)  
    
    def draw(self):
        font = get_font(36, True)
        text = font.render("Library Manager", True, "black")
        rect = text.get_rect(center=(width/2, 30))
        screen.blit(text, rect)

        screen.blit(pygame.transform.scale(logo, size=(40, 40)), (width/2 - 80, 50))

        # buttons
        self.add.draw()
        self.add.update()

        self.remove.draw()
        self.remove.update()

home = HomeScreen()
admin = AdminScreen()
screens = {
    "home": home,
    "admin": admin
}
curr_screen = screens["home"]

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")


    curr_screen.draw()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        running = False

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
