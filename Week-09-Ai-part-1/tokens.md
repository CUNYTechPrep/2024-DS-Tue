# Setting Up API Tokens for Hugging Face & OpenAI in Streamlit Space

## 1. Create Required Tokens
1. **Hugging Face Token**:
   - Log in to [Hugging Face](https://huggingface.co)
   - Go to Settings → Access Tokens
   - Click "New token"
   - Name your token and select permissions
   - Copy the token

2. **OpenAI API Key**:
   - Log in to [OpenAI](https://platform.openai.com)
   - Go to API settings
   - Create new API key
   - Copy the key

## 2. Add Tokens to Space Settings
1. Go to your Hugging Face Space settings (⚙️ icon)
2. Find "Repository Secrets" section
3. Add both tokens:
```toml
HUGGINGFACEHUB_API_TOKEN = "your_huggingface_token_here"
OPENAI_API_KEY = "your_openai_key_here"
```

## 3. Access Tokens in app.py

```python
import os

# Load environment variable(s)
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
```

## Alternative Methods
### Using Streamlit secrets.toml
```toml
# .streamlit/secrets.toml
HUGGINGFACEHUB_API_TOKEN = "your_token_here"
OPENAI_API_KEY = "your_key_here"
```

### Using Local .env File (Development)
```plaintext
HUGGINGFACEHUB_API_TOKEN=your_token_here
OPENAI_API_KEY=your_key_here
```

## Security Best Practices
- Never commit tokens to version control
- Add `.env` and `secrets.toml` to `.gitignore`
- Use read-only tokens when possible
- Regularly rotate your API keys
- Set appropriate token permissions
- Use environment variables for different deployment environments
