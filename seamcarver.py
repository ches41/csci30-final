#!/usr/bin/env python3

from picture import Picture

class SeamCarver(Picture):
    ## TO-DO: fill in the methods below
    def __init__(self, pixels):
        self.pixels = pixels
    def energy(self, i: int, j: int) -> float:
        '''
        Return the energy of pixel at column i and row j
        '''
        changeEX = self.changeEnergyX(i, j)
        changeEY = self.changeEnergyY(i, j)
        return changeEX + changeEY
        raise NotImplementedError
    
    def changeEnergyX(self, i, j):
        width = len(self.pixels[0])
        previousPixel = self.pixels[j][(i - 1) % width]
        nextPixel = self.pixels[j][(i + 1) % width]
        redX = abs(nextPixel[0] - previousPixel[0])
        greenX = abs(nextPixel[1] - previousPixel[1])
        blueX = abs(nextPixel[2] - previousPixel[2])
        return redX**2 + greenX**2 + blueX**2
    
    def changeEnergyY(self, i, j):
        width = len(self.pixels[0])
        previousPixel = self.pixels[j][(i - 1) % width]
        nextPixel = self.pixels[j][(i + 1) % width]
        redY = abs(nextPixel[0] - previousPixel[0])
        greenY = abs(nextPixel[1] - previousPixel[1])
        blueY = abs(nextPixel[2] - previousPixel[2])
        return redY**2 + greenY**2 + blueY**2
    
    def find_vertical_seam(self) -> list[int]:
        '''
        Return a sequence of indices representing the lowest-energy
        vertical seam
        '''
        raise NotImplementedError

    def find_horizontal_seam(self) -> list[int]:
        '''
        Return a sequence of indices representing the lowest-energy
        horizontal seam
        '''
        raise NotImplementedError

    def remove_vertical_seam(self, seam: list[int]):
        '''
        Remove a vertical seam from the picture
        '''
        raise NotImplementedError

    def remove_horizontal_seam(self, seam: list[int]):
        '''
        Remove a horizontal seam from the picture
        '''
        raise NotImplementedError

class SeamError(Exception):
    pass
