## Carcassone - frontend  
  
Created using React/Redux/PixiJS.  
In the project directory, you can run:

### `npm start`

Runs the app in the development mode.  
Open  [http://localhost:3000](http://localhost:3000/)  to view it in the browser.

If you want to create optimized production build, you can run: 

### `npm build`

Project structure:

 - public - static website on which React components are rendered
 - src - folder with source code
	 - assets - images, vector graphics etc.
	 - board - classes responsible for drawing tiles and pawns
	 - components - folder with React components 
	 - error - Redux middleware for error handling
	 - store - Redux store, actions and reducers
	 - ws - classes and functions responsible for handling websocket connection
	 - config.json - configuration file
