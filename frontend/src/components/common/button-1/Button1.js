import React, {Component} from 'react';
import './button1.css'

class Button1 extends Component {
    render() {
        return (
            <div className={"m-button1-wrapper c-flex-ctr c-max-size"}>
                <button onClick={this.props.onClick}
                        className={"m-button1-button c-max-size c-no-select"}>{this.props.text}</button>
            </div>
        );
    }
}

export default Button1;