## README: Crypto Price Checker

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

| Concept | How it's used |
|---------|----------------|
| Dictionaries | Store coin → price mappings |
| `while True` | Create interactive loops |
| `.lower()` | Make input case‑insensitive |
| `.title()` | Display coins nicely |
| f‑strings | Format output with variables |
| `:,.2f` | Format prices as currency |
| `in ['yes','y']` | Accept multiple affirmative answers |
| `float(input(...))` | Convert price input to a number |

---

## 📤 Output Examples

### Showing a price
```
The price of Bitcoin is $64,500.50
```

### Adding a coin
```
Added "Dogecoin" to your list.
```

### Exit message
```
Thanks for using this price-checker.

╰(*°▽°*)╯
```

---

## 🧪 Error Handling

| User action | Program response |
|-------------|------------------|
| Types a coin not in dictionary | `Sorry, "X" is not in our database` |
| Types invalid yes/no answer | Re‑asks the question |
| Types `None` / `quit` | Exits the price check loop |

---

## ✅ Key Takeaways

| Concept | How it's used |
|---------|----------------|
| Dictionaries | Store coin → price mappings |
| `while True` | Create interactive loops |
| `.lower()` | Make input case‑insensitive |
| `.title()` | Display coins nicely |
| f‑strings | Format output with variables |
| `:,.2f` | Format prices as currency |

---

## 📁 Project Status

| Feature | Status |
|---------|--------|
| Display available coins | ✅ |
| Add new coins | ✅ |
| Check coin prices | ✅ |
| Error handling (invalid coin) | ✅ |
| Error handling (invalid yes/no) | ✅ |
| Exit gracefully | ✅ |

---

> *Last updated: May 2026*
```
