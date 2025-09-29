# -------------------------------
# CryptoBuddy: Simple Rule-Based Chatbot
# -------------------------------

# Step 1: Define the Predefined Crypto Data
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8
    }
}

# Step 2: Greeting
print("👋 Hi! I’m CryptoBuddy, your AI-powered financial sidekick! 🌟")
print("Ask me about trending cryptos, sustainability, or which coin is best!\n")

# Step 3: Logic Function
def get_recommendation(user_query):
    user_query = user_query.lower()

    # Sustainability advice
    if "sustainable" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"🌱 Invest in {recommend}! It’s eco-friendly and has long-term potential!"

    # Trending cryptos
    elif "trending" in user_query or "growth" in user_query:
        trending = [c for c in crypto_db if crypto_db[c]["price_trend"] == "rising"]
        return f"🚀 Trending cryptos: {', '.join(trending)}."

    # Long-term growth
    elif "long-term" in user_query:
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] >= 7:
                return f"💡 {coin} is great for long-term growth with rising trends and high sustainability!"
        return "I don’t see a perfect long-term coin right now."

    # Fallback response
    else:
        return "🤔 Sorry, I can only advise on trends and sustainability. Try asking: 'Which crypto is sustainable?'"

# Step 4: Chat Loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("CryptoBuddy: Goodbye! Remember—crypto is risky, do your own research. 🙌")
        break
    response = get_recommendation(user_input)
    print(f"CryptoBuddy: {response}")
