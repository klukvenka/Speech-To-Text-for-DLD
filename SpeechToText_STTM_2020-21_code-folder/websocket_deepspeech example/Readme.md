# Web Microphone Websocket

This is an example of a ReactJS web application streaming microphone audio from the browser
to a NodeJS server and transmitting the DeepSpeech results back to the browser.

To access it : http://locahost:3000/

#### Models:

You need to put the ouput_graph.pbmm and the output_graph.scorer in the same folder as tthe server.js file.

#### Install:

```
yarn install
```

#### Run ReactJS Client:

```
yarn start
```

#### Run NodeJS Server (in a separate terminal window):

```
node server.js
```