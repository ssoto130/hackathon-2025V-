packages:
marked: marked -> html
phospher-svelte : icons
bits-ui: styless ui components

the tree structure uses the tree cli

gather the todos into a single file:

```
grep -rni "TODO" --exclude-dir=node_modules --exclude-dir=.svelte-kit . | sort | awk -F':' '{
    if ($1 != prev_file) {
        if (prev_file) print "";
        print $1;
        prev_file = $1;
    }
    line_content = $3;
    for (i = 4; i <= NF; i++) {
        line_content = line_content ":" $i;
    }
    print "- " line_content;
}' > TODO.md
```

learned svelte from:
https://svelte.dev/tutorial/svelte/welcome-to-svelte - interactive tutorial
https://youtu.be/uOI77E8Y95Q?si=fHf8ZxeADXmTrpL6 - todo app video
