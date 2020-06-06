import React, {Component} from 'react';
import './lobby.css'
import Modal from 'react-bootstrap/Modal'
import Button from "react-bootstrap/Button";
import Spinner from 'react-bootstrap/Spinner'

/**
 * Class responsible for showing lobby
 */
class Lobby extends Component {

    /**
     * Renders component.
     */
    render() {
        return (
            <>
                <Modal
                    show={this.props.show}
                    onHide={() => window.location.reload()}
                    size="lg"
                    aria-labelledby="contained-modal-title-vcenter"
                    centered
                >
                    <Modal.Header closeButton>
                        <Modal.Title id="contained-modal-title-vcenter">
                            Lobby
                        </Modal.Title>
                    </Modal.Header>
                    <Modal.Body className={"c-flex-ctr m-lobby-body"}>
                        {
                            this.props?.lobbyplayers?.length > 0
                                ?
                                this.props?.lobbyplayers?.map((player, i) => (
                                        <div
                                            key={i}
                                            className={"m-lobby-player"}
                                            style={{backgroundColor: player.color}}
                                        >
                                        <span className={""}>
                                            {`Player${player.id}`}
                                        </span>
                                            <span
                                                className={"m-lobby-player-ready"}
                                                style={{
                                                    backgroundColor: player.ready ? "rgb(40, 168, 13)" : "rgb(253, 56, 56)"
                                                }}
                                            >
                                            {player.ready ? "Ready!" : "Not ready :c"}
                                        </span>
                                        </div>
                                    )
                                )
                                :
                                <Spinner animation="grow" variant="secondary"/>
                        }
                    </Modal.Body>
                    <Modal.Footer>
                        <Button onClick={() => this.props.ready(this.props.myid)}>Ready</Button>
                        <Button onClick={() => window.location.reload()}>Close</Button>
                    </Modal.Footer>
                </Modal>
            </>
        );
    }
}

export default Lobby;