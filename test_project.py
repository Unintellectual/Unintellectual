import pygame
import math


def test_isCollision():
    enx, eny, bulx, buly = 100, 100, 100, 100
    assert isCollisionP(enx, eny, bulx, buly) is True

    enx, eny, bulx, buly = 100, 100, 200, 200
    assert isCollision(enx, eny, bulx, buly) is False

def test_isCollisionP():
    enx, eny, playx, playy = 100, 100, 100, 100
    assert isCollisionP(enx, eny, playx, playy) is True

    enx, eny, playx, playy = 100, 100, 200, 200
    assert isCollisionP(enx, eny, playx, playy) is False

if __name__ == "__main__":
    from main import isCollision, isCollisionP

    test_isCollision()
    test_isCollisionP()
    print("All tests passed!")
