import matplotlib.font_manager
import matplotlib as mpl

mpl.font_manager._rebuild()
font_list = matplotlib.font_manager.findSystemFonts(fontpaths=None, fontext='ttf')
print([matplotlib.font_manager.FontProperties(fname=font).get_name() for font in font_list])