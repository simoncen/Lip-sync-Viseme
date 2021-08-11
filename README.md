# Lip-sync-Viseme
Text to speech program that output the Viseme Id for displaying the corresponding SVG.

For 2D characters, you can design a character that suits your scenario and use Scalable Vector Graphics (SVG) for each viseme ID to get a time-based face position. With temporal tags provided in viseme event, these well-designed SVGs will be processed with smoothing modifications, and provide robust animation to the users. For example, below illustration shows a red lip character designed for language learning.

For 3D characters, think of the characters as string puppets. The puppet master pulls the strings from one state to another and the laws of physics do the rest and drive the puppet to move fluidly. The viseme output acts as a puppet master to provide an action timeline. The animation engine defines the physical laws of action. By interpolating frames with easing algorithms, the engine can further generate high-quality animations.
