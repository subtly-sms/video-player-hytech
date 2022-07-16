from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.videoplayer import VideoPlayer


# Video Selector
# - must only accept mp4 and...
# - must gracefully error out if no selection
# - see if you can open native file selection
# Pause on space bar
# IS THERE A WAY TO HAVE TO VIDEO PLAYERS in sync?
# Seek and pause must also be in sync

# Optional
# Loop selector (?)
# Thumbnail creation (?)
# Thumbnail display (?)
# A recent video list
# Package app
# Check kivy options

class MainApp(MDApp):
    title = "HyTech Video Player"

    def select_video(self):
        source = "videos/Gx020796.mkv"
        return source

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        #source = select_video()

        source = "videos/Gx020796.mkv"
        # Create VideoPlayer
        player = VideoPlayer(source = source)
    
        # Assign VideoPlayer State
        #player.state = 'play'

        # Set options
        #player.options = {'eos': 'loop'}

        # Allow stretch
        player.allow_stretch = True

        # Return player
        return player

    def build1(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        #source = select_video()

        source = "videos/Gx020796.mkv"
        # Create VideoPlayer
        player1 = VideoPlayer(source = source)
    
        # Assign VideoPlayer State
        #player.state = 'play'

        # Set options
        #player.options = {'eos': 'loop'}

        # Allow stretch
        player1.allow_stretch = True

        # Return player
        return player1        


MainApp().run()