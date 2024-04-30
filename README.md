# JT-Discord-Bot

Tutorial link: [How to Make a Discord Bot with Python](https://realpython.com/how-to-make-a-discord-bot-python/)

## Discord Sports Bot 

This Discord bot is designed to enhance server engagement by hosting trivia games and delivering sports news. The bot connects to a Discord server, engages members through trivia games, and tracks their scores. Additionally, the bot utilizes webhooks to fetch and relay sports news updates directly from Twitter, keeping your community informed of the latest sports events.

## Commands 
- `!starttrivia`: Initiates a trivia game in the designated trivia channel. The bot randomly selects five questions from the loaded trivia question pool and presents them one at a time to the participants.
- `!answer <response>`: Allows participants to submit their answers. The bot evaluates the response, updates the score accordingly, and proceeds to the next question.

## Setup Instructions

### Prerequisites
- Amazon Web Services (AWS)

### Installation

1. **Clone the repository:**

2. **Create Virtual Environment:**

    ```
    python3 -m venv .venv
    ```

3. **Activate Virtual Environment:**

    ```
    source .venv/bin/activate
    ```

4. **Install Requirements:**

    ```
    pip3 install -r requirements.txt

5. **Install Redis:**
    ```
    pip3 install redis


6. **Set up environment variables:**

    Create a `.env` file in the root directory of your project and add the following variables:

    ```
    DISCORD_TOKEN=your_discord_bot_token
    DISCORD_GUILD=your_guild_id
    WELCOME_CHANNEL_ID=your_welcome_channel_id
    ```

    Replace `your_discord_bot_token`, `your_guild_id`, and `your_welcome_channel_id` with the actual values.

7. **Running the Bot:**

    To run the bot, use the following command in the terminal:

    ```
    python bot.py
    ```

    Ensure that your .env file, trivia_questions.json, and webhook settings are correctly set up in your project directory.

## Deploying the Bot on AWS

To deploy your Discord bot on AWS, you can follow these steps:

1. **Set up an EC2 instance:**
   - Log in to your AWS Management Console.
   - Navigate to the EC2 service.
   - Launch a new EC2 instance with Amazon Linux or any other suitable operating system.
   - Make sure to configure security groups to allow inbound traffic on the necessary ports (e.g., port 80 for webhooks).

2. **Connect to your EC2 instance:**
   - Once your EC2 instance is running, connect to it using SSH.
   - You can use the following command: `ssh -i your-key.pem ec2-user@your-instance-ip`.

3. **Clone your bot repository:**
   - Use `git clone` to clone your bot repository onto the EC2 instance.

4. **Install dependencies:**
   - Navigate to the cloned repository directory.
   - Activate the virtual environment using `source .venv/bin/activate`.
   - Install the required Python packages using `pip install -r requirements.txt`.

5. **Set up environment variables:**
   - Create a `.env` file in the root directory of your project on the EC2 instance.
   - Add the required environment variables (`DISCORD_TOKEN`, `DISCORD_GUILD`, etc.) to this file.

6. **Run the bot:**
   - Ensure that your `.env` file, `trivia_questions.json`, and webhook settings are correctly configured.
   - Start your bot using `python bot.py`.

7. **Optional: Use systemd for process management:**
   - Create a systemd service file (e.g., `discordbot.service`) to manage the bot process.
   - Configure the service file to start your bot automatically on system boot and handle restarts.
   - Enable and start the service using `systemctl enable discordbot` and `systemctl start discordbot`.

8.**Other deployment features:**
   -You can run the bot when you have completed all the steps above by running sudo ./deploy_bot.sh .

9. **Access your bot:**
   - Once your bot is running, you can access it via Discord using the commands you've implemented.


