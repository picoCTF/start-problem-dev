# Playtest Fails

```terminal
$ cmgr playtest picoctf/picoctf2024/non-sql-injection
challenge information available at: http://localhost:4242/
cmgr: [ERROR:  failed to delete build (15): FOREIGN KEY constraint failed]
$
```

This error happens when you have an active playtest opened elsewhere. Just close
the other playtest instance in order to run this one.
