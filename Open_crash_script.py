def test():
    nuke.scriptClear()
    nuke.scriptOpen("")
    #nuke.message('hi')
    for i in nuke.allNodes():
        i.setSelected(True)
        nukescripts.toggle("disable")
        i.setSelected(False)


nuke.menu('Nuke').addMenu('Tharun').addCommand('openscript',test,'Shuffle.png')
