import pygame

__author__ = 'uhs374h'
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pygame import *
from pygame.locals import *

from PIL import Image


class Figur:
	""" Erstellt eine Kugel in pygame mittels OpenGL

	:ivar float x: x coordinate
	:ivar float y: y coordinate
	:ivar float z: z coordinate
	:ivar float r: radius of the planet
	:ivar float c: increment or decrement for zooming and positioning
	:ivar bool done: game finished?
	:ivar bool paused: game paused?
	:ivar tuple display: size of the frame (x,y)
	"""
	def __init__(self):
		""" Initialisiert pygame

		"""
		self.x = 1.0
		self.y = 1.0
		self.z = 1.0
		self.c = 0.1
		self.r = 0.4
		self.done = False
		self.paused = False
		self.light = False
		pygame.init()
		self.w = 800
		self.h = 600
		self.display = (self.w, self.h)
		display.set_mode(self.display, DOUBLEBUF | OPENGL)
		display.set_caption("A simple solarsystem")
		# glShadeModel(GL_FLAT)
		glShadeModel(GL_SMOOTH)
		glClearColor(0.0, 0.0, 0.0, 0.0)
		glClearDepth(1.0)
		glEnable(GL_DEPTH_TEST)

		glMatrixMode(GL_PROJECTION)
		# glLoadIdentity()

		# glShadeModel(GL_SMOOTH)
		gluPerspective(60.0, (self.display[0] / self.display[1]), 0.5, 100)
		# moving back.
		glTranslatef(0, -0.5, -2.0)
		# where we might be
		glRotatef(1, 1, 1, 1)

		glMatrixMode(GL_MODELVIEW)

		self.spinMode = GL_TRUE
		self.singleStep = GL_FALSE

		# These three variables control the animation's state and speed.
		self.hourOfDay = 0.0
		self.dayOfYear = 0.0
		self.marsDayOfYear = 0.0

		self.animateIncrement = 12.0  # Time step for animation (hours)
		glutInit()
		# We could load a image for texuring
		# self.imageID = self.loadImage()

	def loop(self):
		""" The basic loop for presentation

		"""
		while True:
			# events abfragen
			self.input()
			if self.done:
				break
				# Clear the redering window
			glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

			if not self.paused:
				# Update the animation state
				self.hourOfDay += self.animateIncrement
				inc = self.animateIncrement / 24.0
				self.dayOfYear += inc
				self.marsDayOfYear += inc

				self.hourOfDay -= (self.hourOfDay // 24 * 24)
				self.dayOfYear -= (self.dayOfYear // 365 * 365)
				self.marsDayOfYear -= (self.marsDayOfYear // 450 * 450)

			# Clear the current matrix (Modelview)
			glLoadIdentity()
			# Disable lighting for a bright sun
			glDisable(GL_LIGHTING)
			# load a texture
			# self.setupTexture()
			#  Back off eight units to be able to view from the origin.
			glTranslatef(0.0, 0.0, -8.0)  # Rotate the plane of the elliptic
			# (rotate the model's plane about the x axis by fifteen degrees)
			glRotatef(15.0, 1.0, 0.0, 0.0)

			# Draw the sun	-- as a yellow,  wireframe sphere
			glColor3f(1.0, 1.0, 0.0)

			glutSolidSphere(1.0, 50, 50)

			if self.light:
				Figur.setupLighting()
				Figur.placeLight()
			else:
				Figur.lightOff()

			# Draw the Mars
			#  First position it around the sun
			# 	Use DayOfYear to determine its position
			glRotatef(360.0 * self.marsDayOfYear / 450, 0.0, 1.0, 0.0)
			glPushMatrix()  # Save matrix state
			glTranslatef(5.5, 0.0, 0.0)
			#  Second,  rotate the Mars on its axis.
			# Use HourOfDay to determine its rotation.
			glRotatef(360.0 * self.hourOfDay / 24.0, 0.0, 1.0, 0.0)
			# Third,  draw the Mars as a wireframe sphere.
			glColor3f(0.5, 0.0, 0.0)
			glutSolidSphere(0.25, 40, 40)
			glPopMatrix()  # Restore matrix state

			# Draw the Earth
			#  First position it around the sun
			# 	Use DayOfYear to determine its position
			glRotatef(360.0 * self.dayOfYear / 365.0, 0.0, 1.0, 0.0)
			glTranslatef(4.0, 0.0, 0.0)
			glPushMatrix()  # Save matrix state
			#  Second,  rotate the earth on its axis.
			# Use HourOfDay to determine its rotation.
			glRotatef(360.0 * self.hourOfDay / 24.0, 0.0, 1.0, 0.0)
			# Third,  draw the earth as a wireframe sphere.
			glColor3f(0.2, 0.2, 1.0)
			glutSolidSphere(0.4, 40, 40)
			glPopMatrix()  # Restore matrix state
			#  Draw the moon.
			# #	Use DayOfYear to control its rotation around the earth
			glRotatef(360.0 * 12.0 * self.dayOfYear / 365.0, 0.0, 1.0, 0.0)
			glTranslatef(0.5, 0.0, 0.0)
			glColor3f(0.3, 0.7, 0.3)
			glutSolidSphere(0.1, 20, 20)

			# Flush the pipeline
			glFlush()

			# pause the program for an amount of time [ms]
			pygame.time.wait(50)
			display.flip()

		# quit pygame and exit the application
		pygame.quit()

	@staticmethod
	def setupLighting():
		zeros = (0.15, 0.15, 0.15, 0.3)
		ones = (1.0, 1.0, 1.0, 0.3)
		half = (0.5, 0.5, 0.5, 0.5)

		glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, zeros)
		glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, half)
		glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 15)
		glLightfv(GL_LIGHT0, GL_AMBIENT, zeros)
		glLightfv(GL_LIGHT0, GL_DIFFUSE, ones)
		glLightfv(GL_LIGHT0, GL_SPECULAR, half)
		glEnable(GL_LIGHT0)
		glEnable(GL_LIGHTING)
		glColorMaterial(GL_FRONT_AND_BACK, GL_DIFFUSE)

		glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
		glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
		glEnable(GL_TEXTURE_GEN_S)
		glEnable(GL_TEXTURE_GEN_T)

		glEnable(GL_COLOR_MATERIAL)
		glEnable(GL_NORMALIZE)
		glShadeModel(GL_SMOOTH)

	@staticmethod
	def placeLight():
		# last value means point light
		position = (0.0, 0.0, 0.0, 1.0)
		glLightfv(GL_LIGHT0, GL_POSITION, position)

	@staticmethod
	def lightOff():
		glDisable(GL_LIGHTING)
		glDisable(GL_LIGHT0)
	"""
	def loadImage( self, imageName = "earth.bmp" ):
		# PIL defines an "open" method which is Image specific!
		im = Image.open(imageName)
		try:
			ix, iy, image = im.size[0], im.size[1], im.tostring("raw", "RGBA", 0, -1)
		except SystemError:
			ix, iy, image = im.size[0], im.size[1], im.tostring("raw", "RGBX", 0, -1)

		ID = glGenTextures(1)
		# Make our new texture ID the current 2D texture
		glBindTexture(GL_TEXTURE_2D, ID)
		glPixelStorei(GL_UNPACK_ALIGNMENT,1)
		# Copy the texture data into the current texture ID
		glTexImage2D( GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
		# Note that only the ID is returned, no reference to the image object
		# or the string data is stored in user space, the data is only present within the GL after this call exits.
		return ID

	def setupTexture(self):
		# Render-time texture environment setup
		# Configure the texture rendering parameters
		glEnable(GL_TEXTURE_2D)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
		glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
		# Re-select our texture, could use other generated textures if we had generated them earlier...
		glBindTexture(GL_TEXTURE_2D, self.imageID)
	"""

	def input(self):
		""" Reagiert auf Events von Keyboard und Maus

		"""
		ev = pygame.event.poll()
		if ev.type == QUIT:
			self.done = True
			return

		if ev.type == MOUSEBUTTONDOWN:
			if ev.button == 4:
				self.z += self.c
			elif ev.button == 5:
				self.z -= self.c
			elif ev.button == 3:
				self.light = not self.light
			elif ev.button == 1:
				self.paused = not self.paused

			return

		kpb = pygame.key.get_pressed()  # keyboard pressed buttons

		if kpb[K_ESCAPE]:
			self.done = True
		elif kpb[K_SPACE]:
			self.paused = not self.paused
		elif kpb[K_UP]:
			self.animateIncrement *= 1.1
		elif kpb[K_DOWN]:
			self.animateIncrement /= 1.1
		elif kpb[K_RIGHT]:
			self.x += self.c
		elif kpb[K_LEFT]:
			self.x -= self.c
		elif kpb[K_KP_PLUS]:  # vergrößern um 0.1%
			glScalef(1.001, 1.001, 1.001)
		elif kpb[K_KP_MINUS]:  # verkleinern auf 99,9%
			glScalef(0.999, 0.999, 0.999)

if __name__ == '__main__':
	s = Figur()
	s.loop()
