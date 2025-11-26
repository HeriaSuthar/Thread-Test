from dotenv import load_dotenv
load_dotenv()

import asyncio
from bot_core.handlers import build_app
import os
import sys

def main():
    # quick startup checks for common missing envs
    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        print("ERROR: TELEGRAM_TOKEN is not set. Please set it in your .env or environment and retry.")
        sys.exit(1)

    if not os.getenv("MONGODB_URI"):
        print("WARNING: MONGODB_URI not set. Using default or local fallback.")

    app = build_app()
    print("Starting bot...")
    app.run_polling()


if __name__ == "__main__":
    main()