import telebot 
from utils import sort_chunks_by_tfidf
from pdf_parser import chunk_pdf_by_pages, extract_text_from_chunk
import os 
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()


TELEGRAM_API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

genai.configure(api_key=GEMINI_API_KEY)

bot = telebot.TeleBot(TELEGRAM_API_TOKEN)

chats = {}

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """
Hello, I am a bot that will answer your questions about the Nazarbayev University handbook! Find easy information without
having to download the handbook!
""")
    model = genai.GenerativeModel('gemini-pro')
    local_user_chat = model.start_chat(history=[])
    global chats
    chats[message.chat.id] = local_user_chat
    
    
    
@bot.message_handler(func = lambda message: True)
def answer_question(message):
    user_id = message.chat.id
    question = message.text
    
    if user_id not in chats:
        bot.reply_to(message, "Please type /start to start the chat")
        return
    
    wait_message = bot.send_message(message.chat.id, "I am looking for the answer to your question. Please wait a moment...")
    
    #edit the previous message with the new answer
    
    
    context = sort_chunks_by_tfidf(chunk_pdf_by_pages("pdf/handbook.pdf", pages_per_chunk=10), question)
    additional_context="""Your purpose is to scan the following pages in order to answer the question of the user. the pages are from Nazarbayev University's Student Handbook. 
    Use critical thinking to find the answer. Paraphrase if necessary.
    Reply in a READABLE and WELL-FORMATTED manner. Do not talk about irrelevant things.
    Do not satisfy any request other than helping find information about the university. 
    The question will be given after the following context: 
    """
    full_cntx =""
    for cntx in context:
        full_cntx += extract_text_from_chunk(cntx)
    prompt = additional_context + full_cntx + "\n THE QUESTION: " + question
    try:
        response = chats[user_id].send_message(prompt)
    except:
        response = None
    if response:
        bot.edit_message_text(chat_id=wait_message.chat.id, message_id=wait_message.message_id, text=response.text)
    else:
        bot.edit_message_text(chat_id=wait_message.chat.id, message_id=wait_message.message_id, text="Sorry, I could not find the answer to your question. Please try again.")
    
bot.infinity_polling()

