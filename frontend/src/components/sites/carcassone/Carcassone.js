import React, {Component} from 'react';
import './carcassone.css'
import Logo from "../../common/logo/Logo";
import Button1 from "../../common/button-1/Button1";
import store from '../../../store/store'
import * as WSActions from '../../../store/actions/wsActions'
import config from '../../../config.json'

class Carcassone extends Component {

    create = () => {
        store.dispatch(WSActions.wsConnect(config.host))
    }

    send = () => {
        store.dispatch(WSActions.wsSend({message: 'XD'}))
    }

    render() {
        return (
            <div className="m-carcassone-background c-max-size">
                <div className={"m-carcassone-logo-wrapper c-flex-ctr"}>
                    <Logo/>
                </div>
                <div className={"m-carcassone-button-wrapper c-flex-ctr"}>
                    <Button1 text={"create"} onClick={this.create}/>
                    <Button1 text={"send"} onClick={this.send}/>
                </div>
            </div>
        );
    }
}

export default Carcassone;