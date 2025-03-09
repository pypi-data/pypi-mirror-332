# bloyid.py

Python API wrapper for Bloyid originating from [Fiiral](https://github.com/F-iiral), maintained by [Deutscher775](https://github.com/Deutscher775)  
### **[Bloyid Server](https://web.bloyid.com/i/bloyid)** <br>
For questions, help, or anything else feel free to join the **[bloyid.py](https://web.bloyid.com/i/developer)** Bloyid server.

# Quick jumps
- **[Current Features](#current-features)** <br>
See the features that the framework currently supports.
- **[Installation](#installation)** <br>
Guide on how to install bloyid.py.
- **[Example Bot](#example-commands-bot)** <br>
An example bot you can directly use.
- **[Use-case-examples](#use-case-examples)** <br>
Many various examples on how to use specific functions.

# Current features
#### Command Handling:
- Define and register commands using the @client.command decorator.
- Execute commands with parameters.
Register event listeners using the @client.listen decorator.
Handle various events such as:
- on_ready
- on_message_create
- on_message_updated
- on_message_deleted
- on_button_clicked
- on_presence_change
- on_reaction_add
- on_member_updated
- on_role_updated
- on_role_deleted
- on_role_created
- on_channel_updated
- on_channel_deleted
- on_channel_created
- on_server_updated
- on_member_join
- on_member_left
- on_server_joined
- on_server_left
- on_friend_request_sent
- on_friend_request_pending
- on_friend_request_accepted
- on_friend_removed
- on_minute_pulse
- on_hour_pulse

#### Message Handling:
- Send messages to channels.
    - add attachments
    - add buttons with custom callback
- Edit and delete messages.
- React and unreact to messages.

#### Attachment Handling:
- Create and upload attachments.
- Deserialize attachments from JSON.

#### Channel Management:
- Update channel information.
- Send messages to channels.
- Get messages from channels.
- Purge messages from channels.
- Deserialize channels from JSON.

#### Context Handling:
- Send messages, remove messages, and react to messages within a command context.

#### Invite Management:
- Create and delete server invites.
- Deserialize invites from JSON.

#### Member Management:
- Follow, unfollow, add friend, remove friend, and send direct messages to members.
- Kick, ban, and unban server members.
- Deserialize members and server members from JSON.

#### Post Management:
- Create, delete, comment on, like, and unlike posts.
- Get comments on posts.
- Deserialize posts from JSON.

#### Role Management:
- Create, update, and delete roles.
- Deserialize roles from JSON.

#### Server Management:
- Get server details and ban list.
- Create, update, and delete channels and roles.
- Create and delete invites.
- Update server members.
- Deserialize servers from JSON.

#### Status Management:
- Change the presence status of the bot.

#### Button Interaction:
- Handle button interactions and send popups.
- Deserialize button interactions from JSON.

# Installation

To install `bloyid.py` via pip, run the following command:

```bash
pip install bloyid
```

### Manual Installation (Alternative)
If you'd prefer to install manually, follow these 2 simple steps:

1. Clone the repository
```bash
git clone https://github.com/ukyyyy/bloyid.py.git
```

2. Navigate into the project directory and install using `pip`:
```bash
cd bloyid.py
pip install .
```

### Done!

## Example commands bot
```python
import bloyid

client = bloyid.Client(
    token="YOUR_BOT_TOKEN",
    prefix='!',
)

@client.command(name="ping")
async def ping(ctx: bloyid.Context, params: str):
    await ctx.send("Pong!")

@client.listen("on_ready")
async def on_ready(params):
    print(f"Logged in as {client.account.username}")

client.run()
```

## Use case examples
### Sending an attachment
```python
@client.command(name="testattachment")
async def testattachment(ctx: bloyid.Context, params):
    file = await bloyid.Attachment.construct("test.png").upload()
    result = await ctx.send("Test", attachment=file)
```

### Sending buttons with messages
```python
@client.command(name="testbutton")
async def testbutton(ctx: bloyid.Context, params):
    popup_button = bloyid.Button.construct(label="Popup!", id="popuptestbutton", alert=True)
    async def popup_callback(buttoninteraction: bloyid.ButtonInteraction):
        user = client.get_user(buttoninteraction.userId)
        buttoninteraction.send_popup("Test", f"Hello, {user.username}!")
    await popup_button.set_callback(popup_callback)

    message_button = bloyid.Button.construct(label="Message!", id="messagetestbutton")
    async def message_callback(buttoninteraction: bloyid.ButtonInteraction):
        user = client.get_user(buttoninteraction.userId)
        await ctx.send(f"Hello, {user.username}!")
    await message_button.set_callback(message_callback)
    await ctx.send("Test", buttons=[message_button, popup_button])
```

### Creating a post
```python
@client.command(name="createpost")
async def createpost(ctx: bloyid.Context, params):
    content = ""
    for param in params:
        content += param + " "
    await ctx.send("Creating post with text: " + content)
    post = bloyid.Post.create_post(content)
    print(post)
    await ctx.send("Post created.")
```

### Commenting on a post
```python
@client.command(name="comment")
async def comment(ctx: bloyid.Context, params):
    post_id = int(params[0])
    content = ""
    for param in params[1:]:
        content += param + " "
    post = bloyid.Post.get_post(post_id)
    post.create_comment(content)
    await ctx.send("Commented on post.")
```

### Deleting a post
```python
@client.command(name="deletepost")
async def deletepost(ctx: bloyid.Context, params):
    post_id = int(params[0])
    post = bloyid.Post.get_post(post_id)
    post.delete_post()
    await ctx.send("Deleted post.")
```

## Issues
If you encounter any issues while using the framework, feel free to open an [Issue](https://github.com/ukyyyy/bloyid.py).

