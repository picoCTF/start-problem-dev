# General Log Triage

Intermediate general skills challenge focused on practical command-line triage.

## Concept

Players receive a downloadable artifact with noisy operational logs and a lookup
CSV. They must:

1. Isolate suspicious log lines.
2. Extract ordered identifiers.
3. Reconstruct a Base64 payload from mapped chunks.
4. Decode the payload into the final flag.

## Local Build Test

```terminal
docker build . --build-arg FLAG='academy{deadbeef}'
```

## cmgr Test Flow

```terminal
cmgr update
cmgr playtest academy/new-problems/general-log-triage
cmgr test academy/new-problems/general-log-triage
```
