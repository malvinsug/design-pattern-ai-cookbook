# Async Programming
Simply put: imagine you are an employee and you want to optimize your workflow. Some of your tasks requires waiting to get the result of what you need. Instead of waiting and doing nothinng, you optimize your workflow by doing other task that can be done that is not related to the resource that you are waiting. 

# ✅ Correct Mental Model
✔ async creates an asynchronous function
You add async def to a function not because it should “run asynchronously”, but because:

The function will use await inside it
(meaning it performs asynchronous operations)

So the rule is:

➤ Add async if your function needs to use await inside.

If it doesn’t need await, it should not be async.

✔ await is used only when you are waiting for another async operation to finish

Use await when:

calling an async function

calling an I/O operation that returns a coroutine

using libraries like httpx.AsyncClient, aiohttp, asyncio.sleep, etc.

# ❗ Common misconception you might be having:

“Add async to the function that should run in parallel.”

No — functions don’t become parallel just because they are async.

Async only gives Python the ability to pause the function.

To run them concurrently, you must use:

```python
asyncio.gather(...)
```

or create tasks manually.
