from PIL import Image
import os

# Charger le logo
logo = Image.open('logostylrougeok.png').convert('RGBA')

# Créer fond blanc carré 512x512
favicon = Image.new('RGBA', (512, 512), (255, 255, 255, 255))

# Redimensionner le logo à 440x440 centré
logo = logo.resize((440, 440), Image.LANCZOS)

# Coller au centre
favicon.paste(logo, (36, 36), logo)

# Sauvegarder
favicon.save('favicon.png')
print("favicon.png créé")
