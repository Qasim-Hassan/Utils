## Mock-Server

Basic **Node JS** program written to serve as local-first replacement for ```npx serve``` and ```live server extensions``` in Code Editors.

This assures no third-party software/package has access to your codebase. 

### Local-setup

Clone the repo, and navigate to the mock-server directory.

Then change the path on *line 21* in *mockserver.js* file to point it to relative path of the file you want to serve.

Then run:

```node mockserver.js```

Open **localhost:3000** to see your program running.