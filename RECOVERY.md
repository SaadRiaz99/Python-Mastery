# How to Undo the Force Push & Restore Your Old Files

## What Happened

A `git push --force` was run on `main`, which replaced the old remote commits
with new ones. The old commit tip was **`ef6b6d1`**.

---

## Method 1: Check If You Have Another Local Clone

If you have another copy of the repo on your machine or another computer:

```bash
cd /path/to/other/clone
git reflog
git checkout ef6b6d1
# Your old files are back
```

---

## Method 2: GitHub "Rewind" Feature (Fastest)

GitHub Enterprise / some Pro accounts have this. Try it:

1. Go to your repo: `https://github.com/SaadRiaz99/Python-Mastery`
2. Click **"Rewind"** in the repo settings or the branch dropdown
3. Select a point before the force push
4. GitHub will restore the old commits

---

## Method 3: Contact GitHub Support

This is the **most reliable** method. GitHub keeps deleted objects
for a period of time.

1. Go to: `https://github.com/contact`
2. Or email: `support@github.com`
3. Say this:

> Hi, I accidentally force-pushed to my repo `SaadRiaz99/Python-Mastery`
> on the `main` branch. The old HEAD was commit `ef6b6d1`. Can you please
> restore the previous state of the branch?

GitHub support can restore the old branch from their internal backups.

---

## Method 4: Check GitHub Actions / Deploy History

If you had Vercel, Netlify, or GitHub Actions connected:

- **Vercel**: Check deployment history, each deploy has the full source
- **Netlify**: Check deploy logs
- **GitHub Actions**: Old workflow runs may have cached artifacts

---

## Method 5: Check Your Email / CI Notifications

If you had branch protection or notifications enabled, GitHub sends
emails with commit details when pushes happen. Search your inbox for
notifications from `SaadRiaz99/Python-Mastery`.

---

## Method 6: Git Object Recovery (If You Have Disk Access)

If you still have the old `.git` directory on any machine, the objects
might still exist:

```bash
# Find dangling commits (old force-pushed commits)
git fsck --lost-found

# Look for commit objects
ls .git/lost-found/other/

# Show each found commit
git show <hash>

# Once you find your old commit
git branch recover-branch <hash>
```

---

## After Recovery

Once you recover the old commit (`ef6b6d1` or similar):

```bash
# Create a backup branch from the old commit
git branch old-main ef6b6d1

# Push the backup to remote
git push origin old-main

# Then decide what to keep
# You can compare old vs new:
git diff old-main main
```

---

## Prevent This in the Future

Add branch protection:

1. Go to **Settings** > **Branches** > **Add rule**
2. Branch name: `main`
3. Enable: **"Require pull request before merging"**
4. Enable: **"Do not allow force pushes"**

---

## Summary

| Method | Chance of Recovery | Difficulty |
|--------|-------------------|------------|
| Other local clone | High (if exists) | Easy |
| GitHub Rewind | High | Easy |
| GitHub Support | High (within days) | Medium |
| Vercel/Netlify deploy | Medium | Easy |
| `git fsck` on old machine | Medium | Hard |
