import React, {Component} from 'react';
import './lobby.css'
import Modal from 'react-bootstrap/Modal'
import Button from "react-bootstrap/Button";

class Lobby extends Component {

    render() {
        return (
            <>
                <Modal
                    show={this.props.show}
                    onHide={this.props.onHide}
                    size="lg"
                    aria-labelledby="contained-modal-title-vcenter"
                    centered
                >
                    <Modal.Header closeButton>
                        <Modal.Title id="contained-modal-title-vcenter">
                            Lobby
                        </Modal.Title>
                    </Modal.Header>
                    <Modal.Body>
                        {
                            this.props?.lobbyplayers?.map((player, i) => (
                                    <p key={i}>{player.id} {player.color} {player.ready}</p>
                                )
                            )
                        }
                    </Modal.Body>
                    <Modal.Footer>
                        <Button onClick={() => this.props.ready(this.props.myid)}>Ready</Button>
                        <Button onClick={this.props.onHide}>Close</Button>
                    </Modal.Footer>
                </Modal>
            </>
        );
    }
}

export default Lobby;