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
To determine the number of rooms needed:
- We must track **overlapping intervals**.
- Each overlap indicates the need for an additional room.

---

## 🛠️ Approaches  

---

### 1️⃣ Min-Heap (Priority Queue)  

- Sort intervals by start time.
- Use a **min-heap** to track the earliest ending meeting.
- If the current meeting starts after the earliest one ends → reuse the room (pop heap).
- Otherwise, allocate a new room (push into heap).

#### ⏱️ Time & Space Complexity

| Time Complexity | Space Complexity |
|-----------------|------------------|
| O(n log n)      | O(n)             |

---

### 2️⃣ Sweep Line Algorithm (Greedy with Sorting)  

- Break intervals into start & end points with markers (+1 for start, -1 for end).
- Sort by time; if equal, end comes before start.
- Count active meetings at each time step.

#### ⏱️ Time & Space Complexity

| Time Complexity | Space Complexity |
|-----------------|------------------|
| O(n log n)      | O(n)             |

---

### 3️⃣ Two-Pointer Approach  

- Extract all start and end times.
- Sort both arrays.
- Traverse using two pointers:
     -  If a meeting starts before the earliest ending meeting → need new room.
     -  Else → reuse a room.

#### ⏱️ Time & Space Complexity

| Time Complexity | Space Complexity |
|-----------------|------------------|
| O(n log n)      | O(n)             |

---

### 4️⃣ Greedy with Event Timeline  

- Convert each meeting into two events: (start, +1) and (end, -1).
- Sort events:
     -  Earlier time first.
     -  If equal, end event before start event.
- Traverse the events to count overlapping meetings.

#### ⏱️ Time & Space Complexity

| Time Complexity | Space Complexity |
|-----------------|------------------|
| O(n log n)      | O(n)             |

---

## 🏷️ Tags
`Heap` `Greedy`, `Sweep Line`, `Sort`

---

## 🏢 Company
`Amazon`, `Apple`, `Atlassian`, `Bloomberg`, `Expedia`, `Facebook`, `Goldman Sachs`, `Google` ,`Microsoft`, `Oracle`, `Paypal`, `Snapchat`, `Uber`, `Visa`, `Walmart`
