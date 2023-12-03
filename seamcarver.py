#!/usr/bin/env python3

from picture import Picture


class SeamCarver(Picture):
    ## TO-DO: fill in the methods below
    def energy(self, i: int, j: int) -> float:
        """
        Return the energy of pixel at column i and row j
        """
        raise NotImplementedError

    def find_vertical_seam(self) -> list[int]:
        """
        Return a sequence of indices representing the lowest-energy
        vertical seam
        """
        raise NotImplementedError

    def find_horizontal_seam(self) -> list[int]:
        """
        Return a sequence of indices representing the lowest-energy
        horizontal seam
        """
        raise NotImplementedError

    def remove_vertical_seam(self, seam: list[int]):
        """
        Remove a vertical seam from the picture
        """
        if self.width() == 1:
            raise SeamError
        if len(seam) != self.height():
            raise SeamError
        for i in range(len(seam) - 1):
            if abs(seam[i] - seam[i + 1]) > 1:
                raise SeamError

        for row in range(len(seam)):
            for column in range(seam[row], self.width() - 1):
                self[column, row] = self[column + 1, row]
            del self[self._width - 1, row]

        self._width -= 1

    def remove_horizontal_seam(self, seam: list[int]):
        """
        Remove a horizontal seam from the picture
        """
        # transpose the actual image

        original_image = {}
        transposed_image = {}
        new_seam = []

        og_width = self.width()
        og_height = self.height()
        new_width = self.height()
        new_height = self.width()

        # save old image

        column = 0
        row = 0

        while row < og_height:
            while column < og_width:
                original_image[row][column] = self[row, column]
                column += 1
            column = 0
            row += 1

        # create transposed image

        column = 0
        row = 0

        while row < new_height:
            while column < new_width:
                transposed_image[row][column] = self[
                    (abs((og_width - 1) - column)), row
                ]
                column += 1
            column = 0
            row += 1

        self.clear()

        column = 0
        row = 0

        while row < new_height:
            while column < new_width:
                self[row, column] = transposed_image[row][column]
                column += 1
            column = 0
            row += 1

        # convert values in horizontal seam

        pixel = 0

        while pixel < (len(seam) - 1):
            new_seam[pixel] = abs((og_height - 1) - seam[pixel])
            pixel += 1

        self.remove_vertical_seam(new_seam)

        # revert image to original

        self.clear()

        column = 0
        row = 0

        while row < og_height:
            while column < og_width:
                self[row, column] = original_image[row][column]
                column += 1
            column = 0
            row += 1


class SeamError(Exception):
    pass
