# 📘 252. Meeting Rooms

> 📎 **Problem Link**: [LeetCode - 252. Meeting Rooms](https://leetcode.com/problems/meeting-rooms/)  
> 🟢 **Level**: Easy   
> 💻 **Language**: C++, Python

---

## 📝 Problem Statement  
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts.

---

### 🔍 Examples

| Input                             | Output |
|----------------------------------|--------|
| `[(0,30),(5,10),(15,20)]`        | `false`|
| `[(7,10),(2,4)]`                 | `true` |

---

## ✅ Constraints

- `0 <= intervals.length <= 500`  
- `0 <= intervals[i].start < intervals[i].end <= 1,000,000`  

---

## 💡 Intuition  
To attend all meetings, **no two intervals should overlap**.  
If **any two intervals intersect**, the person cannot attend both.

---

## 🛠️ Approaches  

> ### 1️⃣ Brute Force (Compare All Pairs)  
>
>- Compare each interval with every other one.
>- If any two intervals overlap → return `false`.
>- Else, return `true`.
>
> #### 🧮 Overlap Condition:
>Two intervals `A` and `B` **overlap** if:
>min(A.end, B.end) > max(A.start, B.start)
>
> #### ⏱️ Time & Space Complexity
>
>| Time Complexity | Space Complexity |
>|-----------------|------------------|
>| O(n²)           | O(1)             |


>### 2️⃣ Optimized (Sorting by Start Time)  
>
>- Sort intervals based on start time.
>- Then check if any interval overlaps with the previous.
>- If `yes` → return `false`, else → `true`.
>
>
>#### ⏱️ Time & Space Complexity
>
>| Time Complexity | Space Complexity |
>|-----------------|------------------|
>| O(n logn)       | O(1)             |

---

## 🏢 Company
`Amazon`, `Bloomberg`, `Facebook`, `Google`, `Microsoft`, `Twitter`
