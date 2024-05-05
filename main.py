import Char_text as ct
import asyncio
import stt
import tts_

# the id of the chat
chat_token = "5c1d205f-3be0-4ddb-b672-20f386d16014"

# the id of the character
char_id = "RAj3vm_xQVvcApJ4BFosLkOQ8O6osGz5E-K5dn9l2xE"  # bocchi
# jeC02ArWFsboN8OyW16Q734QTnnWza_wwQl7gu_Wy0o # frieren


def output_text(text, ans):
    print(str(text))
    print(f"{ans.name}: {ans.text}")

    f = open("op.txt", "a")
    f.write("you: " + str(text) + "\n")
    f.write(f"{ans.name}: " + str(ans.text) + "\n")
    f.close()


while True:
    text = stt.speech_rec()
    ans = asyncio.run(ct.msg_cont(text, chat_token, char_id))
    output_text(text, ans)
    tts_.output_tts(str(ans.text))
