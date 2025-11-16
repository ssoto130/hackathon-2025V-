.
├── app.css - global app styles. includes: DropdownMenu, ContentRenderer, and general defaults
├── app.d.ts
├── app.html
├── lib
│   ├── code_blocks - contains all the components related to code editors and viewing code
│   │   ├── BaseCodeEditor.svelte - basic code editor with nothing special
│   │   └── CodeEditor.svelte - tabs and syntax highlighting per file
│   ├── components - buttons and other bits ui components
│   │   ├── DropdownMenu.svelte
│   │   ├── StyledButton.svelte
│   │   └── Tabs.svelte
│   ├── ContentRenderer.svelte - renders markdown
│   ├── index.ts
│   ├── server
│   │   └── data.ts - mock database
│   └── types.ts - types used throughout the program
└── routes
├── api
│   ├── courses - api to get the list of courses from mock database
│   │   └── +server.ts
│   ├── question-details - gets the details of a question based off of the questionId given
│   │   └── [questionId]
│   │   └── +server.ts
│   └── question-set - gets the question set info based off of the questionSetId given
│   └── [questionSetId]
│   └── +server.ts
├── +error.svelte - default error page
├── +layout.svelte
├── +page.server.ts - gets and feeds the info the home pages
├── +page.svelte - home page for selecting the course
└── problems
└── [questionSetId]
├── +page.server.ts - gets the questionSet info from questionSetId and gives it tothe page
└── +page.svelte - the page for displaying and solving a question, can select aquestion based off of the questionSet
