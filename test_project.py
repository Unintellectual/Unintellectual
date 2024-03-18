from unittest.mock import patch
from project import show_score, player, enemy

@patch('pygame.font.Font.render')
@patch('pygame.Surface.blit')
def test_show_score(mock_blit, mock_render):
    x, y = 10, 10
    score_value = 10
    show_score(x, y)
    mock_render.assert_called_once_with("Score : 10", True, (255, 255, 255))
    mock_blit.assert_called_once()

@patch('pygame.Surface.blit')
def test_player(mock_blit):
    x, y = 100, 100
    player(x, y)
    mock_blit.assert_called_once()

@patch('pygame.Surface.blit')
def test_enemy(mock_blit):
    x, y, b = 200, 200, 0
    enemy(x, y, b)
    mock_blit.assert_called_once()
