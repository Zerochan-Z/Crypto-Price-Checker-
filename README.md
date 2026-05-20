# 💰 Crypto Price Checker – Code Summary

A Python program that lets users check cryptocurrency prices, add new coins, and loop interactively.

---

## 📋 Program Flow

| Step | Action |
|:----:|--------|
| 1 | Display available coins |
| 2 | Ask user if they want to add coins |
| 3 | If yes → add coin(s) (loop until user says no) |
| 4 | Ask which coin price to show |
| 5 | Display price or error message |
| 6 | Loop until user types `None` / `quit` / `exit` / `end` |

---

## 🧠 Key Code Concepts



## ✅ Key Takeaways

| Concept | How it's used |
|---------|----------------|
| Dictionaries | Store coin → price mappings |
| `while True` | Create interactive loops |
| `.lower()` | Make input case‑insensitive |
| `.title()` | Display coins nicely |
| f‑strings | Format output with variables |
| `:,.2f` | Format prices as currency |
| `coin.title()` | Capitalizes first letter of each word |
| `{price:,.2f}` | Adds thousands separator and 2 decimal places |
| `.lower()` | Makes input case‑insensitive |
| `in ['yes','y']` | Accepts multiple affirmative answers |
| `float(input(...))` | Converts price input to a number |

---