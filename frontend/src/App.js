import React, { Component } from "react";
import Home from "./pages/Home";
import "bootstrap/dist/css/bootstrap.min.css";
import "./scss/Index.scss";
import { Routes, Route, withRouter, Navigate } from "react-router-dom";
import MeetingRoom from "./pages/MeetingRoom";
import HRDashboard from "./pages/HRDashboard";
import TherapistRoom from "./pages/TherapistRoom";
import Login from "./pages/Login";
import sampleData from "./test";
import MeetingSummary from "./pages/MeetingSummary";

const userData = {
  username: "",
  password: "",
};

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      username: "",
      password: "",
    };

    this.updateUserData = this.updateUserData.bind(this);
    this.login = this.login.bind(this);
  }

  updateUserData(name, value) {
    console.log(name, value);
    this.setState({ [name]: value });
  }

  login() {
    console.log("login data", { username: this.state.username, password: this.state.password });
    window.location = "/home";
  }

  render() {
    return (
      <div className="App">
        <Routes>
          <Route path="/" element={<Login updateUserData={this.updateUserData} login={this.login} />} />
          <Route
            path="/home"
            element={<Home userData={{ username: this.state.username, password: this.state.password }} />}
          />
          <Route path="/meeting" element={<MeetingRoom />} />
          <Route path="/meeting-summary" element={<MeetingSummary />} />
          <Route path="/HRdashboard" element={<HRDashboard />} />
          <Route path="/therapist-dashboard" element={<TherapistRoom />} />
        </Routes>
      </div>
    );
  }
}

export default App;
