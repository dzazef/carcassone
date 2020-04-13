import React, {Component} from 'react';
import './carcassone.css'
import Logo from "../../common/logo/Logo";
import Button1 from "../../common/button-1/Button1";

class Carcassone extends Component {

    render() {
        return (
            <div className="m-carcassone-background c-max-size">
                <div className={"m-carcassone-logo-wrapper c-flex-ctr"}>
                    <Logo/>
                </div>
                <div className={"m-carcassone-button-wrapper c-flex-ctr"}>
                    <Button1 text={"Play"} />
                </div>
            </div>
        );
    }
}

export default Carcassone;