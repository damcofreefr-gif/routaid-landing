import Jimp from 'jimp'

const logo = await Jimp.read('logostylrougeok.png')
logo.resize({ w: 440, h: 440 })

const favicon = new Jimp({ width: 512, height: 512, color: 0xffffffff })
favicon.composite(logo, 36, 36)

await favicon.write('favicon.png')
console.log('favicon.png créé (512x512 fond blanc)')
