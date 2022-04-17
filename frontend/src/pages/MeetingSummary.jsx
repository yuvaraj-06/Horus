import React, { Component } from "react";
import { Link } from "react-router-dom";
import { Modal, ModalBody, Button } from "reactstrap";

import home from "../assets/img/home.png";
import cap from "../assets/img/cap.png";
import user from "../assets/img/user.png";
import settings from "../assets/img/settings.png";
import logout from "../assets/img/logout.png";
import close from "../assets/img/close.png";
import github from "../assets/img/github.png";
import jira from "../assets/img/jira.png";
import ReactAudioPlayer from "react-audio-player";

import audio from "../assets/au.mp3";

import { Chart as ChartJS, ArcElement, Tooltip, CategoryScale, LinearScale, BarElement } from "chart.js";
import { Doughnut, Bar } from "react-chartjs-2";
import axios from "axios";
ChartJS.register(ArcElement, Tooltip, CategoryScale, LinearScale, BarElement);

class MeetingSummary extends Component {
  constructor(props) {
    super(props);
    this.state = {
      reportModal: false,
      employeesData: [],
      transInput: "",
      summarizedText: false,
    };

    this.handleTransInput = this.handleTransInput.bind(this);
    this.handleSummarize = this.handleSummarize.bind(this);
  }

  handleTransInput(event) {
    this.setState({ transInput: event.target.value });
  }

  handleSummarize() {
    console.log(this.state.transInput);
    axios
      .get(`http://localhost:5000/summary/"${this.state.transInput}"`)
      .then((res) => {
        console.log("summary: ", res.data);
        this.setState({ summarizedText: res.data });
      })
      .catch((err) => {
        console.warn(err);
      });
  }

  render() {
    return (
      <>
        <main className="teacher-dashboard summary-container">
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
              <Link to={"/"}>
                <img src={logout} alt="" />
              </Link>
            </div>
          </div>

          <div className="right">
            <div className="top-bar">
              <div className="exam-info">{this.state.summarizedText ? <h3>Summary</h3> : <h3>Transcript</h3>}</div>
            </div>

            {this.state.summarizedText ? (
              <div className="bottom-container">
                <div className="summary-wrapper">{this.state.summarizedText.summary}</div>
                <ReactAudioPlayer src={audio} controls />
                {/* <audio src="../../../backend/streamapp/au.mp3"></audio> */}
                {/* <audio controls>
                  <source src="horse.ogg" type="audio/ogg">
                  <source src="horse.mp3" type="audio/mpeg">
                Your browser does not support the audio element.
                </audio> */}
              </div>
            ) : (
              <div className="bottom-container">
                <textarea name="" onChange={this.handleTransInput} id="" cols="30" rows="10"></textarea>
                <button onClick={this.handleSummarize}>Summarize!</button>
              </div>
            )}
          </div>
        </main>
      </>
    );
  }
}

export default MeetingSummary;
