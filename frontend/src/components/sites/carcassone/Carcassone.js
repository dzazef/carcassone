import React, {Component} from 'react';
import './carcassone.css'
import Logo from "../../common/logo/Logo";
import Button1 from "../../common/button-1/Button1";

/**
 * Main site of the Game.
 */
class Carcassone extends Component {
    /**
     * Renders component.
     */
    render() {
        return (
            <div className="m-carcassone-background c-max-size">
                <div className={"m-carcassone-logo-wrapper c-flex-ctr"}>
                    <Logo/>
                </div>
                <div className={"m-carcassone-button-wrapper c-flex-ctr"}>
                    <Button1 text={"play"} onClick={this.props.connect}/>
                </div>
            </div>
        );
    }
}

export default Carcassone;