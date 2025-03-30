# Skin Classification Bot

## 📌 Overview
This project is a **Skin Classification Bot** that uses a machine learning model to classify skin images. It automates the process of analyzing skin conditions and can send results via a messaging API.

## 🚀 Features
- Automatically logs into a website, extracts relevant data, and processes skin images.
- Uses a pre-trained **ViT (Vision Transformer) model** for classification.
- Integrates with a **messaging API** to send classification results to users.
- Webhook server for handling requests and notifications.

## 🛠️ Installation
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/Thanat-Music/Skin_classification_Bot.git
cd Skin_classification_Bot
```

### 2️⃣ Install Dependencies
Make sure you have **Python 3.8+** installed. Then run:
```sh
pip install -r requirements.txt
pip install line-bot-sdk
```

### 3️⃣ Set Up Webhook Server (Optional)
If you need to expose your webhook server, consider using **Cloudflare Tunnel**:
```sh
cloudflared tunnel --url http://localhost:5000
```

## 📦 Usage
### Run the bot
```sh
python webhook.py
```
This will start the webhook server to handle classification requests.

### Classify an Image
You can send an image for classification using:
```sh
python get_image.py --image path/to/image.jpg
```

## 📜 Model and Dataset
- **Model Weights:** Available at [Hugging Face](https://huggingface.co/T-music/google-vit-base-patch16-224-ISICmod-19k)
- **Dataset:** Available on [Kaggle](https://www.kaggle.com/datasets/thanatw/isic2019-modded)

## 📜 File Structure
```
Skin_classification_Bot/
│── classifier.py         # Model processing and prediction
│── get_image.py          # Utility library for LINE SDK integration
│── webhook.py            # Webhook server for API integration
│── test.ipynb            # Jupyter Notebook for testing
│── requirements.txt      # Python dependencies
│── README.md             # Documentation
```

## 🔗 API Integration
The bot integrates with a messaging API to send classification results. Ensure that your API keys are configured properly in `webhook.py`.

## 🤝 Contributing
Feel free to contribute to this project! Submit a PR or open an issue if you find bugs.

## 📄 License
This project is licensed under the **Apache-2.0 license**.

---

Let me know if you want to add specific details! 🚀

