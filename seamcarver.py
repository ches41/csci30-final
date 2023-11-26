#!/usr/bin/env python3

from picture import Picture

class SeamCarver(Picture):
    ## TO-DO: fill in the methods below
    def energy(self, i: int, j: int) -> float:
        '''
        Return the energy of pixel at column i and row j
        '''
        raise NotImplementedError

    def find_vertical_seam(self) -> list[int]:
        '''
        Return a sequence of indices representing the lowest-energy
        vertical seam
        '''
        
        column = 0
        row = 0
        width = self.width()
        height = self.height()
        
        # used https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array
        
        total_energy = [([0] * width) for i in range(height)]
        prev = [([None] * width) for i in range(height)]

        # go through each row
        # store the total energy and previous pixel per pixel
        
        while (row < height):
            while (column < width):
                # in first row
                if (row == 0):
                    total_energy[0][column] = self.energy()
                # in first column
                elif (column == 0):
                    total_energy[row][column] = self.energy() + min(total_energy[row-1][column], total_energy[row-1][column+1])
                    prev[row][column] = total_energy[row-1].index(min(total_energy[row-1][column], total_energy[row-1][column+1]))
                # in last column
                elif (column == (width-1)):
                    total_energy[row][column] = self.energy() + min(total_energy[row-1][column-1], total_energy[row-1][column])
                    prev[row][column] = total_energy[row-1].index(min(total_energy[row-1][column-1], total_energy[row-1][column]))
                # everything else
                else:
                    total_energy[row][column] = self.energy() + min(total_energy[row-1][column-1], total_energy[row-1][column], total_energy[row-1][column+1])
                    prev[row][column] = total_energy[row-1].index(min(total_energy[row-1][column-1], total_energy[row-1][column], total_energy[row-1][column+1]))
                column += 1
            column = 0
            row += 1
            
        # find the minimum energy in the last row
        # backtrack through minimals using prev
        # create the vertical seam as you backtrack
        
        vertical_seam = []
        row = height-2 # start at the second to the last row
        
        vertical_seam.insert(0, total_energy[height-1].index(min(total_energy[height-1])))
        column = vertical_seam[0]
        
        while (row >= 0):
            vertical_seam.insert(0, prev[row][column])
            column = vertical_seam[0]
            row -= 1
            
        return vertical_seam

    def find_horizontal_seam(self) -> list[int]:
        '''
        Return a sequence of indices representing the lowest-energy
        horizontal seam
        '''
        
        # transpose the actual image
        
        original_image = {}
        transposed_image = {}
        
        og_width = self.width()
        og_height = self.height()
        new_width = self.height()
        new_height = self.width()
        
        # save old image
        
        column = 0
        row = 0
        
        while (row < og_height):
            while (column < og_width):
                original_image[row][column] = self[row, column]
                column += 1
            column = 0
            row += 1
            
        # create transposed image
            
        column = 0
        row = 0
            
        while (row < new_height):
            while (column < new_width):
                transposed_image[row][column] = self[(abs((og_width-1)-column)), row]
                column += 1
            column = 0
            row += 1
            
        self.clear()
        
        column = 0
        row = 0
                
        while (row < new_height):
            while (column < new_width):
                self[row, column] = transposed_image[row][column]
                column += 1
            column = 0
            row += 1
        
        # run vertical seam on transposed image
        
        horizontal_seam = self.find_vertical_seam()
        
        # convert values in horizontal seam
        
        pixel = 0
        
        while (pixel < (len(horizontal_seam)-1)):
            horizontal_seam[pixel] = abs((og_height-1)-horizontal_seam[pixel])
            pixel += 1
        
        # revert image to original
        
        self.clear()
        
        column = 0
        row = 0
                
        while (row < og_height):
            while (column < og_width):
                self[row, column] = original_image[row][column]
                column += 1
            column = 0
            row += 1
        
        return horizontal_seam

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
