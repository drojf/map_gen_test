import random

PRINT_SPACING = ' '

class Arr:
	def __init__(self, xsize, ysize):
		self.xsize = xsize
		self.ysize = ysize
		self.occ = [0] * xsize * ysize

	def _index(self, x, y):
		return x + y * self.xsize

	def get(self, x, y):
		return self.occ[self._index(x, y)]

	def set(self, x, y, val):
		self.occ[self._index(x, y)] = val

	def print(self):
		print('\n> Occupancy:')
		for y in range(self.ysize):
			for x in range(self.xsize):
				print(self.get(x,y), end=PRINT_SPACING)
			print()

	def in_bounds(self, x, y):
		return x >= 0 and x < self.xsize and y >= 0 and y < self.ysize


	def draw_square(self, xstart, ystart, xsize, ysize, val):
		for y in range(ystart, ystart+ysize):
			for x in range(xstart, xstart + xsize):
				if self.in_bounds(x,y):
					self.set(x,y, val)

def getRandomPair(start, end):
	return random.randrange(start, end), random.randrange(start, end)


m = Arr(30, 30)
m.print()

# set random points to spawn rooms
room_centers = [getRandomPair(0, 30) for x in range(10)]

for x, y in room_centers:
	m.draw_square(x,y,4,4,1)
	m.set(x,y, 2)

print(room_centers)

m.print()