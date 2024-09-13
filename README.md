# Shiny Chat

Using [chatstream](https://github.com/wch/chatstream/tree/main) to show how easy an OpenAI chat app is!!

## Getting Setup

Make sure you have a `virtualenv` loaded!

Install packages (just `chatstream` and its dependencies, like `shiny`)

```
pip install -r requirements.txt
```

## OpenAI Url
Then determine the `OPENAI_URL` for your OpenAI target.

### Personal Use
```
OPENAI_URL=https://api.openai.com/v1/
```

Make sure to set an `OPENAI_API_KEY` in your environment.

### Workshops
```
OPENAI_URL=http://openai.ai.svc.cluster.local
```

Authentication is handled for you!

## Run the App

Then run the app!

```
shiny run app.py
```

## Done!

You should see a Shiny Chat app running, and see the results that look like this:

![Screenshot of the Chat App](chat-app.png)
