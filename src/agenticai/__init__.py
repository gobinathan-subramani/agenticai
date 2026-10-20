import os

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


def main() -> None:
    print("Hello from agenticai!")
    print(OPENAI_API_KEY)
    print(GOOGLE_API_KEY)


if __name__ == "__main__":
    main()
