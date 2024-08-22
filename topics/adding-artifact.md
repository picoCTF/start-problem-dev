# Adding a Downloadable Artifact

To present a file artifact to the player two main things must happen:

1. You must add the file to `/challenge/artifacts.tar.gz` on the `builder` or
   `challenge` container, or the unnamed stage. See
   [here](/example-problems/sanity-static-flag/Dockerfile#L17)
1. You must link to the artifact in the challenge description. See [here](/example-problems/sanity-static-flag/problem.md#L15)
