import React from 'react';
import {Provider} from 'react-redux'
import ReactDOM from 'react-dom';
import './style/index.css';
import './style/common.css';
import AppF from './components/sites/main/AppF';
import * as serviceWorker from './serviceWorker';
import store from './store/store'

ReactDOM.render(
    <Provider store={store}>
        <AppF/>
    </Provider>,
    document.getElementById('root')
);


// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
