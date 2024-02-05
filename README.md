# Translate Text

This project translates any foreign language text into English. It also summarizes the text into easy-to-understand sentences.

![Alt text](/project-image.png "Title")

# Roadmap

- [x] Text Translation
- [x] Summarizes Text
- [ ] Fix Bugs
- [ ] Improve UI
- [ ] Clean up ReadME
- [ ] TBD

## Getting Started

### Prerequisites

### Installation

1. Set up an account at [OpenAI](https://openai.com/blog/openai-api) to retrieve an API key

2. Clone the repo or fork it

   ```sh
   git clone git@github.com:lokyen/translate-text.git
   ```

3. Go to project folder

   ```sh
   cd langchain-translate
   ```

4. Download libraries and frameworks
   eg.

   ```sh
   pip install --upgrade --quiet  doctran
   ```

5. Set up your .env file by duplicating .env.example file and changing file name to .env and inserting OPENAI API Key

6. Run the project
   ```sh
   streamlit run translate_doc.py
   ```

## Built With

- [LangChain](https://www.langchain.com)
- [Streamlit](https://streamlit.io) App Framework
