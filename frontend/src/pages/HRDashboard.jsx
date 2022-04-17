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

import { Chart as ChartJS, ArcElement, Tooltip, CategoryScale, LinearScale, BarElement } from "chart.js";
import { Doughnut, Bar } from "react-chartjs-2";
import axios from "axios";
// import faker from "faker";
ChartJS.register(ArcElement, Tooltip, CategoryScale, LinearScale, BarElement);

class HRDashboard extends Component {
  constructor(props) {
    super(props);
    this.state = {
      reportModal: false,
      employeesData: [],
      douChartData: {
        labels: ["Angry", "Happy", "Sad", "Neutral", "Scared"],
        datasets: [
          {
            label: "# of Votes",
            data: [12, 19, 3, 5, 2],
            backgroundColor: [
              "rgba(255, 99, 132, 0.2)",
              "rgba(54, 162, 235, 0.2)",
              "rgba(255, 206, 86, 0.2)",
              "rgba(75, 192, 192, 0.2)",
              "rgba(153, 102, 255, 0.2)",
              "rgba(255, 159, 64, 0.2)",
            ],
            borderColor: [
              "rgba(255, 99, 132, 1)",
              "rgba(54, 162, 235, 1)",
              "rgba(255, 206, 86, 1)",
              "rgba(75, 192, 192, 1)",
              "rgba(153, 102, 255, 1)",
              "rgba(255, 159, 64, 1)",
            ],
            borderWidth: 1,
          },
        ],
      },
      barChartData: {
        labels: ["Head Movements", "Concentration", "Distracted", "Talking"],
        datasets: [
          {
            label: "Dataset 1",
            data: [15, 9, 20, 30],
            backgroundColor: "rgba(255, 99, 132, 0.5)",
          },
          // {
          //   label: 'Dataset 2',
          //   data: labels.map(() => faker.datatype.number({ min: 0, max: 1000 })),
          //   backgroundColor: 'rgba(53, 162, 235, 0.5)',
          // },
        ],
      },
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

    this.toggleReportModal = this.toggleReportModal.bind(this);
  }

  toggleReportModal() {
    this.setState((prevState) => ({ reportModal: !prevState.reportModal }));
  }

  componentDidMount() {
    axios
      .get("http://localhost:5000/hr")
      .then((res) => {
        // console.log("HR response", res.data);
        let data = Object.values(res.data);
        this.setState({ employeesData: data });
      })
      .catch((err) => {
        console.warn("Error: ", err);
      });
  }

  render() {
    return (
      <>
        <main className="teacher-dashboard">
          <Modal
            centered
            size="lg"
            className="student-report-modal"
            toggle={this.toggleReportModal}
            isOpen={this.state.reportModal}
          >
            <ModalBody>
              <img src={close} alt="" onClick={this.toggleReportModal} />
              <h3>Employee Report</h3>
              <div className="chart-container">
                <div className="chart-wrapper">
                  <Doughnut
                    data={this.state.douChartData}
                    options={{
                      legend: { display: false },
                      tooltips: {
                        enabled: false,
                      },
                    }}
                  />
                  <h4>Emotions Summary</h4>
                </div>

                <div className="chart-wrapper">
                  <Bar data={this.state.barChartData} />
                  <h4>Events Summary</h4>
                </div>
              </div>
              <div className="btn-wrapper">
                <button>View Questionaire</button>
                <Link to="/therapist-dashboard">
                  <button>Schedule Call</button>
                </Link>
              </div>
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
              <Link to={"/"}>
                <img src={logout} alt="" />
              </Link>
            </div>
          </div>

          <div className="right">
            <div className="top-bar">
              <div className="exam-info">
                <h3>Employees report for -- Today </h3>
              </div>
            </div>

            <div className="bottom-container">
              {this.state.employeesData.map((el, id) => {
                return (
                  <div className="student-card" key={id}>
                    <img src={`https://ui-avatars.com/api/?name=${el.name}`} alt="" />
                    <h3>{el.name}</h3>
                    <div className="link-container">
                      <a href={`https://github.com/${el.github_id}`} target="_blank">
                        <img src={github} alt="" />
                      </a>
                      <a href={`https://github.com/${el.jira}`}>
                        <img src={jira} alt="" />
                      </a>
                    </div>

                    <div className="info-container">
                      <div className="info-box">
                        {/* <p className="info">{ Math.floor(Math.random() * (100 - 50 + 1)) + 50 }</p> */}
                        <p className="info">{100 - parseInt(el.prod_score)}</p>
                        <p className="tag">
                          Productivity <br /> Score
                        </p>
                      </div>
                      <div className="info-box">
                        <p className="info">{100 - parseInt(el.mentalhealth_score)}</p>
                        <p className="tag">
                          Mental <br /> Health
                        </p>
                      </div>
                    </div>

                    <button onClick={this.toggleReportModal}>View Details</button>
                  </div>
                );
              })}
            </div>
          </div>
        </main>
      </>
    );
  }
}

export default HRDashboard;
