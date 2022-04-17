import axios from "axios";
import React, { Component } from "react";
import { Link } from "react-router-dom";
import loginImg from "../assets/img/login.svg";

class Login extends Component {
  constructor(props) {
    super(props);

    this.state = {
      username: "",
      password: "",
    };

    this.updateInput = this.updateInput.bind(this);
    this.login = this.login.bind(this);
  }

  updateInput(event) {
    this.setState({ [event.target.name]: event.target.value });

    this.props.updateUserData(event.target.name, event.target.value);

    // if (this.state.username !== "" && this.state.password !== "") {
    //   this.props.updateUserData({
    //     username: this.state.username,
    //     password: this.state.password,
    //   });
    // }
  }

  login() {
    this.props.login();
  }

  render() {
    return (
      <main className="login-screen">
        <div className="left">
          <img src={loginImg} alt="" />
        </div>
        <div className="main-card card">
          <h1>Sign In</h1>

          <input type="text" name="username" onChange={this.updateInput} autoFocus placeholder="username" />
          <input
            type="password"
            name="password"
            onChange={this.updateInput}
            className="password"
            placeholder="password"
          />

          {/* <Link to={"/home"}> */}
          <button className="fw" onClick={this.login}>
            Login
          </button>
          {/* </Link> */}
        </div>
      </main>
    );
  }
}

export default Login;
