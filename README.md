<img src="https://cdn.discordapp.com/attachments/999631045462859846/1008644722618793985/image.png" align="center">
<h1 align="center" style="font-weight: bolder;">Rank Card Bot</h2>
<p align="center">A simple discord bot written in discord.py which ccepts arguments and runs a function to generate this rank card.</p>

<p align="center">Originally made for <a href="https://github.com/Bobby-McBobface/phnix-discord-bot">Bobby-McBobface/phnix-discord-bot</a>.</p>
<h1>Setup</h1>
<h2>The Basics</h2>
<p>Before you run the bot you need to first setup some varieables.</p>

|Name |Description|Type|
|-|-|-|
|`user`|A discord User |class|
|`level`|The current level of the user|integer|
|`rank`|Rank of user|integer|
|`exp`|The current xp of the user|integer|
|`next_exp`|The xp required to level up|integer|

_Some varieables have to be linked to a database_

<h2>Passing values to the functions</h2>

You should find a function named `create_image`

Pass the varieables in the order:

```py
create_image(user, rank, level, exp, next_exp)
```

<h2>Output</h2>
You should get the following output:
<img src="https://cdn.discordapp.com/attachments/999631045462859846/1009051097127735386/unknown.png">

---
Made with python and ♥ by @AnmolPlayzz