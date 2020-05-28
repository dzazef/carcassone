import React, {Component} from 'react';
import './surrender.css'
import {ReactComponent as CloseIcon} from "../../../assets/close.svg";

class Surrender extends Component {
    render() {
        return (
            <button className={"m-surrender-button"} onClick={() => this.props.surrender(this.props.myId)}>
                <CloseIcon className={"m-surrender-icon"}/>
            </button>
        );
    }
}

export default Surrender;