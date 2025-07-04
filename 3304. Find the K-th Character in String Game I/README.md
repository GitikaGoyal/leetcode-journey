# 🔠 Find the K-th Character in String Game I

## 🔗 Problem Link
[Find the K-th Character in String Game I](https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/)

## 🧩 Level
🟢 Easy

## 💻 Language
C++, Python

## 💡 Intuition
We want to find the **k-th character** of a special string that grows by appending a version of itself with each character incremented by 1 modulo 26.  
This process reflects a binary pattern — each `1` in the binary representation of `k - 1` corresponds to a step forward in the alphabet from `'a'`.

---

## 🧠 Approach

### ✅ Optimized Bit Manipulation Approach

This method uses `std::popcount` to count the number of `1`s in the binary representation of `k - 1`.  
Each `1` adds one step from `'a'`, so `'a' + popcount(k - 1)` gives the desired character.

📈 Efficient and elegant — works in constant space and logarithmic time.

---

### 🔁 Simulation Approach

Simulates the full construction of the string:
- Start with `'a'` (value 0).
- Append a copy of the current string with all values incremented by 1 modulo 26.
- Repeat until the size is at least `k`.

Then return the character at position `k - 1`.

🛠️ More intuitive but much slower and memory-consuming.

---

## ⏱️ Complexity

| ⚙️ Approach                  | 🕒 Time Complexity | 🧠 Space Complexity |
|-----------------------------|--------------------|---------------------|
| ✅ Bit Manipulation          | O(log k)           | O(1)                |
| 🔁 Simulation               | O(k)               | O(k)                |
