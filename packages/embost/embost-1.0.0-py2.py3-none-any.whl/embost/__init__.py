"""
Font embossing module
text = "Hello World!"
import embost
from embost import emboss
styled_text_bold = emboss.style(text, "bold")
styled_text_italic = emboss.style(text, "italic")
styled_text_bold_italic = emboss.style(text, "bold_italic")
styled_text_fraktur = emboss.style(text, "fraktur")
styled_text_script = emboss.style(text, "script")
styled_text_fancy = emboss.style(text, "fancy")

print("Bold:", styled_text_bold)
print("Italic:", styled_text_italic)
print("Bold Italic:", styled_text_bold_italic)
print("Fraktur:", styled_text_fraktur)
print("Script:", styled_text_script)
print("Fancy:", styled_text_fancy)
"""
__version__="1.0.0"
from .embost import emboss