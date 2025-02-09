# Linked List Data Structure

## Singly Linked List in Python

A **Singly Linked List** is a fundamental data structure used in computer science. It consists of nodes where each node contains data and a reference (pointer) to the next node in the sequence.

### Visual Representation:
<img src="https://miro.medium.com/v2/resize:fit:875/1*wo28uwfiOGu-Rsd6zP1Y1A.png" alt="Linked List Example" style="zoom: 80%;" />

Each node in the linked list has two components:
1. **Data**: The value stored in the node.
2. **Next**: A pointer to the next node in the sequence.

Here’s an example of how it looks visually:
<img src="https://miro.medium.com/v2/resize:fit:760/1*nLH_Gj0etGD0Hz9fSB3R3Q.png" alt="Node Diagram" style="zoom: 80%;" />

### Key Notes:
- In a singly linked list, each node points to the next node using the "next" pointer.
- The last node's "next" pointer is set to `None`, indicating the end of the list.

### Memory Allocation:
Unlike arrays, linked lists do not require contiguous memory allocation. Each node can be stored anywhere in memory, and the "next" pointer links them together.

### Types of Linked Lists:
1. **Singly Linked List**: Each node points to the next node only.
2. **Doubly Linked List**: Each node has two pointers, one for the previous node and one for the next node.
3. **Circular Linked List**: The last node points back to the first node, forming a loop.

### Conclusion:
In this document, we discussed the concept of a linked list, its memory allocation, and how it differs from arrays. We also explored the types of linked lists and their visual representation.

---

#### **Egyptian Arabic Version**

# هيكل بيانات لينكد ليست (Linked List)

## لينكد ليست واحدة في بايثون (Singly Linked List)

الـ **لينكد ليست** هي هيكل بيانات أساسي بيتستخدم في علوم الحاسوب. بيتألف من وحدات (Nodes)، وكل وحدة تحتوي على بيانات ومرجع (Pointer) للوحدة اللي بعدها في الترتيب.

### تمثيل بصري:
![مثال لنظام الربط](https://miro.medium.com/v2/resize:fit:875/1*wo28uwfiOGu-Rsd6zP1Y1A.png)

كل وحدة في الـ لينكد ليست بتكون مؤلفة من جزئين:
1. **البيانات (Data)**: القيمة اللي مخزن فيها الوحدة.
2. **التالي (Next)**: أصبع إشارة (Pointer) للوحدة اللي بعدها.

دا كدا شكله بصريًا:
![رسم توضيحي للوحدة](https://miro.medium.com/v2/resize:fit:760/1*nLH_Gj0etGD0Hz9fSB3R3Q.png)

### ملاحظات مهمة:
- في الـ لينكد ليست الواحدة، كل وحدة بتشير للوحدة اللي بعدها باستخدام الأصبع "التالي" (Next).
- الوحدة الأخيرة أصبعها "التالي" بيكون محدد له قيمة `None`، يعني دا نهاية القائمة.

### تخصيص الذاكرة:
على عكس المصفوفات (Arrays)، الـ لينكد ليست مش بتحتاج لتخصيص ذاكرة متصلة. كل وحدة ممكن تتواجد أي مكان في الذاكرة، والأصبع "التالي" بيربطهم مع بعض.

### أنواع الـ لينكد ليست:
1. **لينكد ليست واحدة (Singly Linked List)**: كل وحدة بتشير للوحدة اللي بعدها فقط.
2. **لينكد ليست ثنائية (Doubly Linked List)**: كل وحدة ليها اثنين أصابع، واحد للوحدة اللي قبلها وواحد للوحدة اللي بعدها.
3. **لينكد ليست دائرية (Circular Linked List)**: الوحدة الأخيرة بتشير للوحدة الأولى، يبقى الكيان دائري.

### خلاصة:
في هذة الوثيقة، تحدثنا عن فكرة الـ لينكد ليست، وكيفية تخصيص الذاكرة ليها، واختلافها عن المصفوفات. استعرضنا كمان أنواع الـ لينكد ليست والتمثيل البصري ليها.
