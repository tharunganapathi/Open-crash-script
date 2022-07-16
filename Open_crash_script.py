def test():
    nuke.scriptOpen("")


nuke.menu('Nuke').addMenu('Tharun').addCommand('openscript',test,'Shuffle.png')
