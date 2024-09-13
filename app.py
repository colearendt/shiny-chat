import chatstream
import dotenv
import os

from shiny import App, Inputs, Outputs, Session, ui

dotenv.load_dotenv()
base_url = os.getenv("OPENAI_URL")
print(f'Using url: {base_url}')

if base_url == "":
    raise ValueError("OPENAI_URL environment variable must be set")

app_ui = ui.page_fixed(
    chatstream.chat_ui("mychat"),
)


def server(input: Inputs, output: Outputs, session: Session):
    chatstream.chat_server("mychat", url=base_url)


app = App(app_ui, server)
