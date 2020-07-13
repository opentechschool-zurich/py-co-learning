# Sound in pygame

Pygame has to modules for playing sounds:

- `pygame.Sound` will play a specific sound to its end. You can load the sounds in a variable and play it as many times as you want (this is the right module for sounds that are played often in your game).
- `pygame.music` will load a specific sound and start playing it. You can load only one music at a time and each `play` command will restart the sound. You can pause or stop the music at any time (this is the right module for a background music).

In the demo code:

- Each time you press the `a` key, the cat meows. The sound is played to the end and there is no way to stop it.
- When you press `b` the marbles sound starts. Until the sound finished playing, pressing `b` again has no effect.
- Pressing `c` while the marbles sound is playing, will stop the sound.
- You can play cat sounds while the marbles are rolling.

## Notes

- While pygame.mixer.music can play a bit everything, pygame.mixer.Sound can only play ogg and wav files.
- [meow.ogg](http://soundbible.com/1684-Cat-Meowing-2.html) cc-by Mr Smith
- [marbles.ogg](http://soundbible.com/2199-Marbles.html) cc-by Daniel Simion
