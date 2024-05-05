# this works ehe
from characterai import aiocai
import asyncio


async def msg_cont(text, chat_id,char_id):
    # to continue messaging in previous chat
    char = str(char_id)  # "RrIsYFdxuoD8lKOJfDZqDZ4yiBkV7gpOk0QGOeV0cPE"  # str(tokens["chat1"])
    client = aiocai.Client(tokens["client"])

    me = await client.get_me()

    async with await client.connect() as chat:
        message = await chat.send_message(char, chat_id, text)
        return message


async def msg_new(text):
    # to start a new chat
    # memory is lost
    char = str(tokens["chat1"])
    client = aiocai.Client(tokens["client"])

    me = await client.get_me()
    print(me)

    async with await client.connect() as chat:
        new, answer = await chat.new_chat(char, me.id)
        chat_token = new.chat_id
        message = await chat.send_message(char, new.chat_id, text)
        return message


async def main_text():
    # default copy paste shit
    char = str(tokens["chat1"])

    client = aiocai.Client(tokens["client"])

    me = await client.get_me()

    async with await client.connect() as chat:
        new, answer = await chat.new_chat(char, me.id)

        print(f"{answer.name}: {answer.text}")

        while True:
            text = input("YOU: ")

            message = await chat.send_message(char, new.chat_id, text)

            print(f"{message.name}: {message.text}")


def read_token():
    # to read chat tokens
    # to not expose it
    import pickle

    with open("tokens.dat", "rb") as f:
        tokens = pickle.load(f)
    return tokens

tokens = read_token()


if __name__ == "__main__":
    asyncio.run(main_text())

# print("ans", asyncio.run(msg_cont("hello man",chat_token)))
