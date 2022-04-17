import React, { Component } from "react";
import { Link } from "react-router-dom";
import { Modal, ModalBody, Button } from "reactstrap";

import home from "../assets/img/home.png";
import cap from "../assets/img/cap.png";
import user from "../assets/img/user.png";
import settings from "../assets/img/settings.png";
import logout from "../assets/img/logout.png";
import helmet from "../assets/img/helmet.png";
import stopwatch from "../assets/img/stopwatch.png";
import gintoki from "../assets/img/gintoki.png";
import closeWhite from "../assets/img/closeWhite.png";

// MEETING CONTROL IMAGES
import mic from "../assets/img/meeting-controls/mic.png";
import cameraOn from "../assets/img/meeting-controls/cameraOn.png";
import hand from "../assets/img/meeting-controls/hand.png";
import chat from "../assets/img/meeting-controls/chat.png";
import expand from "../assets/img/meeting-controls/expand.png";
import exit from "../assets/img/meeting-controls/exit.png";
import screenShare from "../assets/img/meeting-controls/screenShare.png";

import daoko from "../assets/daoko.mp4";

class TherapistRoom extends Component {
  constructor(props) {
    super(props);
    this.state = {
      cameraModal: false,
      chatWindow: false,
      studentList: [
        { firstName: "Therapist", lastName: "" },
        { firstName: "You", lastName: "" },
      ],
    };
    this.toggleCameraModal = this.toggleCameraModal.bind(this);
  }

  toggleCameraModal() {
    this.setState((prevState) => ({ cameraModal: !prevState.cameraModal }));
    console.log("log test", this.state.cameraModal);
  }

  render() {
    return (
      <>
        <main className="exam-main">
          <Modal
            centered
            size="lg"
            className="camera-modal"
            toggle={this.toggleCameraModal}
            isOpen={this.state.cameraModal}
          >
            <ModalBody>
              <img src={gintoki} alt="" />
            </ModalBody>
          </Modal>
          <div className="left">
            <div className="side-bar">
              <div>
                <div className="logo">F.</div>
                <div className="icons-list">
                  <img src={home} alt="" />
                  <img src={cap} alt="" />
                  <img src={user} alt="" />
                  <img src={settings} alt="" />
                </div>
              </div>
              <img src={logout} alt="" />
            </div>
          </div>

          <div className="right">
            <div className={this.state.chatWindow ? "chat-window open" : "chat-window"}>
              <div className="title-bar">
                <p>AI ChatBot</p>
                <img
                  src={closeWhite}
                  alt=""
                  onClick={() => {
                    this.setState({ chatWindow: false });
                  }}
                />
              </div>
              <div className="messages">
                <div className="message-wrapper right">
                  <p>Lorem, ipsum.</p>
                </div>
                <div className="message-wrapper left">
                  <p>Lorem, ipsum.</p>
                </div>
                <div className="message-wrapper right">
                  <p>`Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime, veritatis?`</p>
                </div>
              </div>
              <div className="text-box">
                <input type="text" placeholder="Type your message" name="" id="" />
              </div>
            </div>

            <div className="top-bar">
              <div className="exam-info">
                {/* <img src={helmet} alt="" /> */}
                <h3>Therapy Session</h3>
              </div>
            </div>

            <div className="bottom-container">
              <div className="left">
                <div className="meeting-window card">
                  {/* <video src={daoko}></video> */}
                  <img
                    src="https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F23%2F2018%2F08%2F22%2Ffind-therapist-1.jpg&q=60"
                    alt=""
                  />

                  <div className="controls-trigger">
                    <div className="controls-box">
                      <div className="control-wrapper">
                        <img src={mic} alt="" />
                      </div>
                      <div className="control-wrapper" onClick={this.toggleCameraModal.bind(this)}>
                        <img src={cameraOn} alt="" />
                      </div>
                      <div className="control-wrapper">
                        <img src={hand} alt="" />
                      </div>
                      <div
                        className="control-wrapper"
                        onClick={() => {
                          this.setState({ chatWindow: true });
                        }}
                      >
                        <img src={chat} alt="" />
                      </div>
                      <div className="control-wrapper">
                        <img src={screenShare} alt="" />
                      </div>
                      <div className="control-wrapper">
                        <img src={expand} alt="" />
                      </div>
                      <Link to="/">
                        <div className="control-wrapper">
                          <img src={exit} alt="" />
                        </div>
                      </Link>
                    </div>
                  </div>
                </div>
              </div>

              <div className="right card">
                <h3>Participants</h3>

                <div className="student-list">
                  {this.state.studentList.map((el) => {
                    return (
                      <div className="student-wrapper">
                        <img src={`https://ui-avatars.com/api/?name=${el.firstName}+${el.lastName}`} alt="" />
                        <p>{`${el.firstName} ${el.lastName}`}</p>
                      </div>
                    );
                  })}
                </div>

                {/* <div className="chat">
                  <i className="fa fa-comments-o" aria-hidden="true"></i>
                  <p>Chat with the instructor</p>
                </div> */}
              </div>
            </div>
          </div>
        </main>
      </>
    );
  }
}

export default TherapistRoom;
