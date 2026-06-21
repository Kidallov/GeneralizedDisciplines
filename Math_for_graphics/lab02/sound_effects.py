import math
import random
from array import array

import pygame


class SoundEffects:
    """Small procedural sound pack with a silent fallback."""

    def __init__(self):
        self.enabled = pygame.mixer.get_init() is not None
        self.sounds = {}
        if self.enabled:
            try:
                self.sounds["shoot"] = self._tone(760, 0.07, 0.25)
                self.sounds["hit"] = self._noise(0.12, 0.28)
                self.sounds["life_lost"] = self._tone(260, 0.18, 0.32)
                self.sounds["bonus"] = self._tone(940, 0.11, 0.22)
                self.sounds["shield"] = self._tone(430, 0.18, 0.26)
                self.sounds["game_over"] = self._tone(170, 0.45, 0.35)
            except pygame.error:
                self.enabled = False
                self.sounds.clear()

    def play(self, name):
        if self.enabled and name in self.sounds:
            self.sounds[name].play()

    def _tone(self, frequency, duration, volume):
        sample_rate = 44100
        count = int(sample_rate * duration)
        samples = array("h")
        for i in range(count):
            envelope = 1 - (i / count)
            value = int(32767 * volume * envelope * math.sin(2 * math.pi * frequency * i / sample_rate))
            samples.append(value)
        return pygame.mixer.Sound(buffer=samples.tobytes())

    def _noise(self, duration, volume):
        sample_rate = 44100
        count = int(sample_rate * duration)
        samples = array("h")
        for i in range(count):
            envelope = 1 - (i / count)
            samples.append(int(32767 * volume * envelope * random.uniform(-1, 1)))
        return pygame.mixer.Sound(buffer=samples.tobytes())
