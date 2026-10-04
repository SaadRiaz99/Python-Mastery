# Debug Tips

Advice for people debugging for the **first time**. One tip at a time.

---

## Tip #1 — Reproduce it before you touch the code

The single biggest mistake beginners make is opening the source file and starting to
change things "to see what happens". You end up with three edits, two new errors and no
idea which change fixed (or broke) what.

Instead, spend two minutes writing the bug down. Three lines are enough:

```text
1. What I did:      opened /, clicked Submit on "Algebra worksheet"
2. What I expected: the page reloads with a green "Assignment added" banner
3. What happened:   405 Method Not Allowed, no banner
```

Why this works:

- **A bug you can repeat is a bug you can kill.** If you cannot repeat it, you cannot
  prove your fix worked.
- **Writing it forces you to be specific.** "It's broken" is not a bug; "POST / returns
  405" is.
- **It tells you where to look.** Step 1 points at the route, step 2 vs 3 points at the
  difference between them.

### Then run the loop

1. **Reproduce** — the three lines above, every time, before and after the fix.
2. **Read the error from the bottom up.** The last line is the error type and message;
   the frames above it are the path the program took. The top-most frame *in your own
   code* is where the trouble surfaced.
3. **Isolate** — shrink the problem until it is one function, one variable, one value.
   Add `breakpoint()` (or `print(...)`) right before the suspicious line and print the
   actual value and its type: `print(value, type(value))`. Half of all bugs in this app
   were `int` vs `str` or `int` vs `float` — you cannot see that by staring.
4. **Smallest fix** — change one thing. If you cannot say in one sentence what the bug
   is, you are not ready to edit; go back to step 3.
5. **Re-run** — `python _smoke.py`. Green means done; if you broke a different check you
   found a second bug, not a failed fix.

### Where to do it in this app

```bash
uvicorn app.main:app --reload        # run it, click the thing that breaks
python _smoke.py                     # the "expected vs actual" list, automated
curl -i http://127.0.0.1:8000/api/assignments   # see raw status codes + JSON
```

- Browser not enough? Use the auto docs at <http://127.0.0.1:8000/docs> to fire a single
  request and read the status code.
- Need to step through a request line by line:
  `python -m pdb -c "from app.main import app" -c "continue"` or put `breakpoint()` in
  the route handler — `--reload` picks it up and drops you into the console.

**Rule of thumb:** if you changed code before you could state the bug in one sentence,
undo the change and start over at Tip #1.
