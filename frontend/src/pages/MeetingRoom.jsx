import React, { Component } from "react";
import { Link } from "react-router-dom";
import { Modal, ModalBody, Button } from "reactstrap";

import home from "../assets/img/home.png";
import cap from "../assets/img/cap.png";
import user from "../assets/img/user.png";
import settings from "../assets/img/settings.png";
import logout from "../assets/img/logout.png";
import atom from "../assets/img/atom.png";
import stopwatch from "../assets/img/stopwatch.png";
import people from "../assets/img/people.png";
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

class MeetingRoom extends Component {
  constructor(props) {
    super(props);
    this.state = {
      cameraModal: false,
      chatWindow: false,
      studentList: [
        { firstName: "Anakin", lastName: "Skywalker" },
        { firstName: "Obi Wan", lastName: "Kenobi" },
        { firstName: "Galen", lastName: "Marek" },
        { firstName: "Qui Gon", lastName: "Jinn" },
        { firstName: "Plo", lastName: "Koon" },
        { firstName: "Ahsoka", lastName: "Tano" },
        { firstName: "Kit", lastName: "Fisto" },
        { firstName: "Luke", lastName: "Skywalker" },
        { firstName: "Jyn", lastName: "Erso" },
        { firstName: "Din", lastName: "Djarin" },
        { firstName: "Leia", lastName: "Organa" },
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
              <img src="http://192.168.10.150:5000/video_feed" alt="" />
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
                <div className="message-wrapper">
                  <p>Hey, not feeling good ?</p>
                </div>
                <div className="message-wrapper right">
                  <p>Yes</p>
                </div>
                <div className="message-wrapper">
                  <p>
                    What is bothering you the momst <br />
                    a. Academics <br />
                    b. Relationships <br />
                    c. Exams
                  </p>
                </div>
                <div className="message-wrapper right">
                  <p>c</p>
                </div>
              </div>
              <div className="text-box">
                <input type="text" placeholder="Type your message" name="" id="" />
              </div>
            </div>

            <div className="top-bar">
              <h3>Meeting 3 </h3>
              <div className="time-left">
                <img src={stopwatch} alt="" />
                <h3>&nbsp; 1h 29m</h3>
              </div>
            </div>

            <div className="bottom-container">
              <div className="left">
                <div className="meeting-window card">
                  {/* <video src={daoko}></video> */}
                  <img style={{ marginLeft: "130px" }} src={people} alt="" />

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
                      <Link to="/meeting-summary">
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

export default MeetingRoom;
