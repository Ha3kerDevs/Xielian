from setup_bot import StellaricBot

if __name__ == "__main__":
    bot_run = StellaricBot()
    bot_run.run()
    bot_run.load_extension('jishaku')