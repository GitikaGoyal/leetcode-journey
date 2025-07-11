# 📘 253. Meeting Rooms II

> 📎 **Problem Link**: [LeetCode - 253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)  
> 🟠 **Level**: Medium   
> 💻 **Language**: C++, Python

---

## 📝 Problem Statement  
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

---

### 🔍 Examples

| Input                             | Output |
|-----------------------------------|--------|
| `[(0,30),(5,10),(15,20)]`         | `2`    |
| `[(7,10),(2,4)]`                  | `1`    |

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

## 🏷️ Tags
`Heap` `Greedy`, `Sweep Line`, `Sort`

---

## 🏢 Company
`Amazon`, `Apple`, `Atlassian`, `Bloomberg`, `Expedia`, `Facebook`, `Goldman Sachs`, `Google` ,`Microsoft`, `Oracle`, `Paypal`, `Snapchat`, `Uber`, `Visa`, `Walmart`
