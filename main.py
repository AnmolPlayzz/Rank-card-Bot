import discord
from io import BytesIO
from PIL import Image, ImageFont, ImageDraw, ImageFilter
import requests
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.content=='!rank':
            def create_image(user, rank, level, exp, next_exp):
                W, H = (960,330)
                img = Image.open('frame.png', 'r')
                draw = ImageDraw.Draw(img)
                name=str(user)
                avatar=user.avatar_url_as(format='png', size=256)
                bar=int(((exp*100)//next_exp)*4.65)
                text="Rank: "+str(rank)+"  "+"Level: "+str(level)
                text2=str(exp)+"/"+str(next_exp)
                font1 = ImageFont.truetype('font\Roboto-Black.ttf', 24) #User Name font
                font2 = ImageFont.truetype('font\Roboto-Light.ttf', 17) #Rank Level font
                font3 = ImageFont.truetype('font\Roboto-Medium.ttf', 15) #Exp font
                def interpolate(f_co, t_co, interval):
                    det_co =[(t - f) / interval for f , t in zip(f_co, t_co)]
                    for i in range(interval):
                        yield [round(f + det * i) for f, det in zip(f_co, det_co)]
                gradient = Image.new('RGBA', img.size, color=0)
                draw1 = ImageDraw.Draw(gradient)
                f_co = (237, 28, 36)
                t_co = (243, 117, 71)
                for i, color in enumerate(interpolate(f_co, t_co, img.width*2)):
                    draw1.line([(i, 0), (0, i)], tuple(color), width=1)
                gradient=gradient.resize((bar,16), Image.Resampling.LANCZOS)
                def create_rounded_rectangle_mask(size, radius, alpha=255):
                    factor = 5 
                    radius = radius * factor
                    image = Image.new('RGBA', (size[0] * factor, size[1] * factor), (0, 0, 0, 0))
                    corner = Image.new('RGBA', (radius, radius), (0, 0, 0, 0))
                    draw = ImageDraw.Draw(corner)
                    draw.pieslice((0, 0, radius * 2, radius * 2), 180, 270, fill=(50, 50, 50, alpha + 55))
                    mx, my = (size[0] * factor, size[1] * factor)
                    image.paste(corner, (0, 0), corner)
                    image.paste(corner.rotate(90), (0, my - radius), corner.rotate(90))
                    image.paste(corner.rotate(180), (mx - radius, my - radius), corner.rotate(180))
                    image.paste(corner.rotate(270), (mx - radius, 0), corner.rotate(270))
                    draw = ImageDraw.Draw(image)
                    draw.rectangle([(radius, 0), (mx - radius, my)], fill=(50, 50, 50, alpha))
                    draw.rectangle([(0, radius), (mx, my - radius)], fill=(50, 50, 50, alpha))
                    image = image.resize(size, Image.Resampling.LANCZOS)
                    return image
                av=Image.open(BytesIO(requests.get(avatar).content)) 
                mask = create_rounded_rectangle_mask((bar,16), 8)
                mask1 = create_rounded_rectangle_mask((144,144), 75)
                av=av.resize((144,144), Image.Resampling.LANCZOS)
                img.paste(av,(408,44),mask=mask1)
                final_gr=Image.composite(gradient,create_rounded_rectangle_mask((bar, 16), 8, 255),mask)
                img.paste(final_gr, (247, 267), mask)
                w1 = draw.textbbox((0,0),name,font=font1)[2] #Width of User Name
                w2 = draw.textbbox((0,0),text,font=font2)[2] #Width of Rank
                w3 = draw.textbbox((0,0),text2,font=font3)[2] #Width of Exp
                draw.text(((W-w3)/2,267), text2, (255, 255, 255), font=font3,align="center")
                draw.text(((W-w1)/2,200), name, (255, 255, 255), font=font1,align="center")
                draw.text(((W-w2)/2,232), text, (255, 255, 255), font=font2,align="center")
                return img
            embed = discord.Embed(title="Rank for {0}".format(str(message.author)), description="", color=0x2f3136)
            with BytesIO() as image_binary:
                create_image(message.author, 1, 20, 200, 200).save(image_binary, 'PNG') #Main finction, format- user (as an object), user rank, level, exp (total xp required to level up THIS level minus xp currently required to level up), next_exp (total xp required to level up THIS level)
                image_binary.seek(0)
                embed.set_image(url='attachment://image.png')
                await message.channel.send(file=discord.File(fp=image_binary, filename='image.png'), embed=embed)
client = MyClient()
client.run('') #Add your token first owo